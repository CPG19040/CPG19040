import os
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QFileDialog, QMainWindow, QWidget, QDialog
from PySide6.QtGui import QPixmap, QPainter, QBrush, QColor, QPen, QMovie, QPainterPath
from PySide6.QtCore import Qt, Signal, QBuffer, QByteArray, QIODevice, QUrl, QObject, QEvent
from PySide6.QtWebEngineWidgets import QWebEngineView
from App.CRUDTools import DatabaseTools
from App.CustomizedDialog import Ui_CustomDialog

class Utility:

    def __init__(self):
        self.db_tools = DatabaseTools()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def getCircularPixmapFromImagePath(self, image_path, size=100):
        """
            Transform an image into cicular shape

            Args:
                image_path (str): The path of an image
                size (float): Width and height of the image

            Returns:
                target (QPixmap): Generated pixmap image.

            Raises:
                N/A
        """
        # Load the image
        source_pixmap = QPixmap(image_path)
        
        # 1. Create a square transparent canvas
        target = QPixmap(size, size)
        target.fill(Qt.GlobalColor.transparent)
        
        # 2. Scale the source image to fill the square (preserving aspect ratio)
        square_pixmap = source_pixmap.scaled(
            size, size, 
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
            Qt.TransformationMode.SmoothTransformation
        )
        
        # 3. Paint the circle
        painter = QPainter(target)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        
        # Create a circular path
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)
        
        # Draw the image into the clipped area
        # (Offsetting might be needed if the scaled image isn't perfectly square)
        painter.drawPixmap(0, 0, square_pixmap)
        painter.end()
        
        return target

    def makeCircularPixmap(self, src_pixmap, size=80, radius=None):
        """
            Transform an image into cicular shape
            
            Args:
                src_pixmap (QPixmap): The pixmap object
                size (float): Width and height of the image

            Returns:
                target (QPixmap): Transformed pixmap image.

            Raises:
                N/A
        """
        # Create a transparent square canvas
        target = QPixmap(size, size)
        target.fill(Qt.GlobalColor.transparent)
        
        # Scale source image to fill the square
        scaled_pixmap = src_pixmap.scaled(
            size, size, 
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
            Qt.TransformationMode.SmoothTransformation
        )
        
        painter = QPainter(target)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        
        # Create a circular path
        path = QPainterPath()

        if not radius:
            path.addEllipse(0, 0, size, size)
        else:
            path.addRoundedRect(0, 0, size, size, radius, radius)

        painter.setClipPath(path)
        
        # Draw the image into the circle (centered)
        delta_x = (scaled_pixmap.width() - size) // 2
        delta_y = (scaled_pixmap.height() - size) // 2
        painter.drawPixmap(0, 0, scaled_pixmap.copy(delta_x, delta_y, size, size))
        
        # Optional: Add a subtle border
        painter.setClipping(False) # Stop clipping to draw the border
        painter.setPen(QPen(Qt.GlobalColor.lightGray, 1))

        if not radius:
            painter.drawEllipse(0, 0, size - 1, size - 1)
        else:
            painter.drawRoundedRect(0, 0, size - 1, size - 1, radius, radius)
        
        painter.end()
        return target

    def populate_pulldown(self, pulldown, sql, params=None, add_empty=False):
        if not sql:
            print("[Error] populate_pulldown(): SQL query is empty.")
            return

        pulldown.clear()
        cur = self.db_tools.retrieve_records(sql, params)

        if add_empty:
            pulldown.addItem("", None)

        if cur:
            for idx, item in cur:
                pulldown.addItem(item, idx)

    def isEmpty(self, val):
        # 1. Handle None or empty objects immediately
        if val is None or not str(val).strip():
            return True

        # 2. Convert to string and clean it
        clean_val = str(val).strip().upper()

        # 3. Check against forbidden keywords
        if clean_val in ['NONE', 'NULL', 'N/A', '']:
            return True

        return False

    def browsePhoto(self, dialog, width=100, height=100):
        scaled_pixmap = None
        binaryImage = None

        # Open file dialog to select image
        file_path, _ = QFileDialog.getOpenFileName(
            dialog, "Select Profile Picture", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_path:
            with open(file_path, 'rb') as file:
                binaryImage = file.read() # Store binary data

            # Show preview in the label
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    width, height,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

        return scaled_pixmap, binaryImage

    def formatFullname(self, firstname, middlename, lastname, order=0):
        if not firstname or not lastname:
            return ""

        middleInitial = middlename[:1].upper() + '.' if middlename else ""

        if order == 0: # Natural Order
            return f"{firstname} {middleInitial} {lastname}".title()

        if order == 1: # Reverse Order
            return f"{lastname}, {firstname} {middleInitial}".title()
        
        if order == 2: # Formal/Legal Order
            return f"{firstname}, {middlename} {lastname}".title()

        if order == 3: # Monogram or Initialized Style
            return f"{firstname[:1].upper()}, {middlename[:1].upper()} {lastname[:1].upper()}".title()


class Card(QFrame):
    clicked = Signal(object, str)

    """Custom widget representing a single card."""
    def __init__(self, name, stud_id, image, border_radius='10px'):
        super().__init__()

        self.fullName = name
        self.studentid = stud_id
        self.pixMap = image
        self.setProperty("selected", False) # Initialize property
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFixedSize(16777215, 100)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            Card {
                background-color: #ffffff;
                border-radius: """ + border_radius + """;
                border: 1px solid #ddd;
            }
            Card:hover {
                border: 2px solid #3498db;
                background-color: #f7fbfe;
            }
            /* This style applies when the custom property is true */
            Card[selected="true"] {
                background-color: #e1f5fe;
                border: 2px solid #3498db;
            }
            QLabel {
                color: #333;
            }
        """)

        self.util = Utility()

        if self.util.isEmpty(self.pixMap):
            path = os.path.join(self.util.script_dir, "..", "Images", "profile_gray.png")
            self.pixMap = self.util.getCircularPixmapFromImagePath(path, 80)

        # Layout for the card
        layout = QHBoxLayout(self)

        self.photo = QLabel()
        circular_pixmap = self.util.makeCircularPixmap(self.pixMap)
        self.photo.setPixmap(circular_pixmap)
        self.photo.setFixedSize(80, 80)
        self.photo.setStyleSheet("background-color: transparent;")
        
        # Information
        info_layout = QVBoxLayout()
        self.name_label = QLabel(name)
        self.name_label.setStyleSheet("font-weight: bold; font-size: 16px; background-color: transparent;")
        
        self.label_studentid = QLabel(stud_id)
        self.label_studentid.setStyleSheet("color: #777; font-size: 13px; background-color: transparent;")
        
        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.label_studentid)
        info_layout.addStretch()

        layout.addWidget(self.photo)
        layout.addLayout(info_layout)
        layout.addStretch()

        # Ensure the widget can receive focus for keyboard navigation
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def mousePressEvent(self, event):
        """Triggered when the user clicks the card."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self, self.label_studentid.text())
            super().mousePressEvent(event)

    def focusInEvent(self, event):
        """Triggered when the card gains focus (e.g., via Tab key)."""
        if not self.property("selected"):
            self.clicked.emit(self, self.label_studentid.text())
        super().focusInEvent(event)

    def set_selected(self, selected: bool):
        """Updates the property and refreshes the style."""
        self.setProperty("selected", selected)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()


class WickPlayer(QMainWindow):
    def __init__(self, html_filename):
        super().__init__()
        self.setWindowTitle("Wick Animation Player")
        self.resize(1024, 768)

        self.browser = QWebEngineView()
        
        # Resolve the path to the HTML file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "..", "Games", html_filename)
        
        if os.path.exists(file_path):
            self.browser.setUrl(QUrl.fromLocalFile(file_path))
        else:
            print(f"Error: {html_filename} not found in {script_dir}")
            
        self.setCentralWidget(self.browser)

              
class WindowHandler(QObject):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._margin = 8
        self._window.setMouseTracking(True)
        # We must install the filter on the window AND its central widget
        self._window.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.HoverMove:
            self._update_cursor(event.position().toPoint())
        
        elif event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                edge = self._get_edge(event.position().toPoint())
                if edge:
                    self._window.windowHandle().startSystemResize(edge)
                else:
                    self._window.windowHandle().startSystemMove()
                return True
        return super().eventFilter(obj, event)

    def _get_edge(self, pos):
        rect = self._window.rect()
        edge = None
        if pos.x() >= rect.width() - self._margin and pos.y() >= rect.height() - self._margin:
            edge = Qt.Edge.RightEdge | Qt.Edge.BottomEdge
        elif pos.x() >= rect.width() - self._margin:
            edge = Qt.Edge.RightEdge
        elif pos.y() >= rect.height() - self._margin:
            edge = Qt.Edge.BottomEdge
        return edge

    def _update_cursor(self, pos):
        edge = self._get_edge(pos)
        if edge == (Qt.Edge.RightEdge | Qt.Edge.BottomEdge):
            self._window.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif edge == Qt.Edge.RightEdge:
            self._window.setCursor(Qt.CursorShape.SizeHorCursor)
        elif edge == Qt.Edge.BottomEdge:
            self._window.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self._window.setCursor(Qt.CursorShape.ArrowCursor)


class CustomShapeDialog(QDialog, Ui_CustomDialog):

    def __init__(self, message, parent=None, type=1):
        super().__init__(parent)
        self.setupUi(self)

        # 1. Essential Flags
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) # For rounded corners
        self.setModal(True)

        # 2. Re-use WindowHandler for dragging
        self.handler = WindowHandler(self)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_dir, "..", "Images")
        file_path = os.path.join(img_path, "happy.gif") # Default

        if type == 2:
            file_path = os.path.join(img_path, "tonton-sad.gif")

        if type == 3:
            file_path = os.path.join(img_path, "tonton-warning.gif")

        movie = QMovie(file_path)

        # 3. Content
        self.label_gif.setMovie(movie)
        movie.start()
        self.label_message.setText(str(message))
        self.btnClose.clicked.connect(self.accept)

