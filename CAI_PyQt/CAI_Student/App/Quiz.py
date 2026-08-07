from App.CardQuiz import Ui_CardQuiz
from App.Tools import Utility
from App.CRUDTools import DatabaseTools

from psycopg2.extras import execute_values

from PySide6.QtWidgets import (QFrame, QLineEdit, QRadioButton, QButtonGroup, QLabel, QHBoxLayout, QSizePolicy, QSpacerItem)
from PySide6.QtGui import (QImage, QPixmap, QCursor)
from PySide6.QtCore import (Qt, QSize)

class Quiz(QFrame, Ui_CardQuiz):

    def __init__(self, quiz_type):
        super().__init__()
        self.setupUi(self)
        self.db_tools = DatabaseTools()
        self.util = Utility()

        self.quiz_type      = quiz_type
        self.idKey          = None
        self.quiznumber     = None
        self.gradingperiod  = None
        self.lessonid       = None
        self.itemno         = ""
        self.itemnoCnt      = 0
        self.question       = ""
        self.imageQ         = None

        self.choice_a       = ""
        self.choice_b       = ""
        self.choice_c       = ""

        self.user_answer    = ""
        self.correct_answer = ""
        self.remarks        = ""

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
        self.label_itemno.setText(f"ITEM {self.itemnoCnt}")
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

        elif self.quiz_type in ["MC", "TF"]:
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

        else:
            layout_ans_1 = QHBoxLayout()
            layout_ans_2 = QHBoxLayout()

            lbl_1 = QLabel("Your Answer:")
            lbl_2 = QLabel("Correct Answer:")

            self.lable_user_ans = QLabel(self.user_answer)
            self.lable_correct_ans = QLabel(self.correct_answer)

            bg_color = "#C4E8C9"

            if self.remarks == "Incorrect":
                bg_color = "#F0C2C6"

            qss = f'background-color: {bg_color}; min-height: 30px; border-radius: 10px; padding: 0px 10px; font: 11pt "Inter Medium";'
            lbl_1.setStyleSheet('font: 11pt "Inter Medium"')
            lbl_2.setStyleSheet('font: 11pt "Inter Medium"')
            self.lable_user_ans.setStyleSheet(qss)
            self.lable_correct_ans.setStyleSheet(qss)

            layout_ans_1.addWidget(lbl_1)
            layout_ans_1.addWidget(self.lable_user_ans)
            layout_ans_1.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            layout_ans_2.addWidget(lbl_2)
            layout_ans_2.addWidget(self.lable_correct_ans)
            layout_ans_2.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            self.verticalLayout_2.addLayout(layout_ans_1)
            self.verticalLayout_2.addLayout(layout_ans_2)

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

    def __init__(self, grading_period):
        self.db_tools = DatabaseTools()
        self.util = Utility()

        self.quiznumber     = None
        self.gradingperiod  = grading_period
        self.lessonid       = None
        self.publish        = True

        sql  = "SELECT\n"
        sql += "    quiznumber,\n"
        sql += "    lessonid,\n"
        sql += "    publish\n"
        sql += "FROM cai.tbl_quiz\n"
        sql += "WHERE publish = TRUE"
        sql += "    AND gradingperiod = %s"
        record = self.db_tools.fetch_all(sql, (grading_period,))

        if record:
            self.quiznumber     = record[0].get('quiznumber')
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

        if self.util.isEmpty(self.quiznumber) or not self.gradingperiod or self.util.isEmpty(self.lessonid):
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

    def retrieve_quiz_answer(self, studentid:str):
        """
            Retrieves quizzes from database (Identification, Multiple Choice, True or False)

            Args:
                studentid (str): Student Id

            Returns:
                record (list[RealDictCursor]): list of dict for QScrollArea

            Raises:
                N/A
        """

        record = []

        if self.util.isEmpty(self.quiznumber) or not self.gradingperiod or self.util.isEmpty(self.lessonid):
            print("ℹ️ No available quiz.")
            return record

        query = """
            SELECT
                'ID' AS QUIZTYPE,
                Q.IDKEY AS ASSMT_KEY,
                Q.QUIZNUMBER,
                Q.GRADINGPERIOD,
                Q.LESSONID,
                Q.ITEMNO,
                Q.QUESTION,
                Q.IMAGEQUESTION,
                Q.CORRECT_ANSWER,
                COALESCE(ANS.ANSWER, '') AS USER_ANSWER,
                ANS.REMARKS
            FROM
                CAI.TBL_QUIZIDENTIFICATION Q
            LEFT JOIN 
                CAI.TBL_ANSWERS ANS ON Q.IDKEY = ANS.ASSMT_KEY 
                AND ANS.QUIZTYPE = 'ID'
                AND ANS.STUDENTID = %s
            WHERE
                Q.QUIZNUMBER = %s
                AND Q.GRADINGPERIOD = %s
                AND Q.LESSONID = %s

            UNION ALL

            SELECT
                'MC' AS QUIZTYPE,
                Q.MCKEY AS ASSMT_KEY,
                Q.QUIZNUMBER,
                Q.GRADINGPERIOD,
                Q.LESSONID,
                Q.ITEMNO,
                Q.QUESTION,
                Q.IMAGEQUESTION,
                Q.CORRECT_ANSWER,
                COALESCE(ANS.ANSWER, '') AS USER_ANSWER,
                ANS.REMARKS
            FROM
                CAI.TBL_QUIZMULTIPLECHOICE Q
            LEFT JOIN 
                CAI.TBL_ANSWERS ANS ON Q.MCKEY = ANS.ASSMT_KEY 
                AND ANS.QUIZTYPE = 'MC'
                AND ANS.STUDENTID = %s
            WHERE
                Q.QUIZNUMBER = %s
                AND Q.GRADINGPERIOD = %s
                AND Q.LESSONID = %s

            UNION ALL

            SELECT
                'TF' AS QUIZTYPE,
                Q.TFKEY AS ASSMT_KEY,
                Q.QUIZNUMBER,
                Q.GRADINGPERIOD,
                Q.LESSONID,
                Q.ITEMNO,
                Q.QUESTION,
                Q.IMAGEQUESTION,
                Q.CORRECT_ANSWER,
                COALESCE(ANS.ANSWER, '') AS USER_ANSWER,
                ANS.REMARKS
            FROM
                CAI.TBL_QUIZTRUEORFALSE Q
            LEFT JOIN 
                CAI.TBL_ANSWERS ANS ON Q.TFKEY = ANS.ASSMT_KEY 
                AND ANS.QUIZTYPE = 'TF'
                AND ANS.STUDENTID = %s
            WHERE
                Q.QUIZNUMBER = %s
                AND Q.GRADINGPERIOD = %s
                AND Q.LESSONID = %s

            ORDER BY ITEMNO;
        """

        result = self.db_tools.fetch_all(query, (
                studentid, self.quiznumber, self.gradingperiod, self.lessonid,
                studentid, self.quiznumber, self.gradingperiod, self.lessonid,
                studentid, self.quiznumber, self.gradingperiod, self.lessonid
            )
        )

        if result:
            record = result

        return record

    def save_quiz(self, student_id, quiz_cards):
        if not quiz_cards:
            return 3, "Empty quiz."

        conn = None
        try:
            conn = self.db_tools.get_connection()
            conn.autocommit = False

            with conn.cursor() as cur:
                insert_data = []
                for card in quiz_cards:
                    delete_sql = """
                        DELETE FROM cai.tbl_answers
                        WHERE assmt_key = %s AND quiztype = %s AND quiznumber = %s AND studentid = %s;
                    """
                    cur.execute(delete_sql, (card.idKey, card.quiz_type, card.quiznumber, student_id))

                    student_ans = card.get_answer().strip().lower()

                    if student_ans == "":
                        return 2, "Oops! Please answer all the questions."
                
                    is_correct = (card.correct_answer.strip().lower() == student_ans)
                    remark = "Correct" if is_correct else "Incorrect"
                    
                    insert_data.append((
                        card.idKey,
                        card.quiz_type,
                        card.quiznumber,
                        card.itemno,
                        student_ans,
                        student_id,
                        remark
                    ))

                insert_sql = """
                    INSERT INTO cai.tbl_answers (
                        assmt_key, quiztype, quiznumber, itemno, answer, studentid, remarks
                    ) VALUES %s;
                """
                execute_values(cur, insert_sql, insert_data)

            conn.commit()
            self.evaluate_quiz(student_id)
            return 1, "Successfully saved and evaluated this quiz."
            
        except Exception as e:
            if conn: conn.rollback()
            return 3, f"❌ Failed to save: {str(e)}"
        
        finally:
            if conn: conn.close()

    def evaluate_quiz(self, student_id):
        sql = """
            DELETE FROM CAI.TBL_QUIZSCORES
            WHERE QUIZNUMBER = %s AND
                GRADINGPERIOD = %s AND
                LESSONID = %s AND
                STUDENTID = %s;

            INSERT INTO CAI.TBL_QUIZSCORES (QUIZNUMBER, GRADINGPERIOD, LESSONID, STUDENTID, QUIZSCORE, DATETAKEN)
            WITH CombinedQuizzes AS (
                -- 1. Unify and filter the quiz items for the specific scope
                SELECT 'ID' AS quiztype, IDKEY AS assmt_key, QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL, ITEMNO, CORRECT_ANSWER 
                FROM CAI.TBL_QUIZIDENTIFICATION
                WHERE QUIZNUMBER = %s AND LESSONID = %s AND GRADINGPERIOD = %s
                
                UNION ALL
                
                SELECT 'MC' AS quiztype, MCKEY AS assmt_key, QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL, ITEMNO, CORRECT_ANSWER 
                FROM CAI.TBL_QUIZMULTIPLECHOICE
                WHERE QUIZNUMBER = %s AND LESSONID = %s AND GRADINGPERIOD = %s
                
                UNION ALL
                
                SELECT 'TF' AS quiztype, TFKEY AS assmt_key, QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL, ITEMNO, CORRECT_ANSWER 
                FROM CAI.TBL_QUIZTRUEORFALSE
                WHERE QUIZNUMBER = %s AND LESSONID = %s AND GRADINGPERIOD = %s
            ),
            ScoredItems AS (
                -- 2. Join the targeted student's answers, evaluate correctness, and pull multipliers
                SELECT 
                    a.studentid,
                    m.gradingperiod,
                    m.lessonid,
                    m.quiznumber,
                    a.datetaken,
                    CASE 
                        WHEN UPPER(TRIM(a.answer)) = UPPER(TRIM(q.CORRECT_ANSWER)) THEN 1 
                        ELSE 0 
                    END AS is_correct,
                    CASE q.DIFFICULTYLEVEL
                        WHEN 1 THEN COALESCE(m.EASY_MULTIPLIER, 1)
                        WHEN 2 THEN COALESCE(m.AVERAGE_MULTIPLIER, 1)
                        WHEN 3 THEN COALESCE(m.HARD_MULTIPLIER, 1)
                        ELSE 1
                    END AS multiplier
                FROM cai.tbl_answers a
                INNER JOIN CombinedQuizzes q 
                    ON a.quiztype = q.quiztype 
                    AND a.assmt_key = q.assmt_key
                    AND a.quiznumber = q.quiznumber
                    AND a.itemno = q.ITEMNO 
                LEFT JOIN CAI.TBL_SCOREMULTIPLIER m
                    ON q.QUIZNUMBER = m.QUIZNUMBER
                    AND q.LESSONID = m.LESSONID
                    AND q.GRADINGPERIOD = m.GRADINGPERIOD
                WHERE a.studentid = %s
                AND a.quiznumber = %s
            )
            -- 3. Aggregate total score and insert into the destination table
            SELECT 
                quiznumber,
                gradingperiod,
                lessonid,
                studentid,
                SUM(is_correct * multiplier) AS QUIZSCORE,
                MAX(datetaken) AS DATETAKEN -- Pulls the timestamp from the student's submission
            FROM ScoredItems
            GROUP BY 
                studentid, 
                gradingperiod, 
                lessonid, 
                quiznumber;
        """

        params = (
            self.quiznumber, self.gradingperiod, self.lessonid, student_id,
            self.quiznumber, self.lessonid, self.gradingperiod,
            self.quiznumber, self.lessonid, self.gradingperiod,
            self.quiznumber, self.lessonid, self.gradingperiod,
            student_id, self.quiznumber
        )

        try:
            conn = self.db_tools.get_connection()
            conn.autocommit = False

            with conn.cursor() as cur:
                cur.execute(sql, params)
                conn.commit()

        except Exception as e:
            if conn: conn.rollback()
            print(f"❌ Database error: {e}")

        finally:
            if conn: conn.close()

