import os, sys
from functools import partial

from PySide6.QtWidgets import QFrame, QFileDialog, QMainWindow, QDialog
from PySide6.QtGui import QPixmap, QPainter, QPen, QMovie, QPainterPath
from PySide6.QtCore import Qt, Signal, QUrl, QObject, QEvent, QDate
from PySide6.QtWebEngineWidgets import QWebEngineView

from App.CRUDTools import DatabaseTools
from App.MessageBox import Ui_MessageBox
from App.CardStudent import Ui_CardStudent

class Utility:

    def __init__(self):
        self.db_tools = DatabaseTools()

    def get_resource_path(self, relative_path):
        """ Safely retrieves asset paths across development files and standalone compiled EXEs """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.normpath(os.path.join(base_path, relative_path))
    
    def get_dynamic_school_year_dates(self):
        today = QDate.currentDate()
        current_year = today.year()
        current_month = today.month()

        # If today is between Jan and May (e.g., May 2026), the current school year started in June of LAST year (2025).
        # If today is between June and Dec (e.g., June 2026), the current school year started in June of THIS year (2026).
        if current_month < 6:
            base_year = current_year - 1
        else:
            base_year = current_year

        next_year = base_year + 1

        return today, base_year, next_year

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
        """Evaluate if val is NONE, NULL, 'N/A', or empty string."""
        if val is None or not str(val).strip():
            return True

        clean_val = str(val).strip().upper()

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

    def find_tab_by_name(self, tab_widget, name):
        for i in range(tab_widget.count()):
            if tab_widget.tabText(i) == name:
                return i
        return -1


class StudentCard(QFrame, Ui_CardStudent):
    clicked = Signal(object, str)

    def __init__(self, name, stud_id, image):
        """Custom widget representing a single card."""
        super().__init__()
        self.setupUi(self)

        self.fullName = name
        self.studentid = stud_id
        self.pixMap = image
        self.setProperty("selected", False) # Initialize property
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.util = Utility()

        if self.util.isEmpty(self.pixMap):
            path = self.util.get_resource_path(os.path.join("..", "Images", "profile_gray.png"))
            self.pixMap = self.util.getCircularPixmapFromImagePath(path, 100)

        circular_pixmap = self.util.makeCircularPixmap(self.pixMap)
        self.label_profile.setPixmap(circular_pixmap)
        
        # Information
        self.label_student_name.setText(name)
        self.label_student_id.setText(stud_id)
        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # Ensure the widget can receive focus for keyboard navigation
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def mousePressEvent(self, event):
        """Triggered when the user clicks the card."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self, self.label_student_id.text())
            super().mousePressEvent(event)

    def focusInEvent(self, event):
        """Triggered when the card gains focus (e.g., via Tab key)."""
        if not self.property("selected"):
            self.clicked.emit(self, self.label_student_id.text())
        super().focusInEvent(event)

    def set_selected(self, selected: bool):
        """Updates the property and refreshes the style."""
        self.setProperty("selected", selected)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()


class WickPlayer(QMainWindow):

    def __init__(self, folder:str, html_filename:str):
        super().__init__()
        self.setWindowTitle("Wick Animation Player")
        self.resize(1024, 768)
        self.showMaximized()

        self.browser = QWebEngineView()
        self.util = Utility()
        
        _path = self.util.get_resource_path(os.path.join("..", folder))
        file_path = os.path.join(_path, html_filename)
        
        if os.path.exists(file_path):
            self.browser.setUrl(QUrl.fromLocalFile(file_path))
        else:
            print(f"Error: {html_filename} not found in {_path}")
            
        self.setCentralWidget(self.browser)

    def closeEvent(self, event):
        """Triggers automatically when the game window closes."""
        self.fetch_and_save_score()
        event.accept()

    def fetch_and_save_score(self):
        """Queries JavaScript for the score variable or localStorage."""
        
        js_code = "window.score || localStorage.getItem('highScore') || 0;"
        self.browser.page().runJavaScript(js_code, self.save_score_to_json)

    def save_score_to_json(self, current_score):
        try:
            print('🌟', current_score, '🌟')
            current_score = int(current_score)
        except (ValueError, TypeError):
            current_score = 0

              
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


class CustomMessageBox(QDialog, Ui_MessageBox):
    Yes           = 100
    No            = 101
    YesToAll      = 102
    NoToAll       = 103
    Cancel        = QDialog.DialogCode.Rejected  # 0
    Ok            = QDialog.DialogCode.Accepted  # 1

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) # For rounded corners
        self.setModal(True)

        # Re-use WindowHandler for dragging
        self.handler = WindowHandler(self)

        self.btnClose.clicked.connect(self.reject)
        self._connect_signals()
        
    def _connect_signals(self):
        """Connect button signals safely using partial to prevent lambda retention."""
        btn_map = [
            ('btnOk', self.accept),
            ('btnCancel', self.reject),
            ('btnYes', partial(self.done, self.Yes)),
            ('btnNo', partial(self.done, self.No)),
            ('btnYesAll', partial(self.done, self.YesToAll)),
            ('btnNoAll', partial(self.done, self.NoToAll)),
        ]

        for btn_name, slot in btn_map:
            if hasattr(self, btn_name):
                getattr(self, btn_name).clicked.connect(slot)

    def _hide_all_buttons(self):
        """Reset button visibility before showing modal."""
        buttons = ['btnYes', 'btnNo', 'btnYesAll', 'btnNoAll', 'btnOk', 'btnCancel']
        for btn_name in buttons:
            if hasattr(self, btn_name):
                getattr(self, btn_name).setVisible(False)

    def _setup_dialog(self, title: str, message: str, icon_path: str):
        self._hide_all_buttons()
        self.setWindowTitle(title)

        if hasattr(self, 'label_gif'):
            self.label_gif.setMovie(movie := QMovie(icon_path))
            movie.start()

        if hasattr(self, 'label_windowTitle'):
            self.label_windowTitle.setText(title)

        if hasattr(self, 'label_message'):
            self.label_message.setText(message)

    @classmethod
    def _create_and_exec(cls, parent, title, message, icon_path, visible_buttons):
        dlg = cls(parent)
        dlg._setup_dialog(title, message, icon_path)

        for btn_name in visible_buttons:
            if hasattr(dlg, btn_name):
                getattr(dlg, btn_name).setVisible(True)

        dlg.adjustSize()
        return dlg.exec()

    @classmethod
    def information(cls, parent, title, message):
        return cls._create_and_exec(parent, title, message, ":/Images/Images/happy.gif", ['btnOk'])

    @classmethod
    def success(cls, parent, title, message):
        return cls._create_and_exec(parent, title, message, ":/Images/Images/happy.gif", ['btnOk'])

    @classmethod
    def warning(cls, parent, title, message):
        return cls._create_and_exec(parent, title, message, ":/Images/Images/tonton-warning.gif", ['btnOk'])

    @classmethod
    def critical(cls, parent, title, message):
        return cls._create_and_exec(parent, title, message, ":/Images/Images/tonton-sad.gif", ['btnOk'])

    @classmethod
    def question(cls, parent, title, message, include_all=False, show_cancel=False):
        buttons = ['btnYes', 'btnNo']

        if include_all:
            buttons.extend(['btnYesAll', 'btnNoAll'])
        if show_cancel:
            buttons.append('btnCancel')

        return cls._create_and_exec(parent, title, message, ":/Images/Images/tonton-warning.gif", buttons)

