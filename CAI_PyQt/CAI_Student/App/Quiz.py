from App.CardQuiz import Ui_CardQuiz
from App.Tools import Utility
from App.CRUDTools import DatabaseTools

from PySide6.QtWidgets import (QFrame, QLineEdit, QRadioButton, QButtonGroup, QMessageBox)
from PySide6.QtGui import (QImage, QPixmap, QCursor)
from PySide6.QtCore import (Qt, QSize)

class Quiz(QFrame, Ui_CardQuiz):

    def __init__(self, quiz_type):
        super().__init__()
        self.setupUi(self)
        self.db_tools = DatabaseTools()
        self.util = Utility()

        self.quiz_type = quiz_type
        self.idKey = None
        self.quiznumber = None
        self.gradingperiod = None
        self.lessonid = None
        self.itemno = ""
        self.question = ""
        self.imageQ = None

        self.choice_a = ""
        self.choice_b = ""
        self.choice_c = ""

        self.correct_answer = ""

        self.input_css = """
            /* Styling the input field */
            QLineEdit {
                border: 3px solid #ABABAB;
                border-radius: 10px;
                background-color: #FFF;
                padding: 0px 10px 0px;
                height: 35px;
                font: 11pt "Inter";
            }

            /* Highlight when typing (focus) */
            QLineEdit:focus {
                border: 3px solid #007BFF;
            }
        """

    def displayAttributes(self):
        self.label_itemno.setText(f"ITEM {self.itemno}")
        self.label_question.setText(f"{self.question}")

        # Handle Image
        if not self.util.isEmpty(self.imageQ):
            image = QImage.fromData(bytes(self.imageQ))
            if not image.isNull():
                pixmap = QPixmap.fromImage(image)
                self.label_q_image.setPixmap(pixmap)

        self.init_answers()

    def init_answers(self):
        if self.quiz_type == "ID":
            self.ans_input = QLineEdit() # renamed to avoid confusion
            self.ans_input.setPlaceholderText("Enter your answer here")
            self.ans_input.setMinimumSize(QSize(0, 30))
            self.ans_input.setStyleSheet(self.input_css)
            self.verticalLayout_2.addWidget(self.ans_input)

        else:
            self.button_group = QButtonGroup(self)
            labels = [self.choice_a, self.choice_b, self.choice_c] if self.quiz_type == "MC" else ["True", "False"]

            self.opts = [] # To keep references if needed
            for i, text in enumerate(labels):
                radio = QRadioButton(text)
                radio.setMinimumSize(QSize(0, 30))
                radio.setStyleSheet("font: 11pt \"Inter\"; background-color: #93E6D7; border-radius: 10px; padding: 0px 10px 0px;")
                radio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                self.button_group.addButton(radio, i) # Assign an ID (0, 1, 2)
                self.verticalLayout_2.addWidget(radio)
                self.opts.append(radio)

    def get_answer(self):
        """Returns the current input value of the card."""

        if self.quiz_type == "ID":
            return self.ans_input.text().strip()
        
        elif self.quiz_type in ["MC", "TF"]:
            selected_button = self.button_group.checkedButton()

            if selected_button:
                return selected_button.text()
        
        return "" # No answer provided


class QuizUtils:

    def __init__(self):
        self.db_tools = DatabaseTools()
        self.util = Utility()

        self.quiznumber     = None
        self.gradingperiod  = None
        self.lessonid       = None
        self.publish        = True

        sql  = "SELECT\n"
        sql += "    quiznumber,\n"
        sql += "    gradingperiod,\n"
        sql += "    lessonid,\n"
        sql += "    publish\n"
        sql += "FROM cai.tbl_quiz\n"
        sql += "WHERE publish = TRUE"
        record = self.db_tools.fetch_all(sql)

        if record:
            self.quiznumber     = record[0].get('quiznumber')
            self.gradingperiod  = record[0].get('gradingperiod')
            self.lessonid       = record[0].get('lessonid')
            self.publish        = record[0].get('publish')

    def retrieve_quiz(self):
        """
            Retrieves quizzes from database (Identification, Multiple Choice, True or False)

            Args:
                N/A

            Returns:
                record_id (list): list of dict for QScrollArea (Identification)
                record_mc (list): list of dict for QScrollArea (Multiple Choice)
                record_tf (list): list of dict for QScrollArea (True or False)

            Raises:
                N/A
        """

        record_id = record_mc = record_tf = []

        if self.util.isEmpty(self.quiznumber) or self.util.isEmpty(self.gradingperiod) or self.util.isEmpty(self.lessonid):
            print("ℹ️ No available quiz.")
            return record_id, record_mc, record_tf

        sql_id  = "SELECT\n"
        sql_id += "    IDKEY,\n"
        sql_id += "    quiznumber,\n"
        sql_id += "    gradingperiod,\n"
        sql_id += "    lessonid,\n"
        sql_id += "    ITEMNO,\n"
        sql_id += "    QUESTION,\n"
        sql_id += "    IMAGEQUESTION,\n"
        sql_id += "    CORRECT_ANSWER\n"
        sql_id += "FROM\n"
        sql_id += "    cai.tbl_quizidentification\n"
        sql_id += "WHERE\n"
        sql_id += "    quiznumber = %s\n"
        sql_id += "    AND gradingperiod = %s\n"
        sql_id += "    AND lessonid = %s\n"
        sql_id += "ORDER BY itemno\n"

        sql_mc  = "SELECT\n"
        sql_mc += "    MCKEY,\n"
        sql_mc += "    quiznumber,\n"
        sql_mc += "    gradingperiod,\n"
        sql_mc += "    lessonid,\n"
        sql_mc += "    ITEMNO,\n"
        sql_mc += "    QUESTION,\n"
        sql_mc += "    IMAGEQUESTION,\n"
        sql_mc += "    CHOICE_A,\n"
        sql_mc += "    CHOICE_B,\n"
        sql_mc += "    CHOICE_C,\n"
        sql_mc += "    CORRECT_ANSWER\n"
        sql_mc += "FROM\n"
        sql_mc += "    cai.tbl_quizmultiplechoice\n"
        sql_mc += "WHERE\n"
        sql_mc += "    quiznumber = %s\n"
        sql_mc += "    AND gradingperiod = %s\n"
        sql_mc += "    AND lessonid = %s\n"
        sql_mc += "ORDER BY itemno\n"

        sql_tf  = "SELECT\n"
        sql_tf += "    TFKEY,\n"
        sql_tf += "    quiznumber,\n"
        sql_tf += "    gradingperiod,\n"
        sql_tf += "    lessonid,\n"
        sql_tf += "    ITEMNO,\n"
        sql_tf += "    QUESTION,\n"
        sql_tf += "    IMAGEQUESTION,\n"
        sql_tf += "    CORRECT_ANSWER\n"
        sql_tf += "FROM\n"
        sql_tf += "    cai.tbl_quiztrueorfalse\n"
        sql_tf += "WHERE\n"
        sql_tf += "    quiznumber = %s\n"
        sql_tf += "    AND gradingperiod = %s\n"
        sql_tf += "    AND lessonid = %s\n"
        sql_tf += "ORDER BY itemno\n"

        sections = [
            (0, sql_id),
            (1, sql_mc),
            (2, sql_tf)
        ]

        for idx, sql in sections:
            record = self.db_tools.fetch_all(sql, (self.quiznumber, self.gradingperiod, self.lessonid))

            if record:

                if idx == 0:
                    record_id = record

                elif idx == 1:
                    record_mc = record

                else:
                    record_tf = record

        return record_id, record_mc, record_tf

    def save_quiz(self, student_id, quiz_cards):
        if not quiz_cards:
            return 1

        try:
            conn = self.db_tools.get_connection()
            conn.autocommit = False

            with conn.cursor() as cur:

                for card in quiz_cards:
                    student_ans = card.get_answer().strip().lower()
                    is_correct = (card.correct_answer.strip().lower() == student_ans)
                    remark = "Correct" if is_correct else "Incorrect"

                    sql = """
                        INSERT INTO cai.tbl_answers (
                            assmt_key, quiztype, quiznumber, itemno, answer, studentid, remarks
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (assmt_key, quiztype, quiznumber, itemno, studentid)
                        DO UPDATE SET
                        answer = EXCLUDED.answer,
                        datetaken = CURRENT_TIMESTAMP,
                        remarks = EXCLUDED.remarks;
                    """
                    
                    cur.execute(sql, (
                        card.idKey,
                        card.quiz_type,
                        card.quiznumber,
                        card.itemno,
                        student_ans,
                        student_id,
                        remark
                    ))

            conn.commit()

            self.evaluate_quiz(student_id)

            return 0
            
        except Exception as e:
            if conn: conn.rollback()
            print(f"Failed to save: {str(e)}")
            return 1

        finally:
            if conn: conn.close()

    def evaluate_quiz(self, student_id):
        # FETCH MULTIPLIERS
        sql = """
            SELECT easy_multiplier, average_multiplier, hard_multiplier
            FROM cai.tbl_scoremultiplier
            WHERE
                quiznumber = %s
                AND lessonid = %s
                AND gradingperiod = %s
        """
        res_mult = self.db_tools.fetch_all(sql, (self.quiznumber, self.lessonid, self.gradingperiod))

        if not res_mult:
            return
        
        res_mult = res_mult[0]

        # DEFINE CALCULATION HELPERS
        quiz_types = [
            {'table': 'tbl_quizmultiplechoice', 'key': 'mckey', 'type': 'MC'},
            {'table': 'tbl_quizidentification', 'key': 'idkey', 'type': 'ID'},
            {'table': 'tbl_quiztrueorfalse', 'key': 'tfkey', 'type': 'TF'}
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
                self.quiznumber,
                q['type'])
            )

            if res:
                row = res[0]
                total_student_points += sum(row.values()) if isinstance(row, dict) else sum(row)

        sql_upsert = """
            INSERT INTO cai.tbl_quizscores (
                quiznumber, gradingperiod, lessonid, studentid, quizscore
            ) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (studentid, quiznumber, gradingperiod, lessonid)
            DO UPDATE SET
                datetaken = CURRENT_TIMESTAMP,
                quizscore = EXCLUDED.quizscore;
        """

        upsert_params = (
            self.quiznumber, 
            self.gradingperiod, 
            self.lessonid,
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
                l_id = str(self.lessonid)
                q_id = str(self.quiznumber)
                cur.execute(sql_prog, (l_id, f'%{l_id}%', l_id, q_id, f'%{q_id}%', q_id, student_id))
                
                conn.commit()

        except Exception as e:
            if conn: conn.rollback()
            print(f"❌ Database error: {e}")

        finally:
                if conn: conn.close()