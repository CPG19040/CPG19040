import csv

from pathlib import Path

from PySide6.QtGui import QStandardItemModel, QStandardItem, QImage, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFileDialog

from App.CRUDTools import DatabaseTools
from App.LessonDialog import Ui_LessonDialog
from App.Tools import Utility, CustomMessageBox

class Lesson:

    def __init__(self):
        self.db_tools = DatabaseTools()
        self.util = Utility()

    def count(self):
        sql = "SELECT COUNT(*) FROM cai.tbl_lessons;"
        record = self.db_tools.fetch_all(sql)

        count = 0

        if record:
            count = record[0]['count']

        return count

    def check_lesson_duplicate(self, chapter, lessonnum, gradingperiod, title):
        sql = """
            SELECT
                COUNT(lesson_id)
            FROM
                cai.tbl_lessons
            WHERE
                chapter = %s AND
                lessonnum = %s AND
                gradingperiod = %s AND
                title = %s;
        """
        rows = self.db_tools.fetch_all(sql, (chapter, lessonnum, gradingperiod, title))

        if rows and rows[0]["count"] > 0:
            return True

        return False

    def add_all_lessons_from_csv(self, csv_path):
        if not csv_path:
            return "No path for the CSV provided."

        errors = []

        try:
            with open(csv_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row_idx, row in enumerate(reader, start=1):
                    row_errors = []

                    # Validation checks
                    if not row.get("TITLE"): row_errors.append("Lesson Title is required.")
                    if not row.get("GRADING PERIOD"): row_errors.append("Grading Period is required.")
                    if not row.get("CHAPTER"): row_errors.append("Chapter is required.")
                    if not row.get("NUMBER"): row_errors.append("Lesson Number is required.")

                    if row_errors:
                        # Tracks which specific row had the issue
                        errors.append(f"Row {row_idx}: " + " | ".join(row_errors))
                        continue  # Skip inserting this row, but keep checking the rest

                    isDuplicate = self.check_lesson_duplicate(row["CHAPTER"], row["NUMBER"], row["GRADING PERIOD"], row["TITLE"])

                    if isDuplicate:
                        errors.append(f"Row {row_idx}: Lesson '{row['TITLE']}' already exists. Skipped.")
                        continue

                    lessonImage = self.util.read_image_file_bytes(row["IMAGE"])
                    sql  = "INSERT INTO cai.tbl_lessons (\n"
                    sql += "    chapter\n"
                    sql += "    ,lessonnum\n"
                    sql += "    ,gradingperiod\n"
                    sql += "    ,title\n"
                    sql += "    ,lessonfilename\n"
                    sql += "    ,lessonimages\n" if lessonImage else "\n"
                    sql += ") VALUES (%s, %s, %s, %s, %s"
                    sql += ", %s" if lessonImage else ""
                    sql += ");"

                    params = (
                        row["CHAPTER"],
                        row["NUMBER"],
                        row["GRADING PERIOD"],
                        row["TITLE"],
                        f"{row['TITLE']}.pdf"
                    )

                    params = params + (lessonImage,) if lessonImage else params
                    self.db_tools.execute_query(sql, params)

        except Exception as e:
            errors.append(f"Database/File error: {str(e)}")

        # Return all accumulated errors joined by newlines, or an empty string if successful
        return "\n".join(errors) if errors else ""

    def retrieve_lesson_info(self, lesson_id):
        """
        Retrieves detailed information for a specific lesson from the database.

        Args:
            lesson_id (int/str): The unique identifier of the lesson to fetch.

        Returns:
            tuple: A 8-element tuple containing (lesson_id, chapter, lessonnum,
                   gradingperiod, title, path_str, lessonimages, lessonfilename).
                   Returns a tuple of empty strings if no record is found or
                   if lesson_id is invalid.
        """
        if not lesson_id:
            return tuple([""] * 8)

        sql  = 'SELECT\n'
        sql += '    lesson_id\n'
        sql += '    ,chapter \n'
        sql += '    ,lessonnum\n'
        sql += '    ,gradingperiod\n'
        sql += '    ,title\n'
        sql += '    ,path_str\n'
        sql += '    ,lessonimages\n'
        sql += '    ,lessonfilename\n'
        sql += 'FROM cai.tbl_lessons\n'
        sql += 'WHERE lesson_id = %s\n'
        sql += 'ORDER BY lessonnum ASC'
        cursor, conn = self.db_tools.retrieve_records(sql, (lesson_id,))

        if cursor:
            records = cursor.fetchone()
            cursor.close()
            conn.close()
            return records

        if conn: conn.close()
        return tuple([""] * 8)

    def retrieve_lessons_table(self, searchText:str=""):
        sql  = 'SELECT\n'
        sql += '    lesson_id\n'
        sql += '    ,lessonimages AS " "\n'
        sql += '    ,title AS "Lesson Title"\n'
        sql += '    ,gradingperiod AS "Grading Period"\n'
        sql += '    ,lessonnum AS "Lesson Number"\n'
        sql += '    ,chapter AS "Chapter"\n'
        sql += 'FROM\n'
        sql += '    cai.tbl_lessons\n'

        params = None

        if searchText:
            sql += "WHERE title ILIKE %s\n"
            params = (f"%{searchText}%",)

        sql += "ORDER BY gradingperiod, chapter, lessonnum"
        cursor, conn = self.db_tools.retrieve_records(sql, params)

        if cursor:
            headers = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
            model = QStandardItemModel(len(records), len(headers))
            model.setHorizontalHeaderLabels(headers)
            row_pixmaps = []

            for row_idx, row_data in enumerate(records):
                for col_idx, value in enumerate(row_data):
                    item = QStandardItem()

                    # Column index 1 is "lessonimages"
                    if col_idx == 1:
                        if value:
                            pixmap = QPixmap()
                            if isinstance(value, (bytes, bytearray, memoryview)):
                                pixmap.loadFromData(bytes(value))
                            else:
                                pixmap.load(str(value))

                            if not pixmap.isNull():
                                scaled = pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                                item.setData(scaled, Qt.ItemDataRole.DecorationRole)
                                row_pixmaps.append(row_idx)
                    else:
                        item.setText(str(value) if value is not None else "")

                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    model.setItem(row_idx, col_idx, item)

                    if col_idx in [0, 3, 4, 5]:
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            cursor.close()
            conn.close()
            return model, row_pixmaps

        if conn: conn.close()
        return None

    def get_absolute_lesson_path(self, db_path_str):
        """
        Combines the dynamic root path with the filename from the database.
        """
        # Locate the project root (Assuming current file is in CAI_Admin/App)
        # .parent(App) -> .parent(CAI_Admin) -> .parent(ProjectRoot)
        project_root = Path(__file__).resolve().parent.parent.parent

        # Build the path to the Student Lessons folder
        lessons_folder = project_root / "CAI_Student" / "Lessons"

        # Join with the filename stored in the DB
        return lessons_folder / db_path_str


class LessonDialog(QDialog, Ui_LessonDialog):
    RESIZE_MARGIN = 8

    def __init__(self, mode=1, lesson_id=None): # mode: 1 Add, 2 Edit
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # Remove OS default window frame
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setMouseTracking(True)

        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnClose.clicked.connect(self.reject)

        self.db_tools = DatabaseTools()
        self.util     = Utility()
        lesson        = Lesson()

        self.image_data = None

        sql =  """
            SELECT gpid, gpname
	        FROM cai.tbl_grading_period;
        """
        self.util.populate_pulldown(self.cmbGradingPeriod, sql, add_empty=True)

        if mode == 1:
            self.setWindowTitle = "Add Lesson"
            self.btnSave.clicked.connect(self.add_lesson)

        elif mode == 2:
            self.setWindowTitle = "Edit Lesson"
            self.btnSave.clicked.connect(lambda: self.update_lesson(lesson_id))
            record = lesson.retrieve_lesson_info(lesson_id)
            _, chapter, lessonnum, gradingPeriod, title, path_str, lessonimages, lessonfilename = record

            index = self.cmbGradingPeriod.findData(gradingPeriod)
            file_path = ''

            if path_str:
                file_path = lesson.get_absolute_lesson_path(path_str)

            self.txtLessonTitle.setText(title)
            self.cmbGradingPeriod.setCurrentIndex(index)
            self.txtChapter.setText(f"{chapter}")
            self.txtLessonNumber.setText(f"{lessonnum}")
            self.txtLessonPath.setText(str(file_path))

            if not self.util.isEmpty(lessonimages):
                self.image_data = bytes(lessonimages)
                image = QImage.fromData(bytes(lessonimages))

                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)
                    pixmap = self.util.makeCircularPixmap(pixmap, self.label_img.width(), 20)
                    self.label_img.setPixmap(pixmap)

        self.btnUploadPhoto.clicked.connect(self.update_photo)
        self.btnBrowse.clicked.connect(self.browse_lesson)
        self.btnCancel.clicked.connect(self.reject)

    def _get_resize_edge(self, pos):
        """Determine which edge or corner the mouse is over based on RESIZE_MARGIN."""
        rect = self.rect()
        x, y = pos.x(), pos.y()
        w, h = rect.width(), rect.height()
        
        edge = None
        
        # Horizontal edges
        if x <= self.RESIZE_MARGIN:
            edge = Qt.Edge.LeftEdge
        elif x >= w - self.RESIZE_MARGIN:
            edge = Qt.Edge.RightEdge
            
        # Vertical edges
        if y <= self.RESIZE_MARGIN:
            if edge is None:
                edge = Qt.Edge.TopEdge
            else:
                edge |= Qt.Edge.TopEdge
        elif y >= h - self.RESIZE_MARGIN:
            if edge is None:
                edge = Qt.Edge.BottomEdge
            else:
                edge |= Qt.Edge.BottomEdge
                
        return edge

    def _update_cursor_shape(self, edge):
        """Update cursor appearance depending on the active resize edge/corner."""
        if edge == (Qt.Edge.TopEdge | Qt.Edge.LeftEdge) or edge == (Qt.Edge.BottomEdge | Qt.Edge.RightEdge):
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif edge == (Qt.Edge.TopEdge | Qt.Edge.RightEdge) or edge == (Qt.Edge.BottomEdge | Qt.Edge.LeftEdge):
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif edge and (edge & (Qt.Edge.LeftEdge | Qt.Edge.RightEdge)) and not (edge & (Qt.Edge.TopEdge | Qt.Edge.BottomEdge)):
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif edge and (edge & (Qt.Edge.TopEdge | Qt.Edge.BottomEdge)) and not (edge & (Qt.Edge.LeftEdge | Qt.Edge.RightEdge)):
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint()
        edge = self._get_resize_edge(pos)
        self._update_cursor_shape(edge)
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            edge = self._get_resize_edge(pos)
            
            # 1. If clicking near any edge/corner, resize the window
            if edge:
                self.windowHandle().startSystemResize(edge)
                event.accept()
                return

            # 2. If clicking inside the custom header, move the window
            if self.frame_header.geometry().contains(pos):
                self.windowHandle().startSystemMove()
                event.accept()
                return
            
        super().mousePressEvent(event)

    def add_lesson(self):
        title = self.txtLessonTitle.text().strip()
        grading = self.cmbGradingPeriod.currentData()
        chapter = self.txtChapter.text().strip()
        lesson_num = self.txtLessonNumber.text().strip()
        path_str = self.txtLessonPath.text().strip()

        errors = []
        if not title: errors.append("Lesson Title is required.")
        if not grading: errors.append("Grading Period is required.")
        if not chapter: errors.append("Chapter is required.")
        if not lesson_num: errors.append("Lesson Number is required.")

        if errors:
            CustomMessageBox.warning(self, "Validation Failed", "\n".join(errors))
            return

        file_name = ''

        if path_str:
            file_name = Path(path_str).name  # Result: "lesson_one.pdf"

        sql = "INSERT INTO cai.tbl_lessons (\n"
        sql += "    chapter\n"
        sql += "    ,lessonnum\n"
        sql += "    ,gradingperiod\n"
        sql += "    ,title\n"
        sql += "    ,path_str\n"
        sql += "    ,lessonimages\n"
        sql += "    ,lessonfilename\n"
        sql += ")\n"
        sql += "VALUES (%s, %s, %s, %s, %s, %s, %s);"

        try:
            self.db_tools.execute_query(sql, (
                chapter,
                lesson_num,
                grading,
                title,
                file_name,
                self.image_data,
                f"{title.replace(' ', '_')}.pdf"
            ))

            CustomMessageBox.success(self, "Success", "Lesson added successfully!")
            self.accept()

        except Exception as e:
            CustomMessageBox.critical(self, "Database Error", f"Failed to save: {str(e)}")

    def update_lesson(self, lesson_id):
        if not lesson_id:
            return

        title = self.txtLessonTitle.text().strip()
        grading = self.cmbGradingPeriod.currentData()
        chapter = self.txtChapter.text().strip()
        lesson_num = self.txtLessonNumber.text().strip()
        path_str = self.txtLessonPath.text().strip()

        errors = []
        if not title: errors.append("Lesson Title is required.")
        if not grading: errors.append("Grading Period is required.")
        if not chapter: errors.append("Chapter is required.")
        if not lesson_num: errors.append("Lesson Number is required.")

        if errors:
            CustomMessageBox.warning(self, "Validation Failed", "\n".join(errors))
            return

        file_name = ''

        if path_str:
            file_name = Path(path_str).name  # Result: "lesson_one.pdf"

        sql = "UPDATE cai.tbl_lessons\n"
        sql += "SET\n"
        sql += "    chapter = %s\n"
        sql += "    ,lessonnum = %s\n"
        sql += "    ,gradingperiod = %s\n"
        sql += "    ,title = %s\n"
        sql += "    ,path_str = %s\n"
        sql += "    ,lessonimages = %s\n"
        sql += "    ,lessonfilename = %s\n"
        sql += "WHERE lesson_id = %s;"

        try:
            filename = f"{title.replace(' ', '_')}.pdf"

            self.db_tools.execute_query(sql, (
                chapter,
                lesson_num,
                grading,
                title,
                file_name,
                self.image_data,
                filename,
                lesson_id # The ID of the record you are editing
            ))

            CustomMessageBox.success(self, "Success", "Lesson updated successfully!")
            self.accept()

        except Exception as e:
            CustomMessageBox.critical(self, "Database Error", f"Failed to update: {str(e)}")

    def update_photo(self):
        pixmap, binaryImage = self.util.browsePhoto(self, self.label_img.width(), self.label_img.height())

        if pixmap:
            pixmap = self.util.makeCircularPixmap(pixmap, self.label_img.width(), 20)
            self.label_img.setPixmap(pixmap)

        if binaryImage:
            self.image_data = binaryImage

    def browse_lesson(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("HTML (*.html)")

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()

            if selected_files:
                self.txtLessonPath.setText(selected_files[0])

