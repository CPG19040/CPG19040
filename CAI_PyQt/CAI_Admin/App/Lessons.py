from pathlib import Path

from PySide6.QtGui import QStandardItemModel, QStandardItem, QImage, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QDialog, QFileDialog

from App.CRUDTools import DatabaseTools
from App.LessonDialog import Ui_LessonDialog
from App.Tools import Utility

class Lesson:

    def __init__(self):
        self.db_tools = DatabaseTools()
        
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

        sql = 'SELECT\n'
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
                                scaled = pixmap.scaled(25, 25, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                                item.setData(scaled, Qt.ItemDataRole.DecorationRole)
                    else:
                        item.setText(str(value) if value is not None else "")

                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    model.setItem(row_idx, col_idx, item)

            cursor.close()
            conn.close()
            return model

        if conn: conn.close()
        return None
    
    def get_absolute_lesson_path(self, db_path_str):
        """
        Combines the dynamic root path with the filename from the database.
        """
        # 1. Locate the project root (Assuming current file is in CAI_Admin/App)
        # .parent(App) -> .parent(CAI_Admin) -> .parent(ProjectRoot)
        project_root = Path(__file__).resolve().parent.parent.parent
        
        # 2. Build the path to the Student Lessons folder
        lessons_folder = project_root / "CAI_Student" / "Lessons"
        
        # 3. Join with the filename stored in the DB
        return lessons_folder / db_path_str


class LessonDialog(QDialog, Ui_LessonDialog):
    def __init__(self, mode=1, lesson_id=None): # mode: 1 Add, 2 Edit
        super().__init__()
        self.setupUi(self)

        self.db_tools = DatabaseTools()
        self.util = Utility()
        lesson = Lesson()

        self.image_data = None

        sql =  "SELECT 1 AS index, 'First Grading' AS itemname\n"
        sql += "UNION ALL\n"
        sql += "SELECT 2, 'Second Grading'\n"
        sql += "UNION ALL\n"
        sql += "SELECT 3, 'Third Grading'\n"
        sql += "UNION ALL\n"
        sql += "SELECT 4, 'Fourth Grading'\n"
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
                    self.label_img.setPixmap(pixmap)

        self.btnUploadPhoto.clicked.connect(self.update_photo)
        self.btnBrowse.clicked.connect(self.browse_lesson)
        self.btnCancel.clicked.connect(self.reject)

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
            QMessageBox.warning(self, "Validation Error", "\n".join(errors))
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
            
            QMessageBox.information(self, "Success", "Lesson added successfully!")
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to save: {str(e)}")

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
            QMessageBox.warning(self, "Validation Error", "\n".join(errors))
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
            
            QMessageBox.information(self, "Success", "Lesson updated successfully!")
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to update: {str(e)}")

    def update_photo(self):
        pixmap, binaryImage = self.util.browsePhoto(self, self.label_img.width(), self.label_img.height())

        if pixmap:
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