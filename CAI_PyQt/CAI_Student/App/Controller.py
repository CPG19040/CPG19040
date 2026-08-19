import os
from PySide6.QtCore import QSettings, QPoint, QEasingCurve, QPropertyAnimation, QParallelAnimationGroup, Qt, QUrl, QEvent, QObject, QDate
from PySide6.QtWidgets import QMainWindow, QButtonGroup
from PySide6.QtGui import QFontDatabase, QImage, QPixmap
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer, QAudioOutput

from App.Login import Login
from App.FormHome import Ui_FormHome
from App.Student import Student
from App.Tools import Utility, WindowHandler, CustomShapeDialog, WickPlayer
from App.CRUDTools import DatabaseTools
from App.Lessons import Lessons, LessonCard
from App.MyScores import CardScores
from App.Quiz import Quiz, QuizUtils
from App.MyScores import MyScores


# Notice: Controller no longer inherits from QObject
class Controller:

    GRADING_PERIOD = 0

    def __init__(self):
        self.settings = QSettings("CAI_System", "CAI_Student_App")
        self.util = Utility()
        self.db_tools = DatabaseTools()
        self.audio_path = self.util.get_resource_path(os.path.join("..", "Audio"))

        self.login_win = Login()
        self.login_win.login_success.connect(self.on_login_success)

        self.today, self.base_year, self.next_year = self.util.get_dynamic_school_year_dates()
        self.school_year = f"{self.base_year}-{self.next_year}"

        self.load_fonts()
        self.check_session()

    def check_session(self):
        sid = self.settings.value("studentid")
        if sid:
            user = {
                "studentid": sid,
                "firstname": self.settings.value("firstname"),
                "middlename": self.settings.value("middlename"),
                "lastname": self.settings.value("lastname"),
                "gender": self.settings.value("gender"),
                "section": self.settings.value("section"),
            }
            self.show_home(user)
        else:
            self.login_win.show()

    def on_login_success(self, user):
        self.settings.setValue("studentid", user["studentid"])
        self.settings.sync()
        self.show_home(user)

    def show_home(self, user):
        self.home_win = QMainWindow()
        self.ui = Ui_FormHome()
        self.ui.setupUi(self.home_win)

        self.get_dynamic_grading_period_dates()

        # --- EVENT FILTER IMPLEMENTATION ---
        # 1. Create a dedicated QObject inside show_home to act as the filter
        self.home_event_filter = QObject(self.home_win)

        # 2. Define the event filter logic dynamically
        def custom_event_filter(watched_obj, event):
            if event.type() == QEvent.Type.Enter:
                if watched_obj == self.ui.btnClose:
                    self.sounds["exit_sound"].stop()
                    self.sounds["exit_sound"].play()
                elif watched_obj == self.ui.btnQuit:
                    self.sounds["quit_sound"].stop()
                    self.sounds["quit_sound"].play()
                elif watched_obj == self.ui.btnLessons:
                    self.sounds["lesson_sound"].stop()
                    self.sounds["lesson_sound"].play()
                elif watched_obj == self.ui.btnQuiz:
                    self.sounds["quiz_sound"].stop()
                    self.sounds["quiz_sound"].play()
                elif watched_obj == self.ui.btnExercise:
                    self.sounds["exer_sound"].stop()
                    self.sounds["exer_sound"].play()
                elif watched_obj == self.ui.btnScores:
                    self.sounds["scores_sound"].stop()
                    self.sounds["scores_sound"].play()
                elif watched_obj == self.ui.btnGames:
                    self.sounds["games_sound"].stop()
                    self.sounds["games_sound"].play()

            # Since QObject doesn't have a customized eventFilter parent implementation here,
            # we just return False to let PySide handle the event naturally.
            return False

        # 3. Bind the logic to the QObject's eventFilter property
        self.home_event_filter.eventFilter = custom_event_filter
        # ----------------------------------------

        controls = [
            self.ui.btnMinimize,
            self.ui.btnMaximize,
            self.ui.btnClose,
            self.ui.btnQuit,
            self.ui.btnLessons,
            self.ui.btnQuiz,
            self.ui.btnExercise,
            self.ui.btnScores,
            self.ui.btnGames,
        ]

        for control in controls:
            control.setMouseTracking(True)
            # 4. Install the new locally defined filter object instead of 'self'
            control.installEventFilter(self.home_event_filter)

        path = os.path.join(self.audio_path, "bgMusic2.wav")
        self.home_win.player = QMediaPlayer()
        self.home_win.audio_output = QAudioOutput()
        self.home_win.player.setAudioOutput(self.home_win.audio_output)
        self.home_win.player.setSource(QUrl.fromLocalFile(path))
        self.home_win.audio_output.setVolume(0.7)
        self.login_win.player.stop()
        self.home_win.player.play()

        self.sounds = {}

        # Initialize sound effects
        sound_files = {
            "back_sound": "Back.wav",
            "exit_sound": "Exit.wav",
            "quit_sound": "Quit.wav",
            "quiz_sound": "TakeQuiz.wav",
            "lesson_sound": "Lessons.wav",
            "exer_sound": "Exercises.wav",
            "scores_sound": "MyScores.wav",
            "games_sound": "Games.wav",
        }

        for name, filename in sound_files.items():
            path = os.path.normpath(os.path.join(self.audio_path, filename))
            effect = QSoundEffect(self.home_event_filter) # Pass the filter or home_win as parent
            effect.setSource(QUrl.fromLocalFile(path))
            effect.setVolume(0.7)
            self.sounds[name] = effect

        # Remove OS default window frame
        self.home_win.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.home_win.setMouseTracking(True)

        self.window_handler = WindowHandler(self.home_win)

        self.ui.btnClose.clicked.connect(self.home_win.close)
        self.ui.btnMinimize.clicked.connect(self.home_win.showMinimized)
        self.ui.btnMaximize.clicked.connect(self.toggle_maximize)

        self.nav_group = QButtonGroup(self.home_win)
        self.nav_group.setExclusive(True)

        # Navigation
        self.nav_map = {
            self.ui.btnLessons: 0,
            self.ui.btnQuiz: 1,
            self.ui.btnExercise: 3,
            self.ui.btnScores: 4,
            self.ui.btnGames: 5
        }

        for btn, idx in self.nav_map.items():
            btn.setCheckable(True)
            self.nav_group.addButton(btn)
            btn.clicked.connect(lambda checked, b=btn, i=idx: self.handle_nav_click(b, i))

        self.display_lessons()
        self.ui.btnLessons.setChecked(True)

        self.ui.btnLessons.clicked.connect(self.display_lessons)
        self.ui.btn_retake.clicked.connect(lambda: self.slide_to_page(101))
        self.ui.btnSubmitQuiz.clicked.connect(self.save_quiz_answers)
        self.ui.btnQuit.clicked.connect(self.logout)
        self.ui.btnAddition.clicked.connect(lambda _, mode="addition": self.open_game(mode))
        self.ui.btnSubtraction.clicked.connect(lambda _, mode="subtraction": self.open_game(mode))

        self.display_section_info(user["studentid"])

        self.login_win.close()
        self.home_win.show()

    def toggle_maximize(self):
        if self.home_win.isMaximized():
            self.home_win.showNormal()
        else:
            self.home_win.showMaximized()

    def handle_nav_click(self, button, index):
        sid = self.settings.value("studentid")
        isTaken, record = Student().get_quiz_status(sid)

        # Take Quiz
        if index == 1:
            if isTaken:
                index = 2
                self.displayQuizAnswers()
            else:
                self.displayQuiz()

        elif index == 4:
            self.display_myscores()

        self.ui.label_score.setText(f"{record['quizscore']}/{record['totalscore']}")
        
        self.slide_to_page(index)
        button.setChecked(True)

    def slide_to_page(self, index):
        stack = self.ui.stackedWidget
        if stack.currentIndex() == index:
            return

        if index == 101:
            index = 1 # Back to [Take Quiz]
            self.displayQuiz()

        current_page = stack.currentWidget()
        next_page = stack.widget(index)
        width = stack.width()

        next_page.setGeometry(width, 0, width, stack.height())
        next_page.show()
        next_page.raise_()

        self.anim_group = QParallelAnimationGroup()

        anim_in = QPropertyAnimation(next_page, b"pos")
        anim_in.setDuration(450)
        anim_in.setStartValue(QPoint(width, 0))
        anim_in.setEndValue(QPoint(0, 0))
        anim_in.setEasingCurve(QEasingCurve.Type.OutCubic)

        anim_out = QPropertyAnimation(current_page, b"pos")
        anim_out.setDuration(450)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(-width, 0))
        anim_out.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.anim_group.addAnimation(anim_in)
        self.anim_group.addAnimation(anim_out)

        self.anim_group.finished.connect(lambda: stack.setCurrentIndex(index))
        self.anim_group.start()

    def logout(self):
        self.settings.clear()
        self.home_win.player.stop()
        self.home_win.close()
        self.login_win.show()
        self.login_win.player.play()
        self.login_win.txtPassword.clear()

    def load_fonts(self):
        path = self.util.get_resource_path(os.path.join("..", "Fonts"))
        loaded_count = 0

        if os.path.exists(path):
            for f in os.listdir(path):
                if f.endswith((".ttf", ".otf")):
                    font_path = os.path.join(path, f)
                    font_id = QFontDatabase.addApplicationFont(font_path)

                    if font_id != -1:
                        loaded_count += 1
                    else:
                        print(f"❌ Failed to load font: {f}")

            if loaded_count > 0:
                print(f"✅ {loaded_count} font(s) loaded successfully.")
            else:
                print("⚠️ Font folder found, but no valid fonts were loaded.")
        else:
            print(f"⚠️ Font directory not found at: {path}")

    def get_dynamic_grading_period_dates(self):

        sql = """
            SELECT gpid, gpname, startdate, enddate
            FROM cai.tbl_grading_period;
        """
        quarters = self.db_tools.fetch_all(sql)

        # Determine and display the active grading period
        active_quarter = "Off-season / Break"

        for row in quarters:
            start_date = QDate.fromString(str(row['startdate']), "yyyy-MM-dd")
            end_date = QDate.fromString(str(row['enddate']), "yyyy-MM-dd")

            if start_date <= self.today <= end_date:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(row['gpid'], "th")
                active_quarter = f"{row['gpid']}{suffix} Grading Period"
                self.GRADING_PERIOD = row['gpid']
                break

        self.ui.label_gradingperiod.setText(active_quarter)

        return quarters

    def display_section_info(self, studentid):
        if studentid:
            student = Student()
            result = student.retrieve_one_student_info(studentid)
            sid, lname, fname, mname, section, gender, stored_hash, profile_pic, _, _ = result
            self.ui.label_firstname.setText(fname)
            self.ui.label_lastname.setText(lname)
            self.ui.label_studentId.setText(sid)
            self.ui.label_sectionName.setText(section)

            if profile_pic:
                image = QImage.fromData(bytes(profile_pic))
                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)
                    scaled_pixmap = self.util.makeCircularPixmap(pixmap, 200)
                    self.ui.label_profilePic.setPixmap(scaled_pixmap)
                else:
                    self.ui.label_profilePic.setText("Invalid Image")

    def display_lessons(self):
        layout = self.ui.verticalLayout_5

        # Clear old widgets properly
        while layout.count():
            child = layout.takeAt(0)
            widget = child.widget()
            if widget:
                # Safely disconnect any custom clicked signals
                try:
                    widget.clicked.disconnect()
                except (TypeError, RuntimeError):
                    pass
                widget.deleteLater()

        lessons = Lessons()
        record = lessons.retrieve_lesson_info()

        for row in record:
            lesson_id, chapter, lessonnum, gradingperiod, title, path_str, lessonimage, _ = row

            pixmap = None
            if lessonimage:
                img = QImage.fromData(bytes(lessonimage))
                pixmap = QPixmap.fromImage(img)

            card = LessonCard(lesson_id, title, lessonnum, chapter, pixmap)
            
            # FIX: Absorb the signal's boolean 'checked' arg with '_'
            # and capture variables explicitly in the lambda scope
            card.clicked.connect(
                lambda _, c=card, lid=lesson_id: self.handle_lesson_selection(c, lid)
            )
            layout.addWidget(card)

        layout.addStretch()

    def displayQuiz(self):
        qUtils = QuizUtils(self.GRADING_PERIOD)
        self.quiz_cards = []

        layout_id = self.ui.verticalLayout_7
        layout_mc = self.ui.verticalLayout_8
        layout_tf = self.ui.verticalLayout_9

        for layout in [layout_id, layout_mc, layout_tf]:
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            layout.setSpacing(5)

            while layout.count():
                item_to_remove = layout.takeAt(0)
                widget = item_to_remove.widget()
                if widget is not None:
                    widget.deleteLater()

        record_id, record_mc, record_tf = qUtils.retrieve_quiz()
        itemCnt = 1

        for row in record_id:
            quiz = Quiz("ID")
            quiz.idKey = row.get("idkey")
            quiz.quiznumber = row.get("quiznumber")
            quiz.gradingperiod = row.get("gradingperiod")
            quiz.lessonid = row.get("lessonid")
            quiz.itemno = row.get("itemno", "")
            quiz.itemnoCnt = itemCnt
            quiz.question = row.get("question", "")
            quiz.correct_answer = row.get("correct_answer", "")
            quiz.imageQ = row.get("imagequestion", None)
            quiz.displayAttributes()
            self.quiz_cards.append(quiz)
            layout_id.addWidget(quiz)

            itemCnt += 1

        for row in record_mc:
            quiz = Quiz("MC")
            quiz.idKey = row.get("mckey")
            quiz.quiznumber = row.get("quiznumber")
            quiz.gradingperiod = row.get("gradingperiod")
            quiz.lessonid = row.get("lessonid")
            quiz.itemno = row.get("itemno", "")
            quiz.itemnoCnt = itemCnt
            quiz.question = row.get("question", "")
            quiz.choice_a = row.get("choice_a")
            quiz.choice_b = row.get("choice_b")
            quiz.choice_c = row.get("choice_c")
            quiz.correct_answer = row.get("correct_answer", "")
            quiz.imageQ = row.get("imagequestion", None)
            quiz.displayAttributes()
            self.quiz_cards.append(quiz)
            layout_mc.addWidget(quiz)

            itemCnt += 1

        for row in record_tf:
            quiz = Quiz("TF")
            quiz.idKey = row.get("tfkey")
            quiz.quiznumber = row.get("quiznumber")
            quiz.gradingperiod = row.get("gradingperiod")
            quiz.lessonid = row.get("lessonid")
            quiz.itemno = row.get("itemno", "")
            quiz.itemnoCnt = itemCnt
            quiz.question = row.get("question", "")
            quiz.correct_answer = row.get("correct_answer", "")
            quiz.imageQ = row.get("imagequestion", None)
            quiz.displayAttributes()
            self.quiz_cards.append(quiz)
            layout_tf.addWidget(quiz)

            itemCnt += 1

    def displayQuizAnswers(self):
        qUtils = QuizUtils(self.GRADING_PERIOD)
        self.quiz_cards = []

        layout = self.ui.gridLayout_2
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(5)

        while layout.count():
            item_to_remove = layout.takeAt(0)
            widget = item_to_remove.widget()
            if widget is not None:
                widget.deleteLater()

        student_id = self.settings.value("studentid")
        record = qUtils.retrieve_quiz_answer(student_id)
        itemCnt = 1
        NUM_COLUMNS = 3

        for row in record:
            quiz = Quiz("RV")
            quiz.idKey = row.get("idkey")
            quiz.quiznumber = row.get("quiznumber")
            quiz.gradingperiod = row.get("gradingperiod")
            quiz.lessonid = row.get("lessonid")
            quiz.itemno = row.get("itemno", "")
            quiz.itemnoCnt = itemCnt
            quiz.question = row.get("question", "")
            quiz.user_answer = row.get("user_answer", "")
            quiz.correct_answer = row.get("correct_answer", "")
            quiz.remarks = row.get("remarks", "")
            quiz.imageQ = row.get("imagequestion", None)
            quiz.displayAttributes()
            self.quiz_cards.append(quiz)
            layout.addWidget(quiz)

            index = itemCnt - 1
            grid_row = index // NUM_COLUMNS
            grid_col = index % NUM_COLUMNS

            layout.addWidget(quiz, grid_row, grid_col)

            itemCnt += 1

    def display_myscores(self):
        layout = self.ui.gridLayout_3
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        myscores    = MyScores()
        student_id  = self.settings.value("studentid")
        record      = myscores.get_scores(student_id, self.GRADING_PERIOD)
        row_count   = len(record)
        NUM_COLUMNS = 3

        for index, row in enumerate(record):
            quiznumber     = row['quiznumber']
            lesson_id      = row['lessonid']
            title          = row['title'] 
            quizscore      = row['quizscore'] 
            total_score    = row['total_score'] 
            date_taken     = row['datetaken']
            average        = 0.0
            sum_score      = 0.0
            score_str      = f"{quizscore}/{total_score}" if quizscore is not None and total_score else ""
            percentage_str = ""
            percent_val    = 0.0

            # Validate score bounds and avoid DivisionByZero
            if total_score > 0 and quizscore is not None and 0 <= quizscore <= total_score:
                percent_val = (quizscore / total_score) * 100
                sum_score += percent_val
                percentage_str = f"{percent_val:.2f}%"

            date_taken_str = date_taken if date_taken is not None else ""
    
            # Calculate the final average exactly once outside the loop
            if row_count > 0:
                average = sum_score / row_count

            card = CardScores(quiznumber, lesson_id, title, score_str, percent_val, percentage_str)
            # card.clicked.connect(self.handle_lesson_selection)

            grid_row = index // NUM_COLUMNS
            grid_col = index % NUM_COLUMNS

            layout.addWidget(card, grid_row, grid_col)

    def save_quiz_answers(self):
        if not hasattr(self, 'quiz_cards') or not self.quiz_cards:
            return

        from App.Quiz import QuizUtils
        qUtils = QuizUtils(self.GRADING_PERIOD)

        student_id = self.settings.value("studentid")
        success, message = qUtils.save_quiz(student_id, self.quiz_cards)

        if success == 1: # Success, customized message for student
            dialog = CustomShapeDialog("Good Job !!!", parent=self.home_win)
            dialog.exec()

            sid = self.settings.value("studentid")
            _, record = Student().get_quiz_status(sid)
            self.ui.label_score.setText(f"{record['quizscore']}/{record['totalscore']}")
            self.slide_to_page(2)

        elif success == 2: # Failed, customized message for student
            dialog = CustomShapeDialog(message, parent=self.home_win, type=3)
            dialog.exec()

        else:
            print(message) # Failed, message for developers
            dialog = CustomShapeDialog("Something went wrong.", parent=self.home_win, type=2)
            dialog.exec()

    def handle_lesson_selection(self, clicked_card, lesson_id):
        print(f"Selected Lesson ID: {lesson_id}")
        
        # If a window is already open, close it first
        if hasattr(self, 'lesson_window') and self.lesson_window is not None:
            self.lesson_window.close()
            
        lesson = Lessons()
        record = lesson.retrieve_lesson_info(lesson_id)

        if not record:
            return

        filename = record[0][5]

        if not filename:
            dialog = CustomShapeDialog("The file does not exist.", parent=self.home_win, type=2)
            dialog.exec()
            return

        self.home_win.player.stop()
        self.lesson_window = WickPlayer("Lessons", filename)
        self.lesson_window.show()

    def open_game(self, mode):

        if hasattr(self, 'game_window') and self.game_window is not None:
            self.game_window.close()

        filename = ""

        if mode == "addition":
            filename = "gameAddition.html"

        if mode == "subtraction":
            filename = "gameSubtraction.swf"

        if not filename:
            return
        
        self.game_window = WickPlayer("Games", filename)
        self.game_window.show()



