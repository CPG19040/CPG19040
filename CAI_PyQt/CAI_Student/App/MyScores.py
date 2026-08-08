from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

from App.CRUDTools import DatabaseTools
from App.Tools import Utility
from App.CardScores import Ui_CardScores


class MyScores:

    def __init__(self):
        self.db_tools = DatabaseTools()
        self.util = Utility()

    def get_scores(self, studentId, gradingperiod):
        # Optimized SQL combining quiz details and total score calculations in a single trip
        sql = """
            WITH QuizTotals AS (
                SELECT 
                    Q.QUIZNUMBER, 
                    Q.LESSONID,
                    (COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 1 THEN 1 END) * M.EASY_MULTIPLIER) +
                    (COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 2 THEN 1 END) * M.AVERAGE_MULTIPLIER) +
                    (COUNT(CASE WHEN Q.DIFFICULTYLEVEL = 3 THEN 1 END) * M.HARD_MULTIPLIER) AS max_score
                FROM (
                    SELECT QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL FROM CAI.TBL_QUIZIDENTIFICATION
                    UNION ALL
                    SELECT QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL FROM CAI.TBL_QUIZMULTIPLECHOICE
                    UNION ALL
                    SELECT QUIZNUMBER, LESSONID, GRADINGPERIOD, DIFFICULTYLEVEL FROM CAI.TBL_QUIZTRUEORFALSE
                ) Q
                JOIN CAI.TBL_SCOREMULTIPLIER M ON Q.QUIZNUMBER = M.QUIZNUMBER AND Q.LESSONID = M.LESSONID
                WHERE Q.GRADINGPERIOD = %s
                GROUP BY Q.QUIZNUMBER, Q.LESSONID, M.EASY_MULTIPLIER, M.AVERAGE_MULTIPLIER, M.HARD_MULTIPLIER
            )
            SELECT DISTINCT *
            FROM (
                SELECT
                    qs.quiznumber,
                    q.lessonid,
                    l.title,
                    qs.quizscore,
                    COALESCE(qt.max_score, 0) AS total_score,
                    TO_CHAR(qs.datetaken, 'YYYY/MM/DD, HH12:MI AM') AS datetaken
                FROM cai.tbl_quizscores AS qs
                JOIN cai.tbl_quiz AS q ON q.quiznumber = qs.quiznumber AND q.lessonid = qs.lessonid
                JOIN cai.tbl_lessons AS l ON qs.lessonid = l.lesson_id
                LEFT JOIN QuizTotals qt ON q.quiznumber = qt.quiznumber AND q.lessonid = qt.lessonid
                WHERE qs.studentid = %s
                    AND qs.gradingperiod = %s
                    AND qs.quizscore <= qt.max_score
                ORDER BY qs.datetaken DESC
            );
        """

        records = self.db_tools.fetch_all(sql, (gradingperiod, studentId, gradingperiod))

        return records


class CardScores(QWidget):
    clicked = Signal(object, int)

    def __init__(self, quiznumber, lesson_id, lesson_name, score_str, percent_val, percentage_str):
        super().__init__()
        self.ui = Ui_CardScores()
        self.ui.setupUi(self)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.util = Utility()
        
        self.lesson_id = lesson_id
        
        # Set the labels
        self.ui.label_LessonName.setText(lesson_name)
        self.ui.label_quiznum.setText(str(quiznumber))
        self.ui.label_score.setText(str(score_str))
        self.ui.progressBar_score.setValue(percent_val)
        self.ui.label_percentage.setText(f"Percentage: {percentage_str}")

    def mousePressEvent(self, event):
        # When the user clicks the card, emit the signal
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self, self.lesson_id)

    def focusInEvent(self, event):
        """Triggered when the card gains focus (e.g., via Tab key)."""
        if not self.property("selected"):
            self.clicked.emit(self, self.lesson_id)
        super().focusInEvent(event)

    def set_selected(self, selected: bool):
        """Updates the property and refreshes the style."""
        self.setProperty("selected", selected)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()


