import sys, os
import psycopg2

from PySide6.QtGui import QStandardItemModel, QStandardItem, QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QComboBox,
                             QSpinBox, QPushButton, QScrollArea, QButtonGroup,
                             QMessageBox, QFileDialog, QFrame, QDialog)
from PySide6.QtCore import Qt, QSize, Signal

from App.CRUDTools import DatabaseTools
from App.Tools import Utility
from App.QuizDialog import Ui_QuizCreatorDialog
from App.CardQuiz import Ui_CardQuiz


class Quiz:
    def __init__(self):
        self.db_tools = DatabaseTools()

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
                quiz_record (tuple): total_items, id_level, mc_level, tf_level, quizlock from tbl_quiz

            Raises:
                N/A
        """

        quiz_record = (0, False)

        sql  = "SELECT\n"
        sql += "    COALESCE(TOTAL_ITEMS, 0) AS TOTAL_ITEMS,\n"
        sql += "    QUIZLOCK\n"
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
        sql_id += "    CORRECT_ANSWER_1,\n"
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

        return record_id, record_mc, record_tf, quiz_record, multipliers
    
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


class QuizItemWidget(QFrame):
    """A reusable row for a single quiz question."""
    def __init__(self, item_type, remove_callback):
        super().__init__()
        self.util = Utility()
        self.item_type = item_type
        self.img_path = None
        self.id = None
        self.setFrameShape(QFrame.StyledPanel)
        self.setObjectName("Card")
        self.setStyleSheet("#Card { border-radius: 16px; background-color: #FFF; }")

        self.input_css = """
            /* Styling the input field */
            QLineEdit {
                border: 1px solid #ABABAB;
                border-radius: 10px;
                background-color: #FFF;
                padding: 0px 10px 0px;
            }

            /* Highlight when typing (focus) */
            QLineEdit:focus {
                border: 1px solid #007BFF;
            }
        """

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(10)

        # Top Row: Question, Difficulty, Image, Delete
        top_row = QHBoxLayout()
        self.q_input = QLineEdit()
        self.q_input.setMinimumSize(QSize(0, 30))
        self.q_input.setStyleSheet(self.input_css)
        self.q_input.setPlaceholderText("Enter Question (e.g. 1 + 5 = ?)")

        self.btn_img = QPushButton("📸")
        self.btn_img.setFixedWidth(30)
        self.btn_img.setFixedHeight(30)
        self.btn_img.clicked.connect(self.get_image)

        self.img_binary = None
        self.img_label = QLabel("No Image")
        self.img_label.setStyleSheet("font-size: 9px; color: gray; background: transparent;")
        self.img_label.setScaledContents(True)

        self.btn_delete = QPushButton("✖")
        self.btn_delete.setFixedWidth(30)
        self.btn_delete.setFixedHeight(30)
        self.btn_delete.setStyleSheet("color: red; font-weight: bold;")
        self.btn_delete.clicked.connect(lambda: remove_callback(self))

        top_row.addWidget(self.q_input)
        top_row.addWidget(self.btn_img)
        top_row.addWidget(self.img_label)
        top_row.addWidget(self.btn_delete)
        self.main_layout.addLayout(top_row)

        # Bottom Row: Answer Fields
        self.bot_row = QHBoxLayout()
        self.init_answers()
        self.main_layout.addLayout(self.bot_row)

    def init_answers(self):

        if self.item_type == "Identification":
            self.ans = QLineEdit(); self.ans.setPlaceholderText("Correct Answer")
            self.ans.setMinimumSize(QSize(0, 30))
            self.ans.setStyleSheet(self.input_css)
            self.bot_row.addWidget(self.ans)

        elif self.item_type == "Multiple Choice":
            self.opts = [QLineEdit("A"), QLineEdit("B"), QLineEdit("C")]
            self.correct = QComboBox(); self.correct.addItems(["A", "B", "C"])
            self.correct.setMinimumSize(QSize(0, 30))
            self.correct.setStyleSheet(self.input_css)

            for opt in self.opts:
                opt.setMinimumSize(QSize(0, 30))
                opt.setStyleSheet(self.input_css)
                self.bot_row.addWidget(opt)

            label_correct = QLabel("Correct:")
            label_correct.setStyleSheet("background: transparent;")
            self.bot_row.addWidget(label_correct)
            self.bot_row.addWidget(self.correct)

        else: # True/False
            self.ans = QComboBox(); self.ans.addItems(["True", "False"])
            self.ans.setMinimumSize(QSize(0, 30))
            self.ans.setStyleSheet(self.input_css)
            self.bot_row.addWidget(self.ans)

    def get_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.img_path = file_path
            self.img_label.setText(os.path.basename(file_path))
            self.img_label.setStyleSheet("color: green;")


class QuizCreatorDialog(QDialog, Ui_QuizCreatorDialog):
    def __init__(self, q_num, g_period, lesson_id, diff_level):
        super().__init__()
        self.setupUi(self)
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

        self.btnAddItem_id.clicked.connect(lambda: self.add_item("Identification", self.verticalLayout_7))
        self.btnAddItem_mc.clicked.connect(lambda: self.add_item("Multiple Choice", self.verticalLayout_3))
        self.btnAddItem_tf.clicked.connect(lambda: self.add_item("True or False", self.verticalLayout_4))

        self.quiz_no.setValue(q_num)
        
        idx = self.cbGradingPeriod.findData(g_period)
        if idx != -1:
            self.cbGradingPeriod.setCurrentIndex(idx)

        _idx = self.cbLessonName.findData(lesson_id)
        if _idx != -1:
            self.cbLessonName.setCurrentIndex(_idx)

        self.populate_pulldown_lesson()
        self.countLayoutChildren()

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

        self.refresh_quiz()
        self.quiz_no.valueChanged.connect(self.refresh_quiz)
        self.cbGradingPeriod.currentIndexChanged.connect(self.populate_pulldown_lesson)
        self.cbLessonName.currentIndexChanged.connect(self.refresh_quiz)

    def handle_level_click(self, idx):
        self.refresh_quiz()

    def countLayoutChildren(self):
        sections = [
            (self.verticalLayout_7, "count_id", self.label_id_count),
            (self.verticalLayout_3, "count_mc", self.label_mc_count),
            (self.verticalLayout_4, "count_tf", self.label_tf_count)
        ]

        for layout, attr_name, label in sections:
            actual_count = 0
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, QuizItemWidget):
                    actual_count += 1
            
            setattr(self, attr_name, actual_count)

            suffix = "item" if actual_count <= 1 else "items"
            label.setText(f"{actual_count} {suffix}")

        self.updateTotalScoreDisplay()

    def updateTotalScoreDisplay(self):
        # Calculate weighted total
        total = (self.count_id * self.multiplier_easy.value()) + \
                (self.count_mc * self.multiplier_average.value()) + \
                (self.count_tf * self.multiplier_hard.value())
        
        self.label_totalScore.setText(f"{total}")
        return total

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
        self.clear_layout(self.verticalLayout_7)
        self.clear_layout(self.verticalLayout_3)
        self.clear_layout(self.verticalLayout_4)

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
            (self.verticalLayout_7, "Identification"),
            (self.verticalLayout_3, "Multiple Choice"),
            (self.verticalLayout_4, "True or False")
        ]

        for layout, item_type in sections:
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            layout.setSpacing(5)

            if item_type == "Identification":
                sql  = "SELECT QI.idkey, QI.question, QI.imagequestion, QI.correct_answer_1\n"
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
                sql  = "SELECT MC.mckey, MC.question, MC.imagequestion, MC.choice_a, MC.choice_b, MC.choice_c\n"
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

                new_w.q_input.setText(row.get("question", ""))
                imgQ = row.get("imagequestion", "")
                
                # Handle Image
                if not self.util.isEmpty(imgQ):
                    new_w.img_binary = bytes(imgQ)
                    image = QImage.fromData(bytes(imgQ))
                    
                    if not image.isNull():
                        pixmap = QPixmap.fromImage(image)
                        new_w.img_label.setPixmap(pixmap)
                        new_w.img_label.setMaximumWidth(30)
                        new_w.img_label.setMaximumHeight(30)

                if item_type == "Identification":
                    new_w.ans.setText(row.get("correct_answer_1", ""))

                elif item_type == "Multiple Choice":
                    new_w.opts[0].setText(row.get("choice_a", ""))
                    new_w.opts[1].setText(row.get("choice_b", ""))
                    new_w.opts[2].setText(row.get("choice_c", ""))
                    new_w.correct.setCurrentText(row.get("correct_answer", ""))

                else: # True/False
                    new_w.ans.setCurrentText(row.get("correct_answer", ""))

                layout.addWidget(new_w)
                layout.setSpacing(10)

        sql  = "SELECT\n"
        sql += "    QUIZLOCK\n"
        sql += "FROM cai.tbl_quiz\n"
        sql += "WHERE quiznumber = %s\n"
        sql += "    AND gradingperiod = %s\n"
        sql += "    AND lessonid = %s"
        cursor, conn = self.db_tools.retrieve_records(sql, (params[0], params[1], params[2]))
        self.checkBoxLockQuiz.setChecked(False)

        if cursor:
            record = cursor.fetchone()

            if not self.util.isEmpty(record): 
                self.checkBoxLockQuiz.setChecked(record[0])

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
        for layout in [self.verticalLayout_2, self.verticalLayout_3, self.verticalLayout_4]:
            for i in range(layout.count()):
                w = layout.itemAt(i).widget()
                if isinstance(w, QuizItemWidget):
                    # Check Question
                    if not w.q_input.text().strip():
                        self.toggle_validation(w.q_input, False)
                        is_valid = False
                    else:
                        self.toggle_validation(w.q_input, True)

                    # Check Answer (Identification)
                    if hasattr(w, 'ans') and isinstance(w.ans, QLineEdit):
                        if not w.ans.text().strip():
                            self.toggle_validation(w.ans, False)
                            is_valid = False
                        else:
                            self.toggle_validation(w.ans, True)
        return is_valid

    def save_to_db(self):
        try:
            if not self.validate_inputs():
                QMessageBox.warning(self, "Validation Error", "Please fill in all required fields.")
                return

            q_num = self.quiz_no.value()
            g_period = self.cbGradingPeriod.currentData()
            l_id = self.cbLessonName.currentData()

            total_count = self.count_id + self.count_mc + self.count_tf
            sql  = "INSERT INTO CAI.TBL_QUIZ (\n"
            sql += "    QUIZNUMBER\n"
            sql += "    ,GRADINGPERIOD\n"
            sql += "    ,LESSONID\n"
            sql += "    ,TOTAL_ITEMS\n"
            sql += "    ,EASY_COUNT\n"
            sql += "    ,AVERAGE_COUNT\n"
            sql += "    ,HARD_COUNT\n"
            sql += "    ,QUIZLOCK\n"
            sql += ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)\n"
            sql += "ON CONFLICT (QUIZNUMBER, GRADINGPERIOD, LESSONID)\n"
            sql += "DO UPDATE SET\n"
            sql += "    TOTAL_ITEMS = EXCLUDED.TOTAL_ITEMS,\n"
            sql += "    EASY_COUNT = EXCLUDED.EASY_COUNT,\n"
            sql += "    AVERAGE_COUNT = EXCLUDED.AVERAGE_COUNT,\n"
            sql += "    HARD_COUNT = EXCLUDED.HARD_COUNT,\n"
            sql += "    QUIZLOCK = EXCLUDED.QUIZLOCK\n"

            self.db_tools.execute_query(sql, (
                q_num,
                g_period,
                l_id,
                total_count,
                self.count_id,
                self.count_mc,
                self.count_tf,
                True if self.checkBoxLockQuiz.isChecked() else False
            ))

            for i in range(self.verticalLayout_7.count()):
                w = self.verticalLayout_7.itemAt(i).widget()
                if not isinstance(w, QuizItemWidget): continue

                img = self.get_binary(w.img_path)
                sql  = "INSERT INTO CAI.TBL_QUIZIDENTIFICATION (\n"
                sql += "    QUIZNUMBER,\n"
                sql += "    GRADINGPERIOD,\n"
                sql += "    ITEMNO,\n"
                sql += "    LESSONID,\n"
                sql += "    QUESTION,\n"
                sql += "    CORRECT_ANSWER_1,\n"
                sql += "    IMAGEQUESTION,\n"
                sql += "    DIFFICULTYLEVEL\n"
                sql += ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)\n"
                sql += "ON CONFLICT (QUIZNUMBER, GRADINGPERIOD, ITEMNO, LESSONID, DIFFICULTYLEVEL)\n"
                sql += "DO UPDATE SET\n"
                sql += "    QUESTION = EXCLUDED.QUESTION,\n"
                sql += "    CORRECT_ANSWER_1 = EXCLUDED.CORRECT_ANSWER_1,\n"
                sql += "    IMAGEQUESTION = EXCLUDED.IMAGEQUESTION,\n"
                sql += "    DIFFICULTYLEVEL = EXCLUDED.DIFFICULTYLEVEL\n"

                self.db_tools.execute_query(sql, (
                    q_num,
                    g_period,
                    i+1,
                    l_id,
                    w.q_input.text(),
                    w.ans.text(),
                    psycopg2.Binary(img) if img else w.img_binary,
                    self.difficulty_group.checkedId()
                ))

            for i in range(self.verticalLayout_3.count()):
                w = self.verticalLayout_3.itemAt(i).widget()
                if not isinstance(w, QuizItemWidget): continue

                img = self.get_binary(w.img_path)
                sql  = "INSERT INTO CAI.TBL_QUIZMULTIPLECHOICE (\n"
                sql += "    QUIZNUMBER,\n"
                sql += "    GRADINGPERIOD,\n"
                sql += "    ITEMNO,\n"
                sql += "    LESSONID,\n"
                sql += "    QUESTION,\n"
                sql += "    CHOICE_A,\n"
                sql += "    CHOICE_B,\n"
                sql += "    CHOICE_C,\n"
                sql += "    CORRECT_ANSWER,\n"
                sql += "    IMAGEQUESTION,\n"
                sql += "    DIFFICULTYLEVEL\n"
                sql += ") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)\n"
                sql += "ON CONFLICT (QUIZNUMBER, GRADINGPERIOD, ITEMNO, LESSONID, DIFFICULTYLEVEL)\n"
                sql += "DO UPDATE SET\n"
                sql += "    QUESTION = EXCLUDED.QUESTION,\n"
                sql += "    CHOICE_A = EXCLUDED.CHOICE_A,\n"
                sql += "    CHOICE_B = EXCLUDED.CHOICE_B,\n"
                sql += "    CHOICE_C = EXCLUDED.CHOICE_C,\n"
                sql += "    CORRECT_ANSWER = EXCLUDED.CORRECT_ANSWER,\n"
                sql += "    IMAGEQUESTION = EXCLUDED.IMAGEQUESTION,\n"
                sql += "    DIFFICULTYLEVEL = EXCLUDED.DIFFICULTYLEVEL\n"

                self.db_tools.execute_query(sql, (
                    self.quiz_no.value(),
                    g_period,
                    i+1,
                    l_id,
                    w.q_input.text(),
                    w.opts[0].text(),
                    w.opts[1].text(),
                    w.opts[2].text(),
                    w.correct.currentText(),
                    psycopg2.Binary(img) if img else w.img_binary,
                    self.difficulty_group.checkedId()
                ))

            for i in range(self.verticalLayout_4.count()):
                w = self.verticalLayout_4.itemAt(i).widget()
                if not isinstance(w, QuizItemWidget): continue

                img = self.get_binary(w.img_path)
                sql  = "INSERT INTO CAI.TBL_QUIZTRUEORFALSE (\n"
                sql += "    QUIZNUMBER\n"
                sql += "    ,GRADINGPERIOD\n"
                sql += "    ,ITEMNO\n"
                sql += "    ,LESSONID\n"
                sql += "    ,QUESTION\n"
                sql += "    ,CORRECT_ANSWER\n"
                sql += "    ,IMAGEQUESTION\n"
                sql += "    ,DIFFICULTYLEVEL\n"
                sql += ") VALUES (%s,%s,%s,%s,%s,%s,%s,%s)\n"
                sql += "ON CONFLICT (QUIZNUMBER, GRADINGPERIOD, ITEMNO, LESSONID, DIFFICULTYLEVEL)\n"
                sql += "DO UPDATE SET\n"
                sql += "    QUESTION = EXCLUDED.QUESTION,\n"
                sql += "    CORRECT_ANSWER = EXCLUDED.CORRECT_ANSWER,\n"
                sql += "    IMAGEQUESTION = EXCLUDED.IMAGEQUESTION,\n"
                sql += "    DIFFICULTYLEVEL = EXCLUDED.DIFFICULTYLEVEL\n"

                self.db_tools.execute_query(sql, (
                    self.quiz_no.value(),
                    g_period,
                    i+1,
                    l_id,
                    w.q_input.text(),
                    w.ans.currentText(),
                    psycopg2.Binary(img) if img else w.img_binary,
                    self.difficulty_group.checkedId()
                ))

            mult_easy = self.multiplier_easy.value()
            mult_average = self.multiplier_average.value()
            mult_hard = self.multiplier_hard.value()
            total_score = self.label_totalScore.text()

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
            self.db_tools.execute_query(sql, data)

            if self.itemsToRemove:
                # Filter out None values just in case
                ids_to_delete = [i for i in self.itemsToRemove if i is not None]
                
                if ids_to_delete:
                    # Generic deletion query - you'll need to run this for each table 
                    # since idKey, mcKey, and tfKey are likely distinct columns
                    tables = [
                        ("cai.tbl_quizidentification", "idkey"),
                        ("cai.tbl_quizmultiplechoice", "mckey"),
                        ("cai.tbl_quiztrueorfalse", "tfkey")
                    ]
                    
                    for table, col in tables:
                        sql_del = f"DELETE FROM {table} WHERE {col} = ANY(%s)"
                        self.db_tools.execute_query(sql_del, (ids_to_delete,))

            self.itemsToRemove.clear()

            QMessageBox.information(self, "Success", "Quiz updated successfully!")
            self.accept()

        except Exception as e:
            print(f"Database Error: {e}")
            QMessageBox.critical(self, "Error", f"Failed to sync database: {e}")


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
        self.itemno = ""
        self.question = ""
        self.answer = ""
        self.imageQ = None

        # Ensure the widget can receive focus for keyboard navigation
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def setAttributes(self):
        self.label_itemno.setText(f"ITEM {self.itemno}")
        self.label_question.setText(f"{self.question}")
        self.label_ans.setText(f"{self.answer}")

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
