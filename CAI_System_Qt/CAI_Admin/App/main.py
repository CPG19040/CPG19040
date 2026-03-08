import sys
import psycopg2

from passlib.hash import bcrypt
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from FormLogIn import Ui_FormLogin
from FormHome import Ui_MainWindow


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

        # authenticate_user now returns the user object or None
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

            # Query all necessary user details
            query = "SELECT firstname, middlename, lastname, password, position FROM cai.tbl_staff_info WHERE username = %s"
            cur.execute(query, (username,))
            
            result = cur.fetchone()

            if result:
                firstname, middlename, lastname, stored_hash, position = result
                
                # Verify password against hash
                if bcrypt.verify(password, stored_hash):
                    # Return a populated UserObject on success
                    return UserObject(firstname, middlename, lastname, position)
            
            return None

        except Exception as e:
            print(f"Database error: {e}")
            return None

        finally:
            if conn:
                cur.close()
                conn.close()
                

class Controller:
    def __init__(self):
        self.login_win = LoginWindow()
        # Connect the signal to receive the user object
        self.login_win.login_success.connect(self.show_home)
        self.login_win.show()

    def show_home(self, user):
        self.home_main_win = QMainWindow()
        self.ui_home = Ui_MainWindow()
        self.ui_home.setupUi(self.home_main_win)

        full_name = f"{user.firstname} {user.lastname}"
        self.ui_home.btnUserName.setText(full_name)
        self.ui_home.labelPosition.setText(user.position)
        
        self.login_win.close()
        self.home_main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Controller()
    sys.exit(app.exec())
