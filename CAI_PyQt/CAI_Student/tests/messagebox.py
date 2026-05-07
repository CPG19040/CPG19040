import sys
from PySide6.QtWidgets import (QApplication, QDialog, QVBoxLayout, 
                             QLabel, QPushButton, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QColor, QMouseEvent

class CustomShapeDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # This tracks the drag position
        self._drag_pos = QPoint()

        self.init_ui(message)

    def init_ui(self, message):
        # We wrap everything in a container
        self.container = QLabel(self)
        self.container.setFixedSize(500, 300)
        self.container.setObjectName("container")
        
        # Important: Allow mouse events to pass through the label if needed, 
        # but usually, we just need to catch them in the Dialog.
        
        self.container.setStyleSheet("""
            #container {
                color: white;
                font-weight: bold;
                border-image: url("/home/chip1994/Documents/CAI_Project/CAI_Student/Images/slab.png") 0 0 0 0 stretch stretch;
                border: none;
                padding: 40px;
            }
        """)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 150))
        self.container.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self.container)
        
        msg_label = QLabel(message)
        msg_label.setWordWrap(True)
        msg_label.setAlignment(Qt.AlignCenter)
        msg_label.setObjectName("msg_label")
        # Prevent the label from capturing mouse events so the dialog gets them
        msg_label.setAttribute(Qt.WA_TransparentForMouseEvents) 
        msg_label.setStyleSheet("#msg_label { color: brown; border: none; background-color: transparent; font-size: 14px; border-image: url(\"/home/chip1994/Downloads/My Project3-28-2026_11-04-16.svg\") 0 0 0 0 stretch stretch; }")
        layout.addWidget(msg_label)

        close_btn = QPushButton("Close")
        close_btn.setFixedWidth(80)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn, 0, Qt.AlignCenter)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.container)

    # --- Improved Drag Logic ---
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # This tells the OS (Zorin/GNOME) to take over the dragging 
            # logic natively. This is much more reliable on Wayland.
            self.windowHandle().startSystemMove()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            # Move the window to the new global position minus the initial offset
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = CustomShapeDialog("Now it should drag\nsmoothly on Zorin!")
    dialog.show()
    sys.exit(app.exec())