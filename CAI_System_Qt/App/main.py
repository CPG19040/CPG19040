import sys, os
from PyQt6.QtWidgets import QApplication
from controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Initialize the system via the Controller
    manager = Controller(script_dir)

    sys.exit(app.exec())