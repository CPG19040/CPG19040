# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormHome.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_FormHome(object):
    def setupUi(self, FormHome):
        if not FormHome.objectName():
            FormHome.setObjectName(u"FormHome")
        FormHome.resize(1360, 815)
        FormHome.setStyleSheet(u"")
        self.centralwidget = QWidget(FormHome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget { border-image: url(:/Images/Images/Wall.svg) 0 0 0 0 stretch stretch; }\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.widget_WindowsButtons = QWidget(self.centralwidget)
        self.widget_WindowsButtons.setObjectName(u"widget_WindowsButtons")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_WindowsButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.btnMinimize = QPushButton(self.widget_WindowsButtons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(40, 40))
        self.btnMinimize.setMaximumSize(QSize(40, 40))
        self.btnMinimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"#btnMinimize { border-image: url(:/Images/Images/wood_round_min.png); }\n"
"#btnMinimize:hover { border-image: url(:/Images/Images/wood_round_min2.png); }")

        self.horizontalLayout_2.addWidget(self.btnMinimize)

        self.btnMaximize = QPushButton(self.widget_WindowsButtons)
        self.btnMaximize.setObjectName(u"btnMaximize")
        self.btnMaximize.setMinimumSize(QSize(40, 40))
        self.btnMaximize.setMaximumSize(QSize(40, 40))
        self.btnMaximize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMaximize.setStyleSheet(u"#btnMaximize { border-image: url(:/Images/Images/wood_round_max.png); }\n"
"#btnMaximize:hover { border-image: url(:/Images/Images/wood_round_max2.png); }")

        self.horizontalLayout_2.addWidget(self.btnMaximize)

        self.btnClose = QPushButton(self.widget_WindowsButtons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(40, 40))
        self.btnClose.setMaximumSize(QSize(40, 40))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"#btnClose { border-image: url(:/Images/Images/wood_round_ex.png); }\n"
"#btnClose:hover { border-image: url(:/Images/Images/wood_round_ex2.png); }")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout_4.addWidget(self.widget_WindowsButtons)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_left_panel = QWidget(self.widget_2)
        self.widget_left_panel.setObjectName(u"widget_left_panel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left_panel.sizePolicy().hasHeightForWidth())
        self.widget_left_panel.setSizePolicy(sizePolicy)
        self.widget_left_panel.setMinimumSize(QSize(280, 0))
        self.widget_left_panel.setMaximumSize(QSize(280, 16777215))
        self.widget_left_panel.setAutoFillBackground(False)
        self.widget_left_panel.setStyleSheet(u"widget_left_panel { background-color: rgb(205, 171, 143); border-radius: 20px; background-image: url(:/Images/Images/wood_nav_bar.jpeg) 0 0 0 0 stretch stretch; }")
        self.verticalLayout = QVBoxLayout(self.widget_left_panel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_left_panel)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_profilePic = QLabel(self.widget_4)
        self.label_profilePic.setObjectName(u"label_profilePic")
        self.label_profilePic.setMinimumSize(QSize(200, 200))
        self.label_profilePic.setMaximumSize(QSize(200, 200))
        self.label_profilePic.setStyleSheet(u"background-color: transparent;")
        self.label_profilePic.setPixmap(QPixmap(u":/Images/Images/no-image.png"))
        self.label_profilePic.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_profilePic)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget_4)

        self.line = QFrame(self.widget_left_panel)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(206, 152, 115);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_firstname = QLabel(self.widget_left_panel)
        self.label_firstname.setObjectName(u"label_firstname")
        self.label_firstname.setMinimumSize(QSize(0, 30))
        self.label_firstname.setStyleSheet(u"#label_firstname { background-color: transparent; color: rgb(255, 255, 255); font: 50 20pt \"Kissy Hugs\"; }")
        self.label_firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_firstname.setWordWrap(True)
        self.label_firstname.setMargin(0)
        self.label_firstname.setIndent(10)

        self.verticalLayout.addWidget(self.label_firstname)

        self.label_lastname = QLabel(self.widget_left_panel)
        self.label_lastname.setObjectName(u"label_lastname")
        self.label_lastname.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Kissy Hugs"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.label_lastname.setFont(font)
        self.label_lastname.setStyleSheet(u"#label_lastname { background-color: transparent; font: 50 15pt \"Kissy Hugs\"; color: rgb(255, 255, 255); }")
        self.label_lastname.setWordWrap(True)
        self.label_lastname.setMargin(0)
        self.label_lastname.setIndent(10)

        self.verticalLayout.addWidget(self.label_lastname)

        self.label_studentId = QLabel(self.widget_left_panel)
        self.label_studentId.setObjectName(u"label_studentId")
        self.label_studentId.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Inter SemiBold"])
        font1.setPointSize(11)
        self.label_studentId.setFont(font1)
        self.label_studentId.setStyleSheet(u"background-color: transparent; color: rgb(255, 255, 255);")
        self.label_studentId.setIndent(10)

        self.verticalLayout.addWidget(self.label_studentId)

        self.label_sectionName = QLabel(self.widget_left_panel)
        self.label_sectionName.setObjectName(u"label_sectionName")
        self.label_sectionName.setMinimumSize(QSize(0, 30))
        self.label_sectionName.setFont(font1)
        self.label_sectionName.setStyleSheet(u"background-color: transparent; color: rgb(255, 255, 255);")
        self.label_sectionName.setIndent(10)

        self.verticalLayout.addWidget(self.label_sectionName)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_5 = QWidget(self.widget_left_panel)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(53, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btnQuit = QPushButton(self.widget_5)
        self.btnQuit.setObjectName(u"btnQuit")
        self.btnQuit.setMinimumSize(QSize(110, 50))
        self.btnQuit.setMaximumSize(QSize(110, 50))
        self.btnQuit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnQuit.setStyleSheet(u"#btnQuit { border-image: url(:/Images/Images/btnQuit.png); }\n"
"#btnQuit:hover { border-image: url(:/Images/Images/btnQuitGlow.png); }")

        self.horizontalLayout_5.addWidget(self.btnQuit)

        self.horizontalSpacer_5 = QSpacerItem(53, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.widget_5)


        self.horizontalLayout_3.addWidget(self.widget_left_panel)

        self.widget_right_panel = QWidget(self.widget_2)
        self.widget_right_panel.setObjectName(u"widget_right_panel")
        self.widget_right_panel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.widget_right_panel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_right_panel)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnLessons = QPushButton(self.widget)
        self.btnLessons.setObjectName(u"btnLessons")
        self.btnLessons.setMinimumSize(QSize(131, 90))
        self.btnLessons.setMaximumSize(QSize(131, 90))
        self.btnLessons.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLessons.setStyleSheet(u"#btnLessons { border-image: url(:/Images/Images/btnLessons.png); }\n"
"#btnLessons:hover, #btnLessons:checked {  border-image: url(:/Images/Images/btnLessonsGlow.png) 0 0 0 0 stretch; }\n"
"")

        self.horizontalLayout.addWidget(self.btnLessons)

        self.btnQuiz = QPushButton(self.widget)
        self.btnQuiz.setObjectName(u"btnQuiz")
        self.btnQuiz.setMinimumSize(QSize(131, 90))
        self.btnQuiz.setMaximumSize(QSize(131, 90))
        self.btnQuiz.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnQuiz.setStyleSheet(u"#btnQuiz { border-image: url(:/Images/Images/btnQuiz.png) 0 0 0 stretch stretch; }\n"
"#btnQuiz:hover, #btnQuiz:checked {  border-image: url(:/Images/Images/btnQuizGlow.png) 0 0 0 stretch stretch; }\n"
"")

        self.horizontalLayout.addWidget(self.btnQuiz)

        self.btnExercise = QPushButton(self.widget)
        self.btnExercise.setObjectName(u"btnExercise")
        self.btnExercise.setMinimumSize(QSize(131, 90))
        self.btnExercise.setMaximumSize(QSize(131, 90))
        self.btnExercise.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExercise.setStyleSheet(u"#btnExercise { border-image: url(:/Images/Images/btnExercises.png); }\n"
"#btnExercise:hover, #btnExercise:checked {  border-image: url(:/Images/Images/btnExercisesGlow.png); }\n"
"")

        self.horizontalLayout.addWidget(self.btnExercise)

        self.btnScores = QPushButton(self.widget)
        self.btnScores.setObjectName(u"btnScores")
        self.btnScores.setMinimumSize(QSize(131, 90))
        self.btnScores.setMaximumSize(QSize(131, 90))
        self.btnScores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnScores.setStyleSheet(u"#btnScores { border-image: url(:/Images/Images/btnScores.png); }\n"
"#btnScores:hover, #btnScores:checked { border-image: url(:/Images/Images/btnScoresGlow.png); }\n"
"")

        self.horizontalLayout.addWidget(self.btnScores)

        self.btnGames = QPushButton(self.widget)
        self.btnGames.setObjectName(u"btnGames")
        self.btnGames.setMinimumSize(QSize(131, 90))
        self.btnGames.setMaximumSize(QSize(131, 90))
        self.btnGames.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGames.setStyleSheet(u"#btnGames { border-image: url(:/Images/Images/buttonGames.png); }\n"
"#btnGames:hover, #btnGames:checked { border-image: url(:/Images/Images/buttonGamesGlow.png); }\n"
"")

        self.horizontalLayout.addWidget(self.btnGames)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_right_panel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#stackedWidget { background-color: rgb(225, 208, 195); border-radius: 20px; background-image: url(:/Images/Images/wood_nav_bar_H.jpeg) 0 0 0 0 stretch stretch; }")
        self.pageLessons = QWidget()
        self.pageLessons.setObjectName(u"pageLessons")
        self.pageLessons.setStyleSheet(u"border-radius: 20px; background-color: transparent;")
        self.verticalLayout_3 = QVBoxLayout(self.pageLessons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.pageLessons)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"#scrollArea { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"#scrollArea QWidget #qt_scrollarea_viewport {\n"
"    background: transparent;\n"
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
"QScrollBar::handle:horizontal {\n"
"    background: #7a7a7a;\n"
""
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
"#scrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.lessonWidget = QWidget()
        self.lessonWidget.setObjectName(u"lessonWidget")
        self.lessonWidget.setGeometry(QRect(0, 0, 1038, 637))
        self.lessonWidget.setStyleSheet(u"#scrollAreaWidgetContents_2 { background-color: transparent; }")
        self.verticalLayout_5 = QVBoxLayout(self.lessonWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea.setWidget(self.lessonWidget)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.pageLessons)
        self.pageQuiz = QWidget()
        self.pageQuiz.setObjectName(u"pageQuiz")
        self.pageQuiz.setStyleSheet(u"background: transparent;")
        self.verticalLayout_12 = QVBoxLayout(self.pageQuiz)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_4 = QFrame(self.pageQuiz)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_lastname_2 = QLabel(self.frame)
        self.label_lastname_2.setObjectName(u"label_lastname_2")
        self.label_lastname_2.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setFamilies([u"Kissy Hugs"])
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_lastname_2.setFont(font2)
        self.label_lastname_2.setStyleSheet(u"background-color: transparent; font: 13pt \"Kissy Hugs\"; color: #FFF; border-image: url(:/Images/Images/button_wood.png);")
        self.label_lastname_2.setTextFormat(Qt.PlainText)
        self.label_lastname_2.setScaledContents(True)
        self.label_lastname_2.setAlignment(Qt.AlignCenter)
        self.label_lastname_2.setWordWrap(True)
        self.label_lastname_2.setMargin(0)
        self.label_lastname_2.setIndent(10)

        self.verticalLayout_6.addWidget(self.label_lastname_2)

        self.scrollArea_id = QScrollArea(self.frame)
        self.scrollArea_id.setObjectName(u"scrollArea_id")
        self.scrollArea_id.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"QScrollArea { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"QScrollArea QWidget #qt_scrollarea_viewport {\n"
"    background: transparent;\n"
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
"QScrollBar::handle:horizontal {\n"
"    background: #7a7a7a;\n"
""
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
"QScrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.scrollArea_id.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_id.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea_id)


        self.horizontalLayout_7.addWidget(self.frame)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"border: 2px solid brown;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_lastname_3 = QLabel(self.frame_2)
        self.label_lastname_3.setObjectName(u"label_lastname_3")
        self.label_lastname_3.setMinimumSize(QSize(0, 35))
        self.label_lastname_3.setFont(font2)
        self.label_lastname_3.setStyleSheet(u"background-color: transparent; font: 13pt \"Kissy Hugs\"; color: #FFF; border-image: url(:/Images/Images/button_wood.png);")
        self.label_lastname_3.setAlignment(Qt.AlignCenter)
        self.label_lastname_3.setWordWrap(True)
        self.label_lastname_3.setMargin(0)
        self.label_lastname_3.setIndent(10)

        self.verticalLayout_10.addWidget(self.label_lastname_3)

        self.scrollArea_mc = QScrollArea(self.frame_2)
        self.scrollArea_mc.setObjectName(u"scrollArea_mc")
        self.scrollArea_mc.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"QScrollArea { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"QScrollArea QWidget #qt_scrollarea_viewport {\n"
"    background: transparent;\n"
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
"QScrollBar::handle:horizontal {\n"
"    background: #7a7a7a;\n"
""
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
"QScrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.scrollArea_mc.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_mc.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.scrollArea_mc)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"border: 2px solid brown;")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_3)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_lastname_4 = QLabel(self.frame_3)
        self.label_lastname_4.setObjectName(u"label_lastname_4")
        self.label_lastname_4.setMinimumSize(QSize(0, 35))
        self.label_lastname_4.setFont(font2)
        self.label_lastname_4.setStyleSheet(u"background-color: transparent; font: 13pt \"Kissy Hugs\"; color: #FFF; border-image: url(:/Images/Images/button_wood.png);")
        self.label_lastname_4.setAlignment(Qt.AlignCenter)
        self.label_lastname_4.setWordWrap(True)
        self.label_lastname_4.setMargin(0)
        self.label_lastname_4.setIndent(10)

        self.verticalLayout_11.addWidget(self.label_lastname_4)

        self.scrollArea_tf = QScrollArea(self.frame_3)
        self.scrollArea_tf.setObjectName(u"scrollArea_tf")
        self.scrollArea_tf.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"QScrollArea { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"QScrollArea QWidget #qt_scrollarea_viewport {\n"
"    background: transparent;\n"
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
"QScrollBar::handle:horizontal {\n"
"    background: #7a7a7a;\n"
""
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
"QScrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.scrollArea_tf.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_tf.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_11.addWidget(self.scrollArea_tf)


        self.horizontalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.pageQuiz)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.btnSubmitQuiz = QPushButton(self.frame_5)
        self.btnSubmitQuiz.setObjectName(u"btnSubmitQuiz")
        self.btnSubmitQuiz.setMinimumSize(QSize(100, 50))
        self.btnSubmitQuiz.setMaximumSize(QSize(100, 50))
        self.btnSubmitQuiz.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSubmitQuiz.setStyleSheet(u"#btnSubmitQuiz { border-image: url(:/Images/Images/rightArrowWood.png); font: 12pt \"Kissy Hugs\"; color: rgb(255, 255, 255); }\n"
"#btnSubmitQuiz:hover { border-image: url(:/Images/Images/rightArrowWoodGlow.png); }")

        self.horizontalLayout_8.addWidget(self.btnSubmitQuiz)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.pageQuiz)
        self.pageExercise = QWidget()
        self.pageExercise.setObjectName(u"pageExercise")
        self.stackedWidget.addWidget(self.pageExercise)
        self.pageScores = QWidget()
        self.pageScores.setObjectName(u"pageScores")
        self.stackedWidget.addWidget(self.pageScores)
        self.pageGames = QWidget()
        self.pageGames.setObjectName(u"pageGames")
        self.horizontalLayout_6 = QHBoxLayout(self.pageGames)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_6 = QWidget(self.pageGames)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.widget_6.setStyleSheet(u"#widget_6 { background-color: transparent; border-radius: 20px; border-image: url(:/Images/Images/reef2.jpg) 0 0 stretch stretch; }")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnColors = QPushButton(self.widget_6)
        self.btnColors.setObjectName(u"btnColors")
        self.btnColors.setMinimumSize(QSize(100, 100))
        self.btnColors.setMaximumSize(QSize(100, 100))
        self.btnColors.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnColors.setStyleSheet(u"#btnColors { border; none; background: transparent; border-radius: 10px; border-image: url(:/Images/Images/Colors.png); }\n"
"#btnColors:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnColors.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnColors, 2, 0, 1, 1)

        self.btnAddition = QPushButton(self.widget_6)
        self.btnAddition.setObjectName(u"btnAddition")
        self.btnAddition.setMinimumSize(QSize(100, 100))
        self.btnAddition.setMaximumSize(QSize(100, 100))
        self.btnAddition.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddition.setStyleSheet(u"#btnAddition { border; none; background-color: transparent; border-radius: 10px; border-image: url(:/Images/Images/Addition.png); }\n"
"#btnAddition:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnAddition.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnAddition, 0, 0, 1, 1)

        self.btnMultiplication = QPushButton(self.widget_6)
        self.btnMultiplication.setObjectName(u"btnMultiplication")
        self.btnMultiplication.setMinimumSize(QSize(100, 100))
        self.btnMultiplication.setMaximumSize(QSize(100, 100))
        self.btnMultiplication.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMultiplication.setStyleSheet(u"#btnMultiplication { border; none; background: transparent; border-radius: 10px; border-image: url(:/Images/Images/Multiplication.png); }\n"
"#btnMultiplication:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnMultiplication.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnMultiplication, 0, 2, 1, 1)

        self.btnShapes = QPushButton(self.widget_6)
        self.btnShapes.setObjectName(u"btnShapes")
        self.btnShapes.setMinimumSize(QSize(100, 100))
        self.btnShapes.setMaximumSize(QSize(100, 100))
        self.btnShapes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnShapes.setStyleSheet(u"#btnShapes { border; none; background: transparent; border-radius: 10px; border-image: url(:/Images/Images/Shapes.png); }\n"
"#btnShapes:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnShapes.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnShapes, 1, 2, 1, 1)

        self.btnDivision = QPushButton(self.widget_6)
        self.btnDivision.setObjectName(u"btnDivision")
        self.btnDivision.setMinimumSize(QSize(100, 100))
        self.btnDivision.setMaximumSize(QSize(100, 100))
        self.btnDivision.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDivision.setStyleSheet(u"#btnDivision { border; none; background: transparent; border-radius: 10px; border-image: url(:/Images/Images/Division.png); }\n"
"#btnDivision:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnDivision.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnDivision, 1, 0, 1, 1)

        self.btnFraction = QPushButton(self.widget_6)
        self.btnFraction.setObjectName(u"btnFraction")
        self.btnFraction.setMinimumSize(QSize(100, 100))
        self.btnFraction.setMaximumSize(QSize(100, 100))
        self.btnFraction.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnFraction.setStyleSheet(u"#btnFraction { border; none; background: transparent; border-radius: 10px; border-image: url(:/Images/Images/fraction.png); }\n"
"#btnFraction:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnFraction.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnFraction, 1, 1, 1, 1)

        self.btnSubtraction = QPushButton(self.widget_6)
        self.btnSubtraction.setObjectName(u"btnSubtraction")
        self.btnSubtraction.setMinimumSize(QSize(100, 100))
        self.btnSubtraction.setMaximumSize(QSize(100, 100))
        self.btnSubtraction.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSubtraction.setStyleSheet(u"#btnSubtraction { border; none; background: transparent; border-radius: 10px; border-image: url(:/Images/Images/Subtraction.png); }\n"
"#btnSubtraction:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnSubtraction.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnSubtraction, 0, 1, 1, 1)

        self.btnTime = QPushButton(self.widget_6)
        self.btnTime.setObjectName(u"btnTime")
        self.btnTime.setMinimumSize(QSize(100, 100))
        self.btnTime.setMaximumSize(QSize(100, 100))
        self.btnTime.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnTime.setStyleSheet(u"#btnTime { border; none; background: transparent; border-radius: 10px; border-image: url(:/Images/Images/Time.png); }\n"
"#btnTime:hover { background-color: rgba(249, 240, 107, 0.5); }")
        self.btnTime.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btnTime, 2, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.pageGames)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.widget_right_panel)


        self.verticalLayout_4.addWidget(self.widget_2)

        FormHome.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormHome)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormHome)
    # setupUi

    def retranslateUi(self, FormHome):
        FormHome.setWindowTitle(QCoreApplication.translate("FormHome", u"Home", None))
        self.btnMinimize.setText("")
        self.btnMaximize.setText("")
        self.btnClose.setText("")
        self.label_profilePic.setText("")
        self.label_firstname.setText(QCoreApplication.translate("FormHome", u"Phineas", None))
        self.label_lastname.setText(QCoreApplication.translate("FormHome", u"Flynn", None))
        self.label_studentId.setText(QCoreApplication.translate("FormHome", u"2026-0001-STU", None))
        self.label_sectionName.setText(QCoreApplication.translate("FormHome", u"Honesty", None))
        self.btnQuit.setText("")
        self.btnLessons.setText("")
        self.btnQuiz.setText("")
        self.btnExercise.setText("")
        self.btnScores.setText("")
        self.btnGames.setText("")
        self.label_lastname_2.setText(QCoreApplication.translate("FormHome", u"Identification", None))
        self.label_lastname_3.setText(QCoreApplication.translate("FormHome", u"Multiple Choice", None))
        self.label_lastname_4.setText(QCoreApplication.translate("FormHome", u"True or False", None))
        self.btnSubmitQuiz.setText(QCoreApplication.translate("FormHome", u"Submit", None))
        self.btnColors.setText("")
        self.btnAddition.setText("")
        self.btnMultiplication.setText("")
        self.btnShapes.setText("")
        self.btnDivision.setText("")
        self.btnFraction.setText("")
        self.btnSubtraction.setText("")
        self.btnTime.setText("")
    # retranslateUi

