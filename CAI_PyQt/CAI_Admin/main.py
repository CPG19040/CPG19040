import sys
import resources_rc
from PySide6.QtWidgets import QApplication
from App.Controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Initialize the system via the Controller
    manager = Controller()

    sys.exit(app.exec())
