from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QPoint

class DraggableWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Remove the window frame
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(400, 300)

        # UI Setup
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        
        btn_close = QPushButton("Close App")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)

        # Variable to store the mouse click position
        self._old_pos = None

    # 2. Capture initial click position
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.windowHandle().startSystemMove()
            event.accept()

    # 3. Calculate movement and move the window
    def mouseMoveEvent(self, event):
        if self._old_pos is not None:
            delta = QPoint(event.globalPosition().toPoint() - self._old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self._old_pos = event.globalPosition().toPoint()

    # 4. Reset on release
    def mouseReleaseEvent(self, event):
        self._old_pos = None

if __name__ == "__main__":
    app = QApplication([])
    window = DraggableWindow()
    window.show()
    app.exec()