import sys
import psycopg2
import datetime

from passlib.hash import bcrypt
from PyQt6.QtCore import pyqtSignal, QPropertyAnimation, QPoint, QEasingCurve, Qt, QParallelAnimationGroup
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

from FormLogIn import Ui_FormLogin
from FormHome import Ui_MainWindow
from FormAddNewUser import Ui_AddNewUserDialog
from ClassStaff import Staff
from CRUDTools import DatabaseTools

# Scale the application depending on the screen resolution.
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

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
                    return Staff(firstname=firstname, middlename=middlename, lastname=lastname, position=position)
            return None
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()

class Controller:
    def __init__(self):
        self.database_tools = DatabaseTools()
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

        self.ui_home.btnUsers.clicked.connect(self.show_add_user)

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

        positions = self.database_tools.fetch_all("SELECT DISTINCT position_id, position_name FROM cai.staff_positions ORDER BY position_id ASC")  # Fetch positions from the database if needed
        for pos in positions:
            self.ui_add_user.comboBox_position.addItem(pos['position_name'], pos['position_id'])  # Assuming position_name is the second column and position_id is the first
        
        self.ui_add_user.comboBox_recoveryQuestion.addItems([
            "What is your mother's maiden name?",
            "What was the name of your first pet?",
            "What was the make of your first car?"
        ])
        self.ui_add_user.btnSave.clicked.connect(self.register_user)

        self.add_user_dialog.exec()

    def register_user(self):
        firstname = self.ui_add_user.lineEdit_firstname.text()
        middlename = self.ui_add_user.lineEdit_middlename.text()
        lastname = self.ui_add_user.lineEdit_lastname.text()
        username = self.ui_add_user.lineEdit_username.text()
        password = self.ui_add_user.lineEdit_password.text()
        encrypted_password = self.encrypt_password(password)
        position = self.ui_add_user.comboBox_position.currentText()
        RecoveryQuestion = self.ui_add_user.comboBox_recoveryQuestion.currentText()
        RecoveryAnswer = self.ui_add_user.lineEdit_Answer.text()

        if not all([firstname, lastname, username, encrypted_password, position, RecoveryQuestion, RecoveryAnswer]):
            QMessageBox.warning(self.add_user_dialog, "Error", "Please fill in all required fields.")
            return

        cur = self.database_tools.retrieve_records("SELECT COUNT(*) FROM cai.tbl_staff_info")
        current_count = 0

        if cur:
            result = cur.fetchone()
            current_count = result[0]
        else:
            QMessageBox.warning(self.add_user_dialog, "Error", "Failed to retrieve current staff count.")
            return

        new_staff = Staff(
            school_id=self.generate_school_number(current_count), 
            firstname=firstname, 
            middlename=middlename, 
            lastname=lastname, 
            username=username, 
            password=encrypted_password, 
            position=position, 
            RecoveryQuestion=RecoveryQuestion, 
            RecoveryAnswer=RecoveryAnswer)

        new_staff.register()
        QMessageBox.information(self.add_user_dialog, "Success", "New user registered successfully!")
        self.add_user_dialog.close()

    def encrypt_password(self, password):
        return bcrypt.hash(password)

    def generate_school_number(self, current_count):
        year = datetime.datetime.now().year
        new_number = current_count + 1
        return f"{year}-{new_number:04d}-STA"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Controller()
    sys.exit(app.exec())