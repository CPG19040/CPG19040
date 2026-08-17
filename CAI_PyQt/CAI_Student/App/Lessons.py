from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

from App.CRUDTools import DatabaseTools
from App.Tools import Utility
from App.CardLesson import Ui_CardLesson

class Lessons:
    def __init__(self):
        self.db_tools = DatabaseTools()

    def retrieve_lesson_info(self, lessonid=None):
        """
        Fetches detailed metadata for all lessons from the database.

        Returns:
            tuple: A record containing (lesson_id, chapter, lessonnum, gradingperiod, 
                title, path_str, lessonimages, lessonfilename). 
                Returns an 8-element tuple of empty strings if no record is found.
        """

        params = []
        
        sql = """
            SELECT 
                l.lesson_id,
                l.chapter,
                l.lessonnum,
                l.gradingperiod,
                l.title,
                l.path_str,
                l.lessonimages,
                l.lessonfilename
            FROM 
                cai.tbl_lessons l
            INNER JOIN 
                cai.tbl_grading_period gp ON l.gradingperiod = gp.gpid
            WHERE 
                CURRENT_DATE BETWEEN gp.startdate AND gp.enddate
        """

        if lessonid:
            sql += "    AND l.lesson_id = %s"
            params.append(lessonid)

        sql += """
            ORDER BY gradingperiod, chapter, lessonnum ASC;
        """
        cursor, conn = self.db_tools.retrieve_records(sql, tuple(params))

        if cursor:
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records

        conn.close()
        return list()


class LessonCard(QWidget):
    clicked = Signal(object, int)

    def __init__(self, lesson_id, lesson_name, lesson_num, chapter, pixmap=None):
        super().__init__()
        self.ui = Ui_CardLesson()
        self.ui.setupUi(self)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.util = Utility()
        
        self.lesson_id = lesson_id
        
        # Set the labels
        self.ui.label_LessonName.setText(lesson_name)
        self.ui.label_LessonNumber.setText(f"{lesson_num}")
        self.ui.label_Chapter.setText(f"Chapter {chapter}")
        
        if pixmap:
            pixmap = self.util.makeCircularPixmap(pixmap, self.ui.label_LessonImage.width(), 10)
            self.ui.label_LessonImage.setPixmap(pixmap)

    def mousePressEvent(self, event):
        # When the user clicks the card, emit the signal
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self, self.lesson_id)

    def set_selected(self, selected: bool):
        """Updates the property and refreshes the style."""
        self.setProperty("selected", selected)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
