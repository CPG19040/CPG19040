import os, sys, subprocess

from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QFileDialog, QWidget, QMainWindow, QDialog, QComboBox
from PySide6.QtGui import QPixmap, QPainter, QColor, QPen, QPainterPath, QFont
from PySide6.QtCore import Qt, Signal, QDate, QUrl, QRectF
from PySide6.QtWebEngineWidgets import QWebEngineView

from App.CRUDTools import DatabaseTools
from App.MessageBox import Ui_MessageBox

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

    def makeCircularPixmap(self, src_pixmap:QPixmap, size=80):
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
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)

        # Draw the image into the circle (centered)
        delta_x = (scaled_pixmap.width() - size) // 2
        delta_y = (scaled_pixmap.height() - size) // 2
        painter.drawPixmap(0, 0, scaled_pixmap.copy(delta_x, delta_y, size, size))

        # # Optional: Add a subtle border
        # painter.setClipping(False) # Stop clipping to draw the border
        # painter.setPen(QPen(Qt.GlobalColor.lightGray, 1))
        # painter.drawEllipse(0, 0, size - 1, size - 1)

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
            self.populate_lesson_pulldown(selected_period, pulldown_lessons)

    def populate_lesson_pulldown(self, gpid, pulldown_lessons):
        sql  = 'SELECT\n'
        sql += '    lesson_id\n'
        sql += '    ,title\n'
        sql += 'FROM cai.tbl_lessons\n'
        sql += 'WHERE gradingperiod = %s\n'
        sql += 'ORDER BY chapter, lessonnum ASC'
        self.populate_pulldown(pulldown_lessons, sql, params=(gpid,), add_empty=True)

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

    def getDifficultyLevel(self, index):
        levels = { 1: "Easy", 2: "Average", 3: "Hard" }
        return levels.get(index, "")


class CardStudent(QFrame):
    # Define a signal that carries a string (the student's name)
    clicked = Signal(object, str)

    """Custom widget representing a single card."""
    def __init__(self, name, stud_id, image, sectionName):
        super().__init__()
        self.setProperty("selected", False) # Initialize property
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFixedSize(16777215, 100)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            CardStudent {
                background-color: #ffffff;
                border-radius: 10px;
                border: 1px solid #ddd;
            }
            CardStudent:hover {
                border: 1px solid #3498db;
                background-color: #f7fbfe;
            }
            /* This style applies when the custom property is true */
            CardStudent[selected="true"] {
                background-color: #e1f5fe;
                border: 2px solid #3498db;
            }
            QLabel {
                color: #333;
            }
        """)

        self.util = Utility()

        if self.util.isEmpty(image):
            path = self.util.get_resource_path(os.path.join("..", "Images", "profile_gray.png"))
            image = self.util.getCircularPixmapFromImagePath(path, 80)

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
        self.name_label.setStyleSheet("font-weight: bold; font-size: 16px; background-color: transparent;")

        self.label_studentid = QLabel(stud_id)
        self.label_studentid.setStyleSheet("color: #777; font-size: 13px; background-color: transparent;")

        self.label_section = QLabel(sectionName)
        self.label_section.setStyleSheet("color: #777; font-size: 13px; background-color: transparent;")

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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def information(self, title, message):
        self.setWindowTitle(title)
        self.plainTextEdit.setPlainText(message)



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




