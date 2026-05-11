from App.CRUDTools import DatabaseTools

class Assessment:

    def __init__(self):
        self.db_tools = DatabaseTools()

    def evaluate_quiz(self, student_id, quiznumber, lessonid, gradingperiod):
        # FETCH MULTIPLIERS
        sql = """
            SELECT easy_multiplier, average_multiplier, hard_multiplier
            FROM cai.tbl_scoremultiplier
            WHERE
                quiznumber = %s
                AND lessonid = %s
                AND gradingperiod = %s
        """
        res_mult = self.db_tools.fetch_all(sql, (quiznumber, lessonid, gradingperiod))

        if not res_mult:
            return
        
        res_mult = res_mult[0]

        # DEFINE CALCULATION HELPERS
        quiz_types = [
            {'table': 'tbl_quizmultiplechoice', 'key': 'mckey', 'type': 'MC'},
            {'table': 'tbl_quizidentification', 'key': 'idkey', 'type': 'ID'},
            {'table': 'tbl_quiztrueorfalse',     'key': 'tfkey', 'type': 'TF'}
        ]

        total_student_points = 0

        for q in quiz_types:
            sql  = "SELECT\n"
            sql += "    COALESCE(SUM(CASE WHEN q.difficultylevel = '1' THEN 1 ELSE 0 END), 0) * %s AS s1,\n"
            sql += "    COALESCE(SUM(CASE WHEN q.difficultylevel = '2' THEN 1 ELSE 0 END), 0) * %s AS s2,\n"
            sql += "    COALESCE(SUM(CASE WHEN q.difficultylevel = '3' THEN 1 ELSE 0 END), 0) * %s AS s3\n"
            sql += f"FROM cai.{q['table']} q\n"
            sql += f"INNER JOIN cai.tbl_answers a ON q.{q['key']} = a.assmt_key\n"
            sql += "WHERE a.studentid = %s\n"
            sql += "AND a.quiznumber = %s\n"
            sql += "AND a.quiztype = %s\n"
            sql += "AND LOWER(q.correct_answer) = LOWER(a.answer);\n"

            res = self.db_tools.fetch_all(sql, (
                res_mult['easy_multiplier'],
                res_mult['average_multiplier'],
                res_mult['hard_multiplier'],
                student_id,
                quiznumber,
                q['type'])
            )

            if res:
                row = res[0]
                total_student_points += sum(row.values()) if isinstance(row, dict) else sum(row)

        # CALCULATE TOTAL POSSIBLE SCORE
        sql = """
            SELECT (easy_count * %s + average_count * %s + hard_count * %s) AS total_score
            FROM cai.tbl_quiz
            WHERE
                quiznumber = %s
                AND lessonid = %s
                AND gradingperiod = %s
        """

        params = (
            res_mult['easy_multiplier'],
            res_mult['average_multiplier'],
            res_mult['hard_multiplier'],
            quiznumber, 
            lessonid, 
            gradingperiod
        )

        total_score = 0

        row = self.db_tools.fetch_all(sql, params)

        if row:
            total_score = row[0]['total_score']

        sql_upsert = """
            INSERT INTO cai.tbl_quizscores (
                quiznumber, gradingperiod, lessonid, studentid, quizscore
            ) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (studentid, quiznumber, gradingperiod, lessonid)
            DO UPDATE SET
                quizscore = EXCLUDED.quizscore,
                datetaken = CURRENT_TIMESTAMP;
        """

        upsert_params = (
            quiznumber, 
            gradingperiod, 
            lessonid,
            student_id, 
            total_student_points
        )

        sql_prog = """
            UPDATE cai.tbl_progress 
            SET lessonsdone = CASE 
                    WHEN lessonsdone = '' THEN %s 
                    WHEN lessonsdone LIKE %s THEN lessonsdone
                    ELSE lessonsdone || ',' || %s 
                END,
                quizdone = CASE 
                    WHEN quizdone = '' THEN %s 
                    WHEN quizdone LIKE %s THEN quizdone
                    ELSE quizdone || ',' || %s 
                END
            WHERE studentid = %s;
        """

        try:
            conn = self.db_tools.get_connection()
            conn.autocommit = False

            with conn.cursor() as cur:
                cur.execute(sql_upsert, upsert_params)
                
                # Formatting parameters for the "LIKE" check to prevent duplicate entries in the CSV string
                l_id = str(lessonid)
                q_id = str(quiznumber)
                cur.execute(sql_prog, (l_id, f'%{l_id}%', l_id, q_id, f'%{q_id}%', q_id, student_id))
                
                conn.commit()
                print(f"Quiz submitted! Score: {total_student_points}/{total_score}")

        except Exception as e:
            if conn: conn.rollback()
            print(f"❌ Database error: {e}")

        finally:
                if conn: conn.close()