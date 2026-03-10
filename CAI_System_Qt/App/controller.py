import os
from PyQt6.QtCore import QSettings, QTimer, QDateTime, QPoint, QEasingCurve, QPropertyAnimation, QParallelAnimationGroup, Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFontDatabase
from FormHome import Ui_Home
from login import Login
from addUserDialog import AddUserDialog
from CRUDTools import DatabaseTools
from ClassStaff import Staff
from Student import Student

class Controller:
    def __init__(self, script_dir):
        self.script_dir = script_dir
        self.settings = QSettings("CAI_System", "CAI_Admin_App")
        self.db_tools = DatabaseTools()

        self.login_win = Login()
        self.login_win.login_success.connect(self.on_login_success)

        self.load_fonts()
        self.check_session()

        self.student = Student()

    def check_session(self):
        sid = self.settings.value("user_school_id")
        if sid:
            user = Staff(school_id=sid,
                         username=self.settings.value("user_username"),
                         firstname=self.settings.value("user_fname"),
                         lastname=self.settings.value("user_lname"),
                         position=self.settings.value("user_pos"))
            self.show_home(user)
        else:
            self.login_win.show()

    def on_login_success(self, user):
        for key, val in {
            "user_school_id": user.school_id, "user_username": user.username,
            "user_fname": user.firstname, "user_lname": user.lastname,
            "user_pos": user.position
        }.items():
            self.settings.setValue(key, val)
        self.settings.sync()
        self.show_home(user)

    def show_home(self, user):
        self.home_win = QMainWindow()
        self.ui = Ui_Home()
        self.ui.setupUi(self.home_win)

        # Setup UI
        self.ui.btnUserName.setText(f"{user.firstname} {user.lastname}")
        self.ui.labelPosition.setText(user.position)

        # Timer for Clock
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        # Navigation
        self.nav_map = {
            self.ui.btnHome: 0,
            self.ui.btnClassList: 1,
            self.ui.btnLesson: 2,
            self.ui.btnQuiz: 3,
            self.ui.btnExercise: 4,
            self.ui.btnSections: 5,
            self.ui.btnReports: 6
        }
        for btn, idx in self.nav_map.items():
            btn.clicked.connect(lambda checked, i=idx: self.slide_to_page(i))

        self.ui.btnUsers.clicked.connect(lambda: AddUserDialog(self.db_tools).exec())
        self.ui.btnLogout.clicked.connect(self.logout)

        # self.student.retrieve_student_info()
        # print(self.student.firstname, self.student.section, self.student.lastname)

        self.login_win.close()
        self.home_win.show()

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

    def update_clock(self):
        now = QDateTime.currentDateTime()
        self.ui.label_day.setText(now.toString("d"))
        self.ui.label_time.setText(now.toString("h:mm"))

    def logout(self):
        self.settings.clear()
        self.home_win.close()
        self.login_win.show()

    def load_fonts(self):
        # Move up (..) from controller.py to access the "fonts" folder in the project root
        path = os.path.join(self.script_dir, "..", "fonts")
        if os.path.exists(path):
            for f in os.listdir(path):
                if f.endswith((".ttf", ".otf")):
                    QFontDatabase.addApplicationFont(os.path.join(path, f))