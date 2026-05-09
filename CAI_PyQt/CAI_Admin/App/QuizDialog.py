# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QuizDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_QuizCreatorDialog(object):
    def setupUi(self, QuizCreatorDialog):
        if not QuizCreatorDialog.objectName():
            QuizCreatorDialog.setObjectName(u"QuizCreatorDialog")
        QuizCreatorDialog.resize(1011, 689)
        QuizCreatorDialog.setStyleSheet(u"color: black; font: 10pt \"Inter\"; background-color: rgb(222, 221, 218);")
        self.verticalLayout_2 = QVBoxLayout(QuizCreatorDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.label_1 = QLabel(QuizCreatorDialog)
        self.label_1.setObjectName(u"label_1")

        self.headerLayout.addWidget(self.label_1)

        self.quiz_no = QSpinBox(QuizCreatorDialog)
        self.quiz_no.setObjectName(u"quiz_no")
        self.quiz_no.setMinimumSize(QSize(0, 30))
        self.quiz_no.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.quiz_no.setMinimum(1)
        self.quiz_no.setMaximum(999)
        self.quiz_no.setValue(1)

        self.headerLayout.addWidget(self.quiz_no)

        self.label_2 = QLabel(QuizCreatorDialog)
        self.label_2.setObjectName(u"label_2")

        self.headerLayout.addWidget(self.label_2)

        self.cbGradingPeriod = QComboBox(QuizCreatorDialog)
        self.cbGradingPeriod.setObjectName(u"cbGradingPeriod")
        self.cbGradingPeriod.setMinimumSize(QSize(180, 30))
        self.cbGradingPeriod.setStyleSheet(u"color: rgb(0, 0, 0); background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.headerLayout.addWidget(self.cbGradingPeriod)

        self.label_3 = QLabel(QuizCreatorDialog)
        self.label_3.setObjectName(u"label_3")

        self.headerLayout.addWidget(self.label_3)

        self.cbLessonName = QComboBox(QuizCreatorDialog)
        self.cbLessonName.setObjectName(u"cbLessonName")
        self.cbLessonName.setMinimumSize(QSize(250, 30))
        self.cbLessonName.setMaximumSize(QSize(250, 30))
        self.cbLessonName.setStyleSheet(u"color: rgb(0, 0, 0); background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.headerLayout.addWidget(self.cbLessonName)

        self.checkBoxLockQuiz = QCheckBox(QuizCreatorDialog)
        self.checkBoxLockQuiz.setObjectName(u"checkBoxLockQuiz")
        self.checkBoxLockQuiz.setMinimumSize(QSize(0, 30))
        self.checkBoxLockQuiz.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBoxLockQuiz.setStyleSheet(u"QCheckBox {\n"
"	background-color: transparent;\n"
"	padding: 5px 10px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"	background-color: rgb(246, 245, 244);\n"
"	border: 2px solid #555555;\n"
"	border-radius: 3px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/Images/Images/check.png);\n"
"}")

        self.headerLayout.addWidget(self.checkBoxLockQuiz)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(QuizCreatorDialog)
        self.label_4.setObjectName(u"label_4")

        self.headerLayout.addWidget(self.label_4)

        self.label_totalScore = QLabel(QuizCreatorDialog)
        self.label_totalScore.setObjectName(u"label_totalScore")

        self.headerLayout.addWidget(self.label_totalScore)


        self.verticalLayout_2.addLayout(self.headerLayout)

        self.line_3 = QFrame(QuizCreatorDialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.widget_qbuilder = QWidget(QuizCreatorDialog)
        self.widget_qbuilder.setObjectName(u"widget_qbuilder")
        self.verticalLayout_5 = QVBoxLayout(self.widget_qbuilder)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.widget_qbuilder)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"#frame_5 { background-color: transparent; }")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_6)

        self.widget_2 = QWidget(self.frame_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"/* Base style for all difficulty buttons */\n"
"QPushButton {\n"
"    border: 1px solid #999;\n"
"    padding: 5px 15px;\n"
"	font: 10pt \"Inter\";\n"
"    background-color: #f0f0f0; /* Default neutral color */\n"
"}\n"
"\n"
"/* LEFT BUTTON (Easy) */\n"
"QPushButton#btnEasy {\n"
"    border-top-left-radius: 6px;\n"
"    border-bottom-left-radius: 6px;\n"
"    border-right: none; /* Avoid double borders in the middle */\n"
"}\n"
"QPushButton#btnEasy:checked {\n"
"    background-color: #72D582; /* Green */\n"
"	border: 2px solid #448D50;\n"
"    color: #000;\n"
"}\n"
"\n"
"/* MIDDLE BUTTON (Average) */\n"
"QPushButton#btnAverage {\n"
"    border-radius: 0px;\n"
"    border-right: none;\n"
"}\n"
"QPushButton#btnAverage:checked {\n"
"	background-color: #FFF2AC; /* Yellow */\n"
"	border: 2px solid #FCB988;\n"
"	color: #000;\n"
"}\n"
"\n"
"/* RIGHT BUTTON (Hard) */\n"
"QPushButton#btnHard {\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"QPushButton#btnHard:checked {\n"
"	bac"
                        "kground-color: #F07D75; /* Red */\n"
"	border: 2px solid #E65247;\n"
"	color: #000;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnEasy = QPushButton(self.widget_2)
        self.btnEasy.setObjectName(u"btnEasy")
        self.btnEasy.setMinimumSize(QSize(0, 30))
        self.btnEasy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEasy.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnEasy)

        self.btnAverage = QPushButton(self.widget_2)
        self.btnAverage.setObjectName(u"btnAverage")
        self.btnAverage.setMinimumSize(QSize(0, 30))
        self.btnAverage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAverage.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnAverage)

        self.btnHard = QPushButton(self.widget_2)
        self.btnHard.setObjectName(u"btnHard")
        self.btnHard.setMinimumSize(QSize(0, 30))
        self.btnHard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnHard.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnHard)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setStyleSheet(u"font: 10pt \"Inter SemiBold\";")

        self.horizontalLayout.addWidget(self.label_18)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_15)

        self.multiplier_easy = QSpinBox(self.frame_5)
        self.multiplier_easy.setObjectName(u"multiplier_easy")
        self.multiplier_easy.setMinimumSize(QSize(0, 30))
        self.multiplier_easy.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.multiplier_easy.setMinimum(1)
        self.multiplier_easy.setMaximum(999)
        self.multiplier_easy.setValue(1)

        self.horizontalLayout.addWidget(self.multiplier_easy)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_16)

        self.multiplier_average = QSpinBox(self.frame_5)
        self.multiplier_average.setObjectName(u"multiplier_average")
        self.multiplier_average.setMinimumSize(QSize(0, 30))
        self.multiplier_average.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.multiplier_average.setMinimum(1)
        self.multiplier_average.setMaximum(999)
        self.multiplier_average.setValue(1)

        self.horizontalLayout.addWidget(self.multiplier_average)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_17)

        self.multiplier_hard = QSpinBox(self.frame_5)
        self.multiplier_hard.setObjectName(u"multiplier_hard")
        self.multiplier_hard.setMinimumSize(QSize(0, 30))
        self.multiplier_hard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.multiplier_hard.setMinimum(1)
        self.multiplier_hard.setMaximum(999)
        self.multiplier_hard.setValue(1)

        self.horizontalLayout.addWidget(self.multiplier_hard)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.widget_qbuilder)

        self.line_2 = QFrame(QuizCreatorDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.widget = QWidget(QuizCreatorDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setStyleSheet(u"font: 11pt \"Inter SemiBold\"; ")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_id_count = QLabel(self.widget)
        self.label_id_count.setObjectName(u"label_id_count")

        self.horizontalLayout_3.addWidget(self.label_id_count)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnAddItem_id = QPushButton(self.widget)
        self.btnAddItem_id.setObjectName(u"btnAddItem_id")
        self.btnAddItem_id.setMinimumSize(QSize(0, 30))
        self.btnAddItem_id.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddItem_id.setStyleSheet(u"background: #27ae60;")

        self.horizontalLayout_3.addWidget(self.btnAddItem_id)


        self.verticalLayout_2.addWidget(self.widget)

        self.scrollArea_id = QScrollArea(QuizCreatorDialog)
        self.scrollArea_id.setObjectName(u"scrollArea_id")
        self.scrollArea_id.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"#scrollArea_id { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: rgb(246, 245, 244);\n"
"	font: 10pt \"Inter\";\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"#scrollArea_id QWidget #qt_scrollarea_viewport {\n"
"    background: rgb(246, 245, 244);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* 3. VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #7a7a7a;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 4. HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    height: 10px; /* Note: height, not width */\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::ha"
                        "ndle:horizontal {\n"
"    background: #7a7a7a;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 5. REMOVE BUTTONS & TRACK BACKGROUNDS */\n"
"/* This handles both horizontal and vertical arrows/tracks */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* 6. THE CORNER WIDGET \n"
"   (The small square where both bars meet) */\n"
"#scrollArea_id QWidget #qt_scrollarea_corner {\n"
"    background: rgb(246, 245, 244);\n"
"    border: none;\n"
"}")
        self.scrollArea_id.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 993, 128))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_id.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_2.addWidget(self.scrollArea_id)

        self.widget_3 = QWidget(QuizCreatorDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setStyleSheet(u"font: 11pt \"Inter SemiBold\"; ")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.label_mc_count = QLabel(self.widget_3)
        self.label_mc_count.setObjectName(u"label_mc_count")

        self.horizontalLayout_5.addWidget(self.label_mc_count)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btnAddItem_mc = QPushButton(self.widget_3)
        self.btnAddItem_mc.setObjectName(u"btnAddItem_mc")
        self.btnAddItem_mc.setMinimumSize(QSize(0, 30))
        self.btnAddItem_mc.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddItem_mc.setStyleSheet(u"background: #27ae60;")

        self.horizontalLayout_5.addWidget(self.btnAddItem_mc)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.scrollArea_mc = QScrollArea(QuizCreatorDialog)
        self.scrollArea_mc.setObjectName(u"scrollArea_mc")
        self.scrollArea_mc.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"#scrollArea_mc { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: rgb(246, 245, 244);\n"
"	font: 10pt \"Inter\";\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"#scrollArea_mc QWidget #qt_scrollarea_viewport {\n"
"    background: rgb(246, 245, 244);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* 3. VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #7a7a7a;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 4. HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    height: 10px; /* Note: height, not width */\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::ha"
                        "ndle:horizontal {\n"
"    background: #7a7a7a;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 5. REMOVE BUTTONS & TRACK BACKGROUNDS */\n"
"/* This handles both horizontal and vertical arrows/tracks */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* 6. THE CORNER WIDGET \n"
"   (The small square where both bars meet) */\n"
"#scrollArea_mc QWidget #qt_scrollarea_corner {\n"
"    background: rgb(246, 245, 244);\n"
"    border: none;\n"
"}")
        self.scrollArea_mc.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 993, 127))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_mc.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_mc)

        self.widget_4 = QWidget(QuizCreatorDialog)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setStyleSheet(u"font: 11pt \"Inter SemiBold\"; ")

        self.horizontalLayout_6.addWidget(self.label_14)

        self.label_tf_count = QLabel(self.widget_4)
        self.label_tf_count.setObjectName(u"label_tf_count")

        self.horizontalLayout_6.addWidget(self.label_tf_count)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btnAddItem_tf = QPushButton(self.widget_4)
        self.btnAddItem_tf.setObjectName(u"btnAddItem_tf")
        self.btnAddItem_tf.setMinimumSize(QSize(0, 30))
        self.btnAddItem_tf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddItem_tf.setStyleSheet(u"background: #27ae60;")

        self.horizontalLayout_6.addWidget(self.btnAddItem_tf)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.scrollArea_tf = QScrollArea(QuizCreatorDialog)
        self.scrollArea_tf.setObjectName(u"scrollArea_tf")
        self.scrollArea_tf.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"#scrollArea_tf { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: rgb(246, 245, 244);\n"
"	font: 10pt \"Inter\";\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"#scrollArea_tf QWidget #qt_scrollarea_viewport {\n"
"    background: rgb(246, 245, 244);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* 3. VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #7a7a7a;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 4. HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    height: 10px; /* Note: height, not width */\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::ha"
                        "ndle:horizontal {\n"
"    background: #7a7a7a;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 5. REMOVE BUTTONS & TRACK BACKGROUNDS */\n"
"/* This handles both horizontal and vertical arrows/tracks */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* 6. THE CORNER WIDGET \n"
"   (The small square where both bars meet) */\n"
"#scrollArea_tf QWidget #qt_scrollarea_corner {\n"
"    background: rgb(246, 245, 244);\n"
"    border: none;\n"
"}")
        self.scrollArea_tf.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 993, 128))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_tf.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_tf)

        self.frame_4 = QFrame(QuizCreatorDialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4 { border: none; background-color: transparent; }")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.btn_save = QPushButton(self.frame_4)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save.setStyleSheet(u"background: #27ae60; font: 10pt \"Inter SemiBold\";")

        self.horizontalLayout_4.addWidget(self.btn_save)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(QuizCreatorDialog)

        QMetaObject.connectSlotsByName(QuizCreatorDialog)
    # setupUi

    def retranslateUi(self, QuizCreatorDialog):
        QuizCreatorDialog.setWindowTitle(QCoreApplication.translate("QuizCreatorDialog", u"Quiz Editor", None))
        self.label_1.setText(QCoreApplication.translate("QuizCreatorDialog", u"Quiz #:", None))
        self.label_2.setText(QCoreApplication.translate("QuizCreatorDialog", u"Grading Period:", None))
        self.label_3.setText(QCoreApplication.translate("QuizCreatorDialog", u"Lesson Title:", None))
        self.checkBoxLockQuiz.setText(QCoreApplication.translate("QuizCreatorDialog", u"Unpublish Quiz", None))
        self.label_4.setText(QCoreApplication.translate("QuizCreatorDialog", u"Total Score:", None))
        self.label_totalScore.setText(QCoreApplication.translate("QuizCreatorDialog", u"000", None))
        self.label_6.setText(QCoreApplication.translate("QuizCreatorDialog", u"Diffuculty:", None))
        self.btnEasy.setText(QCoreApplication.translate("QuizCreatorDialog", u"Easy", None))
        self.btnAverage.setText(QCoreApplication.translate("QuizCreatorDialog", u"Average", None))
        self.btnHard.setText(QCoreApplication.translate("QuizCreatorDialog", u"Hard", None))
        self.label_18.setText(QCoreApplication.translate("QuizCreatorDialog", u"Points:", None))
        self.label_15.setText(QCoreApplication.translate("QuizCreatorDialog", u"Easy", None))
        self.label_16.setText(QCoreApplication.translate("QuizCreatorDialog", u"Average", None))
        self.label_17.setText(QCoreApplication.translate("QuizCreatorDialog", u"Hard", None))
        self.label_12.setText(QCoreApplication.translate("QuizCreatorDialog", u"Identification", None))
        self.label_9.setText("")
        self.label_id_count.setText(QCoreApplication.translate("QuizCreatorDialog", u"000", None))
        self.btnAddItem_id.setText(QCoreApplication.translate("QuizCreatorDialog", u"+ Add Item", None))
        self.label_13.setText(QCoreApplication.translate("QuizCreatorDialog", u"Multiple Choice", None))
        self.label_mc_count.setText(QCoreApplication.translate("QuizCreatorDialog", u"000", None))
        self.btnAddItem_mc.setText(QCoreApplication.translate("QuizCreatorDialog", u"+ Add Item", None))
        self.label_14.setText(QCoreApplication.translate("QuizCreatorDialog", u"True or False", None))
        self.label_tf_count.setText(QCoreApplication.translate("QuizCreatorDialog", u"000", None))
        self.btnAddItem_tf.setText(QCoreApplication.translate("QuizCreatorDialog", u"+ Add Item", None))
        self.btn_save.setText(QCoreApplication.translate("QuizCreatorDialog", u"Save all", None))
    # retranslateUi

