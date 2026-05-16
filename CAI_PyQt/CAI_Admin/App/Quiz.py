import os
import psycopg2

from PySide6.QtGui import QStandardItemModel, QStandardItem, QImage, QPixmap, QKeySequence, QShortcut
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QComboBox,
                             QSpinBox, QPushButton, QScrollArea, QButtonGroup,
                             QMessageBox, QFileDialog, QFrame, QDialog)
from PySide6.QtCore import Qt, QSize, Signal

from App.CRUDTools import DatabaseTools
from App.Tools import Utility, NoScrollComboBox
from App.QuizDialog import Ui_QuizCreatorDialog
from App.CardQuiz import Ui_CardQuiz
from App.CardQuiz_edit import Ui_CardQuiz_edit


class Quiz:
    def __init__(self):
        self.db_tools = DatabaseTools()

    def get_scores(self, studentId, gradingperiod):
        """
        Retrieves all quiz scores for a given student, including lesson titles.
        Formatted to populate a QStandardItemModel for the UI.

        Returns:
            model (QStandardItemModel):
        """

        sql = """
            SELECT
                qs.quiznumber,
                q.lessonid,
                l.title,
                qs.quizscore,
                q.total_items,
                TO_CHAR(qs.datetaken, 'YYYY/MM/DD, HH12:MI AM') AS datetaken
            FROM cai.tbl_quiz AS q, cai.tbl_quizscores AS qs, cai.tbl_lessons AS l
            WHERE qs.studentid = %s
                AND qs.gradingperiod = %s
                AND q.quiznumber = qs.quiznumber
                AND q.lessonid = qs.lessonid
                AND qs.lessonid = l.lesson_id
            ORDER BY qs.datetaken DESC;
        """

        records = self.db_tools.fetch_all(sql, (studentId, gradingperiod))

        ui_headers = ["QUIZ #", "LESSON TITLE", "SCORE", "PERCENTAGE", "DATE TAKEN"]
        model = QStandardItemModel(len(records), len(ui_headers))
        model.setHorizontalHeaderLabels(ui_headers)
        average = 0

        if not records:
            return model, average
        
        row_count = len(records)
        sum_score = 0

        for row_idx, row_data in enumerate(records):
            _, _, _, total_score = self.getQuizTotalScore(row_data['quiznumber'], gradingperiod, row_data['lessonid'])
            quiz_num_str = f"{row_data['quiznumber']}"
            score_str = f"{row_data['quizscore']}/{total_score}" if row_data['quizscore'] and total_score else ""

            percentage_str = ""

            # Ensure total_score is greater than 0 and score doesn't exceed total
            if total_score > 0 and 0 <= row_data['quizscore'] <= total_score:
                percent_val = (row_data['quizscore'] / total_score) * 100
                sum_score += percent_val

                if percent_val:
                    percentage_str = f"{percent_val:.0f}%"
            
            date_taken_str = row_data['datetaken'] if row_data['datetaken'] is not None else ""

            row_items = [
                QStandardItem(quiz_num_str),
                QStandardItem(row_data['title']),
                QStandardItem(score_str),
                QStandardItem(percentage_str),
                QStandardItem(date_taken_str)
            ]

            for col_idx, item in enumerate(row_items):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                model.setItem(row_idx, col_idx, item)

            if sum_score and row_count:
                average = sum_score / row_count

        return model, average
    
    def retrieve_quiz(self, q_num, g_period, lesson_id, diff_level):
        """
            Retrieves quizzes from database (Identification, Multiple Choice, True or False)

            Args:
                q_num (int): Quiz Number
                g_period (int): Grading Period
                lesson_id (int): Lesson Id

            Returns:
                record_id (list): list of dict for QScrollArea (Identification)
                record_mc (list): list of dict for QScrollArea (Multiple Choice)
                record_tf (list): list of dict for QScrollArea (True or False)
                quiz_record (tuple): total_items, id_level, mc_level, tf_level, publish from tbl_quiz

            Raises:
                N/A
        """

        quiz_record = (0, False)

        sql  = "SELECT\n"
        sql += "    COALESCE(TOTAL_ITEMS, 0) AS TOTAL_ITEMS,\n"
        sql += "    publish\n"
        sql += "FROM cai.tbl_quiz\n"
        sql += "WHERE quiznumber = %s\n"
        sql += "    AND gradingperiod = %s\n"
        sql += "    AND lessonid = %s"
        cursor, conn = self.db_tools.retrieve_records(sql, (q_num, g_period, lesson_id))

        if cursor:
            record = cursor.fetchone()

            if record:
                quiz_record = record

            cursor.close()

        if conn: conn.close()

        record_id = record_mc = record_tf = []

        sql_id  = "SELECT\n"
        sql_id += "    IDKEY,\n"
        sql_id += "    ITEMNO,\n"
        sql_id += "    QUESTION,\n"
        sql_id += "    IMAGEQUESTION,\n"
        sql_id += "    CORRECT_ANSWER,\n"
        sql_id += "    DIFFICULTYLEVEL\n"
        sql_id += "FROM\n"
        sql_id += "    cai.tbl_quizidentification\n"
        sql_id += "WHERE\n"
        sql_id += "    quiznumber = %s\n"
        sql_id += "    AND gradingperiod = %s\n"
        sql_id += "    AND lessonid = %s\n"
        sql_id += "    AND DIFFICULTYLEVEL = %s\n"
        sql_id += "ORDER BY itemno\n"

        sql_mc  = "SELECT\n"
        sql_mc += "    MCKEY,\n"
        sql_mc += "    ITEMNO,\n"
        sql_mc += "    QUESTION,\n"
        sql_mc += "    IMAGEQUESTION,\n"
        sql_mc += "    CHOICE_A,\n"
        sql_mc += "    CHOICE_B,\n"
        sql_mc += "    CHOICE_C,\n"
        sql_mc += "    CORRECT_ANSWER,\n"
        sql_mc += "    DIFFICULTYLEVEL\n"
        sql_mc += "FROM\n"
        sql_mc += "    cai.tbl_quizmultiplechoice\n"
        sql_mc += "WHERE\n"
        sql_mc += "    quiznumber = %s\n"
        sql_mc += "    AND gradingperiod = %s\n"
        sql_mc += "    AND lessonid = %s\n"
        sql_mc += "    AND DIFFICULTYLEVEL = %s\n"
        sql_mc += "ORDER BY itemno\n"

        sql_tf  = "SELECT\n"
        sql_tf += "    TFKEY,\n"
        sql_tf += "    ITEMNO,\n"
        sql_tf += "    QUESTION,\n"
        sql_tf += "    IMAGEQUESTION,\n"
        sql_tf += "    CORRECT_ANSWER,\n"
        sql_tf += "    DIFFICULTYLEVEL\n"
        sql_tf += "FROM\n"
        sql_tf += "    cai.tbl_quiztrueorfalse\n"
        sql_tf += "WHERE\n"
        sql_tf += "    quiznumber = %s\n"
        sql_tf += "    AND gradingperiod = %s\n"
        sql_tf += "    AND lessonid = %s\n"
        sql_tf += "    AND DIFFICULTYLEVEL = %s\n"
        sql_tf += "ORDER BY itemno\n"

        sections = [
            (0, sql_id),
            (1, sql_mc),
            (2, sql_tf)
        ]

        for idx, sql in sections:
            record = self.db_tools.fetch_all(sql, (q_num, g_period, lesson_id, diff_level))

            if record:

                if idx == 0:
                    record_id = record

                elif idx == 1:
                    record_mc = record

                else:
                    record_tf = record

        multipliers = self.getQuizMultiplier(q_num, g_period, lesson_id)
        total_score = self.getQuizTotalScore(q_num, g_period, lesson_id)

        return record_id, record_mc, record_tf, quiz_record, multipliers, total_score

    def getQuizMultiplier(self, q_num, g_period, lesson_id):
        sql  = "SELECT\n"
        sql += "    MULTIPLIERID,\n"
        sql += "    QUIZNUMBER,\n"
        sql += "    LESSONID,\n"
        sql += "    GRADINGPERIOD,\n"
        sql += "    EASY_MULTIPLIER,\n"
        sql += "    AVERAGE_MULTIPLIER,\n"
        sql += "    HARD_MULTIPLIER,\n"
        sql += "    TOTAL_POSSIBLE_POINTS\n"
        sql += "FROM\n"
        sql += "    CAI.TBL_SCOREMULTIPLIER\n"
        sql += "WHERE\n"
        sql += "    QUIZNUMBER = %s\n"
        sql += "    AND GRADINGPERIOD = %s\n"
        sql += "    AND LESSONID = %s\n"
        cursor, conn = self.db_tools.retrieve_records(sql, (q_num, g_period, lesson_id))

        if cursor:
            record = cursor.fetchone()
            cursor.close()
            return record

        if conn: conn.close()

        return None
    
    def getQuizTotalScore(self, quiznumber, gradingperiod, lessonid):
        """
            Args:
                quiznumber (int):
                gradingperiod (int):
                lessonid (int):

            Returns:
                (easy_score, average_score, hard_score, total_score) (tuple):
        """
        sql = """
            SELECT 
                COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 1 THEN 1 END) * M.EASY_MULTIPLIER AS "easy_score",
                COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 2 THEN 1 END) * M.AVERAGE_MULTIPLIER AS "average_score",
                COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 3 THEN 1 END) * M.HARD_MULTIPLIER AS "hard_score",

                (COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 1 THEN 1 END) * M.EASY_MULTIPLIER) +
                (COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 2 THEN 1 END) * M.AVERAGE_MULTIPLIER) +
                (COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 3 THEN 1 END) * M.HARD_MULTIPLIER) as max_score
            FROM (
                SELECT QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL FROM CAI.TBL_QUIZIDENTIFICATION
                UNION ALL
                SELECT QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL FROM CAI.TBL_QUIZMULTIPLECHOICE
                UNION ALL
                SELECT QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL FROM CAI.TBL_QUIZTRUEORFALSE
            ) Q

            JOIN CAI.TBL_SCOREMULTIPLIER M ON Q.QUIZNUMBER = M.QUIZNUMBER AND Q.LESSONID = M.LESSONID
            WHERE q.quiznumber = %s
                AND q.gradingperiod = %s
                AND q.lessonid = %s
            GROUP BY M.QUIZNUMBER, M.LESSONID, M.EASY_MULTIPLIER, M.AVERAGE_MULTIPLIER, M.HARD_MULTIPLIER;
        """

        record = self.db_tools.fetch_all(sql, (quiznumber, gradingperiod, lessonid))

        easy_score = 0
        average_score = 0
        hard_score = 0
        total_score = 0

        if record:
            easy_score = record[0]['easy_score']
            average_score = record[0]['average_score']
            hard_score = record[0]['hard_score']
            total_score = record[0]['max_score']

        return (easy_score, average_score, hard_score, total_score)




class QuizItemWidget(QFrame, Ui_CardQuiz_edit):
    """A reusable row for a single quiz question."""
    def __init__(self, item_type, remove_callback):
        super().__init__()
        self.setupUi(self)

        self.util = Utility()
        self.item_type = item_type
        self.img_path = None
        self.id = None

        self.input_css = """

            *[class="correct-label"] {
                background-color: #f0f0f0;
                color: #555555;
                border: 1px solid #ABABAB;
                border-right: none;
                border-top-left-radius: 15px;
                border-bottom-left-radius: 15px;
                padding-left: 10px;
                max-width: 62px;
            }

            QLineEdit[class="correct-input"] {
                background-color: #ffffff;
                border: 1px solid #ABABAB;
                border-left: none;
                border-top-right-radius: 15px;
                border-bottom-right-radius: 15px;
                padding-left: 8px;
                color: #333333;
            }

            QLineEdit:focus, *[class="correct-input"]:focus {
                border: 1px solid #007BFF;
            }

            QComboBox[class="correct-input"] {
                height: 30px;
                border: 1px solid #999;
                padding: 0px 10px 0px;
                background-color: #ffffff;
                color: #333333;
                font: 10pt "Inter";
                selection-background-color: #7eb4d7;
                border-top-right-radius: 15px;
                border-bottom-right-radius: 15px;
            }

            QLineEdit:hover, QComboBox[class="correct-input"]:hover {
                border: 1px solid #3498db;
            }

            QComboBox[class="correct-input"]::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left-width: 0px;
            }

            QComboBox[class="correct-input"]::down-arrow {
                image: url(:/Images/Images/caret-down.png);
                border: none;
                width: 10px;
                height: 14px;
            }

            QComboBox[class="correct-input"] QAbstractItemView {
                background-color: #ffffff;
                selection-background-color: #7eb4d7;
                border-radius: 5px;
            }

            QComboBox[class="correct-input"] QAbstractItemView::item {
                min-height: 35px;
                padding-left: 10px;
                border-radius: 4px;
            }
        """

        self.img_binary = None # from database
        self.btn_upload_img.clicked.connect(lambda: self.get_image())
        self.btn_delete.clicked.connect(lambda: remove_callback(self))

        self.init_answers()
        self.layout_inputs.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_card_body.setAlignment(Qt.AlignmentFlag.AlignTop)

    def init_answers(self):

        label_correct = QLabel("Correct:")
        label_correct.setProperty("class", "correct-label")
        label_correct.setStyleSheet(self.input_css)

        if self.item_type == "Identification":
            self.ans = QLineEdit()
            self.ans.setMinimumSize(QSize(0, 30))
            self.ans.setProperty("class", "correct-input")
            self.ans.setStyleSheet(self.input_css)
            h_layout = QHBoxLayout()
            h_layout.addWidget(label_correct)
            h_layout.addWidget(self.ans)
            h_layout.setSpacing(0)
            self.layout_inputs.addLayout(h_layout)

        elif self.item_type == "Multiple Choice":
            self.choices = [] # To store QLineEdits if you need to access their text later
            self.options_data = [("A.", ""), ("B.", ""), ("C.", "")]

            for label_text, placeholder in self.options_data:
                h_layout = QHBoxLayout()

                lbl = QLabel(label_text)
                lbl.setProperty("class", "correct-label")
                lbl.setStyleSheet(self.input_css)

                edit = QLineEdit(placeholder)
                edit.setMinimumSize(QSize(0, 30))
                edit.setProperty("class", "correct-input")
                edit.setStyleSheet(self.input_css)
                self.choices.append(edit) # Store reference

                h_layout.addWidget(lbl)
                h_layout.addWidget(edit)
                h_layout.setSpacing(0)
                self.layout_inputs.addLayout(h_layout)

            self.correct = NoScrollComboBox()
            self.correct.addItems(["A", "B", "C"])
            self.correct.setMinimumSize(QSize(0, 30))
            self.correct.setProperty("class", "correct-input")
            self.correct.setStyleSheet(self.input_css)
            self.correct.setFocusPolicy(Qt.StrongFocus)
            h_layout = QHBoxLayout()
            h_layout.addWidget(label_correct)
            h_layout.addWidget(self.correct)
            h_layout.setSpacing(0)
            self.layout_inputs.addLayout(h_layout)

        else: # True/False
            self.ans = NoScrollComboBox(); self.ans.addItems(["True", "False"])
            self.ans.setMinimumSize(QSize(0, 30))
            self.ans.setProperty("class", "correct-input")
            self.ans.setStyleSheet(self.input_css)
            self.ans.setFocusPolicy(Qt.StrongFocus)
            h_layout = QHBoxLayout()
            h_layout.addWidget(label_correct)
            h_layout.addWidget(self.ans)
            h_layout.setSpacing(0)
            self.layout_inputs.addLayout(h_layout)

    def get_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")

        if file_path:
            self.img_path = file_path
            source_pixmap = QPixmap(file_path)
            square_pixmap = source_pixmap.scaled(
                self.label_q_image.width(), self.label_q_image.height(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
            self.label_q_image.setPixmap(square_pixmap)



class QuizCreatorDialog(QDialog, Ui_QuizCreatorDialog):
    def __init__(self, q_num, g_period, lesson_id, diff_level):
        super().__init__()
        self.setupUi(self)

        self.difficulty_group = QButtonGroup(self)
        self.difficulty_group.setExclusive(True)
        self.level_map = { 1: self.btnEasy, 2: self.btnAverage, 3: self.btnHard }

        for idx, btn in self.level_map.items():
            btn.setCheckable(True)
            self.difficulty_group.addButton(btn, idx)
            btn.clicked.connect(lambda checked, i=idx: self.handle_level_click(i))

        button = self.difficulty_group.button(diff_level)
        if button:
            button.setChecked(True)

        quiz = Quiz()
        self.record_id = {}
        self.record_mc = {}
        self.record_tf = {}
        self.is_saved = False
        self.title_init = self.windowTitle()

        if q_num and g_period and lesson_id and diff_level:
            self.record_id, self.record_mc, self.record_tf, _, _, _ = quiz.retrieve_quiz(q_num, g_period, lesson_id, diff_level)

        self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)

        self.db_tools = DatabaseTools()
        self.util = Utility()

        self.itemsToRemove = []

        self.count_id = self.count_mc = self.count_tf = 0
        self.easy_count = self.average_count = self.hard_count = 0

        sql =  "SELECT 1 AS index, 'First Grading' AS itemname\n"
        sql += "UNION ALL\n"
        sql += "SELECT 2, 'Second Grading'\n"
        sql += "UNION ALL\n"
        sql += "SELECT 3, 'Third Grading'\n"
        sql += "UNION ALL\n"
        sql += "SELECT 4, 'Fourth Grading'\n"
        self.util.populate_pulldown(self.cbGradingPeriod, sql)

        self.btn_save.clicked.connect(self.save_to_db)
        self.save_shortcut.activated.connect(self.save_to_db)

        self.layout_identification.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_multiplechoice.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_trueorfalse.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.btnAddItem_id.clicked.connect(lambda: self.add_item("Identification", self.layout_identification))
        self.btnAddItem_mc.clicked.connect(lambda: self.add_item("Multiple Choice", self.layout_multiplechoice))
        self.btnAddItem_tf.clicked.connect(lambda: self.add_item("True or False", self.layout_trueorfalse))

        self.quiz_no.setValue(q_num)
        self.populate_pulldown_lesson()
        self.countLayoutChildren()

        idx = self.cbGradingPeriod.findData(g_period)
        if idx != -1:
            self.cbGradingPeriod.setCurrentIndex(idx)

        _idx = self.cbLessonName.findData(lesson_id)
        if _idx != -1:
            self.cbLessonName.setCurrentIndex(_idx)

        self.refresh_quiz()
        self.quiz_no.valueChanged.connect(self.refresh_quiz)
        self.cbGradingPeriod.currentIndexChanged.connect(self.populate_pulldown_lesson)
        self.cbLessonName.currentIndexChanged.connect(self.refresh_quiz)

    def handle_level_click(self, idx):
        self.refresh_quiz()

        quiz = Quiz()
        q_num = self.quiz_no.value()
        g_period = self.cbGradingPeriod.currentData()
        lesson_id = self.cbLessonName.currentData()
        diff_level = self.difficulty_group.checkedId()
        record_id, record_mc, record_tf, _, _, _ = quiz.retrieve_quiz(q_num, g_period, lesson_id, diff_level)

        record_db = {}
        record_self = {}

        if diff_level == 1:
            record_db = record_id
            record_self = self.record_id
        elif diff_level == 2:
            record_db = record_mc
            record_self = self.record_mc
        elif diff_level == 3:
            record_db = record_tf
            record_self = self.record_tf

        if not self.is_saved and record_db and record_self and record_self != record_db:
            w_title = self.windowTitle()
            self.title_init = w_title
            self.setWindowTitle(f"{w_title} *")

        if q_num and g_period and lesson_id and diff_level:
            self.record_id, self.record_mc, self.record_tf, _, _, _ = quiz.retrieve_quiz(q_num, g_period, lesson_id, diff_level)
            self.is_saved = False

    def countLayoutChildren(self):
        sections = [
            (self.layout_identification, "count_id", self.label_id_count),
            (self.layout_multiplechoice, "count_mc", self.label_mc_count),
            (self.layout_trueorfalse, "count_tf", self.label_tf_count)
        ]

        for layout, attr_name, label in sections:
            actual_count = 0
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, QuizItemWidget):
                    actual_count += 1
                    widget.label_itemno.setText(f"ITEM {actual_count}")

            setattr(self, attr_name, actual_count)

            suffix = "item" if actual_count <= 1 else "items"
            label.setText(f"{actual_count} {suffix}")

        self.updateTotalScoreDisplay()

    def updateTotalScoreDisplay(self):
        quiz = Quiz()
        scores = quiz.getQuizTotalScore(self.quiz_no.value(), self.cbGradingPeriod.currentData(), self.cbLessonName.currentData())
        easy_score, average_score, hard_score, total_score = scores

        score_per_level = ""

        match self.difficulty_group.checkedId():
            case 1:
                score_per_level = f"{easy_score}"
            case 2:
                score_per_level = f"{average_score}"
            case 3:
                score_per_level = f"{hard_score}"

        self.label_scoreperlevel.setText(score_per_level)
        self.label_totalScore.setText(f"{total_score}")

    def populate_pulldown_lesson(self):
        selected_period = self.cbGradingPeriod.currentData()
        self.refresh_quiz()

        if not selected_period:
            return

        sql = 'SELECT\n'
        sql += '    lesson_id\n'
        sql += '    ,title\n'
        sql += 'FROM cai.tbl_lessons\n'
        sql += 'WHERE gradingperiod = %s\n'
        sql += 'ORDER BY chapter, lessonnum ASC'
        self.util.populate_pulldown(self.cbLessonName, sql, params=(selected_period,), add_empty=True)

    def add_item(self, name, container):
        widget = QuizItemWidget(name, self.remove_item)
        container.addWidget(widget)
        container.setSpacing(10)
        self.countLayoutChildren()

    def refresh_quiz(self):
        """Refreshes all quiz sections from the database."""
        lesson_id = self.cbLessonName.currentData()
        self.clear_layout(self.layout_identification)
        self.clear_layout(self.layout_multiplechoice)
        self.clear_layout(self.layout_trueorfalse)

        self.countLayoutChildren()
        self.multiplier_easy.setValue(1)
        self.multiplier_average.setValue(1)
        self.multiplier_hard.setValue(1)

        if not lesson_id:
            return

        params = (
            self.quiz_no.value(),
            self.cbGradingPeriod.currentData(),
            lesson_id,
            self.difficulty_group.checkedId()
        )

        sections = [
            (self.layout_identification, "Identification"),
            (self.layout_multiplechoice, "Multiple Choice"),
            (self.layout_trueorfalse, "True or False")
        ]

        for layout, item_type in sections:
            layout.setSpacing(5)

            if item_type == "Identification":
                sql  = "SELECT QI.idkey, QI.question, QI.imagequestion, QI.correct_answer\n"
                sql += "FROM cai.tbl_quiz Q\n"
                sql += f"INNER JOIN CAI.TBL_QUIZIDENTIFICATION QI\n"
                sql += "    ON Q.quiznumber = QI.quiznumber\n"
                sql += "    AND Q.gradingperiod = QI.gradingperiod\n"
                sql += "    AND Q.lessonid = QI.lessonid\n"
                sql += "WHERE Q.quiznumber = %s\n"
                sql += "    AND Q.gradingperiod = %s\n"
                sql += "    AND Q.lessonid = %s"
                sql += "    AND QI.DIFFICULTYLEVEL = %s"

            if item_type == "Multiple Choice":
                sql  = "SELECT MC.mckey, MC.question, MC.imagequestion, MC.choice_a, MC.choice_b, MC.choice_c, MC.correct_answer\n"
                sql += "FROM cai.tbl_quiz Q\n"
                sql += f"INNER JOIN CAI.TBL_QUIZMULTIPLECHOICE MC\n"
                sql += "    ON Q.quiznumber = MC.quiznumber\n"
                sql += "    AND Q.gradingperiod = MC.gradingperiod\n"
                sql += "    AND Q.lessonid = MC.lessonid\n"
                sql += "WHERE Q.quiznumber = %s\n"
                sql += "    AND Q.gradingperiod = %s\n"
                sql += "    AND Q.lessonid = %s"
                sql += "    AND MC.DIFFICULTYLEVEL = %s"

            if item_type == "True or False":
                sql  = "SELECT TF.tfkey, TF.question, TF.imagequestion, TF.correct_answer\n"
                sql += "FROM cai.tbl_quiz Q\n"
                sql += f"INNER JOIN CAI.TBL_QUIZTRUEORFALSE TF\n"
                sql += "    ON Q.quiznumber = TF.quiznumber\n"
                sql += "    AND Q.gradingperiod = TF.gradingperiod\n"
                sql += "    AND Q.lessonid = TF.lessonid\n"
                sql += "WHERE Q.quiznumber = %s\n"
                sql += "    AND Q.gradingperiod = %s\n"
                sql += "    AND Q.lessonid = %s"
                sql += "    AND TF.DIFFICULTYLEVEL = %s"

            records = self.db_tools.fetch_all(sql, (params[0], params[1], params[2], params[3]))

            for row in records:
                new_w = QuizItemWidget(item_type, self.remove_item)

                if item_type == "Identification":
                    new_w.id = row.get("idkey")

                if item_type == "Multiple Choice":
                    new_w.id = row.get("mckey")

                if item_type == "True or False":
                    new_w.id = row.get("tfkey")

                new_w.txt_question.setPlainText(row.get("question", ""))
                imgQ = row.get("imagequestion", "")

                # Handle Image
                if not self.util.isEmpty(imgQ):
                    new_w.img_binary = bytes(imgQ)
                    image = QImage.fromData(bytes(imgQ))

                    if not image.isNull():
                        pixmap = QPixmap.fromImage(image)
                        new_w.label_q_image.setPixmap(pixmap)

                if item_type == "Identification":
                    new_w.ans.setText(row.get("correct_answer", ""))

                elif item_type == "Multiple Choice":
                    new_w.choices[0].setText(row.get("choice_a", ""))
                    new_w.choices[1].setText(row.get("choice_b", ""))
                    new_w.choices[2].setText(row.get("choice_c", ""))

                    correct = ''

                    if row.get("choice_a", "") == row.get("correct_answer", ""):
                        correct = 'A'

                    elif row.get("choice_b", "") == row.get("correct_answer", ""):
                        correct = 'B'

                    elif row.get("choice_c", "") == row.get("correct_answer", ""):
                        correct = 'C'

                    new_w.correct.setCurrentText(correct)

                else: # True/False
                    new_w.ans.setCurrentText(row.get("correct_answer", ""))

                layout.addWidget(new_w)
                layout.setSpacing(10)

        sql  = "SELECT\n"
        sql += "    PUBLISH\n"
        sql += "FROM cai.tbl_quiz\n"
        sql += "WHERE quiznumber = %s\n"
        sql += "    AND gradingperiod = %s\n"
        sql += "    AND lessonid = %s"
        cursor, conn = self.db_tools.retrieve_records(sql, (params[0], params[1], params[2]))
        self.checkBoxPublish.setChecked(False)

        if cursor:
            record = cursor.fetchone()

            if not self.util.isEmpty(record):
                self.checkBoxPublish.setChecked(record[0])

            cursor.close()

        if conn: conn.close()

        quiz = Quiz()
        multipliers = quiz.getQuizMultiplier(params[0], params[1], params[2])

        if multipliers:
            self.multiplier_easy.setValue(multipliers[4])
            self.multiplier_average.setValue(multipliers[5])
            self.multiplier_hard.setValue(multipliers[6])

        self.countLayoutChildren()

    def clear_layout(self, layout):
        """Helper to safely remove all widgets from a layout."""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def remove_item(self, widget):
        self.itemsToRemove.append(widget.id)
        widget.setParent(None)
        widget.deleteLater()
        self.countLayoutChildren()

    def get_binary(self, path):
        if path and os.path.exists(path):
            with open(path, 'rb') as f:
                return f.read()
        return None

    def toggle_validation(self, widget, is_valid):
        if is_valid:
            # Keep border 2px but make it subtle/grey so layout doesn't shift
            widget.setStyleSheet("""
                border: 1px solid #ABABAB;
                border-radius: 10px;
                background-color: #FFF;
                padding: 0px 10px 0px;
                height: 30px;
            """)
        else:
            widget.setStyleSheet("""
                border: 2px solid #FF8A90;
                border-radius: 10px;
                background-color: #FFC2C5;
                padding: 0px 10px 0px;
                height: 30px;
            """)

    def validate_inputs(self):
        is_valid = True

        # Validate Lesson Name
        if not self.cbLessonName.currentData():
            self.toggle_validation(self.cbLessonName, False)
            is_valid = False
        else:
            self.toggle_validation(self.cbLessonName, True)

        # Validate each QuizItemWidget
        for layout in [self.verticalLayout_2, self.layout_multiplechoice, self.layout_trueorfalse]:
            for i in range(layout.count()):
                w = layout.itemAt(i).widget()
                if isinstance(w, QuizItemWidget):
                    # Check Question
                    if not w.txt_question.toPlainText().strip():
                        self.toggle_validation(w.txt_question, False)
                        is_valid = False
                    else:
                        self.toggle_validation(w.txt_question, True)

                    # Check Answer (Identification)
                    if hasattr(w, 'ans') and isinstance(w.ans, QLineEdit):
                        if not w.ans.text().strip():
                            self.toggle_validation(w.ans, False)
                            is_valid = False
                        else:
                            self.toggle_validation(w.ans, True)
        return is_valid
    
    def count_quiz(self, quiznumber, gradingperiod, lessonid):
        sql = """
            SELECT 
                COUNT(*) AS quiz_count
            FROM (
                SELECT QUIZNUMBER FROM CAI.TBL_QUIZIDENTIFICATION
                UNION ALL
                SELECT QUIZNUMBER FROM CAI.TBL_QUIZMULTIPLECHOICE
                UNION ALL
                SELECT QUIZNUMBER FROM CAI.TBL_QUIZTRUEORFALSE
            ) combined_quizzes
            WHERE 
                QUIZNUMBER = %s AND
                GRADINGPERIOD = %s AND
                LESSONID = %s;
        """

        record = self.db_tools.fetch_all(sql, (quiznumber, gradingperiod, lessonid))
        quiz_count = 0

        if record:
            quiz_count = record[0]['quiz_count']

        return quiz_count

    def save_to_db(self):
        try:
            if not self.validate_inputs():
                QMessageBox.warning(self, "Validation Error", "Please fill in all required fields.")
                return

            q_num = self.quiz_no.value()
            g_period = self.cbGradingPeriod.currentData()
            l_id = self.cbLessonName.currentData()

            id_count = self.layout_identification.count()
            mc_count = self.layout_multiplechoice.count()
            tf_count = self.layout_trueorfalse.count()

            conn = self.db_tools.get_connection()
            conn.autocommit = False

            with conn.cursor() as cur:

                sql = """
                    DELETE FROM cai.tbl_quizidentification WHERE quiznumber = %s AND gradingperiod = %s AND lessonid = %s AND difficultylevel = %s;
                    DELETE FROM cai.tbl_quizmultiplechoice WHERE quiznumber = %s AND gradingperiod = %s AND lessonid = %s AND difficultylevel = %s;
                    DELETE FROM cai.tbl_quiztrueorfalse WHERE quiznumber = %s AND gradingperiod = %s AND lessonid = %s AND difficultylevel = %s;
                """
                cur.execute(sql, (
                    q_num, g_period, l_id, self.difficulty_group.checkedId(),
                    q_num, g_period, l_id, self.difficulty_group.checkedId(),
                    q_num, g_period, l_id, self.difficulty_group.checkedId()
                ))
                ctr = 1

                for i in range(id_count):
                    w = self.layout_identification.itemAt(i).widget()
                    if not isinstance(w, QuizItemWidget): continue

                    img = self.get_binary(w.img_path)
                    sql = """
                        INSERT INTO CAI.TBL_QUIZIDENTIFICATION (
                            QUIZNUMBER,
                            GRADINGPERIOD,
                            ITEMNO,
                            LESSONID,
                            QUESTION,
                            CORRECT_ANSWER,
                            IMAGEQUESTION,
                            DIFFICULTYLEVEL
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """

                    cur.execute(sql, (
                        q_num,
                        g_period,
                        ctr,
                        l_id,
                        w.txt_question.toPlainText().strip(),
                        w.ans.text(),
                        psycopg2.Binary(img) if img else w.img_binary,
                        self.difficulty_group.checkedId()
                    ))

                    ctr += 1

                for i in range(mc_count):
                    w = self.layout_multiplechoice.itemAt(i).widget()
                    if not isinstance(w, QuizItemWidget): continue

                    img = self.get_binary(w.img_path)
                    sql = """
                        INSERT INTO CAI.TBL_QUIZMULTIPLECHOICE (
                            QUIZNUMBER,
                            GRADINGPERIOD,
                            ITEMNO,
                            LESSONID,
                            QUESTION,
                            CHOICE_A,
                            CHOICE_B,
                            CHOICE_C,
                            CORRECT_ANSWER,
                            IMAGEQUESTION,
                            DIFFICULTYLEVEL
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

                    correct = None

                    if w.correct.currentText() == 'A':
                        correct = w.choices[0].text()

                    elif w.correct.currentText() == 'B':
                        correct = w.choices[1].text()

                    elif w.correct.currentText() == 'C':
                        correct = w.choices[2].text()

                    cur.execute(sql, (
                        self.quiz_no.value(),
                        g_period,
                        ctr,
                        l_id,
                        w.txt_question.toPlainText().strip(),
                        w.choices[0].text(),
                        w.choices[1].text(),
                        w.choices[2].text(),
                        correct,
                        psycopg2.Binary(img) if img else w.img_binary,
                        self.difficulty_group.checkedId()
                    ))

                    ctr += 1

                for i in range(tf_count):
                    w = self.layout_trueorfalse.itemAt(i).widget()
                    if not isinstance(w, QuizItemWidget): continue

                    img = self.get_binary(w.img_path)
                    sql  = """
                        INSERT INTO CAI.TBL_QUIZTRUEORFALSE (
                            QUIZNUMBER
                            ,GRADINGPERIOD
                            ,ITEMNO
                            ,LESSONID
                            ,QUESTION
                            ,CORRECT_ANSWER
                            ,IMAGEQUESTION
                            ,DIFFICULTYLEVEL
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """

                    cur.execute(sql, (
                        self.quiz_no.value(),
                        g_period,
                        ctr,
                        l_id,
                        w.txt_question.toPlainText().strip(),
                        w.ans.currentText(),
                        psycopg2.Binary(img) if img else w.img_binary,
                        self.difficulty_group.checkedId()
                    ))

                    ctr += 1

                sql = """
                    UPDATE cai.tbl_quiz
                    SET PUBLISH = CASE 
                        WHEN quiznumber = %s AND gradingperiod = %s AND lessonid = %s THEN %s
                        ELSE false
                    END;

                    WITH QuizCounts AS (
                        SELECT 
                            COUNT(*) AS total,
                            COUNT(*) FILTER (WHERE DIFFICULTYLEVEL = 1) AS easy,
                            COUNT(*) FILTER (WHERE DIFFICULTYLEVEL = 2) AS average,
                            COUNT(*) FILTER (WHERE DIFFICULTYLEVEL = 3) AS hard
                        FROM (
                            SELECT QUIZNUMBER, GRADINGPERIOD, LESSONID, DIFFICULTYLEVEL FROM CAI.TBL_QUIZIDENTIFICATION
                            UNION ALL
                            SELECT QUIZNUMBER, GRADINGPERIOD, LESSONID, DIFFICULTYLEVEL FROM CAI.TBL_QUIZMULTIPLECHOICE
                            UNION ALL
                            SELECT QUIZNUMBER, GRADINGPERIOD, LESSONID, DIFFICULTYLEVEL FROM CAI.TBL_QUIZTRUEORFALSE
                        ) Q
                        WHERE Q.QUIZNUMBER = %s 
                        AND Q.GRADINGPERIOD = %s 
                        AND Q.LESSONID = %s
                    )
                    INSERT INTO CAI.TBL_QUIZ (
                        QUIZNUMBER,
                        GRADINGPERIOD,
                        LESSONID,
                        TOTAL_ITEMS,
                        EASY_COUNT,
                        AVERAGE_COUNT,
                        HARD_COUNT
                    )
                    SELECT 
                        %s, %s, %s,
                        C.total, C.easy, C.average, C.hard
                    FROM QuizCounts C
                    ON CONFLICT (QUIZNUMBER, GRADINGPERIOD, LESSONID)
                    DO UPDATE SET
                        TOTAL_ITEMS = EXCLUDED.TOTAL_ITEMS,
                        EASY_COUNT = EXCLUDED.EASY_COUNT,
                        AVERAGE_COUNT = EXCLUDED.AVERAGE_COUNT,
                        HARD_COUNT = EXCLUDED.HARD_COUNT;
                """

                params = (
                    q_num, g_period, l_id, self.checkBoxPublish.isChecked(),
                    q_num, g_period, l_id,
                    q_num, g_period, l_id
                )

                cur.execute(sql, params)

                mult_easy = self.multiplier_easy.value()
                mult_average = self.multiplier_average.value()
                mult_hard = self.multiplier_hard.value()
                total_score = self.label_scoreperlevel.text()

                sql  = "INSERT INTO CAI.TBL_SCOREMULTIPLIER (\n"
                sql += "    QUIZNUMBER,\n"
                sql += "    LESSONID,\n"
                sql += "    GRADINGPERIOD,\n"
                sql += "    EASY_MULTIPLIER,\n"
                sql += "    AVERAGE_MULTIPLIER,\n"
                sql += "    HARD_MULTIPLIER,\n"
                sql += "    TOTAL_POSSIBLE_POINTS\n"
                sql += ") VALUES (%s, %s, %s, %s, %s, %s, %s)\n"
                sql += "ON CONFLICT (QUIZNUMBER, LESSONID, GRADINGPERIOD)\n"
                sql += "DO UPDATE SET\n"
                sql += "    EASY_MULTIPLIER = EXCLUDED.EASY_MULTIPLIER,\n"
                sql += "    AVERAGE_MULTIPLIER = EXCLUDED.AVERAGE_MULTIPLIER,\n"
                sql += "    HARD_MULTIPLIER = EXCLUDED.HARD_MULTIPLIER,\n"
                sql += "    TOTAL_POSSIBLE_POINTS = EXCLUDED.TOTAL_POSSIBLE_POINTS"

                data = (q_num, l_id, g_period, mult_easy, mult_average, mult_hard, total_score)
                cur.execute(sql, data)

                conn.commit()
                self.itemsToRemove.clear()

                QMessageBox.information(self, "Success", "Quiz updated successfully!")
                self.is_saved = True
                self.setWindowTitle(self.title_init)
                self.accept()

        except Exception as e:
            if conn: conn.rollback()
            print(f"Database Error: {e}")
            QMessageBox.critical(self, "Error", f"Failed to sync database: {e}")

        finally:
            if conn: conn.close()


class CardQuiz(QFrame, Ui_CardQuiz):
    """Custom widget representing a single card."""

    # Define a signal that carries a string (the student's name)
    clicked = Signal(object, str)

    def __init__(self, item_type):
        super().__init__()
        self.setupUi(self)

        self.util = Utility()

        self.item_type = item_type
        self.idKey = None
        self.itemno = 0
        self.question = ""
        self.choices = ""
        self.answer = ""
        self.imageQ = None

        # Ensure the widget can receive focus for keyboard navigation
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def displayAttributes(self):
        self.label_itemno.setText(f"ITEM {self.itemno}")
        self.label_question.setText(f"{self.question}")

        if self.choices:
            self.layout_body_text.addWidget(QLabel(self.choices))

        if self.answer:
            layout = QHBoxLayout()
            lbl = QLabel("Answer:")
            lbl.setMaximumSize(QSize(55, 55))
            lbl.setStyleSheet("font-weight: bold")
            lbl_ans = QLabel(self.answer)

            layout.addWidget(lbl)
            layout.addWidget(lbl_ans)
            self.layout_body_text.addLayout(layout)

        # Handle Image
        if not self.util.isEmpty(self.imageQ):
            image = QImage.fromData(bytes(self.imageQ))
            if not image.isNull():
                pixmap = QPixmap.fromImage(image)
                self.label_q_image.setPixmap(pixmap)

    def mousePressEvent(self, event):
        """Triggered when the user clicks the card."""
        if event.button() == Qt.MouseButton.LeftButton:
            # self.clicked.emit(self, self.label_studentid.text())
            super().mousePressEvent(event)

    def focusInEvent(self, event):
        """Triggered when the card gains focus (e.g., via Tab key)."""
        # if not self.property("selected"):
            # self.clicked.emit(self, self.label_studentid.text())
        super().focusInEvent(event)

    def set_selected(self, selected: bool):
        """Updates the property and refreshes the style."""
        self.setProperty("selected", selected)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
