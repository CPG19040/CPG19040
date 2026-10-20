from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal, Qt
from passlib.hash import bcrypt
from App.FormLogIn import Ui_FormLogin
from App.Tools import CustomMessageBox
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
        self.btnForgotPassword.clicked.connect(self.handle_forgot_password)
        self.app = QApplication.instance()

        _, base_year, next_year = self.app.utility.get_dynamic_school_year_dates()
        
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
        user     = self.authenticate_user(username, password)
        
        if user:
            self.login_success.emit(user)

    def authenticate_user(self, username, password):
        try:
            query = """
                SELECT
                    A.school_id
                    ,A.username
                    ,A.firstname
                    ,A.middlename
                    ,A.lastname
                    ,A.password
                    ,B.position_id
                    ,B.position_name
                FROM cai.tbl_staff_info A
                LEFT JOIN cai.tbl_staff_positions B
                ON A.positionid = B.position_id
                WHERE A.username = %s
            """
            
            cur, conn = self.app.db_tools.retrieve_records(query, (username,))

            if not cur:
                CustomMessageBox.critical(self, "Database Error", "Unable to connect to the database. Please try again later.")
                return None
            
            user_data = cur.fetchone()

            if user_data:
                school_id, uname, fname, mname, lname, stored_hash, pos_id, pos_name = user_data

                if bcrypt.verify(password, stored_hash):
                    self.app.db_tools.execute_query("UPDATE cai.tbl_staff_info SET new_user = FALSE WHERE username = %s", (username,))
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

            else:
                CustomMessageBox.warning(self, "Authentication Failed", "Invalid username or password.")
                
            return None

        except Exception as e:
            self.logger.error(f"Login().authenticate_user(): {e}", exc_info=True)
            return None
            
        finally:
            if conn:
                conn.close()

    def handle_forgot_password(self):
        CustomMessageBox.information(self, "Forgot Password", 
            "Please contact the System Administrator to reset your login credentials."
        )
