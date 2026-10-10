from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Qt
from passlib.hash import bcrypt
from App.FormLogIn import Ui_FormLogin
from App.CRUDTools import DatabaseTools
from App.Tools import Utility, CustomMessageBox
from App.Logger import setup_logger

class Login(QMainWindow, Ui_FormLogin):
    login_success = Signal(object)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.logger = setup_logger("CAI_System", "admin_activity.log")

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # Remove OS default window frame
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setMouseTracking(True)

        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnClose.clicked.connect(self.close)

        self.btnLogin.clicked.connect(self.handle_login)
        self.db_tools = DatabaseTools()
        self.util     = Utility()

        _, base_year, next_year = self.util.get_dynamic_school_year_dates()
        
        self.label_SY.setText(f"School Year: {base_year}-{next_year}")

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()

            # If clicking inside the custom header, move the window
            if self.frame_header.geometry().contains(pos):
                self.windowHandle().startSystemMove()
                event.accept()
                return
            
        super().mousePressEvent(event)

    def handle_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        user = self.authenticate_user(username, password)
        
        if user:
            self.login_success.emit(user)
        else:
            CustomMessageBox.critical(self, "Error", "Invalid Username or Password")

    def authenticate_user(self, username, password):
        try:
            query  = "SELECT\n"
            query += "  A.school_id\n"
            query += "  ,A.username\n"
            query += "  ,A.firstname\n"
            query += "  ,A.middlename\n"
            query += "  ,A.lastname\n"
            query += "  ,A.password\n"
            query += "  ,B.position_id\n"
            query += "  ,B.position_name\n"
            query += "FROM cai.tbl_staff_info A\n"
            query += "LEFT JOIN cai.tbl_staff_positions B\n"
            query += "  ON A.positionid = B.position_id\n"
            query += "WHERE A.username = %s"
            
            cur, conn = self.db_tools.retrieve_records(query, (username,))
            result = cur.fetchone()

            if result:
                school_id, uname, fname, mname, lname, stored_hash, pos_id, pos_name = result
                if bcrypt.verify(password, stored_hash):
                    self.db_tools.execute_query("UPDATE cai.tbl_staff_info SET new_user = FALSE WHERE username = %s", (username,))
                    user = {
                        "school_id": school_id,
                        "username": uname,
                        "firstname": fname,
                        "middlename": mname,
                        "lastname": lname,
                        "position_id": pos_id,
                        "position_name": pos_name
                    }
                    
                    return user
            
            return None

        except Exception as e:
            self.logger.error(f"Login().authenticate_user(): {e}", exc_info=True)
            return None
            
        finally:
            if conn:
                conn.close()
