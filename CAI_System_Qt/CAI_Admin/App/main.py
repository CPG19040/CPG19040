import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Importing project's classes
from FormLogIn import Ui_FormLogin
from Home import Ui_MainWindow


class LoginWindow(QMainWindow, Ui_FormLogin):
    login_success = pyqtSignal() # Create the signal here

    def __init__(self):
        super().__init__()
        self.setupUi(self) # Initialize design
        
        # Connect button from FormLogIn.py
        self.btnLogin.clicked.connect(self.handle_login)

    def handle_login(self):
        # Use the names from setupUi (txtUsername, txtPassword)
        if self.txtUsername.text() == "admin" and self.txtPassword.text() == "1234":
            self.login_success.emit()
        else:
            QMessageBox.warning(self, "Error", "Invalid Credentials")


class Controller:
    def __init__(self):
        self.login_win = LoginWindow() # Use the wrapper class
        self.login_win.login_success.connect(self.show_home)
        self.login_win.show()

    def show_home(self):
        self.home_main_win = QMainWindow()
        self.ui_home = Ui_MainWindow()
        self.ui_home.setupUi(self.home_main_win)
        
        self.login_win.close()
        self.home_main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = Controller()
    sys.exit(app.exec())
