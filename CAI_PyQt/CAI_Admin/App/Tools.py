import os, sys, subprocess, csv
from functools import partial
from pathlib import Path

from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QFileDialog, QWidget, QMainWindow, QDialog, QComboBox
from PySide6.QtGui import QPixmap, QPainter, QColor, QPen, QPainterPath, QFont
from PySide6.QtCore import QIODevice, QSettings, Qt, Signal, QDate, QUrl, QRectF, QPoint, QPropertyAnimation, QEasingCurve, QFile
from PySide6.QtWebEngineWidgets import QWebEngineView

from App.CRUDTools import DatabaseTools
from App.MessageBox import Ui_MessageBox
from App.CardRanking import Ui_CardRanking



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

    def read_image_file_bytes(self, file_name: str) -> bytes:
        """Reads an image file and returns its byte content."""

        script_dir = Path(__file__).parent.resolve()
        cai_admin_dir = script_dir.parent
        full_path = cai_admin_dir / "LessonImages" / file_name

        if not os.path.exists(full_path):
            print(f"[Warning] read_image_file_bytes(): File not found: {full_path}")
            return b""
        
        file = QFile(str(full_path))

        if file.open(QIODevice.ReadOnly):
            file_bytes = file.readAll().data()
            file.close()
            return file_bytes
        
        return b""

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

    def populate_pulldown(self, pulldown, sql:str, params:tuple=None, default_value=None, add_empty:bool=False):
        """
        Fetches records from the database and populates a QComboBox (pulldown).

        Args:
            pulldown: The QComboBox widget to populate.
            sql (str): The SQL SELECT statement.
            params (tuple, optional): Parameters for the SQL query to prevent injection.
            default_value: The underlying data (ID) to select by default.
            add_empty (bool): If True, adds a blank row at the top of the list.
        """
        if not sql:
            print("[Error] populate_pulldown(): SQL query is empty.")
            return

        pulldown.clear()

        if add_empty:
            pulldown.addItem("", None)

        conn = None
        try:
            conn = self.db_tools.get_connection()
            with conn.cursor() as cur:
                cur.execute(sql, params)

                for idx, item in cur:
                    pulldown.addItem(str(item), idx)

                if default_value:
                    idx = pulldown.findData(default_value)

                    if idx != -1:
                        pulldown.setCurrentIndex(idx)

        except Exception as e:
            print(f"[Error] populate_pulldown(): {e}")

        finally:
            if conn:
                conn.close()

    def populate_gradingperiod_pulldown(self, pulldown_gradingPeroid, pulldown_lessons=None, default_gp=None):
        sql =  """
            SELECT gpid, gpname
	        FROM cai.tbl_grading_period;
        """
        self.populate_pulldown(pulldown_gradingPeroid, sql, default_value=default_gp)

        if not pulldown_lessons:
            return

        selected_period = pulldown_gradingPeroid.currentData()

        if selected_period:
            query = """
                SELECT
                    lesson_id
                    ,title
                FROM cai.tbl_lessons
                WHERE gradingperiod = %s
                ORDER BY chapter, lessonnum ASC
            """
            self.populate_pulldown(pulldown_lessons, query, params=(selected_period,), add_empty=True)

    def isEmpty(self, val):
        """Evaluate if val is NONE, NULL, 'N/A', or empty string."""
        if val is None or not str(val).strip():
            return True

        clean_val = str(val).strip().upper()

        if clean_val in ['NONE', 'NULL', 'N/A', '']:
            return True

        return False

    def browsePhoto(self, dialog:QDialog, width=100, height=100):
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

    def formatFullname(self, firstname: str, middlename: str, lastname: str, order: int = 0) -> str:
        first  = (firstname or "").strip()
        middle = (middlename or "").strip()
        last   = (lastname or "").strip()

        if not first or not last:
            return ""

        middle_initial = f"{middle[0].upper()}." if middle else ""

        if order == 0:  # Natural Order: First [M.] Last
            parts = [first, middle_initial, last]
            return " ".join(p for p in parts if p)

        elif order == 1:  # Reverse Order: Last, First [M.]
            given_names = " ".join(p for p in [first, middle_initial] if p)
            return f"{last}, {given_names}"

        elif order == 2:  # Formal/Legal Order: Last, First Middle
            given_names = " ".join(p for p in [first, middle] if p)
            return f"{last}, {given_names}"

        elif order == 3:  # Initialized Style: F. M. L.
            first_init = f"{first[0].upper()}."
            middle_init = f"{middle[0].upper()}." if middle else ""
            last_init = f"{last[0].upper()}."
            
            parts = [first_init, middle_init, last_init]
            return " ".join(p for p in parts if p)

        return f"{first} {last}"

    def getDifficultyLevel(self, index):
        levels = { 1: "Easy", 2: "Average", 3: "Hard" }
        return levels.get(index, "")

    def animate_slide(self, widget, show: bool, direction: str = "right", duration: int = 350):
        """
        Slides any QWidget smoothly into or out of view relative to its parent.
        """
        parent = widget.parentWidget()
        if not parent:
            return

        # Ensure layout doesn't interfere with fixed positional animation
        widget.raise_()

        w_width = widget.width()
        w_height = widget.height()
        p_width = parent.width()
        p_height = parent.height()

        # Cache standard resting position relative to parent layout
        if show:
            widget.setVisible(True)

        # Base Y/X stays aligned with its resting coordinate inside parent
        curr_x = widget.x()
        curr_y = widget.y()

        # Define explicit off-screen vs on-screen target coordinates
        if direction == "right":
            offscreen_point = QPoint(p_width, curr_y)
            # If the panel sits docked to the right edge when fully visible:
            onscreen_point = QPoint(p_width - w_width, curr_y)
        elif direction == "left":
            offscreen_point = QPoint(-w_width, curr_y)
            onscreen_point = QPoint(0, curr_y)
        elif direction == "bottom":
            offscreen_point = QPoint(curr_x, p_height)
            onscreen_point = QPoint(curr_x, p_height - w_height)
        elif direction == "top":
            offscreen_point = QPoint(curr_x, -w_height)
            onscreen_point = QPoint(curr_x, 0)

        # Set explicit start and end coordinates
        start_point = widget.pos() if widget.isVisible() else (offscreen_point if show else onscreen_point)
        end_point = onscreen_point if show else offscreen_point

        # Manage animation instance per widget
        if not hasattr(widget, "_slide_anim"):
            widget._slide_anim = QPropertyAnimation(widget, b"pos")

        anim = widget._slide_anim
        anim.stop()
        
        try:
            anim.finished.disconnect()
        except (RuntimeError, TypeError):
            pass

        anim.setDuration(duration)
        anim.setStartValue(start_point)
        anim.setEndValue(end_point)
        anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        if not show:
            anim.finished.connect(lambda: widget.setVisible(False))

        anim.start()

    def validate_gender(self, gender):
        if not gender:
            return ""

        clean_gender = str(gender).strip().upper()

        lookup = {
            'M': 'Male',
            'MALE': 'Male',
            'F': 'Female',
            'FEMALE': 'Female'
        }

        return lookup.get(clean_gender, "")

    def export_classlist_template(self, parent:QDialog=None):
        file_path, _ = QFileDialog.getSaveFileName(
            parent,
            "Save CSV Template",
            "student_import_template.csv",  # Default file name
            "CSV Files (*.csv);;All Files (*)"
        )

        if not file_path:
            print("Export cancelled by user.")
            return "Cancelled"

        headers = [
            "LAST NAME", 
            "FIRST NAME", 
            "MIDDLE NAME", 
            "GENDER", 
            "PASSWORD", 
            "CONTACT PERSON", 
            "CONTACT NUMBER"
        ]
        
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
            
            message = f"Template successfully saved to:\n{file_path}"
            print(f"Successfully exported template to '{file_path}'")
            
        except Exception as e:
            message = f"Failed to save file:\n{str(e)}"
            print(f"Error exporting template: {e}")

        return message



class CardStudent(QFrame):
    # Define a signal that carries a string (the student's name)
    clicked = Signal(object, str)

    """Custom widget representing a single card."""
    def __init__(self, name, stud_id, image, sectionName, gender):
        super().__init__()

        self.setProperty("selected", False) # Initialize property
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFixedSize(16777215, 100)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.app_settings = QSettings("CAI_System", "CAI_Admin_AppSettings")
        self.is_dark_mode = self.app_settings.value("dark_mode", False, type=bool)

        name_css    = "font-weight: bold; font-size: 16px; background-color: transparent;"
        _id_css     = "color: #777; font-size: 13px; background-color: transparent;"
        section_css = "color: #777; font-size: 13px; background-color: transparent;"

        if self.is_dark_mode:
            bgColor     = "rgba(52, 152, 219, 0.2)"
            borderColor = "#3498DB"

            if gender.upper() == "FEMALE":
                bgColor     = "rgba(229, 91, 144, 0.2)"
                borderColor = "#E55B90"

            self.setStyleSheet(f"""
                CardStudent {{
                    background-color: #2d2d2d;
                    border-radius: 10px;
                    border: 1px solid #4a4a4a;
                }}
                CardStudent:hover {{
                    border: 1px solid {borderColor};
                    background-color: {bgColor};
                }}
                /* This style applies when the custom property is true */
                CardStudent[selected="true"] {{
                    border: 2px solid {borderColor};
                    background-color: {bgColor};
                }}
                QLabel {{
                    color: #ffffff;
                }}
            """)

            name_css    = "font-weight: bold; font-size: 16px; color: #ffffff; background-color: transparent;"
            _id_css     = "color: #a0a0a0; font-size: 13px; background-color: transparent;"
            section_css = "color: #a0a0a0; font-size: 13px; background-color: transparent;"    

        else:
            bgColor     = "#E1F5FE"
            borderColor = "#3498DB"
    
            if gender.upper() == "FEMALE":
                bgColor     = "#FFE5F0"
                borderColor = "#E55B90"

            self.setStyleSheet(f"""
                CardStudent {{
                    background-color: #FFFFFF;
                    border-radius: 10px;
                    border: 1px solid #ddd;
                }}
                CardStudent:hover {{
                    border: 1px solid {borderColor};
                    background-color: {bgColor};
                }}
                /* This style applies when the custom property is true */
                CardStudent[selected="true"] {{
                    border: 2px solid {borderColor};
                    background-color: {bgColor};
                }}
                QLabel {{
                    color: #333;
                }}
            """)

        self.util = Utility()

        if self.util.isEmpty(image):
            image = QPixmap(u":/Images/Images/profile.png")
            image = self.util.makeCircularPixmap(image, 80)

        # Layout for the card
        layout = QHBoxLayout(self)

        self.photo = QLabel()
        circular_pixmap = self.util.makeCircularPixmap(image, 80)
        self.photo.setPixmap(circular_pixmap)
        self.photo.setFixedSize(80, 80)
        self.photo.setStyleSheet("background-color: transparent;")

        # Information
        info_layout = QVBoxLayout()
        self.name_label = QLabel(name)
        self.name_label.setStyleSheet(name_css)

        self.label_studentid = QLabel(stud_id)
        self.label_studentid.setStyleSheet(_id_css)

        self.label_section = QLabel(sectionName)
        self.label_section.setStyleSheet(section_css)

        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.label_studentid)
        info_layout.addWidget(self.label_section)
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

    def __init__(self, file_path:str):
        super().__init__()
        self.setWindowTitle("Wick Animation Player")
        self.resize(1024, 768)
        self.showMaximized()

        self.browser = QWebEngineView()

        if os.path.exists(file_path):
            self.browser.setUrl(QUrl.fromLocalFile(file_path))
        else:
            print(f"Error: {file_path} not found.")

        self.setCentralWidget(self.browser)



class CircularProgress(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self.suffix = "%"
        self.setMinimumSize(150, 150)

    def set_value(self, value):
        self.value = max(0, min(100, value)) # Keep between 0-100
        self.update() # Triggers repaint

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        margin = 10
        rect = QRectF(margin, margin, width - 2*margin, height - 2*margin)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 1. Draw Background Circle (Track)
        pen = QPen()
        pen.setWidth(12)
        pen.setColor(QColor("#e6e6e6")) # Light gray
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawArc(rect, 0, 360 * 16)

        # 2. Draw Progress (The "Bar")
        # Color changes based on performance
        color = "#ff4d4d" # Red
        if self.value >= 85: color = "#2ecc71" # Green
        elif self.value >= 70: color = "#f1c40f" # Yellow

        pen.setColor(QColor(color))
        painter.setPen(pen)

        # Calculate angle: start at 90 degrees (top), span is negative for clockwise
        start_angle = 90 * 16
        span_angle = -self.value * 3.6 * 16
        painter.drawArc(rect, start_angle, int(span_angle))

        # 3. Draw Text in Center
        painter.setPen(QColor("#333333"))
        painter.setFont(QFont("Arial", 18, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, f"{int(self.value)}{self.suffix}")



class NoScrollComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Prevent the widget from accepting focus via scrolling
        self.setFocusPolicy(Qt.StrongFocus)

    def wheelEvent(self, event):
        # Ignore the event so the scroll goes to the parent (the page)
        event.ignore()



class CustomMessageBox(QDialog, Ui_MessageBox):
    Yes           = 100
    No            = 101
    YesToAll      = 102
    NoToAll       = 103
    Cancel        = QDialog.DialogCode.Rejected  # 0
    Ok            = QDialog.DialogCode.Accepted  # 1
    RESIZE_MARGIN = 8

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setMouseTracking(True)

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

        if hasattr(self, 'label_icon'):
            self.label_icon.setPixmap(QPixmap(icon_path))
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
        return cls._create_and_exec(parent, title, message, ":/Images/Images/information.png", ['btnOk'])

    @classmethod
    def success(cls, parent, title, message):
        return cls._create_and_exec(parent, title, message, ":/Images/Images/success.png", ['btnOk'])

    @classmethod
    def warning(cls, parent, title, message):
        return cls._create_and_exec(parent, title, message, ":/Images/Images/warning.png", ['btnOk'])

    @classmethod
    def critical(cls, parent, title, message):
        return cls._create_and_exec(parent, title, message, ":/Images/Images/critical.png", ['btnOk'])

    @classmethod
    def question(cls, parent, title, message, include_all=False, show_cancel=False):
        buttons = ['btnYes', 'btnNo']

        if include_all:
            buttons.extend(['btnYesAll', 'btnNoAll'])
        if show_cancel:
            buttons.append('btnCancel')

        return cls._create_and_exec(parent, title, message, ":/Images/Images/question.png", buttons)

    def _get_resize_edge(self, pos):
        """Determine which edge or corner the mouse is over based on RESIZE_MARGIN."""
        rect = self.rect()
        x, y = pos.x(), pos.y()
        w, h = rect.width(), rect.height()

        left   = x <= self.RESIZE_MARGIN
        right  = x >= w - self.RESIZE_MARGIN
        top    = y <= self.RESIZE_MARGIN
        bottom = y >= h - self.RESIZE_MARGIN

        if top and left:
            return Qt.Edge.TopEdge | Qt.Edge.LeftEdge
        if top and right:
            return Qt.Edge.TopEdge | Qt.Edge.RightEdge
        if bottom and left:
            return Qt.Edge.BottomEdge | Qt.Edge.LeftEdge
        if bottom and right:
            return Qt.Edge.BottomEdge | Qt.Edge.RightEdge
        if left:
            return Qt.Edge.LeftEdge
        if right:
            return Qt.Edge.RightEdge
        if top:
            return Qt.Edge.TopEdge
        if bottom:
            return Qt.Edge.BottomEdge

        return None

    def _update_cursor_shape(self, edge):
        """Update cursor appearance depending on active resize edge/corner."""
        if edge in (Qt.Edge.TopEdge | Qt.Edge.LeftEdge, Qt.Edge.BottomEdge | Qt.Edge.RightEdge):
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif edge in (Qt.Edge.TopEdge | Qt.Edge.RightEdge, Qt.Edge.BottomEdge | Qt.Edge.LeftEdge):
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif edge in (Qt.Edge.LeftEdge, Qt.Edge.RightEdge):
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif edge in (Qt.Edge.TopEdge, Qt.Edge.BottomEdge):
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint() if hasattr(event, 'position') else event.pos()
        edge = self._get_resize_edge(pos)
        self._update_cursor_shape(edge)
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.position().toPoint() if hasattr(event, 'position') else event.pos()
            edge = self._get_resize_edge(pos)
            handle = self.windowHandle()

            if handle is not None:
                # 1. Native Window Resize
                if edge is not None:
                    handle.startSystemResize(edge)
                    event.accept()
                    return

                # 2. Native Window Move (Header Drag)
                if hasattr(self, 'dlg_frame_header'):
                    header_pos = self.dlg_frame_header.mapFrom(self, pos)
                    if self.dlg_frame_header.rect().contains(header_pos):
                        handle.startSystemMove()
                        event.accept()
                        return

        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.reject()
            return
        super().keyPressEvent(event)

    def closeEvent(self, event):
        self.setResult(self.Cancel)
        event.accept()



class CrossPlatformPrinter:
    def __init__(self):
        self.os_type = sys.platform

    def get_available_printers(self):
        """Returns a list of connected printer names on the system."""
        try:
            if self.os_type == "win32":
                # Windows fallback (runs via PowerShell without pywin32)
                cmd = ["powershell", "-Command", "Get-CimInstance Win32_Printer | Select-Object -ExpandProperty Name"]
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                return [line.strip() for line in result.stdout.splitlines() if line.strip()]
            else:
                # Zorin OS / Linux / macOS native printer fetching via CUPS
                result = subprocess.run(['lpstat', '-a'], capture_output=True, text=True, check=True)
                # Extracts the printer queue names from the lpstat utility output
                return [line.split()[0] for line in result.stdout.splitlines() if line]
        except Exception as e:
            print(f"Error fetching printers: {e}")
            return []

    def send_to_printer(self, file_path, printer_name=None):
        """Sends a document directly to the printer using native OS terminal hooks."""
        if not os.path.exists(file_path):
            return False, f"File not found: {file_path}"

        try:
            # --- ZORIN OS / LINUX / UNIX NATIVE PRINTING ---
            if self.os_type in ["linux", "darwin"]:
                # 'lp' is the built-in command to send documents to a printer queue in Zorin OS
                cmd = ['lp']
                if printer_name:
                    cmd.extend(['-d', printer_name])  # Speficy destination printer name
                cmd.append(file_path)

                # Fires headlessly without popping up annoying UI dialogs
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                return True, f"Sent to Zorin OS/CUPS printer queue: {printer_name or 'Default'}"

            # --- WINDOWS FALLBACK ---
            elif self.os_type == "win32":
                if printer_name:
                    cmd = ["powershell", "-Command", f"Start-Process -FilePath '{file_path}' -ArgumentList '/t \"{printer_name}\"' -WindowStyle Hidden"]
                    subprocess.run(cmd, check=True)
                else:
                    os.startfile(file_path, "print")
                return True, f"Sent to Windows print queue: {printer_name or 'Default'}"

            else:
                return False, f"Unsupported OS platform: {self.os_type}"

        except subprocess.CalledProcessError as e:
            return False, f"System command line printing failed: {e.stderr}"
        
        except Exception as e:
            return False, f"Printing failed: {str(e)}"



class CardRanking(QWidget, Ui_CardRanking):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.bgColor      ="#34A25B"
        self.bgColor2     ="#57C27B"
        self.student_rank = 1
        self.name         = ""
        self.avatar       = None
        self.score        = ""
        self.suffix       = "st"

    def set_ranking_info(self):

        if self.student_rank == 2:
            self.bgColor = "#5C5890"
            self.bgColor2 = "#7E74B0"
            self.suffix = "nd"

        elif self.student_rank == 3:
            self.bgColor = "#FEC000"
            self.bgColor2 = "#EFA60B"
            self.suffix = "rd"

        self.qss = f"""
            #widget_27 {{
                background-color: {self.bgColor};
                border-radius: 18px;
            }}

            #widget_26 {{
                background: transparent;
            }}

            #label_stud_name {{
                color: #FFF;
                background-color: transparent;
                font: 12pt "Inter Medium";
            }}

            #label_student_score {{
                font: 20pt "Inter SemiBold";
                background: transparent;
                color: #FFF;
            }}

            #label_student_place {{
                font: 12pt "Inter SemiBold";
                border-radius: 12px;
                background-color: {self.bgColor2};
                color: #FFF;
            }}
        """

        self.widget_27.setStyleSheet(self.qss)

        if self.avatar:
            self.label_profile.setPixmap(self.avatar)
            
        self.label_stud_name.setText(self.name)
        self.label_student_score.setText(f"{self.score}%")
        self.label_student_place.setText(f"{self.student_rank}{self.suffix}")


