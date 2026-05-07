import sys, os
import resources_rc
from PySide6.QtWidgets import QApplication
from App.Controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory (CAI_Admin) to the path so it can find resources.py
    sys.path.append(script_dir)

    # Initialize the system via the Controller
    manager = Controller(script_dir)

    sys.exit(app.exec())
