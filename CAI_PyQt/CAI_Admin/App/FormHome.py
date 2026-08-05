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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1189, 732)
        Home.setMinimumSize(QSize(1036, 675))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        Home.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Images/Images/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Home.setWindowIcon(icon)
        Home.setStyleSheet(u"* {\n"
"	margin: 0px;\n"
"	background-color: rgb(222, 221, 218); \n"
"	font: 10pt \"Inter\"; \n"
"	color: black;\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"	font: 10pt \"Inter\";\n"
"	height: 30px;\n"
"	padding: 0px 12px;\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"] {\n"
"	border: 1px solid #0a5128;\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px 0px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #1ebd5d, \n"
"                                stop:1 #107f3f);\n"
"    color: #FFF;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #2ecc71, \n"
"                                stop:1 #27AE60);\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #0b572a, \n"
"                        "
                        "        stop:1 #129046); \n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:disabled {\n"
"    background: #A5D6A7;\n"
"    color: #E8F5E9;\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"*[class=\"button-normal\"] {\n"
"	font: 10pt \"Inter\";\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #d8ecf6);\n"
"	color: black;\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(154, 153, 150);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:hover {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #f2f6f8);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #dce5e9, \n"
"                                stop:1 #ffffff);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:disabled {\n"
"	background: #f5f5f5;\n"
"	border: 1px solid #dcd"
                        "cdc;\n"
"	color: #aeaeae;\n"
"}\n"
"\n"
"/* 1. THE MAIN CONTAINER */\n"
"QScrollArea { \n"
"    border: none;\n"
"    border-radius: 20px;\n"
"	background-color: rgb(246, 245, 244);\n"
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
"QScrollBar::handl"
                        "e:horizontal {\n"
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
"QScrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QDateEdit {\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"	background: transparent;\n"
"}")
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QComboBox[class=\"combobox-main\"] QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid #999;\n"
"    border-radius: 8px;\n"
"    selection-background-color: #7eb4d7;\n"
"    selection-color: #ffffff;\n"
"    outline: 0; /* Removes the ugly dotted focus border */\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.navigationBar = QWidget(self.centralwidget)
        self.navigationBar.setObjectName(u"navigationBar")
        self.navigationBar.setMaximumSize(QSize(200, 16777215))
        self.navigationBar.setFont(font)
        self.navigationBar.setStyleSheet(u"#navigationBar, #widget_logo, #line, #line_2 {\n"
"	background-color: rgb(61, 61, 61); /* Dark Gray or Storm Dust */\n"
"}\n"
"\n"
"QPushButton[class=\"button-left-nav\"] {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"\n"
"QPushButton[class=\"button-left-nav\"]:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"\n"
"QPushButton[class=\"button-left-nav\"]:checked {\n"
"	background-color: #5d5d5d;\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF;\n"
"}\n"
"\n"
"QPushButton[class=\"button-left-nav\"]:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.navigationBar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 9)
        self.widget_logo = QWidget(self.navigationBar)
        self.widget_logo.setObjectName(u"widget_logo")
        self.widget_logo.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_logo)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.widget_logo)
        self.label_20.setObjectName(u"label_20")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(100, 100))
        self.label_20.setMaximumSize(QSize(100, 100))
        self.label_20.setStyleSheet(u"background-color: rgba(191, 64, 64, 0);")
        self.label_20.setPixmap(QPixmap(u":/Images/Images/lcs logo.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_20)


        self.verticalLayout_5.addWidget(self.widget_logo)

        self.btnHome = QPushButton(self.navigationBar)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(200, 40))
        self.btnHome.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Inter Medium"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btnHome.setFont(font1)
        self.btnHome.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnHome.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/House-01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon1)
        self.btnHome.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnHome)

        self.btnStudentList = QPushButton(self.navigationBar)
        self.btnStudentList.setObjectName(u"btnStudentList")
        self.btnStudentList.setMinimumSize(QSize(200, 40))
        self.btnStudentList.setMaximumSize(QSize(16777215, 40))
        self.btnStudentList.setFont(font1)
        self.btnStudentList.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnStudentList.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Images/Images/list-color.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStudentList.setIcon(icon2)
        self.btnStudentList.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnStudentList)

        self.btnLesson = QPushButton(self.navigationBar)
        self.btnLesson.setObjectName(u"btnLesson")
        self.btnLesson.setMinimumSize(QSize(200, 40))
        self.btnLesson.setMaximumSize(QSize(16777215, 40))
        self.btnLesson.setFont(font1)
        self.btnLesson.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLesson.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Images/Images/books-28.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLesson.setIcon(icon3)
        self.btnLesson.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnLesson)

        self.btnQuiz = QPushButton(self.navigationBar)
        self.btnQuiz.setObjectName(u"btnQuiz")
        self.btnQuiz.setMinimumSize(QSize(200, 40))
        self.btnQuiz.setMaximumSize(QSize(16777215, 40))
        self.btnQuiz.setFont(font1)
        self.btnQuiz.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnQuiz.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/Images/Images/05-bulb.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnQuiz.setIcon(icon4)
        self.btnQuiz.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnQuiz)

        self.btnExercise = QPushButton(self.navigationBar)
        self.btnExercise.setObjectName(u"btnExercise")
        self.btnExercise.setMinimumSize(QSize(200, 40))
        self.btnExercise.setMaximumSize(QSize(16777215, 40))
        self.btnExercise.setFont(font1)
        self.btnExercise.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExercise.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/Images/Images/dumbell.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExercise.setIcon(icon5)
        self.btnExercise.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnExercise)

        self.btnSections = QPushButton(self.navigationBar)
        self.btnSections.setObjectName(u"btnSections")
        self.btnSections.setMinimumSize(QSize(200, 40))
        self.btnSections.setMaximumSize(QSize(16777215, 40))
        self.btnSections.setFont(font1)
        self.btnSections.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSections.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/Images/Images/library-90.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSections.setIcon(icon6)
        self.btnSections.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnSections)

        self.btnReports = QPushButton(self.navigationBar)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setMinimumSize(QSize(200, 40))
        self.btnReports.setMaximumSize(QSize(16777215, 40))
        self.btnReports.setFont(font1)
        self.btnReports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnReports.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/Images/Images/product-data.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnReports.setIcon(icon7)
        self.btnReports.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnReports)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.line_2 = QFrame(self.navigationBar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.btnUserName = QPushButton(self.navigationBar)
        self.btnUserName.setObjectName(u"btnUserName")
        self.btnUserName.setMinimumSize(QSize(200, 40))
        self.btnUserName.setMaximumSize(QSize(16777215, 32))
        self.btnUserName.setFont(font1)
        self.btnUserName.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUserName.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"    padding: 0px 0px 0px 10px;\n"
"	font: 10pt \"Inter Medium\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Images/Images/icon-user-7.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUserName.setIcon(icon8)
        self.btnUserName.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btnUserName)

        self.labelPosition = QLabel(self.navigationBar)
        self.labelPosition.setObjectName(u"labelPosition")
        self.labelPosition.setMinimumSize(QSize(0, 30))
        self.labelPosition.setMaximumSize(QSize(16777215, 30))
        self.labelPosition.setFont(font1)
        self.labelPosition.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent; margin-left: 10px; font: 57 10pt \"Inter Medium\";")
        self.labelPosition.setMargin(0)

        self.verticalLayout_5.addWidget(self.labelPosition)

        self.btnLogout = QPushButton(self.navigationBar)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(200, 40))
        self.btnLogout.setMaximumSize(QSize(16777215, 40))
        self.btnLogout.setFont(font1)
        self.btnLogout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogout.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/Images/Images/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLogout.setIcon(icon9)
        self.btnLogout.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnLogout)

        self.line = QFrame(self.navigationBar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.btnUsers = QPushButton(self.navigationBar)
        self.btnUsers.setObjectName(u"btnUsers")
        self.btnUsers.setMinimumSize(QSize(200, 40))
        self.btnUsers.setMaximumSize(QSize(16777215, 40))
        self.btnUsers.setFont(font1)
        self.btnUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUsers.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/Images/Images/users-61.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUsers.setIcon(icon10)
        self.btnUsers.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnUsers)

        self.btnUtility = QPushButton(self.navigationBar)
        self.btnUtility.setObjectName(u"btnUtility")
        self.btnUtility.setMinimumSize(QSize(200, 40))
        self.btnUtility.setMaximumSize(QSize(16777215, 40))
        self.btnUtility.setFont(font1)
        self.btnUtility.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUtility.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/Images/Images/settings-125.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUtility.setIcon(icon11)
        self.btnUtility.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnUtility)


        self.horizontalLayout_2.addWidget(self.navigationBar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 30))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.horizontalLayout_14 = QHBoxLayout(self.pageHome)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget = QWidget(self.pageHome)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_23 = QVBoxLayout(self.widget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.widget_5.setStyleSheet(u"background-color: rgb(246, 245, 244);\n"
"padding: 0px 10px;\n"
"border-radius: 20px;")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 2, -1, 2)
        self.label_timeAP_3 = QLabel(self.widget_5)
        self.label_timeAP_3.setObjectName(u"label_timeAP_3")
        self.label_timeAP_3.setMinimumSize(QSize(0, 30))
        self.label_timeAP_3.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Inter Medium"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_timeAP_3.setFont(font2)
        self.label_timeAP_3.setStyleSheet(u"QLabel { color: rgb(36, 31, 49); background-color: transparent; font: 12pt \"Inter Medium\"; }")
        self.label_timeAP_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_timeAP_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_8)

        self.label_gradingperiod = QLabel(self.widget_5)
        self.label_gradingperiod.setObjectName(u"label_gradingperiod")
        self.label_gradingperiod.setMinimumSize(QSize(0, 25))
        self.label_gradingperiod.setMaximumSize(QSize(16777215, 25))
        self.label_gradingperiod.setFont(font1)
        self.label_gradingperiod.setStyleSheet(u"font: 10pt \"Inter Medium\"; border-radius: 15px; padding: 0px 10px 0px;")
        self.label_gradingperiod.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_gradingperiod)

        self.label_SY = QLabel(self.widget_5)
        self.label_SY.setObjectName(u"label_SY")
        self.label_SY.setMinimumSize(QSize(0, 30))
        self.label_SY.setMaximumSize(QSize(16777215, 30))
        self.label_SY.setFont(font2)
        self.label_SY.setStyleSheet(u"QLabel { color: rgb(36, 31, 49); background-color: transparent; font: 12pt \"Inter Medium\"; }")
        self.label_SY.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_SY)


        self.verticalLayout_23.addWidget(self.widget_5)

        self.widget_11 = QWidget(self.widget)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_11)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_36 = QVBoxLayout(self.widget_13)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.widget_12 = QWidget(self.widget_13)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_student = QWidget(self.widget_12)
        self.widget_student.setObjectName(u"widget_student")
        self.widget_student.setMinimumSize(QSize(220, 0))
        self.widget_student.setMaximumSize(QSize(220, 16777215))
        self.widget_student.setStyleSheet(u"#widget_student {\n"
"	border: 1px solid #64bbb6;\n"
"	border-radius: 20px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #D8F1FF, \n"
"                                stop:1 #64bbb6);\n"
"}\n"
"\n"
"#widget_14 {\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_stud {\n"
"	font: 14pt \"Inter\";\n"
"	color: #4e76a6;\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_student_total {\n"
"	background: transparent;\n"
"	color: rgb(36, 31, 49); \n"
"	font: 20pt \"Inter SemiBold\";\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_student)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_24 = QLabel(self.widget_student)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(80, 80))
        self.label_24.setMaximumSize(QSize(80, 80))
        self.label_24.setStyleSheet(u"background-color: transparent;")
        self.label_24.setPixmap(QPixmap(u":/Images/Images/student.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_24)

        self.widget_14 = QWidget(self.widget_student)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.widget_14)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_stud = QLabel(self.widget_14)
        self.label_stud.setObjectName(u"label_stud")
        self.label_stud.setStyleSheet(u"")
        self.label_stud.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_stud)

        self.label_student_total = QLabel(self.widget_14)
        self.label_student_total.setObjectName(u"label_student_total")
        font3 = QFont()
        font3.setFamilies([u"Inter SemiBold"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_student_total.setFont(font3)
        self.label_student_total.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_student_total)


        self.horizontalLayout_25.addWidget(self.widget_14)


        self.horizontalLayout_28.addWidget(self.widget_student)

        self.widget_lessons = QWidget(self.widget_12)
        self.widget_lessons.setObjectName(u"widget_lessons")
        self.widget_lessons.setMinimumSize(QSize(220, 0))
        self.widget_lessons.setMaximumSize(QSize(220, 16777215))
        self.widget_lessons.setStyleSheet(u"#widget_lessons {\n"
"	border-radius: 20px;\n"
"	border: 1px solid #da75d7;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #f8d9fd, \n"
"                                stop:1 #da91e5);\n"
"}\n"
"\n"
"#label_8 {\n"
"	font: 14pt \"Inter\";\n"
"	color: rgb(119, 118, 123);\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_lessons_total {\n"
"	background: transparent;\n"
"	color: #000; \n"
"	font: 20pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"#widget_16 {\n"
"	background: transparent;\n"
"}")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_lessons)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_25 = QLabel(self.widget_lessons)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(80, 80))
        self.label_25.setMaximumSize(QSize(80, 80))
        self.label_25.setStyleSheet(u"background-color: transparent;")
        self.label_25.setPixmap(QPixmap(u":/Images/Images/stack-of-books.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_25)

        self.widget_16 = QWidget(self.widget_lessons)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_25 = QVBoxLayout(self.widget_16)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_8 = QLabel(self.widget_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_8)

        self.label_lessons_total = QLabel(self.widget_16)
        self.label_lessons_total.setObjectName(u"label_lessons_total")
        self.label_lessons_total.setFont(font3)
        self.label_lessons_total.setStyleSheet(u"")
        self.label_lessons_total.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_lessons_total)


        self.horizontalLayout_26.addWidget(self.widget_16)


        self.horizontalLayout_28.addWidget(self.widget_lessons)

        self.widget_teachers = QWidget(self.widget_12)
        self.widget_teachers.setObjectName(u"widget_teachers")
        self.widget_teachers.setMinimumSize(QSize(220, 0))
        self.widget_teachers.setMaximumSize(QSize(220, 16777215))
        self.widget_teachers.setStyleSheet(u"#widget_teachers {\n"
"	border-radius: 20px;\n"
"	border: 1px solid #ffbe6f;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffeed9, \n"
"                                stop:1 #e4bc8b);\n"
"}\n"
"\n"
"#label_teachers_total { \n"
"	color: rgb(36, 31, 49); \n"
"	background-color: transparent; \n"
"	font: 20pt \"Inter SemiBold\"; \n"
"}\n"
"\n"
"#label_9 {\n"
"	font: 14pt \"Inter\";\n"
"	color: #7c684e;\n"
"	background: transparent; \n"
"}\n"
"\n"
"#widget_18 {\n"
"	background: transparent; \n"
"}")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_teachers)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_27 = QLabel(self.widget_teachers)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(80, 80))
        self.label_27.setMaximumSize(QSize(80, 80))
        self.label_27.setStyleSheet(u"background-color: transparent;")
        self.label_27.setPixmap(QPixmap(u":/Images/Images/teacher.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_27)

        self.widget_18 = QWidget(self.widget_teachers)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_26 = QVBoxLayout(self.widget_18)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_9 = QLabel(self.widget_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_9)

        self.label_teachers_total = QLabel(self.widget_18)
        self.label_teachers_total.setObjectName(u"label_teachers_total")
        self.label_teachers_total.setFont(font3)
        self.label_teachers_total.setStyleSheet(u"")
        self.label_teachers_total.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_teachers_total)


        self.horizontalLayout_27.addWidget(self.widget_18)


        self.horizontalLayout_28.addWidget(self.widget_teachers)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_20)


        self.verticalLayout_36.addWidget(self.widget_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_3)

        self.widget_top_scorers = QWidget(self.widget_13)
        self.widget_top_scorers.setObjectName(u"widget_top_scorers")
        self.widget_top_scorers.setMinimumSize(QSize(0, 220))
        self.widget_top_scorers.setMaximumSize(QSize(16777215, 220))
        self.widget_top_scorers.setStyleSheet(u"#widget_top_scorers {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#widget_student {\n"
"	background-color: rgb(255, 190, 111);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#widget_14 {\n"
"	background: transparent;\n"
"	border-left: 2px solid rgb(255, 163, 72);\n"
"}\n"
"\n"
"#label_stud {\n"
"	font: 14pt \"Inter\";\n"
"	color: rgb(119, 118, 123);\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_student_total {\n"
"	background: transparent;\n"
"	color: rgb(36, 31, 49); \n"
"	font: 20pt \"Inter SemiBold\";\n"
"}")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_top_scorers)
        self.horizontalLayout_42.setSpacing(10)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_22)

        self.widget_27 = QWidget(self.widget_top_scorers)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 200))
        self.widget_27.setMaximumSize(QSize(16777215, 200))
        self.widget_27.setStyleSheet(u"#widget_27 {\n"
"	background-color: #34a25b;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#widget_26 {\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_stud_name {\n"
"	color: #FFF;\n"
"	background-color: transparent;\n"
"	font: 12pt \"Inter Medium\";\n"
"}\n"
"\n"
"#label_student_score {\n"
"	font: 20pt \"Inter SemiBold\";\n"
"	background: transparent;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#label_student_place {\n"
"	font: 12pt \"Inter SemiBold\";\n"
"	border-radius: 12px;\n"
"	background-color: #57c27b;\n"
"	color: #FFF;\n"
"}")
        self.verticalLayout_37 = QVBoxLayout(self.widget_27)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 10, -1, 10)
        self.widget_26 = QWidget(self.widget_27)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_13)

        self.label_profile = QLabel(self.widget_26)
        self.label_profile.setObjectName(u"label_profile")
        sizePolicy.setHeightForWidth(self.label_profile.sizePolicy().hasHeightForWidth())
        self.label_profile.setSizePolicy(sizePolicy)
        self.label_profile.setMinimumSize(QSize(80, 80))
        self.label_profile.setMaximumSize(QSize(80, 80))
        self.label_profile.setStyleSheet(u"background-color: transparent;")
        self.label_profile.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile.setScaledContents(True)
        self.label_profile.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_profile)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_14)


        self.verticalLayout_37.addWidget(self.widget_26)

        self.label_stud_name = QLabel(self.widget_27)
        self.label_stud_name.setObjectName(u"label_stud_name")
        self.label_stud_name.setFont(font2)
        self.label_stud_name.setStyleSheet(u"")
        self.label_stud_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_stud_name)

        self.label_student_score = QLabel(self.widget_27)
        self.label_student_score.setObjectName(u"label_student_score")
        self.label_student_score.setFont(font3)
        self.label_student_score.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_student_score)

        self.label_student_place = QLabel(self.widget_27)
        self.label_student_place.setObjectName(u"label_student_place")
        font4 = QFont()
        font4.setFamilies([u"Inter SemiBold"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_student_place.setFont(font4)
        self.label_student_place.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_student_place)


        self.horizontalLayout_42.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_top_scorers)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 200))
        self.widget_28.setMaximumSize(QSize(16777215, 200))
        self.widget_28.setStyleSheet(u"#widget_28 {\n"
"	background-color: #5c5890;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#widget_29 {\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_stud_name_2 {\n"
"	color: #FFF;\n"
"	background-color: transparent;\n"
"	font: 12pt \"Inter Medium\";\n"
"}\n"
"\n"
"#label_student_score_2 {\n"
"	font: 20pt \"Inter SemiBold\";\n"
"	background: transparent;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#label_student_place_2 {\n"
"	font: 12pt \"Inter SemiBold\";\n"
"	border-radius: 12px;\n"
"	background-color: #7e74b0;\n"
"	color: #FFF;\n"
"}")
        self.verticalLayout_38 = QVBoxLayout(self.widget_28)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 10, -1, 10)
        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_16)

        self.label_profile_2 = QLabel(self.widget_29)
        self.label_profile_2.setObjectName(u"label_profile_2")
        sizePolicy.setHeightForWidth(self.label_profile_2.sizePolicy().hasHeightForWidth())
        self.label_profile_2.setSizePolicy(sizePolicy)
        self.label_profile_2.setMinimumSize(QSize(80, 80))
        self.label_profile_2.setMaximumSize(QSize(80, 80))
        self.label_profile_2.setStyleSheet(u"background-color: transparent;")
        self.label_profile_2.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile_2.setScaledContents(True)
        self.label_profile_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_profile_2)

        self.horizontalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_17)


        self.verticalLayout_38.addWidget(self.widget_29)

        self.label_stud_name_2 = QLabel(self.widget_28)
        self.label_stud_name_2.setObjectName(u"label_stud_name_2")
        self.label_stud_name_2.setFont(font2)
        self.label_stud_name_2.setStyleSheet(u"")
        self.label_stud_name_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_stud_name_2)

        self.label_student_score_2 = QLabel(self.widget_28)
        self.label_student_score_2.setObjectName(u"label_student_score_2")
        self.label_student_score_2.setFont(font3)
        self.label_student_score_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_student_score_2)

        self.label_student_place_2 = QLabel(self.widget_28)
        self.label_student_place_2.setObjectName(u"label_student_place_2")
        self.label_student_place_2.setFont(font4)
        self.label_student_place_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_student_place_2)


        self.horizontalLayout_42.addWidget(self.widget_28)

        self.widget_30 = QWidget(self.widget_top_scorers)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(0, 200))
        self.widget_30.setMaximumSize(QSize(16777215, 200))
        self.widget_30.setStyleSheet(u"#widget_30 {\n"
"	background-color: #fec000;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#widget_31 {\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_stud_name_3 {\n"
"	color: #FFF;\n"
"	background-color: transparent;\n"
"	font: 12pt \"Inter Medium\";\n"
"}\n"
"\n"
"#label_student_score_3 {\n"
"	font: 20pt \"Inter SemiBold\";\n"
"	background: transparent;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#label_student_place_3 {\n"
"	font: 12pt \"Inter SemiBold\";\n"
"	border-radius: 12px;\n"
"	background-color: #efa60b;\n"
"	color: #FFF;\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.widget_30)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 10, -1, 10)
        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_18)

        self.label_profile_3 = QLabel(self.widget_31)
        self.label_profile_3.setObjectName(u"label_profile_3")
        sizePolicy.setHeightForWidth(self.label_profile_3.sizePolicy().hasHeightForWidth())
        self.label_profile_3.setSizePolicy(sizePolicy)
        self.label_profile_3.setMinimumSize(QSize(80, 80))
        self.label_profile_3.setMaximumSize(QSize(80, 80))
        self.label_profile_3.setStyleSheet(u"background-color: transparent;")
        self.label_profile_3.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile_3.setScaledContents(True)
        self.label_profile_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_profile_3)

        self.horizontalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_19)


        self.verticalLayout_39.addWidget(self.widget_31)

        self.label_stud_name_3 = QLabel(self.widget_30)
        self.label_stud_name_3.setObjectName(u"label_stud_name_3")
        self.label_stud_name_3.setFont(font2)
        self.label_stud_name_3.setStyleSheet(u"")
        self.label_stud_name_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_stud_name_3)

        self.label_student_score_3 = QLabel(self.widget_30)
        self.label_student_score_3.setObjectName(u"label_student_score_3")
        self.label_student_score_3.setFont(font3)
        self.label_student_score_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_student_score_3)

        self.label_student_place_3 = QLabel(self.widget_30)
        self.label_student_place_3.setObjectName(u"label_student_place_3")
        self.label_student_place_3.setFont(font4)
        self.label_student_place_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_student_place_3)


        self.horizontalLayout_42.addWidget(self.widget_30)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_21)


        self.verticalLayout_36.addWidget(self.widget_top_scorers)


        self.horizontalLayout_24.addWidget(self.widget_13)

        self.widget_datetime = QWidget(self.widget_11)
        self.widget_datetime.setObjectName(u"widget_datetime")
        self.widget_datetime.setMinimumSize(QSize(211, 221))
        self.widget_datetime.setMaximumSize(QSize(211, 16777215))
        self.label_month = QLabel(self.widget_datetime)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setGeometry(QRect(59, 10, 91, 34))
        font5 = QFont()
        font5.setFamilies([u"Inter Medium"])
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_month.setFont(font5)
        self.label_month.setStyleSheet(u"color: rgb(255, 255, 255); background-color: transparent; font: 57 18pt \"Inter Medium\";")
        self.label_month.setAlignment(Qt.AlignCenter)
        self.label_day = QLabel(self.widget_datetime)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setGeometry(QRect(60, 50, 87, 82))
        font6 = QFont()
        font6.setFamilies([u"Inter Medium"])
        font6.setPointSize(50)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_day.setFont(font6)
        self.label_day.setStyleSheet(u"QLabel { color: rgb(36, 31, 49); background-color: transparent; font: 50pt \"Inter Medium\"; }")
        self.label_day.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.widget_datetime)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 10, 151, 151))
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setStyleSheet(u"background-color: rgba(191, 64, 64, 0);")
        self.label_19.setPixmap(QPixmap(u":/Images/Images/calendar_widget.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.widget_datetime)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 170, 155, 51))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_time = QLabel(self.horizontalLayoutWidget)
        self.label_time.setObjectName(u"label_time")
        font7 = QFont()
        font7.setFamilies([u"Inter Medium"])
        font7.setPointSize(30)
        font7.setBold(False)
        font7.setItalic(False)
        self.label_time.setFont(font7)
        self.label_time.setStyleSheet(u"QLabel { color: rgb(36, 31, 49); background-color: transparent; font: 57 30pt \"Inter Medium\"; }")
        self.label_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_time)

        self.label_timeAP = QLabel(self.horizontalLayoutWidget)
        self.label_timeAP.setObjectName(u"label_timeAP")
        font8 = QFont()
        font8.setFamilies([u"Inter Medium"])
        font8.setPointSize(14)
        font8.setBold(False)
        font8.setItalic(False)
        self.label_timeAP.setFont(font8)
        self.label_timeAP.setStyleSheet(u"QLabel { color: rgb(36, 31, 49); background-color: transparent; font: 57 14pt \"Inter Medium\"; }")
        self.label_timeAP.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_timeAP)

        self.label_19.raise_()
        self.label_month.raise_()
        self.label_day.raise_()
        self.horizontalLayoutWidget.raise_()

        self.horizontalLayout_24.addWidget(self.widget_datetime)


        self.verticalLayout_23.addWidget(self.widget_11)


        self.horizontalLayout_14.addWidget(self.widget)

        self.stackedWidget.addWidget(self.pageHome)
        self.pageClassList = QWidget()
        self.pageClassList.setObjectName(u"pageClassList")
        self.pageClassList.setStyleSheet(u"*[class=\"label-faded\"] {\n"
"	color: rgb(124, 124, 124);\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#grp_SectionInfo QLabel, \n"
"#frame_student_info QLabel, \n"
"#frame_contact_info QLabel {\n"
"	font: 11pt \"Inter\"; \n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"] {\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding-left: 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\";\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    border: "
                        "none;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white !important;\n"
"    border: 1px solid #999;\n"
"    selection-background-color: #7eb4d7;\n"
"    selection-color: #ffffff;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding-left: 10px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover state for items inside the dropdown */\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QSpinBox"
                        "::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-bottom-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Images/Images/caret-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.pageClassList)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_table_stud = QWidget(self.pageClassList)
        self.widget_table_stud.setObjectName(u"widget_table_stud")
        self.widget_table_stud.setMinimumSize(QSize(494, 0))
        self.verticalLayout_6 = QVBoxLayout(self.widget_table_stud)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_h = QWidget(self.widget_table_stud)
        self.widget_h.setObjectName(u"widget_h")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_h)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.widget_h)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(100, 20))
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.label_32)

        self.cmb_school_year = QComboBox(self.widget_h)
        self.cmb_school_year.setObjectName(u"cmb_school_year")
        self.cmb_school_year.setMinimumSize(QSize(120, 30))
        self.cmb_school_year.setMaximumSize(QSize(16777215, 30))
        self.cmb_school_year.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.cmb_school_year)

        self.btnRefreshSY = QPushButton(self.widget_h)
        self.btnRefreshSY.setObjectName(u"btnRefreshSY")
        self.btnRefreshSY.setMinimumSize(QSize(30, 30))
        self.btnRefreshSY.setMaximumSize(QSize(30, 30))
        self.btnRefreshSY.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/Images/Images/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRefreshSY.setIcon(icon12)
        self.btnRefreshSY.setIconSize(QSize(22, 22))

        self.horizontalLayout_18.addWidget(self.btnRefreshSY)

        self.cmb_studSection = QComboBox(self.widget_h)
        self.cmb_studSection.setObjectName(u"cmb_studSection")
        self.cmb_studSection.setMinimumSize(QSize(150, 30))
        self.cmb_studSection.setMaximumSize(QSize(16777215, 30))
        self.cmb_studSection.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.cmb_studSection)

        self.widget_search_2 = QWidget(self.widget_h)
        self.widget_search_2.setObjectName(u"widget_search_2")
        self.widget_search_2.setMinimumSize(QSize(0, 30))
        self.widget_search_2.setMaximumSize(QSize(16777215, 30))
        self.widget_search_2.setStyleSheet(u"*[class=\"widget-search-container\"] {\n"
"	background-color: #FFF;\n"
"	border: 1px solid #999;\n"
"	border-radius: 15px;\n"
"}")
        self.layout_search_2 = QHBoxLayout(self.widget_search_2)
        self.layout_search_2.setSpacing(0)
        self.layout_search_2.setObjectName(u"layout_search_2")
        self.layout_search_2.setContentsMargins(4, 0, 6, 0)
        self.label_magnifying_stud = QLabel(self.widget_search_2)
        self.label_magnifying_stud.setObjectName(u"label_magnifying_stud")
        self.label_magnifying_stud.setMinimumSize(QSize(30, 30))
        self.label_magnifying_stud.setMaximumSize(QSize(30, 30))
        self.label_magnifying_stud.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.label_magnifying_stud.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_stud.setScaledContents(True)
        self.label_magnifying_stud.setMargin(5)

        self.layout_search_2.addWidget(self.label_magnifying_stud)

        self.txt_classList_search = QLineEdit(self.widget_search_2)
        self.txt_classList_search.setObjectName(u"txt_classList_search")
        self.txt_classList_search.setMinimumSize(QSize(0, 30))
        self.txt_classList_search.setMaximumSize(QSize(16777215, 30))
        self.txt_classList_search.setStyleSheet(u"#txt_classList_search {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")

        self.layout_search_2.addWidget(self.txt_classList_search)

        self.btnClearSearch_1 = QPushButton(self.widget_search_2)
        self.btnClearSearch_1.setObjectName(u"btnClearSearch_1")
        self.btnClearSearch_1.setMinimumSize(QSize(20, 20))
        self.btnClearSearch_1.setMaximumSize(QSize(20, 20))
        self.btnClearSearch_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClearSearch_1.setStyleSheet(u"*[class=\"button-clear-search\"] {\n"
"	border-radius: 10px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:hover {\n"
"	background-color: #FFC0C0;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:pressed {\n"
"	background-color: #FFD2D2;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon13.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btnClearSearch_1.setIcon(icon13)
        self.btnClearSearch_1.setIconSize(QSize(8, 8))

        self.layout_search_2.addWidget(self.btnClearSearch_1)


        self.horizontalLayout_18.addWidget(self.widget_search_2)


        self.verticalLayout_6.addWidget(self.widget_h)

        self.line_8 = QFrame(self.widget_table_stud)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_8)

        self.widget_19 = QWidget(self.widget_table_stud)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.widget_19)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(100, 20))
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_47)

        self.label_totalStudCount = QLabel(self.widget_19)
        self.label_totalStudCount.setObjectName(u"label_totalStudCount")
        self.label_totalStudCount.setMaximumSize(QSize(100, 20))
        font9 = QFont()
        font9.setFamilies([u"Inter SemiBold"])
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_totalStudCount.setFont(font9)
        self.label_totalStudCount.setStyleSheet(u"background-color: transparent; font: 10pt \"Inter SemiBold\";")

        self.horizontalLayout_3.addWidget(self.label_totalStudCount)

        self.horizontalSpacer_27 = QSpacerItem(509, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_27)


        self.verticalLayout_6.addWidget(self.widget_19)

        self.scrollArea_classlist = QScrollArea(self.widget_table_stud)
        self.scrollArea_classlist.setObjectName(u"scrollArea_classlist")
        self.scrollArea_classlist.setAutoFillBackground(True)
        self.scrollArea_classlist.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.scrollArea_classlist.setFrameShape(QFrame.StyledPanel)
        self.scrollArea_classlist.setFrameShadow(QFrame.Plain)
        self.scrollArea_classlist.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_classlist.setWidgetResizable(True)
        self.scrollArea_classlist.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.container = QWidget()
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(0, 0, 100, 30))
        self.gridLayout_stud_card = QGridLayout(self.container)
        self.gridLayout_stud_card.setObjectName(u"gridLayout_stud_card")
        self.scrollArea_classlist.setWidget(self.container)

        self.verticalLayout_6.addWidget(self.scrollArea_classlist)

        self.widget_f = QWidget(self.widget_table_stud)
        self.widget_f.setObjectName(u"widget_f")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_f)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btnAddStudent = QPushButton(self.widget_f)
        self.btnAddStudent.setObjectName(u"btnAddStudent")
        self.btnAddStudent.setMinimumSize(QSize(130, 30))
        self.btnAddStudent.setMaximumSize(QSize(16777215, 30))
        self.btnAddStudent.setFont(font)
        self.btnAddStudent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddStudent.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/Images/Images/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddStudent.setIcon(icon14)

        self.horizontalLayout_17.addWidget(self.btnAddStudent)

        self.btnDeleteStudent = QPushButton(self.widget_f)
        self.btnDeleteStudent.setObjectName(u"btnDeleteStudent")
        self.btnDeleteStudent.setMinimumSize(QSize(140, 30))
        self.btnDeleteStudent.setMaximumSize(QSize(16777215, 30))
        self.btnDeleteStudent.setFont(font)
        self.btnDeleteStudent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDeleteStudent.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/Images/Images/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDeleteStudent.setIcon(icon15)

        self.horizontalLayout_17.addWidget(self.btnDeleteStudent)

        self.btnPrintStudentList = QPushButton(self.widget_f)
        self.btnPrintStudentList.setObjectName(u"btnPrintStudentList")
        self.btnPrintStudentList.setMinimumSize(QSize(140, 30))
        self.btnPrintStudentList.setMaximumSize(QSize(16777215, 30))
        self.btnPrintStudentList.setFont(font)
        self.btnPrintStudentList.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrintStudentList.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u":/Images/Images/printer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrintStudentList.setIcon(icon16)

        self.horizontalLayout_17.addWidget(self.btnPrintStudentList)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)


        self.verticalLayout_6.addWidget(self.widget_f)


        self.horizontalLayout_15.addWidget(self.widget_table_stud)

        self.InformationPanel = QWidget(self.pageClassList)
        self.InformationPanel.setObjectName(u"InformationPanel")
        self.InformationPanel.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.InformationPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sub_info_panel = QWidget(self.InformationPanel)
        self.sub_info_panel.setObjectName(u"sub_info_panel")
        self.sub_info_panel.setMinimumSize(QSize(0, 100))
        self.verticalLayout_9 = QVBoxLayout(self.sub_info_panel)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.label_16 = QLabel(self.sub_info_panel)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"background-color: transparent; color: rgb(253, 64, 115); font: 57 14pt \"Inter Medium\";")

        self.verticalLayout_9.addWidget(self.label_16)

        self.grp_SectionInfo = QFrame(self.sub_info_panel)
        self.grp_SectionInfo.setObjectName(u"grp_SectionInfo")
        self.grp_SectionInfo.setMaximumSize(QSize(16777215, 130))
        self.grp_SectionInfo.setFont(font)
        self.grp_SectionInfo.setStyleSheet(u"border-radius: 15px; background-color: rgb(255, 255, 255);")
        self.formLayout_2 = QFormLayout(self.grp_SectionInfo)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_33 = QLabel(self.grp_SectionInfo)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        font10 = QFont()
        font10.setFamilies([u"Inter"])
        font10.setPointSize(11)
        font10.setBold(False)
        font10.setItalic(False)
        self.label_33.setFont(font10)
        self.label_33.setStyleSheet(u"")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.label_34 = QLabel(self.grp_SectionInfo)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setFont(font10)
        self.label_34.setStyleSheet(u"")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_34)

        self.label_28 = QLabel(self.grp_SectionInfo)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 20))
        self.label_28.setFont(font10)
        self.label_28.setStyleSheet(u"")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.label_studentCount = QLabel(self.grp_SectionInfo)
        self.label_studentCount.setObjectName(u"label_studentCount")
        self.label_studentCount.setMaximumSize(QSize(16777215, 20))
        self.label_studentCount.setFont(font10)
        self.label_studentCount.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_studentCount)

        self.label_girlCount = QLabel(self.grp_SectionInfo)
        self.label_girlCount.setObjectName(u"label_girlCount")
        self.label_girlCount.setMaximumSize(QSize(16777215, 20))
        self.label_girlCount.setFont(font10)
        self.label_girlCount.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_girlCount)

        self.label_boyCount = QLabel(self.grp_SectionInfo)
        self.label_boyCount.setObjectName(u"label_boyCount")
        self.label_boyCount.setMaximumSize(QSize(16777215, 20))
        self.label_boyCount.setFont(font10)
        self.label_boyCount.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_boyCount)

        self.label_35 = QLabel(self.grp_SectionInfo)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 20))
        self.label_35.setFont(font10)
        self.label_35.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_35)

        self.label_section = QLabel(self.grp_SectionInfo)
        self.label_section.setObjectName(u"label_section")
        self.label_section.setMaximumSize(QSize(16777215, 20))
        self.label_section.setFont(font10)
        self.label_section.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_section)


        self.verticalLayout_9.addWidget(self.grp_SectionInfo)

        self.label_17 = QLabel(self.sub_info_panel)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"background-color: transparent; color: rgb(253, 64, 115); font: 57 14pt \"Inter Medium\";")

        self.verticalLayout_9.addWidget(self.label_17)

        self.frame_student_info = QFrame(self.sub_info_panel)
        self.frame_student_info.setObjectName(u"frame_student_info")
        self.frame_student_info.setFont(font)
        self.frame_student_info.setStyleSheet(u"border-radius: 15px; background-color: rgb(255, 255, 255);")
        self.formLayout = QFormLayout(self.frame_student_info)
        self.formLayout.setObjectName(u"formLayout")
        self.label_43 = QLabel(self.frame_student_info)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(95, 20))
        self.label_43.setFont(font10)
        self.label_43.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_43)

        self.label_studentId = QLabel(self.frame_student_info)
        self.label_studentId.setObjectName(u"label_studentId")
        self.label_studentId.setMaximumSize(QSize(16777215, 20))
        self.label_studentId.setFont(font10)
        self.label_studentId.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_studentId)

        self.label_36 = QLabel(self.frame_student_info)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(95, 20))
        self.label_36.setFont(font10)
        self.label_36.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_36)

        self.label_studentLastName = QLabel(self.frame_student_info)
        self.label_studentLastName.setObjectName(u"label_studentLastName")
        self.label_studentLastName.setMaximumSize(QSize(16777215, 20))
        self.label_studentLastName.setFont(font10)
        self.label_studentLastName.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_studentLastName)

        self.label_38 = QLabel(self.frame_student_info)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(95, 20))
        self.label_38.setFont(font10)
        self.label_38.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_38)

        self.label_studentFirstName = QLabel(self.frame_student_info)
        self.label_studentFirstName.setObjectName(u"label_studentFirstName")
        self.label_studentFirstName.setMaximumSize(QSize(16777215, 20))
        self.label_studentFirstName.setFont(font10)
        self.label_studentFirstName.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_studentFirstName)

        self.label_41 = QLabel(self.frame_student_info)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(95, 20))
        self.label_41.setFont(font10)
        self.label_41.setStyleSheet(u"")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_41)

        self.label_studentMiddleName = QLabel(self.frame_student_info)
        self.label_studentMiddleName.setObjectName(u"label_studentMiddleName")
        self.label_studentMiddleName.setMaximumSize(QSize(16777215, 20))
        self.label_studentMiddleName.setFont(font10)
        self.label_studentMiddleName.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_studentMiddleName)

        self.label_37 = QLabel(self.frame_student_info)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(95, 20))
        self.label_37.setFont(font10)
        self.label_37.setStyleSheet(u"")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_37)

        self.label_studentGender = QLabel(self.frame_student_info)
        self.label_studentGender.setObjectName(u"label_studentGender")
        self.label_studentGender.setMaximumSize(QSize(16777215, 20))
        self.label_studentGender.setFont(font10)
        self.label_studentGender.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.label_studentGender)


        self.verticalLayout_9.addWidget(self.frame_student_info)

        self.label_51 = QLabel(self.sub_info_panel)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 30))
        self.label_51.setMaximumSize(QSize(16777215, 20))
        self.label_51.setFont(font8)
        self.label_51.setStyleSheet(u"background-color: transparent; color: rgb(253, 64, 115); font: 57 14pt \"Inter Medium\";")

        self.verticalLayout_9.addWidget(self.label_51)

        self.frame_contact_info = QFrame(self.sub_info_panel)
        self.frame_contact_info.setObjectName(u"frame_contact_info")
        self.frame_contact_info.setFont(font)
        self.frame_contact_info.setStyleSheet(u"border-radius: 15px; background-color: rgb(255, 255, 255);")
        self.formLayout_4 = QFormLayout(self.frame_contact_info)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_59 = QLabel(self.frame_contact_info)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font10)
        self.label_59.setStyleSheet(u"")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_59)

        self.label_56 = QLabel(self.frame_contact_info)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font10)
        self.label_56.setStyleSheet(u"")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_56)

        self.label_contact_person = QLabel(self.frame_contact_info)
        self.label_contact_person.setObjectName(u"label_contact_person")
        self.label_contact_person.setMaximumSize(QSize(16777215, 20))
        self.label_contact_person.setFont(font10)
        self.label_contact_person.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_contact_person)

        self.label_contact_number = QLabel(self.frame_contact_info)
        self.label_contact_number.setObjectName(u"label_contact_number")
        self.label_contact_number.setMaximumSize(QSize(16777215, 20))
        self.label_contact_number.setFont(font10)
        self.label_contact_number.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_contact_number)


        self.verticalLayout_9.addWidget(self.frame_contact_info)

        self.widget_21 = QWidget(self.sub_info_panel)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 12, -1, -1)
        self.btnEditStudent = QPushButton(self.widget_21)
        self.btnEditStudent.setObjectName(u"btnEditStudent")
        self.btnEditStudent.setMinimumSize(QSize(130, 30))
        self.btnEditStudent.setMaximumSize(QSize(130, 30))
        self.btnEditStudent.setFont(font)
        self.btnEditStudent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditStudent.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/Images/Images/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditStudent.setIcon(icon17)

        self.horizontalLayout_23.addWidget(self.btnEditStudent)


        self.verticalLayout_9.addWidget(self.widget_21)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)


        self.verticalLayout_3.addWidget(self.sub_info_panel)

        self.widget_2 = QWidget(self.InformationPanel)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_22 = QVBoxLayout(self.widget_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout_15.addWidget(self.InformationPanel)

        self.stackedWidget.addWidget(self.pageClassList)
        self.pageLesson = QWidget()
        self.pageLesson.setObjectName(u"pageLesson")
        self.pageLesson.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-right: none;\n"
"}\n"
"\n"
"*[class=\"textbox-search\"] {\n"
"	background-color: rgb(255, 255, 255); \n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-left: none;\n"
"}\n"
"\n"
"*[class=\"widget-search-container\"] {\n"
"	background: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.pageLesson)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_search_4 = QWidget(self.pageLesson)
        self.widget_search_4.setObjectName(u"widget_search_4")
        self.widget_search_4.setMinimumSize(QSize(0, 30))
        self.widget_search_4.setMaximumSize(QSize(16777215, 30))
        self.widget_search_4.setStyleSheet(u"*[class=\"widget-search-container\"] {\n"
"	background-color: #FFF;\n"
"	border: 1px solid #999;\n"
"	border-radius: 15px;\n"
"}")
        self.layout_search_3 = QHBoxLayout(self.widget_search_4)
        self.layout_search_3.setSpacing(0)
        self.layout_search_3.setObjectName(u"layout_search_3")
        self.layout_search_3.setContentsMargins(4, 0, 6, 0)
        self.label_magnifying_stud_2 = QLabel(self.widget_search_4)
        self.label_magnifying_stud_2.setObjectName(u"label_magnifying_stud_2")
        self.label_magnifying_stud_2.setMinimumSize(QSize(30, 30))
        self.label_magnifying_stud_2.setMaximumSize(QSize(30, 30))
        self.label_magnifying_stud_2.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.label_magnifying_stud_2.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_stud_2.setScaledContents(True)
        self.label_magnifying_stud_2.setMargin(5)

        self.layout_search_3.addWidget(self.label_magnifying_stud_2)

        self.txtSearchLesson = QLineEdit(self.widget_search_4)
        self.txtSearchLesson.setObjectName(u"txtSearchLesson")
        self.txtSearchLesson.setMinimumSize(QSize(0, 30))
        self.txtSearchLesson.setMaximumSize(QSize(16777215, 30))
        self.txtSearchLesson.setStyleSheet(u"*[class=\"textbox-search\"] {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")

        self.layout_search_3.addWidget(self.txtSearchLesson)

        self.btnClearSearch_2 = QPushButton(self.widget_search_4)
        self.btnClearSearch_2.setObjectName(u"btnClearSearch_2")
        self.btnClearSearch_2.setMinimumSize(QSize(20, 20))
        self.btnClearSearch_2.setMaximumSize(QSize(20, 20))
        self.btnClearSearch_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClearSearch_2.setStyleSheet(u"*[class=\"button-clear-search\"] {\n"
"	border-radius: 10px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:hover {\n"
"	background-color: #FFC0C0;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:pressed {\n"
"	background-color: #FFD2D2;\n"
"}")
        self.btnClearSearch_2.setIcon(icon13)
        self.btnClearSearch_2.setIconSize(QSize(8, 8))

        self.layout_search_3.addWidget(self.btnClearSearch_2)


        self.verticalLayout.addWidget(self.widget_search_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_17 = QWidget(self.pageLesson)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(100, 0))
        self.widget_17.setStyleSheet(u"#widget_17 {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #999;\n"
"    padding: 5px 15px;\n"
"	font: 10pt \"Inter\";\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"#btnAnimation {\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-right: none;\n"
"}\n"
"\n"
"#btnAnimation:checked {\n"
"    background-color: #72D582;\n"
"	border: 2px solid #448D50;\n"
"    color: #000;\n"
"}\n"
"\n"
"#btnPowerPoint {\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#btnPowerPoint:checked {\n"
"    background-color: #72D582;\n"
"	border: 2px solid #448D50;\n"
"    color: #000;\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.btnAnimation = QPushButton(self.widget_17)
        self.btnAnimation.setObjectName(u"btnAnimation")
        self.btnAnimation.setMinimumSize(QSize(126, 30))
        self.btnAnimation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_32.addWidget(self.btnAnimation)

        self.btnPowerPoint = QPushButton(self.widget_17)
        self.btnPowerPoint.setObjectName(u"btnPowerPoint")
        self.btnPowerPoint.setMinimumSize(QSize(126, 30))
        self.btnPowerPoint.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_32.addWidget(self.btnPowerPoint)


        self.horizontalLayout_4.addWidget(self.widget_17)

        self.btnRefreshLessonTable = QPushButton(self.pageLesson)
        self.btnRefreshLessonTable.setObjectName(u"btnRefreshLessonTable")
        self.btnRefreshLessonTable.setMinimumSize(QSize(30, 30))
        self.btnRefreshLessonTable.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRefreshLessonTable.setIcon(icon12)
        self.btnRefreshLessonTable.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.btnRefreshLessonTable)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btnLessonView = QPushButton(self.pageLesson)
        self.btnLessonView.setObjectName(u"btnLessonView")
        self.btnLessonView.setMinimumSize(QSize(100, 30))
        self.btnLessonView.setMaximumSize(QSize(16777215, 30))
        self.btnLessonView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/Images/Images/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLessonView.setIcon(icon18)

        self.horizontalLayout_4.addWidget(self.btnLessonView)

        self.btnLessonEdit = QPushButton(self.pageLesson)
        self.btnLessonEdit.setObjectName(u"btnLessonEdit")
        self.btnLessonEdit.setMinimumSize(QSize(100, 30))
        self.btnLessonEdit.setMaximumSize(QSize(16777215, 30))
        self.btnLessonEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLessonEdit.setIcon(icon17)

        self.horizontalLayout_4.addWidget(self.btnLessonEdit)

        self.btnLessonAdd = QPushButton(self.pageLesson)
        self.btnLessonAdd.setObjectName(u"btnLessonAdd")
        self.btnLessonAdd.setMinimumSize(QSize(100, 30))
        self.btnLessonAdd.setMaximumSize(QSize(16777215, 30))
        self.btnLessonAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLessonAdd.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.btnLessonAdd)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.table_lesson = QTableView(self.pageLesson)
        self.table_lesson.setObjectName(u"table_lesson")
        self.table_lesson.setStyleSheet(u"QTableView {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"    gridline-color: #f0f0f0;\n"
"    background-color: white;\n"
"    selection-background-color: rgba(38, 162, 105, 0.2);\n"
"    selection-color: black;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Remove the row numbers (Vertical Header) */\n"
"QHeaderView:vertical {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    width: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Style the top horizontal header */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: rgb(38, 162, 105);  \n"
"    color: white;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Custom Scrollbars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(38, 162, 105);\n"
"    min-height: 30px;\n"
"    border-radius: 3px; \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar:horizont"
                        "al {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(38, 162, 105);\n"
"    min-width: 30px;\n"
"    border-radius: 3px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"/* Remove scrollbar arrows */\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width: 0px; height: 0px;\n"
"}")
        self.table_lesson.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_lesson.setSortingEnabled(True)
        self.table_lesson.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_lesson)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_lessonTotalCount = QLabel(self.pageLesson)
        self.label_lessonTotalCount.setObjectName(u"label_lessonTotalCount")

        self.horizontalLayout_5.addWidget(self.label_lessonTotalCount)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.pageLesson)
        self.pageQuiz = QWidget()
        self.pageQuiz.setObjectName(u"pageQuiz")
        self.pageQuiz.setStyleSheet(u"QComboBox[class=\"combobox-main\"] {\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding-left: 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\";\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    border: none;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white !important;\n"
"    border: 1px solid #999;\n"
"    selection-background-color: #7eb4d7;\n"
"    selection-color: #ffffff"
                        ";\n"
"    outline: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding-left: 10px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover state for items inside the dropdown */\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
""
                        "\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-bottom-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Images/Images/caret-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.pageQuiz)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.labelGradingPeriod_2 = QLabel(self.pageQuiz)
        self.labelGradingPeriod_2.setObjectName(u"labelGradingPeriod_2")
        self.labelGradingPeriod_2.setMaximumSize(QSize(16777215, 30))

        self.headerLayout.addWidget(self.labelGradingPeriod_2)

        self.quiz_no = QSpinBox(self.pageQuiz)
        self.quiz_no.setObjectName(u"quiz_no")
        self.quiz_no.setMinimumSize(QSize(70, 30))
        self.quiz_no.setMaximumSize(QSize(70, 30))
        self.quiz_no.setStyleSheet(u"")
        self.quiz_no.setAlignment(Qt.AlignCenter)
        self.quiz_no.setMinimum(1)
        self.quiz_no.setMaximum(999)
        self.quiz_no.setValue(1)

        self.headerLayout.addWidget(self.quiz_no)

        self.labelGradingPeriod = QLabel(self.pageQuiz)
        self.labelGradingPeriod.setObjectName(u"labelGradingPeriod")
        self.labelGradingPeriod.setMaximumSize(QSize(16777215, 30))

        self.headerLayout.addWidget(self.labelGradingPeriod)

        self.cbGradingPeriod = QComboBox(self.pageQuiz)
        self.cbGradingPeriod.setObjectName(u"cbGradingPeriod")
        self.cbGradingPeriod.setMinimumSize(QSize(150, 30))
        self.cbGradingPeriod.setMaximumSize(QSize(16777215, 30))
        self.cbGradingPeriod.setStyleSheet(u"")
        self.cbGradingPeriod.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.headerLayout.addWidget(self.cbGradingPeriod)

        self.labelLesson = QLabel(self.pageQuiz)
        self.labelLesson.setObjectName(u"labelLesson")

        self.headerLayout.addWidget(self.labelLesson)

        self.cbLessonName = QComboBox(self.pageQuiz)
        self.cbLessonName.setObjectName(u"cbLessonName")
        self.cbLessonName.setMinimumSize(QSize(150, 30))
        self.cbLessonName.setMaximumSize(QSize(16777215, 30))
        self.cbLessonName.setStyleSheet(u"")
        self.cbLessonName.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.headerLayout.addWidget(self.cbLessonName)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.headerLayout.addLayout(self.horizontalLayout_6)

        self.checkBoxPublish = QCheckBox(self.pageQuiz)
        self.checkBoxPublish.setObjectName(u"checkBoxPublish")
        self.checkBoxPublish.setMinimumSize(QSize(0, 30))
        self.checkBoxPublish.setMaximumSize(QSize(16777215, 30))
        self.checkBoxPublish.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBoxPublish.setStyleSheet(u"QCheckBox {\n"
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

        self.headerLayout.addWidget(self.checkBoxPublish)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer_9)

        self.label_7 = QLabel(self.pageQuiz)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))

        self.headerLayout.addWidget(self.label_7)

        self.label_totalScore = QLabel(self.pageQuiz)
        self.label_totalScore.setObjectName(u"label_totalScore")
        self.label_totalScore.setMinimumSize(QSize(0, 30))
        self.label_totalScore.setMaximumSize(QSize(16777215, 30))
        self.label_totalScore.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")

        self.headerLayout.addWidget(self.label_totalScore)


        self.verticalLayout_8.addLayout(self.headerLayout)

        self.line_3 = QFrame(self.pageQuiz)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.widget_quiz_1 = QWidget(self.pageQuiz)
        self.widget_quiz_1.setObjectName(u"widget_quiz_1")
        self.widget_quiz_1.setStyleSheet(u"#frame_6 { background-color: transparent; }")
        self.horizontalLayout = QHBoxLayout(self.widget_quiz_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.widget_quiz_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_6)

        self.widget_4 = QWidget(self.widget_quiz_1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"/* Base style for all difficulty buttons */\n"
"QPushButton {\n"
"    border: 1px solid #999;\n"
"    padding: 5px 15px;\n"
"	font: 10pt \"Inter\";\n"
"    background-color: #f0f0f0; /* Default neutral color */\n"
"}\n"
"\n"
"/* LEFT BUTTON (Easy) */\n"
"QPushButton#btnEasy {\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
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
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"QPushButton#btnHard:checked {\n"
""
                        "	background-color: #F07D75; /* Red */\n"
"	border: 2px solid #E65247;\n"
"	color: #000;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btnEasy = QPushButton(self.widget_4)
        self.btnEasy.setObjectName(u"btnEasy")
        self.btnEasy.setMinimumSize(QSize(82, 30))
        self.btnEasy.setMaximumSize(QSize(82, 30))
        self.btnEasy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEasy.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnEasy)

        self.btnAverage = QPushButton(self.widget_4)
        self.btnAverage.setObjectName(u"btnAverage")
        self.btnAverage.setMinimumSize(QSize(82, 30))
        self.btnAverage.setMaximumSize(QSize(82, 30))
        self.btnAverage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAverage.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnAverage)

        self.btnHard = QPushButton(self.widget_4)
        self.btnHard.setObjectName(u"btnHard")
        self.btnHard.setMinimumSize(QSize(82, 30))
        self.btnHard.setMaximumSize(QSize(82, 30))
        self.btnHard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnHard.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnHard)


        self.horizontalLayout.addWidget(self.widget_4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.label_21 = QLabel(self.widget_quiz_1)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setStyleSheet(u"font: 10pt \"Inter SemiBold\";")

        self.horizontalLayout.addWidget(self.label_21)

        self.label_15 = QLabel(self.widget_quiz_1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_15)

        self.multiplier_easy = QLabel(self.widget_quiz_1)
        self.multiplier_easy.setObjectName(u"multiplier_easy")
        self.multiplier_easy.setMinimumSize(QSize(0, 30))
        self.multiplier_easy.setMaximumSize(QSize(16777215, 30))
        self.multiplier_easy.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")
        self.multiplier_easy.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.multiplier_easy)

        self.label_22 = QLabel(self.widget_quiz_1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_22)

        self.multiplier_average = QLabel(self.widget_quiz_1)
        self.multiplier_average.setObjectName(u"multiplier_average")
        self.multiplier_average.setMinimumSize(QSize(0, 30))
        self.multiplier_average.setMaximumSize(QSize(16777215, 30))
        self.multiplier_average.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")
        self.multiplier_average.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.multiplier_average)

        self.label_23 = QLabel(self.widget_quiz_1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_23)

        self.multiplier_hard = QLabel(self.widget_quiz_1)
        self.multiplier_hard.setObjectName(u"multiplier_hard")
        self.multiplier_hard.setMinimumSize(QSize(0, 30))
        self.multiplier_hard.setMaximumSize(QSize(16777215, 30))
        self.multiplier_hard.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")
        self.multiplier_hard.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.multiplier_hard)

        self.label_3 = QLabel(self.widget_quiz_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_scoreperlevel = QLabel(self.widget_quiz_1)
        self.label_scoreperlevel.setObjectName(u"label_scoreperlevel")
        self.label_scoreperlevel.setMinimumSize(QSize(0, 30))
        self.label_scoreperlevel.setMaximumSize(QSize(16777215, 30))
        self.label_scoreperlevel.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.label_scoreperlevel)


        self.verticalLayout_8.addWidget(self.widget_quiz_1)

        self.line_7 = QFrame(self.pageQuiz)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_7)

        self.widget_quiz_2 = QWidget(self.pageQuiz)
        self.widget_quiz_2.setObjectName(u"widget_quiz_2")
        self.gridLayout = QGridLayout(self.widget_quiz_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_tf = QScrollArea(self.widget_quiz_2)
        self.scrollArea_tf.setObjectName(u"scrollArea_tf")
        self.scrollArea_tf.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.scrollArea_tf.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_tf.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout.addWidget(self.scrollArea_tf, 4, 2, 1, 1)

        self.label_13 = QLabel(self.widget_quiz_2)
        self.label_13.setObjectName(u"label_13")
        font11 = QFont()
        font11.setFamilies([u"Inter SemiBold"])
        font11.setPointSize(14)
        font11.setBold(False)
        font11.setItalic(False)
        self.label_13.setFont(font11)
        self.label_13.setStyleSheet(u"font: 63 14pt \"Inter SemiBold\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)

        self.scrollArea_mc = QScrollArea(self.widget_quiz_2)
        self.scrollArea_mc.setObjectName(u"scrollArea_mc")
        self.scrollArea_mc.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.scrollArea_mc.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_mc.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.scrollArea_mc, 4, 1, 1, 1)

        self.scrollArea_id = QScrollArea(self.widget_quiz_2)
        self.scrollArea_id.setObjectName(u"scrollArea_id")
        self.scrollArea_id.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.scrollArea_id.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_id.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea_id, 4, 0, 1, 1)

        self.label_11 = QLabel(self.widget_quiz_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font11)
        self.label_11.setStyleSheet(u"font: 14pt \"Inter SemiBold\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_12 = QLabel(self.widget_quiz_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font11)
        self.label_12.setStyleSheet(u"font: 63 14pt \"Inter SemiBold\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.widget_quiz_2)

        self.widget_quiz_3 = QWidget(self.pageQuiz)
        self.widget_quiz_3.setObjectName(u"widget_quiz_3")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_quiz_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.btnQuizAdd = QPushButton(self.widget_quiz_3)
        self.btnQuizAdd.setObjectName(u"btnQuizAdd")
        self.btnQuizAdd.setMinimumSize(QSize(100, 30))
        self.btnQuizAdd.setMaximumSize(QSize(16777215, 30))
        self.btnQuizAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btnQuizAdd)


        self.verticalLayout_8.addWidget(self.widget_quiz_3)

        self.stackedWidget.addWidget(self.pageQuiz)
        self.pageExercise = QWidget()
        self.pageExercise.setObjectName(u"pageExercise")
        self.pageExercise.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-right: none;\n"
"}\n"
"\n"
"*[class=\"textbox-search\"] {\n"
"	background-color: rgb(255, 255, 255); \n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-left: none;\n"
"}\n"
"\n"
"*[class=\"widget-search-container\"] {\n"
"	background: transparent;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.pageExercise)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_search_5 = QWidget(self.pageExercise)
        self.widget_search_5.setObjectName(u"widget_search_5")
        self.widget_search_5.setMinimumSize(QSize(0, 30))
        self.widget_search_5.setMaximumSize(QSize(16777215, 30))
        self.widget_search_5.setStyleSheet(u"*[class=\"widget-search-container\"] {\n"
"	background-color: #FFF;\n"
"	border: 1px solid #999;\n"
"	border-radius: 15px;\n"
"}")
        self.layout_search_4 = QHBoxLayout(self.widget_search_5)
        self.layout_search_4.setSpacing(0)
        self.layout_search_4.setObjectName(u"layout_search_4")
        self.layout_search_4.setContentsMargins(4, 0, 6, 0)
        self.label_magnifying_stud_3 = QLabel(self.widget_search_5)
        self.label_magnifying_stud_3.setObjectName(u"label_magnifying_stud_3")
        self.label_magnifying_stud_3.setMinimumSize(QSize(30, 30))
        self.label_magnifying_stud_3.setMaximumSize(QSize(30, 30))
        self.label_magnifying_stud_3.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.label_magnifying_stud_3.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_stud_3.setScaledContents(True)
        self.label_magnifying_stud_3.setMargin(5)

        self.layout_search_4.addWidget(self.label_magnifying_stud_3)

        self.txtSearchExercise = QLineEdit(self.widget_search_5)
        self.txtSearchExercise.setObjectName(u"txtSearchExercise")
        self.txtSearchExercise.setMinimumSize(QSize(0, 30))
        self.txtSearchExercise.setMaximumSize(QSize(16777215, 30))
        self.txtSearchExercise.setStyleSheet(u"*[class=\"textbox-search\"] {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")

        self.layout_search_4.addWidget(self.txtSearchExercise)

        self.btnClearSearch_3 = QPushButton(self.widget_search_5)
        self.btnClearSearch_3.setObjectName(u"btnClearSearch_3")
        self.btnClearSearch_3.setMinimumSize(QSize(20, 20))
        self.btnClearSearch_3.setMaximumSize(QSize(20, 20))
        self.btnClearSearch_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClearSearch_3.setStyleSheet(u"*[class=\"button-clear-search\"] {\n"
"	border-radius: 10px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:hover {\n"
"	background-color: #FFC0C0;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:pressed {\n"
"	background-color: #FFD2D2;\n"
"}")
        self.btnClearSearch_3.setIcon(icon13)
        self.btnClearSearch_3.setIconSize(QSize(8, 8))

        self.layout_search_4.addWidget(self.btnClearSearch_3)


        self.verticalLayout_10.addWidget(self.widget_search_5)

        self.verticalSpacer_2 = QSpacerItem(195, 588, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.btnExerciseEdit = QPushButton(self.pageExercise)
        self.btnExerciseEdit.setObjectName(u"btnExerciseEdit")
        self.btnExerciseEdit.setMinimumSize(QSize(100, 30))
        self.btnExerciseEdit.setMaximumSize(QSize(16777215, 30))
        self.btnExerciseEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.btnExerciseEdit)

        self.btnExerciseAdd = QPushButton(self.pageExercise)
        self.btnExerciseAdd.setObjectName(u"btnExerciseAdd")
        self.btnExerciseAdd.setMinimumSize(QSize(100, 30))
        self.btnExerciseAdd.setMaximumSize(QSize(16777215, 30))
        self.btnExerciseAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.btnExerciseAdd)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.stackedWidget.addWidget(self.pageExercise)
        self.pageSections = QWidget()
        self.pageSections.setObjectName(u"pageSections")
        self.pageSections.setStyleSheet(u"QComboBox[class=\"combobox-main\"] {\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding-left: 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\";\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    border: none;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white !important;\n"
"    border: 1px solid #999;\n"
"    selection-background-color: #7eb4d7;\n"
"    selection-color: #ffffff"
                        ";\n"
"    outline: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding-left: 10px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover state for items inside the dropdown */\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
""
                        "\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-bottom-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Images/Images/caret-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.pageSections)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.pageSections)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_8.addWidget(self.label_4)

        self.comboBox_Section = QComboBox(self.pageSections)
        self.comboBox_Section.setObjectName(u"comboBox_Section")
        self.comboBox_Section.setMinimumSize(QSize(0, 30))
        self.comboBox_Section.setMaximumSize(QSize(16777215, 30))
        self.comboBox_Section.setStyleSheet(u"")
        self.comboBox_Section.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_8.addWidget(self.comboBox_Section)

        self.btnSectionAdd = QPushButton(self.pageSections)
        self.btnSectionAdd.setObjectName(u"btnSectionAdd")
        self.btnSectionAdd.setMinimumSize(QSize(30, 30))
        self.btnSectionAdd.setMaximumSize(QSize(16777215, 30))
        self.btnSectionAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSectionAdd.setStyleSheet(u"padding: 0px 10px 0px;")

        self.horizontalLayout_8.addWidget(self.btnSectionAdd)

        self.btnSectionDelete = QPushButton(self.pageSections)
        self.btnSectionDelete.setObjectName(u"btnSectionDelete")
        self.btnSectionDelete.setEnabled(True)
        self.btnSectionDelete.setMinimumSize(QSize(30, 30))
        self.btnSectionDelete.setMaximumSize(QSize(16777215, 30))
        self.btnSectionDelete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSectionDelete.setStyleSheet(u"padding: 0px 10px 0px;")

        self.horizontalLayout_8.addWidget(self.btnSectionDelete)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.btnSectionEdit = QPushButton(self.pageSections)
        self.btnSectionEdit.setObjectName(u"btnSectionEdit")
        self.btnSectionEdit.setMinimumSize(QSize(50, 30))
        self.btnSectionEdit.setMaximumSize(QSize(16777215, 30))
        self.btnSectionEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.btnSectionEdit)

        self.label_5 = QLabel(self.pageSections)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(55, 30))

        self.horizontalLayout_8.addWidget(self.label_5)

        self.label_Adviser = QLabel(self.pageSections)
        self.label_Adviser.setObjectName(u"label_Adviser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_Adviser.sizePolicy().hasHeightForWidth())
        self.label_Adviser.setSizePolicy(sizePolicy1)
        self.label_Adviser.setMinimumSize(QSize(150, 0))
        self.label_Adviser.setMaximumSize(QSize(16777215, 30))
        self.label_Adviser.setStyleSheet(u"padding: 0px 10px 0px; background-color: rgb(246, 245, 244); border-radius: 10px;")
        self.label_Adviser.setTextFormat(Qt.PlainText)
        self.label_Adviser.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.label_Adviser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.table_section = QTableView(self.pageSections)
        self.table_section.setObjectName(u"table_section")
        self.table_section.setStyleSheet(u"QTableView {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"    gridline-color: #f0f0f0;\n"
"    background-color: white;\n"
"    selection-background-color: rgba(38, 162, 105, 0.2);\n"
"    selection-color: black;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Remove the row numbers (Vertical Header) */\n"
"QHeaderView:vertical {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    width: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Style the top horizontal header */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: rgb(38, 162, 105);  \n"
"    color: white;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Custom Scrollbars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(38, 162, 105);\n"
"    min-height: 30px;\n"
"    border-radius: 3px; \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar:horizont"
                        "al {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(38, 162, 105);\n"
"    min-width: 30px;\n"
"    border-radius: 3px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"/* Remove scrollbar arrows */\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width: 0px; height: 0px;\n"
"}")
        self.table_section.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_section.setSortingEnabled(True)
        self.table_section.verticalHeader().setVisible(False)
        self.table_section.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_2.addWidget(self.table_section)

        self.stackedWidget.addWidget(self.pageSections)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.pageReports.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.pageReports)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_reports = QTabWidget(self.pageReports)
        self.tabWidget_reports.setObjectName(u"tabWidget_reports")
        self.tabWidget_reports.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-right: none;\n"
"}\n"
"\n"
"*[class=\"textbox-search\"] {\n"
"	background-color: rgb(255, 255, 255); \n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-left: none;\n"
"}\n"
"\n"
"*[class=\"widget-search-container\"] {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QComboBox {\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px; /* Fully rounded pills */\n"
"    padding-left: 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\"; /* Consolidated font settings */\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
""
                        "    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
"    /* Match the 15px border-radius of the main control */\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    border: none;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white !important;\n"
"    border: 1px solid #999;\n"
"    selection-background-color: #7eb4d7;\n"
"    selection-color: #ffffff;\n"
"    outline: 0; /* Removes the ugly dotted focus border */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding-left: 10px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover state for items inside the dropdown */\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
""
                        "QSpinBox {\n"
"	font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-bottom-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Images/Images/caret-up.png);\n"
"    width: 8p"
                        "x;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"QTableView {\n"
"    border: 1px solid rgb(161, 161, 161);\n"
"    gridline-color: #f0f0f0;\n"
"    background-color: white;\n"
"    selection-background-color: rgba(38, 162, 105, 0.2);\n"
"    selection-color: black;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Remove the row numbers (Vertical Header) */\n"
"QHeaderView:vertical {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    width: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Style the top horizontal header */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: rgb(246, 245, 244);  \n"
"    color: black;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Custom Scrollbars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(38, 162, 105);\n"
"    min-height: 30px;\n"
"    border-radius: 3px; \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background"
                        ": #f8f8f8;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(38, 162, 105);\n"
"    min-width: 30px;\n"
"    border-radius: 3px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"/* Remove scrollbar arrows */\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width: 0px; height: 0px;\n"
"}\n"
"\n"
"*[class=\"button-normal\"] {\n"
"	font: 10pt \"Inter\";\n"
"	background-color: #e7e7e7;\n"
"	color: black;\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(154, 153, 150);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:hover {\n"
"	background-color: white;\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:disabled {\n"
"    background-color: #bdc3c7;\n"
"    color: #7f8c8d;\n"
"    border: 1px solid #95a5a6;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.tab_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_22 = QWidget(self.tab_1)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(0, 10))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_22)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 0))
        self.formLayout_3 = QFormLayout(self.widget_20)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.widget_20)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(100, 20))
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_48)

        self.cmb_school_year_2 = QComboBox(self.widget_20)
        self.cmb_school_year_2.setObjectName(u"cmb_school_year_2")
        self.cmb_school_year_2.setMinimumSize(QSize(120, 30))
        self.cmb_school_year_2.setMaximumSize(QSize(16777215, 30))
        self.cmb_school_year_2.setStyleSheet(u"")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmb_school_year_2)

        self.label_18 = QLabel(self.widget_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.comboBox_ReportsSection = QComboBox(self.widget_20)
        self.comboBox_ReportsSection.setObjectName(u"comboBox_ReportsSection")
        self.comboBox_ReportsSection.setMinimumSize(QSize(150, 30))
        self.comboBox_ReportsSection.setMaximumSize(QSize(16777215, 30))
        self.comboBox_ReportsSection.setStyleSheet(u"")
        self.comboBox_ReportsSection.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_ReportsSection)


        self.horizontalLayout_36.addWidget(self.widget_20)

        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(0, 50))
        self.widget_23.setStyleSheet(u"#widget_23 {\n"
"	background-color: rgb(192, 191, 188);\n"
"	border-radius: 15px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #c6e9ff);\n"
"}\n"
"\n"
"#widget_ReportsFilter {\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.widget_23)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_50 = QLabel(self.widget_23)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 30))
        self.label_50.setStyleSheet(u"font: 11pt \"Inter SemiBold\";")

        self.verticalLayout_30.addWidget(self.label_50)

        self.widget_ReportsFilter = QWidget(self.widget_23)
        self.widget_ReportsFilter.setObjectName(u"widget_ReportsFilter")
        self.widget_ReportsFilter.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_ReportsFilter)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.widget_ReportsFilter)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_9.addWidget(self.label_45)

        self.comboBox_ReportsGradingPeriod = QComboBox(self.widget_ReportsFilter)
        self.comboBox_ReportsGradingPeriod.setObjectName(u"comboBox_ReportsGradingPeriod")
        self.comboBox_ReportsGradingPeriod.setMinimumSize(QSize(150, 30))
        self.comboBox_ReportsGradingPeriod.setMaximumSize(QSize(16777215, 30))
        self.comboBox_ReportsGradingPeriod.setStyleSheet(u"")
        self.comboBox_ReportsGradingPeriod.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_9.addWidget(self.comboBox_ReportsGradingPeriod)

        self.label_46 = QLabel(self.widget_ReportsFilter)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_9.addWidget(self.label_46)

        self.spin_quiz_no = QSpinBox(self.widget_ReportsFilter)
        self.spin_quiz_no.setObjectName(u"spin_quiz_no")
        self.spin_quiz_no.setMinimumSize(QSize(70, 30))
        self.spin_quiz_no.setMaximumSize(QSize(70, 30))
        self.spin_quiz_no.setStyleSheet(u"")
        self.spin_quiz_no.setAlignment(Qt.AlignCenter)
        self.spin_quiz_no.setMinimum(1)
        self.spin_quiz_no.setMaximum(999)
        self.spin_quiz_no.setValue(1)

        self.horizontalLayout_9.addWidget(self.spin_quiz_no)

        self.label_49 = QLabel(self.widget_ReportsFilter)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_9.addWidget(self.label_49)

        self.comboBox_ReportsLesson = QComboBox(self.widget_ReportsFilter)
        self.comboBox_ReportsLesson.setObjectName(u"comboBox_ReportsLesson")
        self.comboBox_ReportsLesson.setMinimumSize(QSize(200, 30))
        self.comboBox_ReportsLesson.setMaximumSize(QSize(16777215, 30))
        self.comboBox_ReportsLesson.setStyleSheet(u"")
        self.comboBox_ReportsLesson.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_9.addWidget(self.comboBox_ReportsLesson)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_30.addWidget(self.widget_ReportsFilter)


        self.horizontalLayout_36.addWidget(self.widget_23)


        self.verticalLayout_7.addWidget(self.widget_22)

        self.table_quizcompletionstat = QTableView(self.tab_1)
        self.table_quizcompletionstat.setObjectName(u"table_quizcompletionstat")
        self.table_quizcompletionstat.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.table_quizcompletionstat.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_quizcompletionstat.setSortingEnabled(True)

        self.verticalLayout_7.addWidget(self.table_quizcompletionstat)

        self.tabWidget_reports.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"QTableView {\n"
"    border: 1px solid rgb(161, 161, 161);\n"
"    gridline-color: #f0f0f0;\n"
"    background-color: white;\n"
"    selection-background-color: rgba(38, 162, 105, 0.2);\n"
"    selection-color: black;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Remove the row numbers (Vertical Header) */\n"
"QHeaderView:vertical {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    width: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Style the top horizontal header */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: rgb(246, 245, 244);  \n"
"    color: black;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Custom Scrollbars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(38, 162, 105);\n"
"    min-height: 30px;\n"
"    border-radius: 3px; \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background"
                        ": #f8f8f8;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(38, 162, 105);\n"
"    min-width: 30px;\n"
"    border-radius: 3px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"/* Remove scrollbar arrows */\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width: 0px; height: 0px;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.tab_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_10 = QWidget(self.tab_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_20 = QVBoxLayout(self.widget_10)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_stud_tblheader_idv = QWidget(self.widget_10)
        self.widget_stud_tblheader_idv.setObjectName(u"widget_stud_tblheader_idv")
        self.widget_stud_tblheader_idv.setMinimumSize(QSize(0, 44))
        self.widget_stud_tblheader_idv.setStyleSheet(u"#widget_stud_tblheader_idv { \n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #c6e9ff);\n"
"	border: 1px solid rgb(98, 160, 234);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_stud_tblheader_idv)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_52 = QLabel(self.widget_stud_tblheader_idv)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(100, 20))
        self.label_52.setFont(font)
        self.label_52.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_52)

        self.cmb_school_year_3 = QComboBox(self.widget_stud_tblheader_idv)
        self.cmb_school_year_3.setObjectName(u"cmb_school_year_3")
        self.cmb_school_year_3.setMinimumSize(QSize(120, 30))
        self.cmb_school_year_3.setMaximumSize(QSize(16777215, 30))
        self.cmb_school_year_3.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.cmb_school_year_3)

        self.widget_search_6 = QWidget(self.widget_stud_tblheader_idv)
        self.widget_search_6.setObjectName(u"widget_search_6")
        self.widget_search_6.setMinimumSize(QSize(0, 30))
        self.widget_search_6.setMaximumSize(QSize(16777215, 30))
        self.widget_search_6.setStyleSheet(u"*[class=\"widget-search-container\"] {\n"
"	background-color: #FFF;\n"
"	border: 1px solid #999;\n"
"	border-radius: 15px;\n"
"}")
        self.layout_search_5 = QHBoxLayout(self.widget_search_6)
        self.layout_search_5.setSpacing(0)
        self.layout_search_5.setObjectName(u"layout_search_5")
        self.layout_search_5.setContentsMargins(4, 0, 6, 0)
        self.label_magnifying_stud_4 = QLabel(self.widget_search_6)
        self.label_magnifying_stud_4.setObjectName(u"label_magnifying_stud_4")
        self.label_magnifying_stud_4.setMinimumSize(QSize(30, 30))
        self.label_magnifying_stud_4.setMaximumSize(QSize(30, 30))
        self.label_magnifying_stud_4.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.label_magnifying_stud_4.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_stud_4.setScaledContents(True)
        self.label_magnifying_stud_4.setMargin(5)

        self.layout_search_5.addWidget(self.label_magnifying_stud_4)

        self.txt_search_score_idv = QLineEdit(self.widget_search_6)
        self.txt_search_score_idv.setObjectName(u"txt_search_score_idv")
        self.txt_search_score_idv.setMinimumSize(QSize(0, 30))
        self.txt_search_score_idv.setMaximumSize(QSize(16777215, 30))
        self.txt_search_score_idv.setStyleSheet(u"*[class=\"textbox-search\"] {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")

        self.layout_search_5.addWidget(self.txt_search_score_idv)

        self.btnClearSearch_4 = QPushButton(self.widget_search_6)
        self.btnClearSearch_4.setObjectName(u"btnClearSearch_4")
        self.btnClearSearch_4.setMinimumSize(QSize(20, 20))
        self.btnClearSearch_4.setMaximumSize(QSize(20, 20))
        self.btnClearSearch_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClearSearch_4.setStyleSheet(u"*[class=\"button-clear-search\"] {\n"
"	border-radius: 10px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:hover {\n"
"	background-color: #FFC0C0;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:pressed {\n"
"	background-color: #FFD2D2;\n"
"}")
        self.btnClearSearch_4.setIcon(icon13)
        self.btnClearSearch_4.setIconSize(QSize(8, 8))

        self.layout_search_5.addWidget(self.btnClearSearch_4)


        self.horizontalLayout_7.addWidget(self.widget_search_6)


        self.verticalLayout_20.addWidget(self.widget_stud_tblheader_idv)

        self.table_student_score_idv = QTableView(self.widget_10)
        self.table_student_score_idv.setObjectName(u"table_student_score_idv")
        self.table_student_score_idv.setStyleSheet(u"")
        self.table_student_score_idv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_student_score_idv.setSortingEnabled(True)
        self.table_student_score_idv.verticalHeader().setVisible(False)

        self.verticalLayout_20.addWidget(self.table_student_score_idv)


        self.verticalLayout_21.addWidget(self.widget_10)

        self.widget_8 = QWidget(self.tab_2)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_19 = QVBoxLayout(self.widget_8)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_8)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"#widget_7 { \n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #c6e9ff);\n"
"	border: 1px solid rgb(98, 160, 234);\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#label_student_icon {\n"
"	\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 5, -1, 5)
        self.widget_3 = QWidget(self.widget_7)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(34, 34))
        self.widget_3.setMaximumSize(QSize(34, 34))
        self.widget_3.setStyleSheet(u"border-radius: 17px;\n"
"background-color: rgb(98, 160, 234);")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_student_icon = QLabel(self.widget_3)
        self.label_student_icon.setObjectName(u"label_student_icon")
        self.label_student_icon.setMaximumSize(QSize(30, 30))
        self.label_student_icon.setStyleSheet(u"background: transparent;")
        self.label_student_icon.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_student_icon.setScaledContents(True)

        self.horizontalLayout_35.addWidget(self.label_student_icon)


        self.horizontalLayout_21.addWidget(self.widget_3)

        self.label_student_name = QLabel(self.widget_7)
        self.label_student_name.setObjectName(u"label_student_name")
        self.label_student_name.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.label_student_name)

        self.label_avg_icon = QLabel(self.widget_7)
        self.label_avg_icon.setObjectName(u"label_avg_icon")
        self.label_avg_icon.setMaximumSize(QSize(30, 30))
        self.label_avg_icon.setPixmap(QPixmap(u":/Images/Images/trophy.png"))
        self.label_avg_icon.setScaledContents(True)
        self.label_avg_icon.setMargin(2)

        self.horizontalLayout_21.addWidget(self.label_avg_icon)

        self.label_avg = QLabel(self.widget_7)
        self.label_avg.setObjectName(u"label_avg")
        self.label_avg.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.label_avg)

        self.label_average_percentage = QLabel(self.widget_7)
        self.label_average_percentage.setObjectName(u"label_average_percentage")
        self.label_average_percentage.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.label_average_percentage)

        self.label_lessons_prog_icon = QLabel(self.widget_7)
        self.label_lessons_prog_icon.setObjectName(u"label_lessons_prog_icon")
        self.label_lessons_prog_icon.setMaximumSize(QSize(30, 30))
        self.label_lessons_prog_icon.setPixmap(QPixmap(u":/Images/Images/stack-of-books.png"))
        self.label_lessons_prog_icon.setScaledContents(True)
        self.label_lessons_prog_icon.setMargin(2)

        self.horizontalLayout_21.addWidget(self.label_lessons_prog_icon)

        self.label_lessons_prog_1 = QLabel(self.widget_7)
        self.label_lessons_prog_1.setObjectName(u"label_lessons_prog_1")
        self.label_lessons_prog_1.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.label_lessons_prog_1)

        self.label_lessons_prog = QLabel(self.widget_7)
        self.label_lessons_prog.setObjectName(u"label_lessons_prog")
        self.label_lessons_prog.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.label_lessons_prog)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)

        self.labelGradingPeriod_4 = QLabel(self.widget_7)
        self.labelGradingPeriod_4.setObjectName(u"labelGradingPeriod_4")
        self.labelGradingPeriod_4.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.labelGradingPeriod_4)

        self.cb_gp_quiz_idv = QComboBox(self.widget_7)
        self.cb_gp_quiz_idv.setObjectName(u"cb_gp_quiz_idv")
        self.cb_gp_quiz_idv.setMinimumSize(QSize(150, 30))
        self.cb_gp_quiz_idv.setMaximumSize(QSize(16777215, 30))
        self.cb_gp_quiz_idv.setStyleSheet(u"")
        self.cb_gp_quiz_idv.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_21.addWidget(self.cb_gp_quiz_idv)

        self.btnPrintQuizScores = QPushButton(self.widget_7)
        self.btnPrintQuizScores.setObjectName(u"btnPrintQuizScores")
        self.btnPrintQuizScores.setEnabled(False)
        self.btnPrintQuizScores.setMinimumSize(QSize(100, 30))
        self.btnPrintQuizScores.setMaximumSize(QSize(16777215, 30))
        self.btnPrintQuizScores.setFont(font)
        self.btnPrintQuizScores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrintQuizScores.setStyleSheet(u"")
        self.btnPrintQuizScores.setIcon(icon16)

        self.horizontalLayout_21.addWidget(self.btnPrintQuizScores)


        self.verticalLayout_19.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_8)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 70))
        self.widget_9.setStyleSheet(u"#widget_9 { \n"
"	border-left: 1px solid rgb(161, 161, 161);\n"
"	border-right: 1px solid rgb(161, 161, 161);\n"
"	background-color: rgb(246, 245, 244);\n"
"}\n"
"\n"
"#plainTextEdit_remarks {\n"
"	background-color: #FFF;\n"
"	padding: 0px 5px;\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.plainTextEdit_remarks = QPlainTextEdit(self.widget_9)
        self.plainTextEdit_remarks.setObjectName(u"plainTextEdit_remarks")
        self.plainTextEdit_remarks.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_remarks.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_22.addWidget(self.plainTextEdit_remarks)


        self.verticalLayout_18.addWidget(self.widget_9)

        self.table_quiz_score_idv = QTableView(self.widget_6)
        self.table_quiz_score_idv.setObjectName(u"table_quiz_score_idv")
        self.table_quiz_score_idv.setStyleSheet(u"")
        self.table_quiz_score_idv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_quiz_score_idv.setSortingEnabled(True)
        self.table_quiz_score_idv.verticalHeader().setVisible(False)

        self.verticalLayout_18.addWidget(self.table_quiz_score_idv)


        self.verticalLayout_19.addWidget(self.widget_6)


        self.verticalLayout_21.addWidget(self.widget_8)

        self.tabWidget_reports.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_reports.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget_reports)

        self.stackedWidget.addWidget(self.pageReports)
        self.pageUsers = QWidget()
        self.pageUsers.setObjectName(u"pageUsers")
        self.pageUsers.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-right: none;\n"
"}\n"
"\n"
"*[class=\"textbox-search\"] {\n"
"	background-color: rgb(255, 255, 255); \n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	border-left: none;\n"
"}\n"
"\n"
"*[class=\"widget-search-container\"] {\n"
"	background: transparent;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.pageUsers)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_header = QWidget(self.pageUsers)
        self.widget_header.setObjectName(u"widget_header")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_search_7 = QWidget(self.widget_header)
        self.widget_search_7.setObjectName(u"widget_search_7")
        self.widget_search_7.setMinimumSize(QSize(0, 30))
        self.widget_search_7.setMaximumSize(QSize(16777215, 30))
        self.widget_search_7.setStyleSheet(u"*[class=\"widget-search-container\"] {\n"
"	background-color: #FFF;\n"
"	border: 1px solid #999;\n"
"	border-radius: 15px;\n"
"}")
        self.layout_search_6 = QHBoxLayout(self.widget_search_7)
        self.layout_search_6.setSpacing(0)
        self.layout_search_6.setObjectName(u"layout_search_6")
        self.layout_search_6.setContentsMargins(4, 0, 6, 0)
        self.label_magnifying_stud_5 = QLabel(self.widget_search_7)
        self.label_magnifying_stud_5.setObjectName(u"label_magnifying_stud_5")
        self.label_magnifying_stud_5.setMinimumSize(QSize(30, 30))
        self.label_magnifying_stud_5.setMaximumSize(QSize(30, 30))
        self.label_magnifying_stud_5.setStyleSheet(u"*[class=\"label-magnifying-search\"] {\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.label_magnifying_stud_5.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_stud_5.setScaledContents(True)
        self.label_magnifying_stud_5.setMargin(5)

        self.layout_search_6.addWidget(self.label_magnifying_stud_5)

        self.txt_search_user = QLineEdit(self.widget_search_7)
        self.txt_search_user.setObjectName(u"txt_search_user")
        self.txt_search_user.setMinimumSize(QSize(0, 30))
        self.txt_search_user.setMaximumSize(QSize(16777215, 30))
        self.txt_search_user.setStyleSheet(u"*[class=\"textbox-search\"] {\n"
"	border: none;\n"
"	background: transparent;\n"
"}")

        self.layout_search_6.addWidget(self.txt_search_user)

        self.btnClearSearch_5 = QPushButton(self.widget_search_7)
        self.btnClearSearch_5.setObjectName(u"btnClearSearch_5")
        self.btnClearSearch_5.setMinimumSize(QSize(20, 20))
        self.btnClearSearch_5.setMaximumSize(QSize(20, 20))
        self.btnClearSearch_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClearSearch_5.setStyleSheet(u"*[class=\"button-clear-search\"] {\n"
"	border-radius: 10px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:hover {\n"
"	background-color: #FFC0C0;\n"
"}\n"
"\n"
"*[class=\"button-clear-search\"]:pressed {\n"
"	background-color: #FFD2D2;\n"
"}")
        self.btnClearSearch_5.setIcon(icon13)
        self.btnClearSearch_5.setIconSize(QSize(8, 8))

        self.layout_search_6.addWidget(self.btnClearSearch_5)


        self.horizontalLayout_19.addWidget(self.widget_search_7)

        self.btnAddNewUser = QPushButton(self.widget_header)
        self.btnAddNewUser.setObjectName(u"btnAddNewUser")
        self.btnAddNewUser.setEnabled(True)
        self.btnAddNewUser.setMinimumSize(QSize(30, 30))
        self.btnAddNewUser.setMaximumSize(QSize(16777215, 30))
        self.btnAddNewUser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddNewUser.setStyleSheet(u"padding: 0px 10px 0px;")

        self.horizontalLayout_19.addWidget(self.btnAddNewUser)

        self.btnEditUserInfo = QPushButton(self.widget_header)
        self.btnEditUserInfo.setObjectName(u"btnEditUserInfo")
        self.btnEditUserInfo.setEnabled(True)
        self.btnEditUserInfo.setMinimumSize(QSize(30, 30))
        self.btnEditUserInfo.setMaximumSize(QSize(16777215, 30))
        self.btnEditUserInfo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditUserInfo.setStyleSheet(u"QPushButton { padding: 0px 10px 0px; }")

        self.horizontalLayout_19.addWidget(self.btnEditUserInfo)

        self.btnDeleteUser = QPushButton(self.widget_header)
        self.btnDeleteUser.setObjectName(u"btnDeleteUser")
        self.btnDeleteUser.setEnabled(True)
        self.btnDeleteUser.setMinimumSize(QSize(30, 30))
        self.btnDeleteUser.setMaximumSize(QSize(16777215, 30))
        self.btnDeleteUser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDeleteUser.setStyleSheet(u"QPushButton { padding: 0px 10px 0px; }")

        self.horizontalLayout_19.addWidget(self.btnDeleteUser)

        self.btnRefreshUsers = QPushButton(self.widget_header)
        self.btnRefreshUsers.setObjectName(u"btnRefreshUsers")
        self.btnRefreshUsers.setEnabled(True)
        self.btnRefreshUsers.setMinimumSize(QSize(30, 30))
        self.btnRefreshUsers.setMaximumSize(QSize(30, 30))
        self.btnRefreshUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRefreshUsers.setStyleSheet(u"")
        self.btnRefreshUsers.setIcon(icon12)
        self.btnRefreshUsers.setIconSize(QSize(20, 20))

        self.horizontalLayout_19.addWidget(self.btnRefreshUsers)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_12)


        self.verticalLayout_17.addWidget(self.widget_header)

        self.table_users = QTableView(self.pageUsers)
        self.table_users.setObjectName(u"table_users")
        self.table_users.setStyleSheet(u"QTableView {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"    gridline-color: #f0f0f0;\n"
"    background-color: white;\n"
"    selection-background-color: rgba(38, 162, 105, 0.2);\n"
"    selection-color: black;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Remove the row numbers (Vertical Header) */\n"
"QHeaderView:vertical {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    width: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Style the top horizontal header */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: rgb(38, 162, 105);  \n"
"    color: white;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Custom Scrollbars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(38, 162, 105);\n"
"    min-height: 30px;\n"
"    border-radius: 5px; \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar:horizont"
                        "al {\n"
"    border: none;\n"
"    background: #f8f8f8;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(38, 162, 105);\n"
"    min-width: 30px;\n"
"    border-radius: 5px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"/* Remove scrollbar arrows */\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width: 0px; height: 0px;\n"
"}")
        self.table_users.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_users.setSortingEnabled(True)
        self.table_users.verticalHeader().setVisible(False)
        self.table_users.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_17.addWidget(self.table_users)

        self.stackedWidget.addWidget(self.pageUsers)
        self.pageUtilities = QWidget()
        self.pageUtilities.setObjectName(u"pageUtilities")
        self.pageUtilities.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.pageUtilities)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tabWidget_utility = QTabWidget(self.pageUtilities)
        self.tabWidget_utility.setObjectName(u"tabWidget_utility")
        self.tabWidget_utility.setStyleSheet(u"QTableView {\n"
"    border: 1px solid #ff7d87;\n"
"    gridline-color: #f0f0f0;\n"
"    background-color: white;\n"
"    selection-background-color: rgba(255, 125, 135, 0.2); /* Transparent coral highlight */\n"
"    selection-color: black;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Hide the row numbers (Vertical Header) */\n"
"QHeaderView:vertical {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    width: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Style the top horizontal header with the #ff7d87 theme */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: #ff7d87;  \n"
"    color: white;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Hide top-left corner button by matching header color */\n"
"QTableCornerButton::section {\n"
"    background-color: #ff7d87;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Custom Scrollbars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #fdfdfd;\n"
"    width:"
                        " 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #ff7d87;\n"
"    min-height: 30px;\n"
"    border-radius: 3px; \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #e66a74; /* Slightly darker shade for hover effect */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #fdfdfd;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #ff7d87;\n"
"    min-width: 30px;\n"
"    border-radius: 3px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #e66a74;\n"
"}\n"
"\n"
"/* Remove scrollbar arrows and extra space */\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width: 0px; height: 0px;\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"] {\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-r"
                        "adius: 15px; /* Fully rounded pills */\n"
"    padding-left: 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\"; /* Consolidated font settings */\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
"    /* Match the 15px border-radius of the main control */\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    border: none;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white !important;\n"
"    border: 1px solid #999;\n"
"    selection-background-color: #7eb4d7;\n"
"    selection"
                        "-color: #ffffff;\n"
"    outline: 0; /* Removes the ugly dotted focus border */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding-left: 10px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover state for items inside the dropdown */\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox, QDateEdit {\n"
"	font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QSpinBox:focus, QDateEdit:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QSpinBox:hover, QDateEdit:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QSpinBox::up-button, QDateEdit::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 8px;\n"
"    hei"
                        "ght: 8px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::down-button, QDateEdit::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-bottom-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QDateEdit::up-arrow {\n"
"    image: url(:/Images/Images/caret-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow, QDateEdit::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.tab_settings.setStyleSheet(u"#widget_SY_header, #widget_SY_header_2 { \n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #c6e9ff);\n"
"	border: 1px solid rgb(98, 160, 234);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#widget_SY_body_1, #widget_SY_body_2, #widget_SY_body_3 {\n"
"	background-color: #fff;\n"
"	border: 1px solid #999;\n"
"	border-top: none;\n"
"}\n"
"\n"
"#widget_SY_body_2 QDateEdit:disabled {\n"
"	background-color: rgb(192, 191, 188);\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: black;\n"
"    spacing: 8px;\n"
"	padding: 0px 10px;\n"
"	background: transparent;\n"
"	font: 10pt \"Inter Medium\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	border: 1px solid #999;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border-color: #3b82f6;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #3b82f6;\n"
"    background-color: blue;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.tab_settings)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_SY_settings = QWidget(self.tab_settings)
        self.widget_SY_settings.setObjectName(u"widget_SY_settings")
        self.verticalLayout_28 = QVBoxLayout(self.widget_SY_settings)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_SY_header = QWidget(self.widget_SY_settings)
        self.widget_SY_header.setObjectName(u"widget_SY_header")
        self.widget_SY_header.setMinimumSize(QSize(0, 50))
        self.widget_SY_header.setMaximumSize(QSize(16777215, 50))
        self.widget_SY_header.setStyleSheet(u"")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_SY_header)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_10 = QLabel(self.widget_SY_header)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        font12 = QFont()
        font12.setFamilies([u"Inter"])
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        self.label_10.setFont(font12)
        self.label_10.setStyleSheet(u"background: transparent; \n"
"font: 12pt \"Inter\";")

        self.horizontalLayout_30.addWidget(self.label_10)

        self.spinBox_SY_start = QSpinBox(self.widget_SY_header)
        self.spinBox_SY_start.setObjectName(u"spinBox_SY_start")
        self.spinBox_SY_start.setMinimumSize(QSize(80, 30))
        self.spinBox_SY_start.setMaximumSize(QSize(80, 30))
        self.spinBox_SY_start.setStyleSheet(u"")
        self.spinBox_SY_start.setAlignment(Qt.AlignCenter)
        self.spinBox_SY_start.setMinimum(2000)
        self.spinBox_SY_start.setMaximum(3000)

        self.horizontalLayout_30.addWidget(self.spinBox_SY_start)

        self.label_14 = QLabel(self.widget_SY_header)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_30.addWidget(self.label_14)

        self.spinBox_SY_end = QSpinBox(self.widget_SY_header)
        self.spinBox_SY_end.setObjectName(u"spinBox_SY_end")
        self.spinBox_SY_end.setMinimumSize(QSize(80, 30))
        self.spinBox_SY_end.setMaximumSize(QSize(80, 30))
        self.spinBox_SY_end.setStyleSheet(u"")
        self.spinBox_SY_end.setAlignment(Qt.AlignCenter)
        self.spinBox_SY_end.setMinimum(2000)
        self.spinBox_SY_end.setMaximum(3000)

        self.horizontalLayout_30.addWidget(self.spinBox_SY_end)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_23)

        self.btnSaveSettings_SY = QPushButton(self.widget_SY_header)
        self.btnSaveSettings_SY.setObjectName(u"btnSaveSettings_SY")
        self.btnSaveSettings_SY.setMinimumSize(QSize(130, 30))
        self.btnSaveSettings_SY.setMaximumSize(QSize(16777215, 30))
        self.btnSaveSettings_SY.setFont(font9)
        self.btnSaveSettings_SY.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSaveSettings_SY.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #0a5128;\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px 0px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #1ebd5d, \n"
"                                stop:1 #107f3f);\n"
"    color: #FFF;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #2ecc71, \n"
"                                stop:1 #27AE60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #0b572a, \n"
"                                stop:1 #129046); \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #A5D6A7;\n"
"    color: #E8F5E9;\n"
"    opacity: 0.6;\n"
"}")

        self.horizontalLayout_30.addWidget(self.btnSaveSettings_SY)


        self.verticalLayout_28.addWidget(self.widget_SY_header)

        self.widget_SY_body_1 = QWidget(self.widget_SY_settings)
        self.widget_SY_body_1.setObjectName(u"widget_SY_body_1")
        self.widget_SY_body_1.setStyleSheet(u"")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_SY_body_1)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_60 = QLabel(self.widget_SY_body_1)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 30))
        self.label_60.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_31.addWidget(self.label_60)

        self.widget_15 = QWidget(self.widget_SY_body_1)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"#widget_15 {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #999;\n"
"    padding: 4px 14px;\n"
"    font: 10pt \"Inter\";\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"#btn_manual {\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-right: none;\n"
"}\n"
"\n"
"#btn_manual:checked {\n"
"    background-color: #72D582;\n"
"    border: 2px solid #448D50;\n"
"    color: #000;\n"
"}\n"
"\n"
"#btn_auto {\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#btn_auto:checked {\n"
"    background-color: #72D582;\n"
"    border: 2px solid #448D50;\n"
"    color: #000;\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_manual = QPushButton(self.widget_15)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setMinimumSize(QSize(100, 30))
        self.btn_manual.setMaximumSize(QSize(100, 30))
        self.btn_manual.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_manual.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.btn_manual)

        self.btn_auto = QPushButton(self.widget_15)
        self.btn_auto.setObjectName(u"btn_auto")
        self.btn_auto.setMinimumSize(QSize(100, 30))
        self.btn_auto.setMaximumSize(QSize(100, 30))
        self.btn_auto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_auto.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.btn_auto)


        self.horizontalLayout_31.addWidget(self.widget_15)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_24)


        self.verticalLayout_28.addWidget(self.widget_SY_body_1)

        self.widget_SY_body_2 = QWidget(self.widget_SY_settings)
        self.widget_SY_body_2.setObjectName(u"widget_SY_body_2")
        self.gridLayout_3 = QGridLayout(self.widget_SY_body_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.label_31 = QLabel(self.widget_SY_body_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_31, 2, 0, 1, 1)

        self.label_39 = QLabel(self.widget_SY_body_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_40 = QLabel(self.widget_SY_body_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_40, 4, 0, 1, 1)

        self.dateEdit_firstgrading_start = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_firstgrading_start.setObjectName(u"dateEdit_firstgrading_start")
        self.dateEdit_firstgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_firstgrading_start.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_firstgrading_start.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_firstgrading_start, 1, 1, 1, 1)

        self.label_30 = QLabel(self.widget_SY_body_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.label_30, 1, 0, 1, 1)

        self.dateEdit_fourthgrading_end = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_fourthgrading_end.setObjectName(u"dateEdit_fourthgrading_end")
        self.dateEdit_fourthgrading_end.setMinimumSize(QSize(0, 30))
        self.dateEdit_fourthgrading_end.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_fourthgrading_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_fourthgrading_end, 4, 2, 1, 1)

        self.dateEdit_firstgrading_end = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_firstgrading_end.setObjectName(u"dateEdit_firstgrading_end")
        self.dateEdit_firstgrading_end.setMinimumSize(QSize(0, 30))
        self.dateEdit_firstgrading_end.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_firstgrading_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_firstgrading_end, 1, 2, 1, 1)

        self.label_44 = QLabel(self.widget_SY_body_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 11pt \"Inter SemiBold\";")

        self.gridLayout_3.addWidget(self.label_44, 0, 2, 1, 1)

        self.label_42 = QLabel(self.widget_SY_body_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font: 11pt \"Inter SemiBold\";")

        self.gridLayout_3.addWidget(self.label_42, 0, 1, 1, 1)

        self.dateEdit_thirdgrading_start = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_thirdgrading_start.setObjectName(u"dateEdit_thirdgrading_start")
        self.dateEdit_thirdgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_thirdgrading_start.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_thirdgrading_start.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_thirdgrading_start, 3, 1, 1, 1)

        self.dateEdit_secondgrading_end = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_secondgrading_end.setObjectName(u"dateEdit_secondgrading_end")
        self.dateEdit_secondgrading_end.setMinimumSize(QSize(0, 30))
        self.dateEdit_secondgrading_end.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_secondgrading_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_secondgrading_end, 2, 2, 1, 1)

        self.dateEdit_fourthgrading_start = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_fourthgrading_start.setObjectName(u"dateEdit_fourthgrading_start")
        self.dateEdit_fourthgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_fourthgrading_start.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_fourthgrading_start.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_fourthgrading_start, 4, 1, 1, 1)

        self.dateEdit_secondgrading_start = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_secondgrading_start.setObjectName(u"dateEdit_secondgrading_start")
        self.dateEdit_secondgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_secondgrading_start.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_secondgrading_start.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_secondgrading_start, 2, 1, 1, 1)

        self.dateEdit_thirdgrading_end = QDateEdit(self.widget_SY_body_2)
        self.dateEdit_thirdgrading_end.setObjectName(u"dateEdit_thirdgrading_end")
        self.dateEdit_thirdgrading_end.setMinimumSize(QSize(0, 30))
        self.dateEdit_thirdgrading_end.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_thirdgrading_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dateEdit_thirdgrading_end, 3, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 5, 0, 1, 1)


        self.verticalLayout_28.addWidget(self.widget_SY_body_2)


        self.verticalLayout_27.addWidget(self.widget_SY_settings)

        self.widget_SY_settings_2 = QWidget(self.tab_settings)
        self.widget_SY_settings_2.setObjectName(u"widget_SY_settings_2")
        self.widget_SY_settings_2.setStyleSheet(u"")
        self.verticalLayout_29 = QVBoxLayout(self.widget_SY_settings_2)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_SY_header_2 = QWidget(self.widget_SY_settings_2)
        self.widget_SY_header_2.setObjectName(u"widget_SY_header_2")
        self.widget_SY_header_2.setMinimumSize(QSize(0, 50))
        self.widget_SY_header_2.setMaximumSize(QSize(16777215, 50))
        self.widget_SY_header_2.setStyleSheet(u"")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_SY_header_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_29 = QLabel(self.widget_SY_header_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 30))
        self.label_29.setMaximumSize(QSize(16777215, 30))
        self.label_29.setFont(font12)
        self.label_29.setStyleSheet(u"background: transparent; \n"
"font: 12pt \"Inter\";")

        self.horizontalLayout_33.addWidget(self.label_29)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_25)


        self.verticalLayout_29.addWidget(self.widget_SY_header_2)

        self.widget_SY_body_3 = QWidget(self.widget_SY_settings_2)
        self.widget_SY_body_3.setObjectName(u"widget_SY_body_3")
        self.widget_SY_body_3.setStyleSheet(u"")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_SY_body_3)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.btnBrowseLessonsCSV = QPushButton(self.widget_SY_body_3)
        self.btnBrowseLessonsCSV.setObjectName(u"btnBrowseLessonsCSV")
        self.btnBrowseLessonsCSV.setMinimumSize(QSize(100, 30))
        self.btnBrowseLessonsCSV.setMaximumSize(QSize(16777215, 30))
        self.btnBrowseLessonsCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBrowseLessonsCSV.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Inter\";\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #d8ecf6);\n"
"	color: black;\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(154, 153, 150);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #f2f6f8);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #dce5e9, \n"
"                                stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background: #f5f5f5;\n"
"	border: 1px solid #dcdcdc;\n"
"	color: #aeaeae;\n"
"}")

        self.horizontalLayout_34.addWidget(self.btnBrowseLessonsCSV)

        self.label_lesson_CSV_path = QLabel(self.widget_SY_body_3)
        self.label_lesson_CSV_path.setObjectName(u"label_lesson_CSV_path")
        self.label_lesson_CSV_path.setMinimumSize(QSize(100, 30))
        self.label_lesson_CSV_path.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_34.addWidget(self.label_lesson_CSV_path)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_26)

        self.btnImportAllLessons = QPushButton(self.widget_SY_body_3)
        self.btnImportAllLessons.setObjectName(u"btnImportAllLessons")
        self.btnImportAllLessons.setMinimumSize(QSize(130, 30))
        self.btnImportAllLessons.setMaximumSize(QSize(16777215, 30))
        self.btnImportAllLessons.setFont(font9)
        self.btnImportAllLessons.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnImportAllLessons.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #0a5128;\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px 0px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #1ebd5d, \n"
"                                stop:1 #107f3f);\n"
"    color: #FFF;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #2ecc71, \n"
"                                stop:1 #27AE60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #0b572a, \n"
"                                stop:1 #129046); \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #A5D6A7;\n"
"    color: #E8F5E9;\n"
"    opacity: 0.6;\n"
"}")

        self.horizontalLayout_34.addWidget(self.btnImportAllLessons)


        self.verticalLayout_29.addWidget(self.widget_SY_body_3)

        self.tableView_LessonsCSV = QTableView(self.widget_SY_settings_2)
        self.tableView_LessonsCSV.setObjectName(u"tableView_LessonsCSV")

        self.verticalLayout_29.addWidget(self.tableView_LessonsCSV)


        self.verticalLayout_27.addWidget(self.widget_SY_settings_2)

        self.tabWidget_utility.addTab(self.tab_settings, "")
        self.tab_audit_trail = QWidget()
        self.tab_audit_trail.setObjectName(u"tab_audit_trail")
        self.verticalLayout_15 = QVBoxLayout(self.tab_audit_trail)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.table_AuditTrail = QTableView(self.tab_audit_trail)
        self.table_AuditTrail.setObjectName(u"table_AuditTrail")
        self.table_AuditTrail.setAutoFillBackground(False)
        self.table_AuditTrail.setFrameShape(QFrame.StyledPanel)
        self.table_AuditTrail.setFrameShadow(QFrame.Plain)
        self.table_AuditTrail.setLineWidth(1)
        self.table_AuditTrail.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_AuditTrail.setAlternatingRowColors(False)
        self.table_AuditTrail.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_AuditTrail.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_AuditTrail.setSortingEnabled(True)
        self.table_AuditTrail.setWordWrap(True)
        self.table_AuditTrail.horizontalHeader().setCascadingSectionResizes(True)
        self.table_AuditTrail.verticalHeader().setVisible(False)

        self.verticalLayout_15.addWidget(self.table_AuditTrail)

        self.tabWidget_utility.addTab(self.tab_audit_trail, "")
        self.tab_archive = QWidget()
        self.tab_archive.setObjectName(u"tab_archive")
        self.verticalLayout_16 = QVBoxLayout(self.tab_archive)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.table_student_archive = QTableView(self.tab_archive)
        self.table_student_archive.setObjectName(u"table_student_archive")
        self.table_student_archive.setAutoFillBackground(False)
        self.table_student_archive.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_student_archive.setAlternatingRowColors(False)
        self.table_student_archive.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_student_archive.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_student_archive.setSortingEnabled(True)
        self.table_student_archive.setWordWrap(True)
        self.table_student_archive.horizontalHeader().setCascadingSectionResizes(True)
        self.table_student_archive.verticalHeader().setVisible(False)

        self.verticalLayout_16.addWidget(self.table_student_archive)

        self.tabWidget_utility.addTab(self.tab_archive, "")

        self.verticalLayout_14.addWidget(self.tabWidget_utility)

        self.stackedWidget.addWidget(self.pageUtilities)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        Home.setCentralWidget(self.centralwidget)

        self.retranslateUi(Home)

        self.stackedWidget.setCurrentIndex(0)
        self.btnRefreshSY.setDefault(True)
        self.btnClearSearch_1.setDefault(True)
        self.btnClearSearch_2.setDefault(True)
        self.btnClearSearch_3.setDefault(True)
        self.tabWidget_reports.setCurrentIndex(0)
        self.btnClearSearch_4.setDefault(True)
        self.btnClearSearch_5.setDefault(True)
        self.tabWidget_utility.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Computer-Aided Instructions System in Mathematics for the Grade 1 Students of La Camelle School", None))
        self.label_20.setText("")
        self.btnHome.setText(QCoreApplication.translate("Home", u"Home", None))
        self.btnHome.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnStudentList.setText(QCoreApplication.translate("Home", u"Student List", None))
        self.btnStudentList.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnLesson.setText(QCoreApplication.translate("Home", u"Lesson", None))
        self.btnLesson.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnQuiz.setText(QCoreApplication.translate("Home", u"Quiz", None))
        self.btnQuiz.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnExercise.setText(QCoreApplication.translate("Home", u"Exercise", None))
        self.btnExercise.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnSections.setText(QCoreApplication.translate("Home", u"Sections", None))
        self.btnSections.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnReports.setText(QCoreApplication.translate("Home", u"Reports", None))
        self.btnReports.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnUserName.setText(QCoreApplication.translate("Home", u"Christopher", None))
        self.labelPosition.setText(QCoreApplication.translate("Home", u"Admin", None))
        self.btnLogout.setText(QCoreApplication.translate("Home", u"Log out", None))
        self.btnLogout.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnUsers.setText(QCoreApplication.translate("Home", u"Users", None))
        self.btnUsers.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.btnUtility.setText(QCoreApplication.translate("Home", u"Utilities", None))
        self.btnUtility.setProperty(u"class", QCoreApplication.translate("Home", u"button-left-nav", None))
        self.label_timeAP_3.setText(QCoreApplication.translate("Home", u"Welcome to La Camelle School", None))
        self.label_gradingperiod.setText(QCoreApplication.translate("Home", u"Grading", None))
        self.label_SY.setText(QCoreApplication.translate("Home", u"School Year", None))
        self.label_24.setText("")
        self.label_stud.setText(QCoreApplication.translate("Home", u"Students", None))
        self.label_student_total.setText(QCoreApplication.translate("Home", u"0", None))
        self.label_25.setText("")
        self.label_8.setText(QCoreApplication.translate("Home", u"Lessons", None))
        self.label_lessons_total.setText(QCoreApplication.translate("Home", u"0", None))
        self.label_27.setText("")
        self.label_9.setText(QCoreApplication.translate("Home", u"Teachers", None))
        self.label_teachers_total.setText(QCoreApplication.translate("Home", u"0", None))
        self.label_profile.setText("")
        self.label_stud_name.setText(QCoreApplication.translate("Home", u"Juan De La Cruz", None))
        self.label_student_score.setText(QCoreApplication.translate("Home", u"00.00%", None))
        self.label_student_place.setText(QCoreApplication.translate("Home", u"1st", None))
        self.label_profile_2.setText("")
        self.label_stud_name_2.setText(QCoreApplication.translate("Home", u"Annie Batumbakal", None))
        self.label_student_score_2.setText(QCoreApplication.translate("Home", u"00.00%", None))
        self.label_student_place_2.setText(QCoreApplication.translate("Home", u"2nd", None))
        self.label_profile_3.setText("")
        self.label_stud_name_3.setText(QCoreApplication.translate("Home", u"Gian Santos", None))
        self.label_student_score_3.setText(QCoreApplication.translate("Home", u"00.00%", None))
        self.label_student_place_3.setText(QCoreApplication.translate("Home", u"3rd", None))
        self.label_month.setText(QCoreApplication.translate("Home", u"MAR", None))
        self.label_day.setText(QCoreApplication.translate("Home", u"00", None))
        self.label_19.setText("")
        self.label_time.setText(QCoreApplication.translate("Home", u"00:00", None))
        self.label_timeAP.setText(QCoreApplication.translate("Home", u"AM", None))
        self.label_32.setText(QCoreApplication.translate("Home", u"School Year:", None))
        self.cmb_school_year.setPlaceholderText("")
        self.cmb_school_year.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
#if QT_CONFIG(tooltip)
        self.btnRefreshSY.setToolTip(QCoreApplication.translate("Home", u"Refresh the school year", None))
#endif // QT_CONFIG(tooltip)
        self.btnRefreshSY.setText("")
        self.btnRefreshSY.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.cmb_studSection.setPlaceholderText(QCoreApplication.translate("Home", u"Select Section", None))
        self.cmb_studSection.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.widget_search_2.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_stud.setText("")
        self.label_magnifying_stud.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txt_classList_search.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txt_classList_search.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
#if QT_CONFIG(tooltip)
        self.btnClearSearch_1.setToolTip(QCoreApplication.translate("Home", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearSearch_1.setText("")
        self.btnClearSearch_1.setProperty(u"class", QCoreApplication.translate("Home", u"button-clear-search", None))
        self.label_47.setText(QCoreApplication.translate("Home", u"Showing:", None))
        self.label_totalStudCount.setText(QCoreApplication.translate("Home", u"0 Student", None))
        self.label_totalStudCount.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.btnAddStudent.setText(QCoreApplication.translate("Home", u" Add/Import", None))
        self.btnAddStudent.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnDeleteStudent.setText(QCoreApplication.translate("Home", u" Delete", None))
        self.btnDeleteStudent.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnPrintStudentList.setText(QCoreApplication.translate("Home", u" Print", None))
        self.btnPrintStudentList.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.label_16.setText(QCoreApplication.translate("Home", u"Section Information", None))
        self.label_33.setText(QCoreApplication.translate("Home", u"No. of students:", None))
        self.label_33.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_34.setText(QCoreApplication.translate("Home", u"Boys:", None))
        self.label_34.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_28.setText(QCoreApplication.translate("Home", u"Girls:", None))
        self.label_28.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_studentCount.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_girlCount.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_boyCount.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_35.setText(QCoreApplication.translate("Home", u"Section:", None))
        self.label_35.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_section.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_17.setText(QCoreApplication.translate("Home", u"Student Information", None))
        self.label_43.setText(QCoreApplication.translate("Home", u"ID:", None))
        self.label_43.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_studentId.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_36.setText(QCoreApplication.translate("Home", u"Last name:", None))
        self.label_36.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_studentLastName.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_38.setText(QCoreApplication.translate("Home", u"First name:", None))
        self.label_38.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_studentFirstName.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_41.setText(QCoreApplication.translate("Home", u"Middle name:", None))
        self.label_41.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_studentMiddleName.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_37.setText(QCoreApplication.translate("Home", u"Gender:", None))
        self.label_37.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_studentGender.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_51.setText(QCoreApplication.translate("Home", u"Emergency Contact", None))
        self.label_59.setText(QCoreApplication.translate("Home", u"Name:", None))
        self.label_59.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_56.setText(QCoreApplication.translate("Home", u"Mobile:", None))
        self.label_56.setProperty(u"class", QCoreApplication.translate("Home", u"label-faded", None))
        self.label_contact_person.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_contact_number.setText(QCoreApplication.translate("Home", u"null", None))
        self.btnEditStudent.setText(QCoreApplication.translate("Home", u" Edit", None))
        self.btnEditStudent.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.widget_search_4.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_stud_2.setText("")
        self.label_magnifying_stud_2.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txtSearchLesson.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txtSearchLesson.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
#if QT_CONFIG(tooltip)
        self.btnClearSearch_2.setToolTip(QCoreApplication.translate("Home", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearSearch_2.setText("")
        self.btnClearSearch_2.setProperty(u"class", QCoreApplication.translate("Home", u"button-clear-search", None))
        self.btnAnimation.setText(QCoreApplication.translate("Home", u"Animation", None))
        self.btnAnimation.setProperty(u"class", "")
        self.btnPowerPoint.setText(QCoreApplication.translate("Home", u"MS PowerPoint", None))
        self.btnPowerPoint.setProperty(u"class", "")
#if QT_CONFIG(tooltip)
        self.btnRefreshLessonTable.setToolTip(QCoreApplication.translate("Home", u"Refresh table", None))
#endif // QT_CONFIG(tooltip)
        self.btnRefreshLessonTable.setText("")
        self.btnRefreshLessonTable.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnLessonView.setText(QCoreApplication.translate("Home", u" View", None))
        self.btnLessonView.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnLessonEdit.setText(QCoreApplication.translate("Home", u" Edit", None))
        self.btnLessonEdit.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnLessonAdd.setText(QCoreApplication.translate("Home", u" Add", None))
        self.btnLessonAdd.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.label_lessonTotalCount.setText(QCoreApplication.translate("Home", u"0 item", None))
        self.labelGradingPeriod_2.setText(QCoreApplication.translate("Home", u"Quiz #:", None))
        self.labelGradingPeriod.setText(QCoreApplication.translate("Home", u"Grading Period:", None))
        self.cbGradingPeriod.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.labelLesson.setText(QCoreApplication.translate("Home", u"Lesson Title:", None))
        self.cbLessonName.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.checkBoxPublish.setText(QCoreApplication.translate("Home", u"Publish", None))
        self.label_7.setText(QCoreApplication.translate("Home", u"Total Score:", None))
        self.label_totalScore.setText(QCoreApplication.translate("Home", u"000", None))
        self.label_6.setText(QCoreApplication.translate("Home", u"Diffuculty:", None))
        self.btnEasy.setText(QCoreApplication.translate("Home", u"Easy", None))
        self.btnAverage.setText(QCoreApplication.translate("Home", u"Average", None))
        self.btnHard.setText(QCoreApplication.translate("Home", u"Hard", None))
        self.label_21.setText(QCoreApplication.translate("Home", u"Points:", None))
        self.label_15.setText(QCoreApplication.translate("Home", u"Easy", None))
        self.multiplier_easy.setText(QCoreApplication.translate("Home", u"00", None))
        self.label_22.setText(QCoreApplication.translate("Home", u"Average", None))
        self.multiplier_average.setText(QCoreApplication.translate("Home", u"00", None))
        self.label_23.setText(QCoreApplication.translate("Home", u"Hard", None))
        self.multiplier_hard.setText(QCoreApplication.translate("Home", u"00", None))
        self.label_3.setText(QCoreApplication.translate("Home", u"Score:", None))
        self.label_scoreperlevel.setText(QCoreApplication.translate("Home", u"000", None))
        self.label_13.setText(QCoreApplication.translate("Home", u"True or False", None))
        self.label_11.setText(QCoreApplication.translate("Home", u"Identification", None))
        self.label_12.setText(QCoreApplication.translate("Home", u"Multiple Choice", None))
        self.btnQuizAdd.setText(QCoreApplication.translate("Home", u"Add or Edit", None))
        self.btnQuizAdd.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.widget_search_5.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_stud_3.setText("")
        self.label_magnifying_stud_3.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txtSearchExercise.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txtSearchExercise.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
#if QT_CONFIG(tooltip)
        self.btnClearSearch_3.setToolTip(QCoreApplication.translate("Home", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearSearch_3.setText("")
        self.btnClearSearch_3.setProperty(u"class", QCoreApplication.translate("Home", u"button-clear-search", None))
        self.btnExerciseEdit.setText(QCoreApplication.translate("Home", u"Edit", None))
        self.btnExerciseEdit.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnExerciseAdd.setText(QCoreApplication.translate("Home", u"Add", None))
        self.btnExerciseAdd.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.label_4.setText(QCoreApplication.translate("Home", u"Section:", None))
        self.comboBox_Section.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.btnSectionAdd.setText(QCoreApplication.translate("Home", u"Add new section", None))
        self.btnSectionAdd.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnSectionDelete.setText(QCoreApplication.translate("Home", u"Delete this section", None))
        self.btnSectionDelete.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnSectionEdit.setText(QCoreApplication.translate("Home", u"Edit", None))
        self.btnSectionEdit.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.label_5.setText(QCoreApplication.translate("Home", u"Adviser:", None))
        self.label_Adviser.setText("")
        self.label_48.setText(QCoreApplication.translate("Home", u"School Year:", None))
        self.cmb_school_year_2.setPlaceholderText("")
        self.cmb_school_year_2.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.label_18.setText(QCoreApplication.translate("Home", u"Section:", None))
        self.comboBox_ReportsSection.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.label_50.setText(QCoreApplication.translate("Home", u"Quiz Selector", None))
        self.label_45.setText(QCoreApplication.translate("Home", u"Grading Period:", None))
        self.comboBox_ReportsGradingPeriod.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.label_46.setText(QCoreApplication.translate("Home", u"Quiz No:", None))
        self.label_49.setText(QCoreApplication.translate("Home", u"Lesson:", None))
        self.comboBox_ReportsLesson.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.tabWidget_reports.setTabText(self.tabWidget_reports.indexOf(self.tab_1), QCoreApplication.translate("Home", u"Quiz Tracker", None))
        self.label_52.setText(QCoreApplication.translate("Home", u"School Year:", None))
        self.cmb_school_year_3.setPlaceholderText("")
        self.cmb_school_year_3.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.widget_search_6.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_stud_4.setText("")
        self.label_magnifying_stud_4.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txt_search_score_idv.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txt_search_score_idv.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
#if QT_CONFIG(tooltip)
        self.btnClearSearch_4.setToolTip(QCoreApplication.translate("Home", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearSearch_4.setText("")
        self.btnClearSearch_4.setProperty(u"class", QCoreApplication.translate("Home", u"button-clear-search", None))
        self.label_student_icon.setText("")
        self.label_student_name.setText(QCoreApplication.translate("Home", u"Student Name", None))
        self.label_avg_icon.setText("")
        self.label_avg.setText(QCoreApplication.translate("Home", u"Average:", None))
        self.label_average_percentage.setText(QCoreApplication.translate("Home", u"85%", None))
        self.label_lessons_prog_icon.setText("")
        self.label_lessons_prog_1.setText(QCoreApplication.translate("Home", u"Lessons:", None))
        self.label_lessons_prog.setText(QCoreApplication.translate("Home", u"12/20", None))
        self.labelGradingPeriod_4.setText(QCoreApplication.translate("Home", u"Grading Period:", None))
        self.cb_gp_quiz_idv.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.btnPrintQuizScores.setText(QCoreApplication.translate("Home", u" Print", None))
        self.btnPrintQuizScores.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.plainTextEdit_remarks.setPlaceholderText(QCoreApplication.translate("Home", u"Write teacher's remarks/comments here.", None))
        self.tabWidget_reports.setTabText(self.tabWidget_reports.indexOf(self.tab_2), QCoreApplication.translate("Home", u"Raw scores (Individual)", None))
        self.tabWidget_reports.setTabText(self.tabWidget_reports.indexOf(self.tab_3), QCoreApplication.translate("Home", u"Raw score (All)", None))
        self.widget_search_7.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_stud_5.setText("")
        self.label_magnifying_stud_5.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txt_search_user.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txt_search_user.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
#if QT_CONFIG(tooltip)
        self.btnClearSearch_5.setToolTip(QCoreApplication.translate("Home", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearSearch_5.setText("")
        self.btnClearSearch_5.setProperty(u"class", QCoreApplication.translate("Home", u"button-clear-search", None))
        self.btnAddNewUser.setText(QCoreApplication.translate("Home", u"Add New User", None))
        self.btnAddNewUser.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnEditUserInfo.setText(QCoreApplication.translate("Home", u"Edit User Information", None))
        self.btnEditUserInfo.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnDeleteUser.setText(QCoreApplication.translate("Home", u"Delete User", None))
        self.btnDeleteUser.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
#if QT_CONFIG(tooltip)
        self.btnRefreshUsers.setToolTip(QCoreApplication.translate("Home", u"Refresh the table", None))
#endif // QT_CONFIG(tooltip)
        self.btnRefreshUsers.setText("")
        self.btnRefreshUsers.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.label_10.setText(QCoreApplication.translate("Home", u"School Year", None))
        self.label_14.setText(QCoreApplication.translate("Home", u"-", None))
        self.btnSaveSettings_SY.setText(QCoreApplication.translate("Home", u"Save", None))
        self.label_60.setText(QCoreApplication.translate("Home", u"Set the dates for each grading period:", None))
        self.btn_manual.setText(QCoreApplication.translate("Home", u"Manual", None))
        self.btn_auto.setText(QCoreApplication.translate("Home", u"Automated", None))
        self.label_31.setText(QCoreApplication.translate("Home", u"Second:", None))
        self.label_39.setText(QCoreApplication.translate("Home", u"Third:", None))
        self.label_40.setText(QCoreApplication.translate("Home", u"Fourth:", None))
        self.dateEdit_firstgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.label_30.setText(QCoreApplication.translate("Home", u"First:", None))
        self.dateEdit_fourthgrading_end.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.dateEdit_firstgrading_end.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.label_44.setText(QCoreApplication.translate("Home", u"End", None))
        self.label_42.setText(QCoreApplication.translate("Home", u"Start", None))
        self.dateEdit_thirdgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.dateEdit_secondgrading_end.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.dateEdit_fourthgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.dateEdit_secondgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.dateEdit_thirdgrading_end.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy / MM / dd", None))
        self.label_29.setText(QCoreApplication.translate("Home", u"Import All Predefined Lessons", None))
        self.btnBrowseLessonsCSV.setText(QCoreApplication.translate("Home", u"Browse", None))
        self.label_lesson_CSV_path.setText("")
        self.btnImportAllLessons.setText(QCoreApplication.translate("Home", u"Import", None))
        self.tabWidget_utility.setTabText(self.tabWidget_utility.indexOf(self.tab_settings), QCoreApplication.translate("Home", u"Settings", None))
        self.tabWidget_utility.setTabText(self.tabWidget_utility.indexOf(self.tab_audit_trail), QCoreApplication.translate("Home", u"Audit Trail", None))
        self.tabWidget_utility.setTabText(self.tabWidget_utility.indexOf(self.tab_archive), QCoreApplication.translate("Home", u"Archive", None))
    # retranslateUi

