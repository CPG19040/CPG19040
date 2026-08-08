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
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CardScores(object):
    def setupUi(self, CardScores):
        if not CardScores.objectName():
            CardScores.setObjectName(u"CardScores")
        CardScores.resize(459, 164)
        CardScores.setMaximumSize(QSize(16777215, 164))
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
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 26))
        self.label_3.setMaximumSize(QSize(16777215, 26))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"font: 12pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(50, 50))
        self.widget_5.setMaximumSize(QSize(50, 50))
        self.widget_5.setStyleSheet(u"#widget_5 {\n"
"	border-image: url(:/Images/Images/wood_round.png);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_quiznum = QLabel(self.widget_5)
        self.label_quiznum.setObjectName(u"label_quiznum")
        self.label_quiznum.setStyleSheet(u"border-radius: 10px; font: 22pt \"Biscuit Glitch\"; color: rgb(255, 255, 255);")
        self.label_quiznum.setScaledContents(True)
        self.label_quiznum.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_quiznum)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
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
        self.label_LessonName.setLayoutDirection(Qt.LeftToRight)
        self.label_LessonName.setStyleSheet(u"font: 14pt \"Inter Medium\"; color: rgb(99, 69, 44); padding: 0px 10px;")
        self.label_LessonName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_LessonName.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_LessonName)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 26))
        self.label_2.setMaximumSize(QSize(16777215, 26))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"font: 12pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_score = QLabel(self.widget_4)
        self.label_score.setObjectName(u"label_score")
        self.label_score.setMaximumSize(QSize(16777215, 40))
        self.label_score.setLayoutDirection(Qt.LeftToRight)
        self.label_score.setStyleSheet(u"font: 22pt \"Biscuit Glitch\"; color: rgb(230, 97, 0);")
        self.label_score.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_score)

        self.widget_progress = QWidget(self.widget_4)
        self.widget_progress.setObjectName(u"widget_progress")
        self.widget_progress.setMinimumSize(QSize(250, 50))
        self.widget_progress.setMaximumSize(QSize(250, 50))
        self.widget_progress.setStyleSheet(u"#widget_progress {\n"
"	color: rgb(51, 209, 122);\n"
"	border-image: url(:/Images/Images/button_wood.png);\n"
"	background: transparent;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_progress)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(24, 13, 24, 13)
        self.progressBar_score = QProgressBar(self.widget_progress)
        self.progressBar_score.setObjectName(u"progressBar_score")
        self.progressBar_score.setStyleSheet(u"QProgressBar {\n"
"	border-radius: 10px;\n"
"	background-color: #5f2845;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 rgb(87, 227, 137), \n"
"                                stop:1 rgb(4, 167, 38));\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(4, 167, 38);\n"
"}")
        self.progressBar_score.setValue(24)
        self.progressBar_score.setAlignment(Qt.AlignCenter)
        self.progressBar_score.setTextVisible(False)
        self.progressBar_score.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.progressBar_score)


        self.horizontalLayout_2.addWidget(self.widget_progress)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 26))
        self.label_4.setMaximumSize(QSize(16777215, 26))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"font: 12pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_percentage = QLabel(self.widget_3)
        self.label_percentage.setObjectName(u"label_percentage")
        self.label_percentage.setMinimumSize(QSize(0, 26))
        self.label_percentage.setLayoutDirection(Qt.LeftToRight)
        self.label_percentage.setStyleSheet(u"font: 14pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_percentage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_percentage.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_percentage)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(CardScores)

        QMetaObject.connectSlotsByName(CardScores)
    # setupUi

    def retranslateUi(self, CardScores):
        CardScores.setWindowTitle(QCoreApplication.translate("CardScores", u"Frame", None))
        self.label_3.setText(QCoreApplication.translate("CardScores", u"Quiz #:", None))
        self.label_quiznum.setText(QCoreApplication.translate("CardScores", u"1", None))
        self.label_1.setText(QCoreApplication.translate("CardScores", u"Lesson Title:", None))
        self.label_LessonName.setText(QCoreApplication.translate("CardScores", u"Lesson Name", None))
        self.label_2.setText(QCoreApplication.translate("CardScores", u"Score:", None))
        self.label_score.setText(QCoreApplication.translate("CardScores", u"0/0", None))
        self.label_4.setText(QCoreApplication.translate("CardScores", u"Percentage:", None))
        self.label_percentage.setText(QCoreApplication.translate("CardScores", u"0.0%", None))
    # retranslateUi

