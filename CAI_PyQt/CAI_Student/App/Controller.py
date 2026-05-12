import os, sys
from PySide6.QtCore import QSettings, QPoint, QEasingCurve, QPropertyAnimation, QParallelAnimationGroup, Qt
from PySide6.QtWidgets import QMainWindow, QButtonGroup, QLineEdit
from PySide6.QtGui import QFontDatabase, QImage, QPixmap

from App.Login import Login
from App.FormHome import Ui_FormHome
from App.Student import Student
from App.Tools import Utility, WindowHandler
from App.Lessons import Lessons, LessonCard


class Controller:
    RESIZE_MARGIN = 8  # The clickable area around the edges (in pixels)
    
    def __init__(self):
        self.settings = QSettings("CAI_System", "CAI_Student_App")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(self.script_dir)
        self.util = Utility()

        self.login_win = Login()
        self.login_win.login_success.connect(self.on_login_success)

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
            self.ui.btnExercise: 2,
            self.ui.btnScores: 3,
            self.ui.btnGames: 4,
        }

        for btn, idx in self.nav_map.items():
            btn.setCheckable(True)
            self.nav_group.addButton(btn)
            btn.clicked.connect(lambda checked, b=btn, i=idx: self.handle_nav_click(b, i))

        self.display_lessons()
        self.ui.btnLessons.setChecked(True)

        # Optional: Set the initial active button (Home)
        self.ui.btnLessons.setChecked(True)
        self.ui.btnLessons.clicked.connect(self.display_lessons)
        self.ui.btnQuiz.clicked.connect(self.displayQuiz)
        self.ui.btnSubmitQuiz.clicked.connect(self.save_quiz_answers)
        self.ui.btnQuit.clicked.connect(self.logout)
        self.ui.btnAddition.clicked.connect(self.open_game)

        self.display_section_info(user["studentid"])

        self.login_win.close()
        self.home_win.show()

    def toggle_maximize(self):
        if self.home_win.isMaximized():
            self.home_win.showNormal()
            # Optional: Change icon back to 'maximize'
            # self.btnMaximize.setIcon(QIcon("expand.png"))
        else:
            self.home_win.showMaximized()
            # Optional: Change icon to 'restore' 
            # self.btnMaximize.setIcon(QIcon("restore.png"))

    def handle_nav_click(self, button, index):
        self.slide_to_page(index)
        button.setChecked(True)

    def slide_to_page(self, index):
        stack = self.ui.stackedWidget
        if stack.currentIndex() == index:
            return

        # 1. Setup variables
        current_page = stack.currentWidget()
        next_page = stack.widget(index)
        width = stack.width()

        # 2. Prepare next page (move it to the right side off-screen)
        next_page.setGeometry(width, 0, width, stack.height())
        next_page.show()
        next_page.raise_()

        # 3. Create Parallel Animations
        self.anim_group = QParallelAnimationGroup()

        # Slide next page IN (from right to center)
        anim_in = QPropertyAnimation(next_page, b"pos")
        anim_in.setDuration(450)
        anim_in.setStartValue(QPoint(width, 0))
        anim_in.setEndValue(QPoint(0, 0))
        anim_in.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Slide current page OUT (from center to left)
        anim_out = QPropertyAnimation(current_page, b"pos")
        anim_out.setDuration(450)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(-width, 0))
        anim_out.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.anim_group.addAnimation(anim_in)
        self.anim_group.addAnimation(anim_out)

        # 4. On finish, update the StackedWidget index to "reset" the layout
        self.anim_group.finished.connect(lambda: stack.setCurrentIndex(index))
        self.anim_group.start()

    def logout(self):
        self.settings.clear()
        self.home_win.close()
        self.login_win.show()
        self.login_win.txtPassword.clear()

    def load_fonts(self):
        # Move up (..) from controller.py to access the "fonts" folder in the project root
        path = os.path.join(self.script_dir, "..", "Fonts")
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
        
        # Clear existing items
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        lessons = Lessons()
        record = lessons.retrieve_lesson_info() 

        for row in record:
            lesson_id, chapter, lessonnum, gradingperiod, title, path_str, lessonimage, _ = row
            
            # Convert blob to Pixmap if exists
            pixmap = None
            if lessonimage:
                img = QImage.fromData(bytes(lessonimage))
                pixmap = QPixmap.fromImage(img)

            card = LessonCard(lesson_id, title, lessonnum, chapter, pixmap)
            
            # Connect the signal! 
            card.clicked.connect(self.handle_lesson_selection)
            
            # Add to layout
            layout.addWidget(card)

        # Add a spacer at the bottom so cards stay at the top
        layout.addStretch()

    def displayQuiz(self):
        from App.Quiz import Quiz, QuizUtils
        qUtils = QuizUtils()
        self.quiz_cards = []

        layout_id = self.ui.verticalLayout_7
        layout_mc = self.ui.verticalLayout_8
        layout_tf = self.ui.verticalLayout_9

        for layout in [layout_id, layout_mc, layout_tf]:
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            layout.setSpacing(5)

            while layout.count():
                # takeAt removes the layout item, allowing access to the widget
                item_to_remove = layout.takeAt(0)
                widget = item_to_remove.widget()

                if widget is not None:
                    # deleteLater is safer than sip.delete for preventing crashes
                    widget.deleteLater()

        record_id, record_mc, record_tf = qUtils.retrieve_quiz()

        for row in record_id:
            quiz = Quiz("ID") # Identification
            quiz.idKey = row.get("idkey")
            quiz.quiznumber = row.get("quiznumber")
            quiz.gradingperiod = row.get("gradingperiod")
            quiz.lessonid = row.get("lessonid")
            quiz.itemno = row.get("itemno", "")
            quiz.question = row.get("question", "")
            quiz.correct_answer = row.get("correct_answer", "")
            quiz.imageQ = row.get("imagequestion", None)
            quiz.displayAttributes()
            self.quiz_cards.append(quiz)
            layout_id.addWidget(quiz)

        for row in record_mc:
            quiz = Quiz("MC") # Multiple Choice
            quiz.idKey = row.get("mckey")
            quiz.quiznumber = row.get("quiznumber")
            quiz.gradingperiod = row.get("gradingperiod")
            quiz.lessonid = row.get("lessonid")
            quiz.itemno = row.get("itemno", "")
            quiz.question = row.get("question", "")
            quiz.choice_a = row.get("choice_a")
            quiz.choice_b = row.get("choice_b")
            quiz.choice_c = row.get("choice_c")
            quiz.correct_answer = row.get("correct_answer", "")
            quiz.imageQ = row.get("imagequestion", None)
            quiz.displayAttributes()
            self.quiz_cards.append(quiz)
            layout_mc.addWidget(quiz)

        for row in record_tf:
            quiz = Quiz("TF") # True or False
            quiz.idKey = row.get("tfkey")
            quiz.quiznumber = row.get("quiznumber")
            quiz.gradingperiod = row.get("gradingperiod")
            quiz.lessonid = row.get("lessonid")
            quiz.itemno = row.get("itemno", "")
            quiz.question = row.get("question", "")
            quiz.correct_answer = row.get("correct_answer", "")
            quiz.imageQ = row.get("imagequestion", None)
            quiz.displayAttributes()
            self.quiz_cards.append(quiz)
            layout_tf.addWidget(quiz)

    def save_quiz_answers(self):

        if not hasattr(self, 'quiz_cards') or not self.quiz_cards:
            return
        
        from App.Quiz import QuizUtils
        qUtils = QuizUtils()

        student_id = self.settings.value("studentid")
        qUtils.save_quiz(student_id, self.quiz_cards)

    def handle_lesson_selection(self, clicked_card, lesson_id):
        print(f"Selected Lesson ID: {lesson_id}")

    def open_game(self):
        from App.Tools import WickPlayer  # Local import to avoid circular dependencies
        
        # Create the window instance. 
        # We store it as 'self.game_window' so Python's garbage collector 
        # doesn't delete it immediately after the function finishes.
        self.game_window = WickPlayer("multipleRooms3-26-2026_13-36-21.html")
        
        # Show the game window
        self.game_window.show()

    

  