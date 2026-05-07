import sys
import random
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QGridLayout, QFrame, QMessageBox)
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QFont, QColor

class TenFrameSlot(QPushButton):
    """A single circle slot in the Ten-Frame."""
    def __init__(self):
        super().__init__("")
        self.setFixedSize(60, 60)
        self.setCheckable(True)
        # Style: White circle with black border; turns Red when checked
        self.refresh_style()
        self.toggled.connect(self.refresh_style)

    def refresh_style(self):
        if self.isChecked():
            self.setStyleSheet("background-color: #FF5733; border: 3px solid #C70039; border-radius: 30px;")
        else:
            self.setStyleSheet("background-color: white; border: 3px solid #2C3E50; border-radius: 30px;")

class TenFrameExercise(QWidget):
    def __init__(self):
        super().__init__()
        self.target_number = 0
        self.init_ui()
        self.generate_new_question()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(20)

        # 1. Instruction Label
        self.lbl_instruction = QLabel("Show me 0 dots!")
        self.lbl_instruction.setAlignment(Qt.AlignCenter)
        self.lbl_instruction.setFont(QFont("Arial", 24, QFont.Bold))
        self.layout.addWidget(self.lbl_instruction)

        # 2. The Ten-Frame Grid (2 rows, 5 columns)
        self.frame_container = QFrame()
        self.frame_container.setStyleSheet("background-color: #ECF0F1; border: 4px solid #2C3E50; border-radius: 10px;")
        self.grid = QGridLayout(self.frame_container)
        self.grid.setSpacing(10)
        
        self.slots = []
        for i in range(10):
            slot = TenFrameSlot()
            slot.toggled.connect(self.check_auto_verify)
            row, col = divmod(i, 5)
            self.grid.addWidget(slot, row, col)
            self.slots.append(slot)
            
        self.layout.addWidget(self.frame_container)

        # 3. Action Buttons
        self.btn_layout = QHBoxLayout()
        
        self.btn_reset = QPushButton("Clear All")
        self.btn_reset.setFixedSize(120, 50)
        self.btn_reset.clicked.connect(self.reset_slots)
        
        self.btn_check = QPushButton("Check Answer!")
        self.btn_check.setFixedSize(200, 50)
        self.btn_check.setStyleSheet("background-color: #2ECC71; color: white; font-weight: bold; font-size: 18px;")
        self.btn_check.clicked.connect(self.manual_verify)

        self.btn_layout.addStretch()
        self.btn_layout.addWidget(self.btn_reset)
        self.btn_layout.addWidget(self.btn_check)
        self.btn_layout.addStretch()
        
        self.layout.addLayout(self.btn_layout)

    def generate_new_question(self):
        self.target_number = random.randint(1, 10)
        self.lbl_instruction.setText(f"Can you show me {self.target_number}?")
        self.reset_slots()

    def reset_slots(self):
        for slot in self.slots:
            slot.blockSignals(True) # Prevent triggering verify while resetting
            slot.setChecked(False)
            slot.blockSignals(False)
            slot.refresh_style()

    def get_current_count(self):
        return sum(1 for slot in self.slots if slot.isChecked())

    def check_auto_verify(self):
        # Optional: Auto-verify if they hit the target exactly
        if self.get_current_count() == self.target_number:
            self.lbl_instruction.setText(f"🌟 Correct! It is {self.target_number}! 🌟")

    def manual_verify(self):
        current = self.get_current_count()
        if current == self.target_number:
            QMessageBox.information(self, "Great Job!", f"Perfect! That is exactly {self.target_number} dots.")
            self.generate_new_question()
        else:
            diff = "too many" if current > self.target_number else "not enough"
            QMessageBox.warning(self, "Keep Trying!", f"You have {current} dots. That is {diff}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TenFrameExercise()
    window.setWindowTitle("Grade 1 Math Practice")
    window.resize(400, 350)
    window.show()
    sys.exit(app.exec_())