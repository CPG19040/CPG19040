import sys
import psycopg2

from passlib.hash import bcrypt
from PyQt6.QtCore import pyqtSignal, QPropertyAnimation, QPoint, QEasingCurve, Qt, QParallelAnimationGroup
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

from FormLogIn import Ui_FormLogin
from FormHome import Ui_MainWindow
from FormAddNewUser import Ui_AddNewUserDialog

# Scale the application depending on the screen resolution.
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class UserObject:
    def __init__(self, firstname, middlename, lastname, position):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.position = position

class LoginWindow(QMainWindow, Ui_FormLogin):
    login_success = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()

        user = self.authenticate_user(username, password)
        
        if user:
            self.login_success.emit(user)
        else:
            QMessageBox.warning(self, "Error", "Invalid Username or Password")

    def authenticate_user(self, username, password):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="DB_CAI",
                user="postgres", 
                password="1234",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()
            query = "SELECT firstname, middlename, lastname, password, position FROM cai.tbl_staff_info WHERE username = %s"
            cur.execute(query, (username,))
            result = cur.fetchone()

            if result:
                firstname, middlename, lastname, stored_hash, position = result
                if bcrypt.verify(password, stored_hash):
                    return UserObject(firstname, middlename, lastname, position)
            return None
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()

class Controller:
    def __init__(self):
        self.login_win = LoginWindow()
        self.login_win.login_success.connect(self.show_home)
        self.login_win.show()
        self.anim_group = None # Reference to prevent garbage collection

    def show_home(self, user):
        self.home_main_win = QMainWindow()
        self.ui_home = Ui_MainWindow()
        self.ui_home.setupUi(self.home_main_win)

        self.nav_map = {
            self.ui_home.btnHome: 0,
            self.ui_home.btnClassList: 1,
            self.ui_home.btnLesson: 2,
            self.ui_home.btnQuiz: 3,
            self.ui_home.btnExercise: 4,
            self.ui_home.btnSections: 5,
            self.ui_home.btnReports: 6
        }

        for btn, index in self.nav_map.items():
            btn.clicked.connect(lambda checked, i=index: self.slide_to_page(i))

        full_name = f"{user.firstname} {user.lastname}"
        self.ui_home.btnUserName.setText(full_name)
        self.ui_home.labelPosition.setText(user.position)
        
        self.login_win.close()
        self.home_main_win.show()

    def slide_to_page(self, index):
        stack = self.ui_home.stackedWidget
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

    def show_add_user(self):
        self.add_user_dialog = QDialog()
        self.ui_add_user = Ui_AddNewUserDialog()
        self.ui_add_user.setupUi(self.add_user_dialog)
        self.add_user_dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Controller()
    sys.exit(app.exec())