from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSignal
from passlib.hash import bcrypt
from FormLogIn import Ui_FormLogin
from ClassStaff import Staff
from CRUDTools import DatabaseTools

class Login(QMainWindow, Ui_FormLogin):
    login_success = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.handle_login)
        self.db_tools = DatabaseTools()

    def handle_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        user = self.authenticate_user(username, password)
        
        if user:
            self.login_success.emit(user)
        else:
            QMessageBox.warning(self, "Error", "Invalid Username or Password")

    def authenticate_user(self, username, password):
        try:
            query = "SELECT school_id, username, firstname, middlename, lastname, password, position FROM cai.tbl_staff_info WHERE username = %s"
            cur = self.db_tools.retrieve_records(query, (username,))
            result = cur.fetchone()

            if result:
                school_id, uname, fname, mname, lname, stored_hash, pos = result
                if bcrypt.verify(password, stored_hash):
                    self.db_tools.execute_query("UPDATE cai.tbl_staff_info SET new_user = FALSE WHERE username = %s", (username,))
                    return Staff(school_id=school_id, username=uname, firstname=fname, 
                                 middlename=mname, lastname=lname, position=pos)
            return None
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            self.db_tools.close_connection()
