# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardScores.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_CardScores(object):
    def setupUi(self, CardScores):
        if not CardScores.objectName():
            CardScores.setObjectName(u"CardScores")
        CardScores.resize(183, 124)
        CardScores.setFocusPolicy(Qt.StrongFocus)
        CardScores.setStyleSheet(u"#CardLesson { background-color: transparent; }")
        self.horizontalLayout = QHBoxLayout(CardScores)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(CardScores)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"	background-color: #f8e6cb;\n"
"	border-radius: 15px;\n"
"	border: 1px solid #ddd;\n"
"}\n"
"#widget_2:hover {\n"
"	border: 2px solid #cd99d0;\n"
"	background-color: #f7fbfe;\n"
"}\n"
"/* This style applies when the custom property is true */\n"
"#widget_2[selected=\"true\"] {\n"
"	background-color: #e1f5fe;\n"
"	border: 2px solid #3498db;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.label_quiznum = QLabel(self.widget_2)
        self.label_quiznum.setObjectName(u"label_quiznum")
        self.label_quiznum.setStyleSheet(u"border-radius: 10px; font: 22pt \"Biscuit Glitch\";")
        self.label_quiznum.setScaledContents(True)
        self.label_quiznum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_quiznum)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(0, 26))
        self.label_1.setMaximumSize(QSize(16777215, 26))
        self.label_1.setLayoutDirection(Qt.LeftToRight)
        self.label_1.setStyleSheet(u"font: 12pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.label_LessonName = QLabel(self.widget)
        self.label_LessonName.setObjectName(u"label_LessonName")
        self.label_LessonName.setMinimumSize(QSize(0, 26))
        self.label_LessonName.setMaximumSize(QSize(16777215, 26))
        self.label_LessonName.setLayoutDirection(Qt.LeftToRight)
        self.label_LessonName.setStyleSheet(u"font: 14pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_LessonName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_LessonName)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 26))
        self.label_2.setMaximumSize(QSize(16777215, 26))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"font: 12pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_score = QLabel(self.widget_3)
        self.label_score.setObjectName(u"label_score")
        self.label_score.setMinimumSize(QSize(0, 26))
        self.label_score.setMaximumSize(QSize(16777215, 26))
        self.label_score.setLayoutDirection(Qt.LeftToRight)
        self.label_score.setStyleSheet(u"font: 22pt \"Biscuit Glitch\"; color: rgb(230, 97, 0);")
        self.label_score.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_score)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(CardScores)

        QMetaObject.connectSlotsByName(CardScores)
    # setupUi

    def retranslateUi(self, CardScores):
        CardScores.setWindowTitle(QCoreApplication.translate("CardScores", u"Frame", None))
        self.label_quiznum.setText(QCoreApplication.translate("CardScores", u"1", None))
        self.label_1.setText(QCoreApplication.translate("CardScores", u"Lesson Title:", None))
        self.label_LessonName.setText(QCoreApplication.translate("CardScores", u"Lesson Name", None))
        self.label_2.setText(QCoreApplication.translate("CardScores", u"Score:", None))
        self.label_score.setText(QCoreApplication.translate("CardScores", u"0/0", None))
    # retranslateUi

