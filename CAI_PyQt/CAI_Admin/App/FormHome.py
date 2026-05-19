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
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
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
"	background-color: rgb(222, 221, 218); \n"
"	margin: 0px;\n"
"	font: 10pt \"Inter\"; \n"
"	color: black;\n"
"}\n"
"\n"
"#grp_SectionInfo QLabel, \n"
"#frame_student_info QLabel, \n"
"#frame_contact_info QLabel {\n"
"	font: 11pt \"Inter\"; \n"
"}\n"
"\n"
"*[class=\"button-green\"] {\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px 0px;\n"
"    background: #129046;\n"
"    color: #FFF;\n"
"	font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"*[class=\"button-green\"]:hover {\n"
"    background: #27AE60;\n"
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
"}\n"
"\n"
"*[class=\"label-magnifying-search\"] {\n"
"	background-color: rgb(255, 255, 2"
                        "55);\n"
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
"QComboBox[class=\"combobox-main\"] {\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px; /* Fully rounded pills */\n"
"    padding-left: 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter\"; /* Consolidated font settings */\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"]:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"]:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"]:"
                        ":drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
"    /* Match the 15px border-radius of the main control */\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"]::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    border: none;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #999;\n"
"    border-radius: 8px;\n"
"    selection-background-color: #7eb4d7;\n"
"    selection-color: #ffffff;\n"
"    outline: 0; /* Removes the ugly dotted focus border */\n"
"}\n"
"\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView::item {\n"
"    min-height: 35px; /* Requires QStyledItemDelegate() in Python */\n"
"    padding-left: 10px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover "
                        "state for items inside the dropdown */\n"
"QComboBox[class=\"combobox-main\"] QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font-size: 12px;\n"
"    selection-background-color: #7eb4d7;\n"
"	font: 10pt \"Inter\";\n"
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
"    bo"
                        "rder-bottom-right-radius: 15px;\n"
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
"}\n"
"\n"
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
""
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
"    backgr"
                        "ound: none;\n"
"}\n"
"\n"
"/* 6. THE CORNER WIDGET \n"
"   (The small square where both bars meet) */\n"
"QScrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"#widget_SY_header, #widget_GP_header { \n"
"	background-color: rgb(224, 243, 255);\n"
"	border: 1px solid rgb(98, 160, 234);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#widget_SY_body, #widget_GP_body {\n"
"	background-color: #fff;\n"
"	border: 1px solid #999;\n"
"	border-top: none;\n"
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
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.navigationBar = QGroupBox(self.centralwidget)
        self.navigationBar.setObjectName(u"navigationBar")
        self.navigationBar.setMaximumSize(QSize(200, 16777215))
        self.navigationBar.setFont(font)
        self.navigationBar.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.verticalLayout_5 = QVBoxLayout(self.navigationBar)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.navigationBar)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_20 = QLabel(self.widget_3)
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

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.btnHome = QPushButton(self.navigationBar)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(200, 30))
        self.btnHome.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Inter Medium"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btnHome.setFont(font1)
        self.btnHome.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnHome.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"/* This is the highlight state */\n"
"QPushButton:checked {\n"
"	background-color: #5d5d5d; /* Highlight color */\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF; /* Active accent line */\n"
"}\n"
"QPushButton:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/House-01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon1)
        self.btnHome.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnHome)

        self.btnStudentList = QPushButton(self.navigationBar)
        self.btnStudentList.setObjectName(u"btnStudentList")
        self.btnStudentList.setMinimumSize(QSize(200, 30))
        self.btnStudentList.setMaximumSize(QSize(16777215, 30))
        self.btnStudentList.setFont(font1)
        self.btnStudentList.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnStudentList.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"/* This is the highlight state */\n"
"QPushButton:checked {\n"
"	background-color: #5d5d5d; /* Highlight color */\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF; /* Active accent line */\n"
"}\n"
"QPushButton:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Images/Images/list-color.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStudentList.setIcon(icon2)
        self.btnStudentList.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnStudentList)

        self.btnLesson = QPushButton(self.navigationBar)
        self.btnLesson.setObjectName(u"btnLesson")
        self.btnLesson.setMinimumSize(QSize(200, 30))
        self.btnLesson.setMaximumSize(QSize(16777215, 30))
        self.btnLesson.setFont(font1)
        self.btnLesson.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLesson.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"/* This is the highlight state */\n"
"QPushButton:checked {\n"
"	background-color: #5d5d5d; /* Highlight color */\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF; /* Active accent line */\n"
"}\n"
"QPushButton:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Images/Images/books-28.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLesson.setIcon(icon3)
        self.btnLesson.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnLesson)

        self.btnQuiz = QPushButton(self.navigationBar)
        self.btnQuiz.setObjectName(u"btnQuiz")
        self.btnQuiz.setMinimumSize(QSize(200, 30))
        self.btnQuiz.setMaximumSize(QSize(16777215, 30))
        self.btnQuiz.setFont(font1)
        self.btnQuiz.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnQuiz.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"/* This is the highlight state */\n"
"QPushButton:checked {\n"
"	background-color: #5d5d5d; /* Highlight color */\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF; /* Active accent line */\n"
"}\n"
"QPushButton:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Images/Images/05-bulb.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnQuiz.setIcon(icon4)
        self.btnQuiz.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnQuiz)

        self.btnExercise = QPushButton(self.navigationBar)
        self.btnExercise.setObjectName(u"btnExercise")
        self.btnExercise.setMinimumSize(QSize(200, 30))
        self.btnExercise.setMaximumSize(QSize(16777215, 30))
        self.btnExercise.setFont(font1)
        self.btnExercise.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExercise.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"/* This is the highlight state */\n"
"QPushButton:checked {\n"
"	background-color: #5d5d5d; /* Highlight color */\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF; /* Active accent line */\n"
"}\n"
"QPushButton:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Images/Images/dumbell.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExercise.setIcon(icon5)
        self.btnExercise.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnExercise)

        self.btnSections = QPushButton(self.navigationBar)
        self.btnSections.setObjectName(u"btnSections")
        self.btnSections.setMinimumSize(QSize(200, 30))
        self.btnSections.setMaximumSize(QSize(16777215, 30))
        self.btnSections.setFont(font1)
        self.btnSections.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSections.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"/* This is the highlight state */\n"
"QPushButton:checked {\n"
"	background-color: #5d5d5d; /* Highlight color */\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF; /* Active accent line */\n"
"}\n"
"QPushButton:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Images/Images/library-90.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSections.setIcon(icon6)
        self.btnSections.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnSections)

        self.btnReports = QPushButton(self.navigationBar)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setMinimumSize(QSize(200, 30))
        self.btnReports.setMaximumSize(QSize(16777215, 30))
        self.btnReports.setFont(font1)
        self.btnReports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnReports.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}\n"
"/* This is the highlight state */\n"
"QPushButton:checked {\n"
"	background-color: #5d5d5d; /* Highlight color */\n"
"	color: white;\n"
"	border-left: 5px solid #FF00FF; /* Active accent line */\n"
"}\n"
"QPushButton:hover:!checked {\n"
"	background-color: #5d5d5d;\n"
"}")
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
        self.btnLogout.setMinimumSize(QSize(200, 30))
        self.btnLogout.setMaximumSize(QSize(16777215, 30))
        self.btnLogout.setFont(font1)
        self.btnLogout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogout.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"    padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}")
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
        self.btnUsers.setMinimumSize(QSize(200, 30))
        self.btnUsers.setMaximumSize(QSize(16777215, 30))
        self.btnUsers.setFont(font1)
        self.btnUsers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUsers.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"    padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Images/Images/users-61.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUsers.setIcon(icon10)
        self.btnUsers.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btnUsers)

        self.btnUtility = QPushButton(self.navigationBar)
        self.btnUtility.setObjectName(u"btnUtility")
        self.btnUtility.setMinimumSize(QSize(200, 30))
        self.btnUtility.setMaximumSize(QSize(16777215, 30))
        self.btnUtility.setFont(font1)
        self.btnUtility.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnUtility.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	background: transparent;\n"
"	color: white;\n"
"	text-align: left;\n"
"    padding: 0px 0px 0px 10px;\n"
"	font: 57 10pt \"Inter Medium\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	background: #5d5d5d;\n"
"}")
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
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.widget_5.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_timeAP_3 = QLabel(self.widget_5)
        self.label_timeAP_3.setObjectName(u"label_timeAP_3")
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

        self.label_SY = QLabel(self.widget_5)
        self.label_SY.setObjectName(u"label_SY")
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
"	background-color: #e4f8ed;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#widget_14 {\n"
"	background: transparent;\n"
"	border-left: 2px solid rgb(153, 193, 241);\n"
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
"	background-color: #f8d9fd;\n"
"	border-radius: 20px;\n"
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
"	color: rgb(36, 31, 49); \n"
"	font: 20pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"#widget_16 {\n"
"	border-left: 2px solid rgb(218, 117, 215);\n"
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
"	background-color: #ffeed9;\n"
"	border-radius: 20px;\n"
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
"	color: rgb(119, 118, 123);\n"
"	background: transparent; \n"
"}\n"
"\n"
"#widget_18 {\n"
"	border-left: 2px solid rgb(255, 190, 111);\n"
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
        self.label_month.setGeometry(QRect(80, 10, 50, 34))
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
        self.pageClassList.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.pageClassList)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.InformationPanel = QWidget(self.pageClassList)
        self.InformationPanel.setObjectName(u"InformationPanel")
        self.InformationPanel.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.InformationPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.InformationPanel)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"background-color: transparent; color: rgb(253, 64, 115); font: 57 14pt \"Inter Medium\";")

        self.verticalLayout_3.addWidget(self.label_16)

        self.line_6 = QFrame(self.InformationPanel)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.grp_SectionInfo = QFrame(self.InformationPanel)
        self.grp_SectionInfo.setObjectName(u"grp_SectionInfo")
        self.grp_SectionInfo.setMaximumSize(QSize(16777215, 130))
        self.grp_SectionInfo.setFont(font)
        self.grp_SectionInfo.setStyleSheet(u"")
        self.formLayout_2 = QFormLayout(self.grp_SectionInfo)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_33 = QLabel(self.grp_SectionInfo)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        font9 = QFont()
        font9.setFamilies([u"Inter"])
        font9.setPointSize(11)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_33.setFont(font9)
        self.label_33.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.label_34 = QLabel(self.grp_SectionInfo)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setFont(font9)
        self.label_34.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_34)

        self.label_28 = QLabel(self.grp_SectionInfo)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 20))
        self.label_28.setFont(font9)
        self.label_28.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.label_studentCount = QLabel(self.grp_SectionInfo)
        self.label_studentCount.setObjectName(u"label_studentCount")
        self.label_studentCount.setMaximumSize(QSize(16777215, 20))
        self.label_studentCount.setFont(font9)
        self.label_studentCount.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_studentCount)

        self.label_girlCount = QLabel(self.grp_SectionInfo)
        self.label_girlCount.setObjectName(u"label_girlCount")
        self.label_girlCount.setMaximumSize(QSize(16777215, 20))
        self.label_girlCount.setFont(font9)
        self.label_girlCount.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_girlCount)

        self.label_boyCount = QLabel(self.grp_SectionInfo)
        self.label_boyCount.setObjectName(u"label_boyCount")
        self.label_boyCount.setMaximumSize(QSize(16777215, 20))
        self.label_boyCount.setFont(font9)
        self.label_boyCount.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_boyCount)

        self.label_35 = QLabel(self.grp_SectionInfo)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 20))
        self.label_35.setFont(font9)
        self.label_35.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_35)

        self.label_section = QLabel(self.grp_SectionInfo)
        self.label_section.setObjectName(u"label_section")
        self.label_section.setMaximumSize(QSize(16777215, 20))
        self.label_section.setFont(font9)
        self.label_section.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_section)


        self.verticalLayout_3.addWidget(self.grp_SectionInfo)

        self.label_17 = QLabel(self.InformationPanel)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"background-color: transparent; color: rgb(253, 64, 115); font: 57 14pt \"Inter Medium\";")

        self.verticalLayout_3.addWidget(self.label_17)

        self.line_5 = QFrame(self.InformationPanel)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.frame_student_info = QFrame(self.InformationPanel)
        self.frame_student_info.setObjectName(u"frame_student_info")
        self.frame_student_info.setFont(font)
        self.frame_student_info.setStyleSheet(u"")
        self.formLayout_3 = QFormLayout(self.frame_student_info)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_43 = QLabel(self.frame_student_info)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(95, 20))
        self.label_43.setFont(font9)
        self.label_43.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_43)

        self.label_studentId = QLabel(self.frame_student_info)
        self.label_studentId.setObjectName(u"label_studentId")
        self.label_studentId.setMaximumSize(QSize(16777215, 20))
        self.label_studentId.setFont(font9)
        self.label_studentId.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_studentId)

        self.label_36 = QLabel(self.frame_student_info)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(95, 20))
        self.label_36.setFont(font9)
        self.label_36.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_36)

        self.label_studentLastName = QLabel(self.frame_student_info)
        self.label_studentLastName.setObjectName(u"label_studentLastName")
        self.label_studentLastName.setMaximumSize(QSize(16777215, 20))
        self.label_studentLastName.setFont(font9)
        self.label_studentLastName.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_studentLastName)

        self.label_38 = QLabel(self.frame_student_info)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(95, 20))
        self.label_38.setFont(font9)
        self.label_38.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_38)

        self.label_studentFirstName = QLabel(self.frame_student_info)
        self.label_studentFirstName.setObjectName(u"label_studentFirstName")
        self.label_studentFirstName.setMaximumSize(QSize(16777215, 20))
        self.label_studentFirstName.setFont(font9)
        self.label_studentFirstName.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_studentFirstName)

        self.label_41 = QLabel(self.frame_student_info)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(95, 20))
        self.label_41.setFont(font9)
        self.label_41.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_41)

        self.label_studentMiddleName = QLabel(self.frame_student_info)
        self.label_studentMiddleName.setObjectName(u"label_studentMiddleName")
        self.label_studentMiddleName.setMaximumSize(QSize(16777215, 20))
        self.label_studentMiddleName.setFont(font9)
        self.label_studentMiddleName.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.label_studentMiddleName)

        self.label_37 = QLabel(self.frame_student_info)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(95, 20))
        self.label_37.setFont(font9)
        self.label_37.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_3.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_37)

        self.label_studentGender = QLabel(self.frame_student_info)
        self.label_studentGender.setObjectName(u"label_studentGender")
        self.label_studentGender.setMaximumSize(QSize(16777215, 20))
        self.label_studentGender.setFont(font9)
        self.label_studentGender.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.label_studentGender)


        self.verticalLayout_3.addWidget(self.frame_student_info)

        self.label_51 = QLabel(self.InformationPanel)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 30))
        self.label_51.setMaximumSize(QSize(16777215, 20))
        self.label_51.setFont(font8)
        self.label_51.setStyleSheet(u"background-color: transparent; color: rgb(253, 64, 115); font: 57 14pt \"Inter Medium\";")

        self.verticalLayout_3.addWidget(self.label_51)

        self.line_4 = QFrame(self.InformationPanel)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.frame_contact_info = QFrame(self.InformationPanel)
        self.frame_contact_info.setObjectName(u"frame_contact_info")
        self.frame_contact_info.setFont(font)
        self.frame_contact_info.setStyleSheet(u"")
        self.formLayout_4 = QFormLayout(self.frame_contact_info)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_59 = QLabel(self.frame_contact_info)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font9)
        self.label_59.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_59)

        self.label_56 = QLabel(self.frame_contact_info)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font9)
        self.label_56.setStyleSheet(u"color: rgb(124, 124, 124); background-color: transparent;")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_56)

        self.label_contact_person = QLabel(self.frame_contact_info)
        self.label_contact_person.setObjectName(u"label_contact_person")
        self.label_contact_person.setMaximumSize(QSize(16777215, 20))
        self.label_contact_person.setFont(font9)
        self.label_contact_person.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_contact_person)

        self.label_contact_number = QLabel(self.frame_contact_info)
        self.label_contact_number.setObjectName(u"label_contact_number")
        self.label_contact_number.setMaximumSize(QSize(16777215, 20))
        self.label_contact_number.setFont(font9)
        self.label_contact_number.setStyleSheet(u"color: rgb(18, 18, 18); background-color: transparent;")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_contact_number)


        self.verticalLayout_3.addWidget(self.frame_contact_info)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.widget_2 = QWidget(self.InformationPanel)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_22 = QVBoxLayout(self.widget_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btnAddStudent = QPushButton(self.widget_2)
        self.btnAddStudent.setObjectName(u"btnAddStudent")
        self.btnAddStudent.setMinimumSize(QSize(130, 30))
        self.btnAddStudent.setMaximumSize(QSize(16777215, 30))
        self.btnAddStudent.setFont(font)
        self.btnAddStudent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAddStudent.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/Images/Images/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAddStudent.setIcon(icon12)

        self.verticalLayout_22.addWidget(self.btnAddStudent)

        self.btnEditStudent = QPushButton(self.widget_2)
        self.btnEditStudent.setObjectName(u"btnEditStudent")
        self.btnEditStudent.setMinimumSize(QSize(130, 30))
        self.btnEditStudent.setMaximumSize(QSize(16777215, 30))
        self.btnEditStudent.setFont(font)
        self.btnEditStudent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEditStudent.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/Images/Images/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEditStudent.setIcon(icon13)

        self.verticalLayout_22.addWidget(self.btnEditStudent)

        self.btnDeleteStudent = QPushButton(self.widget_2)
        self.btnDeleteStudent.setObjectName(u"btnDeleteStudent")
        self.btnDeleteStudent.setMinimumSize(QSize(140, 30))
        self.btnDeleteStudent.setMaximumSize(QSize(16777215, 30))
        self.btnDeleteStudent.setFont(font)
        self.btnDeleteStudent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnDeleteStudent.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/Images/Images/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDeleteStudent.setIcon(icon14)

        self.verticalLayout_22.addWidget(self.btnDeleteStudent)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout_15.addWidget(self.InformationPanel)

        self.line_8 = QFrame(self.pageClassList)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_8)

        self.widget_table_stud = QWidget(self.pageClassList)
        self.widget_table_stud.setObjectName(u"widget_table_stud")
        self.widget_table_stud.setMinimumSize(QSize(494, 0))
        self.verticalLayout_6 = QVBoxLayout(self.widget_table_stud)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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

        self.spinBox_SY1 = QSpinBox(self.widget_h)
        self.spinBox_SY1.setObjectName(u"spinBox_SY1")
        self.spinBox_SY1.setMinimumSize(QSize(0, 30))
        self.spinBox_SY1.setMaximumSize(QSize(16777215, 30))
        self.spinBox_SY1.setStyleSheet(u"")
        self.spinBox_SY1.setAlignment(Qt.AlignCenter)
        self.spinBox_SY1.setMinimum(2000)
        self.spinBox_SY1.setMaximum(3000)

        self.horizontalLayout_18.addWidget(self.spinBox_SY1)

        self.label_26 = QLabel(self.widget_h)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(15, 16777215))
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_26)

        self.spinBox_SY2 = QSpinBox(self.widget_h)
        self.spinBox_SY2.setObjectName(u"spinBox_SY2")
        self.spinBox_SY2.setMinimumSize(QSize(0, 30))
        self.spinBox_SY2.setMaximumSize(QSize(16777215, 30))
        self.spinBox_SY2.setStyleSheet(u"")
        self.spinBox_SY2.setAlignment(Qt.AlignCenter)
        self.spinBox_SY2.setMinimum(2000)
        self.spinBox_SY2.setMaximum(3000)

        self.horizontalLayout_18.addWidget(self.spinBox_SY2)

        self.btnRefreshSY = QPushButton(self.widget_h)
        self.btnRefreshSY.setObjectName(u"btnRefreshSY")
        self.btnRefreshSY.setMinimumSize(QSize(30, 30))
        self.btnRefreshSY.setMaximumSize(QSize(30, 30))
        self.btnRefreshSY.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/Images/Images/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRefreshSY.setIcon(icon15)
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
        self.widget_search_2.setMaximumSize(QSize(16777215, 30))
        self.widget_search_2.setStyleSheet(u"")
        self.layout_search_2 = QHBoxLayout(self.widget_search_2)
        self.layout_search_2.setSpacing(0)
        self.layout_search_2.setObjectName(u"layout_search_2")
        self.layout_search_2.setContentsMargins(0, 0, 0, 0)
        self.label_magnifying_stud = QLabel(self.widget_search_2)
        self.label_magnifying_stud.setObjectName(u"label_magnifying_stud")
        self.label_magnifying_stud.setMinimumSize(QSize(30, 30))
        self.label_magnifying_stud.setMaximumSize(QSize(30, 30))
        self.label_magnifying_stud.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_stud.setScaledContents(True)
        self.label_magnifying_stud.setMargin(5)

        self.layout_search_2.addWidget(self.label_magnifying_stud)

        self.txt_classList_search = QLineEdit(self.widget_search_2)
        self.txt_classList_search.setObjectName(u"txt_classList_search")
        self.txt_classList_search.setMinimumSize(QSize(0, 30))
        self.txt_classList_search.setMaximumSize(QSize(16777215, 30))
        self.txt_classList_search.setStyleSheet(u"")

        self.layout_search_2.addWidget(self.txt_classList_search)


        self.horizontalLayout_18.addWidget(self.widget_search_2)


        self.verticalLayout_6.addWidget(self.widget_h)

        self.scrollArea = QScrollArea(self.widget_table_stud)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.container = QWidget()
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(0, 0, 594, 634))
        self.verticalLayout_9 = QVBoxLayout(self.container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea.setWidget(self.container)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.widget_f = QWidget(self.widget_table_stud)
        self.widget_f.setObjectName(u"widget_f")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_f)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)

        self.label_totalStudCount = QLabel(self.widget_f)
        self.label_totalStudCount.setObjectName(u"label_totalStudCount")
        self.label_totalStudCount.setMaximumSize(QSize(100, 20))
        self.label_totalStudCount.setFont(font)
        self.label_totalStudCount.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_17.addWidget(self.label_totalStudCount)


        self.verticalLayout_6.addWidget(self.widget_f)


        self.horizontalLayout_15.addWidget(self.widget_table_stud)

        self.stackedWidget.addWidget(self.pageClassList)
        self.pageLesson = QWidget()
        self.pageLesson.setObjectName(u"pageLesson")
        self.pageLesson.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.pageLesson)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_search = QWidget(self.pageLesson)
        self.widget_search.setObjectName(u"widget_search")
        self.widget_search.setStyleSheet(u"")
        self.layout_search = QHBoxLayout(self.widget_search)
        self.layout_search.setSpacing(0)
        self.layout_search.setObjectName(u"layout_search")
        self.layout_search.setContentsMargins(0, 0, 0, 0)
        self.label_magnifying = QLabel(self.widget_search)
        self.label_magnifying.setObjectName(u"label_magnifying")
        self.label_magnifying.setMinimumSize(QSize(30, 30))
        self.label_magnifying.setMaximumSize(QSize(30, 30))
        self.label_magnifying.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying.setScaledContents(True)
        self.label_magnifying.setMargin(5)

        self.layout_search.addWidget(self.label_magnifying)

        self.txtSearchLesson = QLineEdit(self.widget_search)
        self.txtSearchLesson.setObjectName(u"txtSearchLesson")
        self.txtSearchLesson.setMinimumSize(QSize(0, 30))
        self.txtSearchLesson.setStyleSheet(u"")

        self.layout_search.addWidget(self.txtSearchLesson)


        self.verticalLayout.addWidget(self.widget_search)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnAnimation = QPushButton(self.pageLesson)
        self.btnAnimation.setObjectName(u"btnAnimation")
        self.btnAnimation.setMinimumSize(QSize(120, 30))
        self.btnAnimation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btnAnimation)

        self.btnPowerPoint = QPushButton(self.pageLesson)
        self.btnPowerPoint.setObjectName(u"btnPowerPoint")
        self.btnPowerPoint.setMinimumSize(QSize(120, 30))
        self.btnPowerPoint.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btnPowerPoint)

        self.btnRefreshLessonTable = QPushButton(self.pageLesson)
        self.btnRefreshLessonTable.setObjectName(u"btnRefreshLessonTable")
        self.btnRefreshLessonTable.setMinimumSize(QSize(30, 30))
        self.btnRefreshLessonTable.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRefreshLessonTable.setIcon(icon15)
        self.btnRefreshLessonTable.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.btnRefreshLessonTable)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


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
        self.table_lesson.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_lesson.setSortingEnabled(True)
        self.table_lesson.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_lesson)

        self.label_lessonTotalCount = QLabel(self.pageLesson)
        self.label_lessonTotalCount.setObjectName(u"label_lessonTotalCount")

        self.verticalLayout.addWidget(self.label_lessonTotalCount)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.btnLessonView = QPushButton(self.pageLesson)
        self.btnLessonView.setObjectName(u"btnLessonView")
        self.btnLessonView.setMinimumSize(QSize(100, 30))
        self.btnLessonView.setMaximumSize(QSize(16777215, 30))
        self.btnLessonView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/Images/Images/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLessonView.setIcon(icon16)

        self.horizontalLayout_5.addWidget(self.btnLessonView)

        self.btnLessonEdit = QPushButton(self.pageLesson)
        self.btnLessonEdit.setObjectName(u"btnLessonEdit")
        self.btnLessonEdit.setMinimumSize(QSize(100, 30))
        self.btnLessonEdit.setMaximumSize(QSize(16777215, 30))
        self.btnLessonEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLessonEdit.setIcon(icon13)

        self.horizontalLayout_5.addWidget(self.btnLessonEdit)

        self.btnLessonAdd = QPushButton(self.pageLesson)
        self.btnLessonAdd.setObjectName(u"btnLessonAdd")
        self.btnLessonAdd.setMinimumSize(QSize(100, 30))
        self.btnLessonAdd.setMaximumSize(QSize(16777215, 30))
        self.btnLessonAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLessonAdd.setIcon(icon12)

        self.horizontalLayout_5.addWidget(self.btnLessonAdd)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.pageLesson)
        self.pageQuiz = QWidget()
        self.pageQuiz.setObjectName(u"pageQuiz")
        self.pageQuiz.setStyleSheet(u"")
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
        self.quiz_no.setMinimumSize(QSize(0, 30))
        self.quiz_no.setMaximumSize(QSize(16777215, 30))
        self.quiz_no.setStyleSheet(u"")
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
        self.cbGradingPeriod.setMinimumSize(QSize(120, 30))
        self.cbGradingPeriod.setMaximumSize(QSize(16777215, 30))
        self.cbGradingPeriod.setStyleSheet(u"")

        self.headerLayout.addWidget(self.cbGradingPeriod)

        self.labelLesson = QLabel(self.pageQuiz)
        self.labelLesson.setObjectName(u"labelLesson")

        self.headerLayout.addWidget(self.labelLesson)

        self.cbLessonName = QComboBox(self.pageQuiz)
        self.cbLessonName.setObjectName(u"cbLessonName")
        self.cbLessonName.setMinimumSize(QSize(120, 30))
        self.cbLessonName.setMaximumSize(QSize(16777215, 30))
        self.cbLessonName.setStyleSheet(u"")

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
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.frame_6 = QFrame(self.pageQuiz)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"#frame_6 { background-color: transparent; }")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_6)

        self.widget_4 = QWidget(self.frame_6)
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
        self.horizontalLayout_11 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btnEasy = QPushButton(self.widget_4)
        self.btnEasy.setObjectName(u"btnEasy")
        self.btnEasy.setMinimumSize(QSize(0, 30))
        self.btnEasy.setMaximumSize(QSize(16777215, 30))
        self.btnEasy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEasy.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnEasy)

        self.btnAverage = QPushButton(self.widget_4)
        self.btnAverage.setObjectName(u"btnAverage")
        self.btnAverage.setMinimumSize(QSize(0, 30))
        self.btnAverage.setMaximumSize(QSize(16777215, 30))
        self.btnAverage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAverage.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnAverage)

        self.btnHard = QPushButton(self.widget_4)
        self.btnHard.setObjectName(u"btnHard")
        self.btnHard.setMinimumSize(QSize(0, 30))
        self.btnHard.setMaximumSize(QSize(16777215, 30))
        self.btnHard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnHard.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnHard)


        self.horizontalLayout.addWidget(self.widget_4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setStyleSheet(u"font: 10pt \"Inter SemiBold\";")

        self.horizontalLayout.addWidget(self.label_21)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_15)

        self.multiplier_easy = QLabel(self.frame_6)
        self.multiplier_easy.setObjectName(u"multiplier_easy")
        self.multiplier_easy.setMinimumSize(QSize(0, 30))
        self.multiplier_easy.setMaximumSize(QSize(16777215, 30))
        self.multiplier_easy.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")
        self.multiplier_easy.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.multiplier_easy)

        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_22)

        self.multiplier_average = QLabel(self.frame_6)
        self.multiplier_average.setObjectName(u"multiplier_average")
        self.multiplier_average.setMinimumSize(QSize(0, 30))
        self.multiplier_average.setMaximumSize(QSize(16777215, 30))
        self.multiplier_average.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")
        self.multiplier_average.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.multiplier_average)

        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_23)

        self.multiplier_hard = QLabel(self.frame_6)
        self.multiplier_hard.setObjectName(u"multiplier_hard")
        self.multiplier_hard.setMinimumSize(QSize(0, 30))
        self.multiplier_hard.setMaximumSize(QSize(16777215, 30))
        self.multiplier_hard.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")
        self.multiplier_hard.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.multiplier_hard)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_scoreperlevel = QLabel(self.frame_6)
        self.label_scoreperlevel.setObjectName(u"label_scoreperlevel")
        self.label_scoreperlevel.setMinimumSize(QSize(0, 30))
        self.label_scoreperlevel.setMaximumSize(QSize(16777215, 30))
        self.label_scoreperlevel.setStyleSheet(u"background-color: rgb(255, 255, 255); padding: 0px 10px 0px; border-radius: 5px;")

        self.horizontalLayout.addWidget(self.label_scoreperlevel)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.line_7 = QFrame(self.pageQuiz)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.pageQuiz)
        self.label_13.setObjectName(u"label_13")
        font10 = QFont()
        font10.setFamilies([u"Inter SemiBold"])
        font10.setPointSize(14)
        font10.setBold(False)
        font10.setItalic(False)
        self.label_13.setFont(font10)
        self.label_13.setStyleSheet(u"font: 63 14pt \"Inter SemiBold\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 2, 4, 1, 1)

        self.scrollArea_mc = QScrollArea(self.pageQuiz)
        self.scrollArea_mc.setObjectName(u"scrollArea_mc")
        self.scrollArea_mc.setStyleSheet(u"")
        self.scrollArea_mc.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 311, 532))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_mc.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.scrollArea_mc, 4, 2, 1, 1)

        self.line_9 = QFrame(self.pageQuiz)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 4, 1, 1, 1)

        self.scrollArea_tf = QScrollArea(self.pageQuiz)
        self.scrollArea_tf.setObjectName(u"scrollArea_tf")
        self.scrollArea_tf.setStyleSheet(u"")
        self.scrollArea_tf.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 311, 532))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_tf.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout.addWidget(self.scrollArea_tf, 4, 4, 1, 1)

        self.label_11 = QLabel(self.pageQuiz)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font10)
        self.label_11.setStyleSheet(u"font: 14pt \"Inter SemiBold\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_12 = QLabel(self.pageQuiz)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font10)
        self.label_12.setStyleSheet(u"font: 63 14pt \"Inter SemiBold\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)

        self.scrollArea_id = QScrollArea(self.pageQuiz)
        self.scrollArea_id.setObjectName(u"scrollArea_id")
        self.scrollArea_id.setStyleSheet(u"")
        self.scrollArea_id.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 311, 532))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_id.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea_id, 4, 0, 1, 1)

        self.line_10 = QFrame(self.pageQuiz)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 4, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.btnQuizAdd = QPushButton(self.pageQuiz)
        self.btnQuizAdd.setObjectName(u"btnQuizAdd")
        self.btnQuizAdd.setMinimumSize(QSize(100, 30))
        self.btnQuizAdd.setMaximumSize(QSize(16777215, 30))
        self.btnQuizAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btnQuizAdd)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.pageQuiz)
        self.pageExercise = QWidget()
        self.pageExercise.setObjectName(u"pageExercise")
        self.pageExercise.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.pageExercise)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_search_3 = QWidget(self.pageExercise)
        self.widget_search_3.setObjectName(u"widget_search_3")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_search_3)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_magnifying_exer = QLabel(self.widget_search_3)
        self.label_magnifying_exer.setObjectName(u"label_magnifying_exer")
        self.label_magnifying_exer.setMinimumSize(QSize(30, 30))
        self.label_magnifying_exer.setMaximumSize(QSize(30, 30))
        self.label_magnifying_exer.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_exer.setScaledContents(True)
        self.label_magnifying_exer.setMargin(5)

        self.horizontalLayout_23.addWidget(self.label_magnifying_exer)

        self.txtSearchExercise = QLineEdit(self.widget_search_3)
        self.txtSearchExercise.setObjectName(u"txtSearchExercise")
        self.txtSearchExercise.setMinimumSize(QSize(0, 30))
        self.txtSearchExercise.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.txtSearchExercise)


        self.verticalLayout_10.addWidget(self.widget_search_3)

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
        self.pageSections.setStyleSheet(u"")
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
        self.comboBox_Section.setMinimumSize(QSize(200, 30))
        self.comboBox_Section.setMaximumSize(QSize(16777215, 30))
        self.comboBox_Section.setStyleSheet(u"")

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
        self.table_section.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_section.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table_section)

        self.stackedWidget.addWidget(self.pageSections)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.pageReports.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.pageReports)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.pageReports)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_9.addWidget(self.label_18)

        self.comboBox_ReportsSection = QComboBox(self.tab)
        self.comboBox_ReportsSection.setObjectName(u"comboBox_ReportsSection")
        self.comboBox_ReportsSection.setMinimumSize(QSize(250, 30))
        self.comboBox_ReportsSection.setMaximumSize(QSize(16777215, 30))
        self.comboBox_ReportsSection.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.comboBox_ReportsSection)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.btnPreview = QPushButton(self.tab)
        self.btnPreview.setObjectName(u"btnPreview")
        self.btnPreview.setMinimumSize(QSize(100, 30))
        self.btnPreview.setMaximumSize(QSize(16777215, 30))
        self.btnPreview.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btnPreview)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.tabWidget.addTab(self.tab, "")
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
"    border-radius: 5px; \n"
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
"    border-radius: 5px;\n"
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
        self.verticalLayout_20 = QVBoxLayout(self.widget_10)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_stud_tblheader_idv = QWidget(self.widget_10)
        self.widget_stud_tblheader_idv.setObjectName(u"widget_stud_tblheader_idv")
        self.widget_stud_tblheader_idv.setStyleSheet(u"#widget_stud_tblheader_idv { \n"
"	background-color: rgb(224, 243, 255);\n"
"	border: 1px solid rgb(98, 160, 234);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_stud_tblheader_idv)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_search_idv = QWidget(self.widget_stud_tblheader_idv)
        self.widget_search_idv.setObjectName(u"widget_search_idv")
        self.widget_search_idv.setMinimumSize(QSize(0, 30))
        self.widget_search_idv.setMaximumSize(QSize(16777215, 30))
        self.widget_search_idv.setStyleSheet(u"")
        self.layout_search_idv = QHBoxLayout(self.widget_search_idv)
        self.layout_search_idv.setSpacing(0)
        self.layout_search_idv.setObjectName(u"layout_search_idv")
        self.layout_search_idv.setContentsMargins(0, 0, 0, 0)
        self.label_magnifying_idv = QLabel(self.widget_search_idv)
        self.label_magnifying_idv.setObjectName(u"label_magnifying_idv")
        self.label_magnifying_idv.setMinimumSize(QSize(30, 30))
        self.label_magnifying_idv.setMaximumSize(QSize(30, 30))
        self.label_magnifying_idv.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_idv.setScaledContents(True)
        self.label_magnifying_idv.setMargin(5)

        self.layout_search_idv.addWidget(self.label_magnifying_idv)

        self.txt_search_score_idv = QLineEdit(self.widget_search_idv)
        self.txt_search_score_idv.setObjectName(u"txt_search_score_idv")
        self.txt_search_score_idv.setMinimumSize(QSize(0, 30))
        self.txt_search_score_idv.setMaximumSize(QSize(16777215, 30))
        self.txt_search_score_idv.setStyleSheet(u"")

        self.layout_search_idv.addWidget(self.txt_search_score_idv)


        self.horizontalLayout_7.addWidget(self.widget_search_idv)


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
"	background-color: rgb(224, 243, 255);\n"
"	border: 1px solid rgb(98, 160, 234);\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_student_icon = QLabel(self.widget_7)
        self.label_student_icon.setObjectName(u"label_student_icon")
        self.label_student_icon.setMaximumSize(QSize(30, 30))
        self.label_student_icon.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_student_icon.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_student_icon)

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
        self.cb_gp_quiz_idv.addItem("")
        self.cb_gp_quiz_idv.setObjectName(u"cb_gp_quiz_idv")
        self.cb_gp_quiz_idv.setMinimumSize(QSize(150, 30))
        self.cb_gp_quiz_idv.setMaximumSize(QSize(16777215, 30))
        self.cb_gp_quiz_idv.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.cb_gp_quiz_idv)


        self.verticalLayout_19.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_8)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"#widget_9 { \n"
"	border-left: 1px solid rgb(161, 161, 161);\n"
"	border-right: 1px solid rgb(161, 161, 161);\n"
"	background-color: rgb(246, 245, 244);\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_search_idv_2 = QWidget(self.widget_9)
        self.widget_search_idv_2.setObjectName(u"widget_search_idv_2")
        self.widget_search_idv_2.setMinimumSize(QSize(0, 30))
        self.widget_search_idv_2.setMaximumSize(QSize(16777215, 30))
        self.widget_search_idv_2.setStyleSheet(u"")
        self.layout_search_idv_2 = QHBoxLayout(self.widget_search_idv_2)
        self.layout_search_idv_2.setSpacing(0)
        self.layout_search_idv_2.setObjectName(u"layout_search_idv_2")
        self.layout_search_idv_2.setContentsMargins(0, 0, 0, 0)
        self.label_magnifying_idv_2 = QLabel(self.widget_search_idv_2)
        self.label_magnifying_idv_2.setObjectName(u"label_magnifying_idv_2")
        self.label_magnifying_idv_2.setMinimumSize(QSize(30, 30))
        self.label_magnifying_idv_2.setMaximumSize(QSize(30, 30))
        self.label_magnifying_idv_2.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_magnifying_idv_2.setScaledContents(True)
        self.label_magnifying_idv_2.setMargin(5)

        self.layout_search_idv_2.addWidget(self.label_magnifying_idv_2)

        self.txt_search_score_d_idv = QLineEdit(self.widget_search_idv_2)
        self.txt_search_score_d_idv.setObjectName(u"txt_search_score_d_idv")
        self.txt_search_score_d_idv.setMinimumSize(QSize(0, 30))
        self.txt_search_score_d_idv.setMaximumSize(QSize(16777215, 30))
        self.txt_search_score_d_idv.setStyleSheet(u"")

        self.layout_search_idv_2.addWidget(self.txt_search_score_d_idv)


        self.horizontalLayout_22.addWidget(self.widget_search_idv_2)


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

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.pageReports)
        self.pageUsers = QWidget()
        self.pageUsers.setObjectName(u"pageUsers")
        self.pageUsers.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.pageUsers)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_header = QWidget(self.pageUsers)
        self.widget_header.setObjectName(u"widget_header")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_search_section = QWidget(self.widget_header)
        self.widget_search_section.setObjectName(u"widget_search_section")
        self.widget_search_section.setMinimumSize(QSize(100, 0))
        self.widget_search_section.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_search_section)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_search_section)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/Images/Images/search.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.txt_search_user = QLineEdit(self.widget_search_section)
        self.txt_search_user.setObjectName(u"txt_search_user")
        self.txt_search_user.setMinimumSize(QSize(0, 30))
        self.txt_search_user.setMaximumSize(QSize(16777215, 30))
        self.txt_search_user.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.txt_search_user)


        self.horizontalLayout_19.addWidget(self.widget_search_section)

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
        self.btnRefreshUsers.setIcon(icon15)
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
"    border-radius: 5px; \n"
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
"    border-radius: 5px;\n"
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
"}")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.tab_settings.setStyleSheet(u"")
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
        font11 = QFont()
        font11.setFamilies([u"Inter"])
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setItalic(False)
        self.label_10.setFont(font11)
        self.label_10.setStyleSheet(u"background: transparent; \n"
"font: 12pt \"Inter\";")

        self.horizontalLayout_30.addWidget(self.label_10)

        self.spinBox_SY_start = QSpinBox(self.widget_SY_header)
        self.spinBox_SY_start.setObjectName(u"spinBox_SY_start")
        self.spinBox_SY_start.setMinimumSize(QSize(0, 30))
        self.spinBox_SY_start.setMaximumSize(QSize(16777215, 30))
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
        self.spinBox_SY_end.setMinimumSize(QSize(0, 30))
        self.spinBox_SY_end.setMaximumSize(QSize(16777215, 30))
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
        font12 = QFont()
        font12.setFamilies([u"Inter SemiBold"])
        font12.setPointSize(10)
        font12.setBold(False)
        font12.setItalic(False)
        self.btnSaveSettings_SY.setFont(font12)
        self.btnSaveSettings_SY.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSaveSettings_SY.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.btnSaveSettings_SY)


        self.verticalLayout_28.addWidget(self.widget_SY_header)

        self.widget_SY_body = QWidget(self.widget_SY_settings)
        self.widget_SY_body.setObjectName(u"widget_SY_body")
        self.formLayout = QFormLayout(self.widget_SY_body)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(15, 15, 15, 15)
        self.label_30 = QLabel(self.widget_SY_body)
        self.label_30.setObjectName(u"label_30")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.dateEdit_firstgrading_start = QDateEdit(self.widget_SY_body)
        self.dateEdit_firstgrading_start.setObjectName(u"dateEdit_firstgrading_start")
        self.dateEdit_firstgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_firstgrading_start.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dateEdit_firstgrading_start)

        self.label_31 = QLabel(self.widget_SY_body)
        self.label_31.setObjectName(u"label_31")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_31)

        self.dateEdit_secondgrading_start = QDateEdit(self.widget_SY_body)
        self.dateEdit_secondgrading_start.setObjectName(u"dateEdit_secondgrading_start")
        self.dateEdit_secondgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_secondgrading_start.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateEdit_secondgrading_start)

        self.label_39 = QLabel(self.widget_SY_body)
        self.label_39.setObjectName(u"label_39")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_39)

        self.dateEdit_thirdgrading_start = QDateEdit(self.widget_SY_body)
        self.dateEdit_thirdgrading_start.setObjectName(u"dateEdit_thirdgrading_start")
        self.dateEdit_thirdgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_thirdgrading_start.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEdit_thirdgrading_start)

        self.label_40 = QLabel(self.widget_SY_body)
        self.label_40.setObjectName(u"label_40")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_40)

        self.dateEdit_fourthgrading_start = QDateEdit(self.widget_SY_body)
        self.dateEdit_fourthgrading_start.setObjectName(u"dateEdit_fourthgrading_start")
        self.dateEdit_fourthgrading_start.setMinimumSize(QSize(0, 30))
        self.dateEdit_fourthgrading_start.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateEdit_fourthgrading_start)


        self.verticalLayout_28.addWidget(self.widget_SY_body)


        self.verticalLayout_27.addWidget(self.widget_SY_settings)

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
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_utility.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Computer-Aided Instructions System in Mathematics for the Grade 1 Students of La Camelle School", None))
        self.label_20.setText("")
        self.btnHome.setText(QCoreApplication.translate("Home", u"Home", None))
        self.btnStudentList.setText(QCoreApplication.translate("Home", u"Student List", None))
        self.btnLesson.setText(QCoreApplication.translate("Home", u"Lesson", None))
        self.btnQuiz.setText(QCoreApplication.translate("Home", u"Quiz", None))
        self.btnExercise.setText(QCoreApplication.translate("Home", u"Exercise", None))
        self.btnSections.setText(QCoreApplication.translate("Home", u"Sections", None))
        self.btnReports.setText(QCoreApplication.translate("Home", u"Reports", None))
        self.btnUserName.setText(QCoreApplication.translate("Home", u"Christopher", None))
        self.labelPosition.setText(QCoreApplication.translate("Home", u"Admin", None))
        self.btnLogout.setText(QCoreApplication.translate("Home", u"Log out", None))
        self.btnUsers.setText(QCoreApplication.translate("Home", u"Users", None))
        self.btnUtility.setText(QCoreApplication.translate("Home", u"Utilities", None))
        self.label_timeAP_3.setText(QCoreApplication.translate("Home", u"Welcome to La Camelle School", None))
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
        self.label_month.setText(QCoreApplication.translate("Home", u"Mar", None))
        self.label_day.setText(QCoreApplication.translate("Home", u"00", None))
        self.label_19.setText("")
        self.label_time.setText(QCoreApplication.translate("Home", u"00:00", None))
        self.label_timeAP.setText(QCoreApplication.translate("Home", u"AM", None))
        self.label_16.setText(QCoreApplication.translate("Home", u"Section Information", None))
        self.label_33.setText(QCoreApplication.translate("Home", u"No. of students:", None))
        self.label_33.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_34.setText(QCoreApplication.translate("Home", u"Boys:", None))
        self.label_34.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_28.setText(QCoreApplication.translate("Home", u"Girls:", None))
        self.label_28.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_studentCount.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_girlCount.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_boyCount.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_35.setText(QCoreApplication.translate("Home", u"Section:", None))
        self.label_35.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_section.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_17.setText(QCoreApplication.translate("Home", u"Student Information", None))
        self.label_43.setText(QCoreApplication.translate("Home", u"Student Id:", None))
        self.label_43.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_studentId.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_36.setText(QCoreApplication.translate("Home", u"Last name:", None))
        self.label_36.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_studentLastName.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_38.setText(QCoreApplication.translate("Home", u"First name:", None))
        self.label_38.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_studentFirstName.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_41.setText(QCoreApplication.translate("Home", u"Middle name:", None))
        self.label_41.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_studentMiddleName.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_37.setText(QCoreApplication.translate("Home", u"Gender:", None))
        self.label_37.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_studentGender.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_51.setText(QCoreApplication.translate("Home", u"Emergency Contact", None))
        self.label_59.setText(QCoreApplication.translate("Home", u"Contact person:", None))
        self.label_59.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_56.setText(QCoreApplication.translate("Home", u"Contact number:", None))
        self.label_56.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.label_contact_person.setText(QCoreApplication.translate("Home", u"null", None))
        self.label_contact_number.setText(QCoreApplication.translate("Home", u"null", None))
        self.btnAddStudent.setText(QCoreApplication.translate("Home", u"Add", None))
        self.btnAddStudent.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnEditStudent.setText(QCoreApplication.translate("Home", u"Edit", None))
        self.btnEditStudent.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnDeleteStudent.setText(QCoreApplication.translate("Home", u"Delete", None))
        self.btnDeleteStudent.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.label_32.setText(QCoreApplication.translate("Home", u"School Year:", None))
        self.label_26.setText(QCoreApplication.translate("Home", u"-", None))
        self.btnRefreshSY.setText("")
        self.btnRefreshSY.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.cmb_studSection.setPlaceholderText(QCoreApplication.translate("Home", u"Select Section", None))
        self.cmb_studSection.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.widget_search_2.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_stud.setText("")
        self.label_magnifying_stud.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txt_classList_search.setPlaceholderText(QCoreApplication.translate("Home", u"Search Lesson", None))
        self.txt_classList_search.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
        self.label_totalStudCount.setText(QCoreApplication.translate("Home", u"0 items", None))
        self.label_totalStudCount.setProperty(u"class", QCoreApplication.translate("Home", u"label-header", None))
        self.widget_search.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying.setText("")
        self.label_magnifying.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txtSearchLesson.setPlaceholderText(QCoreApplication.translate("Home", u"Search Lesson", None))
        self.txtSearchLesson.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
        self.btnAnimation.setText(QCoreApplication.translate("Home", u"Animation", None))
        self.btnAnimation.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnPowerPoint.setText(QCoreApplication.translate("Home", u"MS PowerPoint", None))
        self.btnPowerPoint.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
#if QT_CONFIG(tooltip)
        self.btnRefreshLessonTable.setToolTip(QCoreApplication.translate("Home", u"Refresh table", None))
#endif // QT_CONFIG(tooltip)
        self.btnRefreshLessonTable.setText("")
        self.btnRefreshLessonTable.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.label_lessonTotalCount.setText(QCoreApplication.translate("Home", u"40 items", None))
        self.btnLessonView.setText(QCoreApplication.translate("Home", u"View", None))
        self.btnLessonView.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnLessonEdit.setText(QCoreApplication.translate("Home", u"Edit", None))
        self.btnLessonEdit.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.btnLessonAdd.setText(QCoreApplication.translate("Home", u"Add", None))
        self.btnLessonAdd.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
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
        self.widget_search_3.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_exer.setText("")
        self.label_magnifying_exer.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txtSearchExercise.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txtSearchExercise.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
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
        self.label_18.setText(QCoreApplication.translate("Home", u"Section:", None))
        self.comboBox_ReportsSection.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.btnPreview.setText(QCoreApplication.translate("Home", u"Preview", None))
        self.btnPreview.setProperty(u"class", QCoreApplication.translate("Home", u"button-normal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Home", u"Class list", None))
        self.widget_search_idv.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_idv.setText("")
        self.label_magnifying_idv.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txt_search_score_idv.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txt_search_score_idv.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
        self.label_student_icon.setText("")
        self.label_student_name.setText(QCoreApplication.translate("Home", u"Student Name", None))
        self.label_avg_icon.setText("")
        self.label_avg.setText(QCoreApplication.translate("Home", u"Average:", None))
        self.label_average_percentage.setText(QCoreApplication.translate("Home", u"85%", None))
        self.label_lessons_prog_icon.setText("")
        self.label_lessons_prog_1.setText(QCoreApplication.translate("Home", u"Lessons:", None))
        self.label_lessons_prog.setText(QCoreApplication.translate("Home", u"12/20", None))
        self.labelGradingPeriod_4.setText(QCoreApplication.translate("Home", u"Grading Period:", None))
        self.cb_gp_quiz_idv.setItemText(0, QCoreApplication.translate("Home", u"Fourth Grading", None))

        self.cb_gp_quiz_idv.setProperty(u"class", QCoreApplication.translate("Home", u"combobox-main", None))
        self.widget_search_idv_2.setProperty(u"class", QCoreApplication.translate("Home", u"widget-search-container", None))
        self.label_magnifying_idv_2.setText("")
        self.label_magnifying_idv_2.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txt_search_score_d_idv.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txt_search_score_d_idv.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Home", u"Raw scores (Individual)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Home", u"Raw score (All)", None))
        self.label_2.setText("")
        self.label_2.setProperty(u"class", QCoreApplication.translate("Home", u"label-magnifying-search", None))
        self.txt_search_user.setPlaceholderText(QCoreApplication.translate("Home", u"Search", None))
        self.txt_search_user.setProperty(u"class", QCoreApplication.translate("Home", u"textbox-search", None))
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
        self.btnSaveSettings_SY.setProperty(u"class", QCoreApplication.translate("Home", u"button-green", None))
        self.label_30.setText(QCoreApplication.translate("Home", u"First:", None))
        self.dateEdit_firstgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy/MM/dd", None))
        self.label_31.setText(QCoreApplication.translate("Home", u"Second:", None))
        self.dateEdit_secondgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy/MM/dd", None))
        self.label_39.setText(QCoreApplication.translate("Home", u"Third:", None))
        self.dateEdit_thirdgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy/MM/dd", None))
        self.label_40.setText(QCoreApplication.translate("Home", u"Fourth:", None))
        self.dateEdit_fourthgrading_start.setDisplayFormat(QCoreApplication.translate("Home", u"yyyy/MM/dd", None))
        self.tabWidget_utility.setTabText(self.tabWidget_utility.indexOf(self.tab_settings), QCoreApplication.translate("Home", u"Settings", None))
        self.tabWidget_utility.setTabText(self.tabWidget_utility.indexOf(self.tab_audit_trail), QCoreApplication.translate("Home", u"Audit Trail", None))
        self.tabWidget_utility.setTabText(self.tabWidget_utility.indexOf(self.tab_archive), QCoreApplication.translate("Home", u"Archive", None))
    # retranslateUi

