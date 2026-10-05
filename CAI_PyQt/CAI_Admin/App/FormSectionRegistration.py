# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormSectionRegistration.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_SectionRegistrationDialog(object):
    def setupUi(self, SectionRegistrationDialog):
        if not SectionRegistrationDialog.objectName():
            SectionRegistrationDialog.setObjectName(u"SectionRegistrationDialog")
        SectionRegistrationDialog.resize(620, 586)
        SectionRegistrationDialog.setMinimumSize(QSize(620, 580))
        SectionRegistrationDialog.setMaximumSize(QSize(742, 586))
        SectionRegistrationDialog.setStyleSheet(u"* {\n"
"	color: black;\n"
"}\n"
"\n"
"#SectionRegistrationDialog {\n"
"	background: transparent;\n"
"}\n"
"\n"
"#verticalFrame {\n"
"	background-color: rgb(222, 221, 218); \n"
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
"                                stop:1 #129046); \n"
"}\n"
"\n"
"QPushButto"
                        "n[class=\"button-green\"]:disabled {\n"
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
"	border: 1px solid #dcdcdc;\n"
"	color: #aeaeae;\n"
"}\n"
"\n"
"QLabel:dis"
                        "abled {\n"
"	color: #aeaeae;\n"
"}\n"
"\n"
"*[class=\"input-field\"] {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit {\n"
"	background-color: #ffffff;\n"
"	border: 1px solid #999;\n"
"	border-left: none;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	padding: 0px 8px;\n"
"	color: black;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLabel {\n"
"	background-color: rgb(192, 191, 188);\n"
"	border-left: 1px solid #999;\n"
"	border-top: 1px solid #999;\n"
"	border-bottom: 1px solid #999;\n"
"	border-right: none;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	padding-left: 8px;\n"
"	color: black;\n"
"}\n"
"\n"
"QProgressBar {\n"
"	border-radius: 10px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #007BFF;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #999;\n"
"    border-left: none;\n"
"    padding: 0px 10px;\n"
"    background-color: #ffffff;"
                        "\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\";\n"
"    selection-background-color: #7eb4d7;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox:focus, QLineEdit:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox:hover, QLineEdit:hover {\n"
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
"    selection-color: #ffffff;\n"
"    "
                        "outline: 0; /* Removes the ugly dotted focus border */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 0px 15px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover state for items inside the dropdown */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
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
"QScrollBar::handle:vertical"
                        ":hover {\n"
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
"    background: none;\n"
"}\n"
"\n"
"/* 6. THE C"
                        "ORNER WIDGET \n"
"   (The small square where both bars meet) */\n"
"QScrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(SectionRegistrationDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(SectionRegistrationDialog)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 35))
        self.frame_header.setMaximumSize(QSize(16777215, 35))
        self.frame_header.setMouseTracking(True)
        self.frame_header.setStyleSheet(u"#frame_header {\n"
"	background-color: #deddda;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"	border: 1px solid #7a7a7a;\n"
"	border-bottom: none;\n"
"}")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.widget_window_icon = QWidget(self.frame_header)
        self.widget_window_icon.setObjectName(u"widget_window_icon")
        self.widget_window_icon.setMinimumSize(QSize(54, 35))
        self.widget_window_icon.setMaximumSize(QSize(54, 35))
        self.widget_window_icon.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_window_icon)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.widget_window_icon)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_windowTitle = QLabel(self.frame_header)
        self.label_windowTitle.setObjectName(u"label_windowTitle")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_windowTitle.setFont(font)
        self.label_windowTitle.setStyleSheet(u"background: transparent;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Inter SemiBold\";")

        self.horizontalLayout_6.addWidget(self.label_windowTitle)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btnMinimize = QPushButton(self.frame_header)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(24, 24))
        self.btnMinimize.setMaximumSize(QSize(24, 24))
        self.btnMinimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"#btnMinimize {\n"
"	border-radius: 12px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#btnMinimize:hover {\n"
"	background-color: #f8e45c;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Images/Images/minimize-sign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QSize(12, 12))

        self.horizontalLayout_6.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.frame_header)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(24, 24))
        self.btnClose.setMaximumSize(QSize(24, 24))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"#btnClose {\n"
"	border-radius: 12px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#btnClose:hover {\n"
"	background-color: rgb(246, 97, 81);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.frame_header)

        self.verticalFrame = QFrame(SectionRegistrationDialog)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"#verticalFrame {\n"
"	background-color: #deddda;\n"
"	border: 1px solid #7a7a7a;\n"
"	border-top: none;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.label_sy = QLabel(self.verticalFrame)
        self.label_sy.setObjectName(u"label_sy")

        self.verticalLayout_5.addWidget(self.label_sy)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_1 = QWidget(self.verticalFrame)
        self.widget_1.setObjectName(u"widget_1")
        self.horizontalLayout = QHBoxLayout(self.widget_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 30))
        self.label_9.setMaximumSize(QSize(100, 30))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.txtSectionName = QLineEdit(self.widget_1)
        self.txtSectionName.setObjectName(u"txtSectionName")
        self.txtSectionName.setMinimumSize(QSize(0, 30))
        self.txtSectionName.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.horizontalLayout.addWidget(self.txtSectionName)


        self.verticalLayout_2.addWidget(self.widget_1)

        self.widget_2 = QWidget(self.verticalFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 30))
        self.label_10.setMaximumSize(QSize(100, 30))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.cmb_teacher = QComboBox(self.widget_2)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 30))
        self.cmb_teacher.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmb_teacher.setEditable(False)

        self.horizontalLayout_3.addWidget(self.cmb_teacher)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.verticalFrame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.rb_importCSV = QRadioButton(self.verticalFrame)
        self.rb_importCSV.setObjectName(u"rb_importCSV")
        self.rb_importCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rb_importCSV.setStyleSheet(u"background-color: #deddda;")

        self.verticalLayout_5.addWidget(self.rb_importCSV)

        self.widget_CSV = QWidget(self.verticalFrame)
        self.widget_CSV.setObjectName(u"widget_CSV")
        self.widget_CSV.setEnabled(True)
        self.widget_CSV.setMinimumSize(QSize(100, 0))
        self.widget_CSV.setStyleSheet(u"#label_14 {\n"
"	background-color: rgb(192, 191, 188);\n"
"	border-left: 1px solid #999;\n"
"	border-top: 1px solid #999;\n"
"	border-bottom: 1px solid #999;\n"
"	border-right: none;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	padding-left: 8px;\n"
"	color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #ffffff;\n"
"	color: black;\n"
"	border: 1px solid #999;\n"
"	border-right: none;\n"
"	border-left: none;\n"
"	padding: 0px 10px;\n"
"}\n"
"\n"
"#btnBrowseCSV {\n"
"	font: 10pt \"Inter\";\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #d8ecf6);\n"
"	color: black;\n"
"	border: 1px solid rgb(154, 153, 150);\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#btnBrowseCSV:hover {\n"
"	background-color: #FFF;\n"
"}\n"
"\n"
"#btnBrowseCSV:disabled, #label_14:disabled {\n"
"	background-color: rgb(192, 191, 188);\n"
"	border: none;"
                        "\n"
"	color: #aeaeae;\n"
"}\n"
"\n"
"#widget_CSV QLineEdit:disabled {\n"
"	background-color: #f5f5f5;\n"
"	border: none;\n"
"	color: #aeaeae;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_CSV)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_CSV)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 30))
        self.label_14.setMaximumSize(QSize(100, 30))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_14)

        self.txtCSVPath = QLineEdit(self.widget_CSV)
        self.txtCSVPath.setObjectName(u"txtCSVPath")
        self.txtCSVPath.setMinimumSize(QSize(0, 30))
        self.txtCSVPath.setMaximumSize(QSize(16777215, 30))
        self.txtCSVPath.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.txtCSVPath)

        self.btnBrowseCSV = QPushButton(self.widget_CSV)
        self.btnBrowseCSV.setObjectName(u"btnBrowseCSV")
        self.btnBrowseCSV.setMinimumSize(QSize(100, 30))
        self.btnBrowseCSV.setMaximumSize(QSize(100, 30))
        self.btnBrowseCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBrowseCSV.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnBrowseCSV)


        self.verticalLayout_5.addWidget(self.widget_CSV)

        self.widget_template = QWidget(self.verticalFrame)
        self.widget_template.setObjectName(u"widget_template")
        self.widget_template.setEnabled(True)
        self.widget_template.setMinimumSize(QSize(0, 200))
        self.verticalLayout_3 = QVBoxLayout(self.widget_template)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.widget_template)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: #deddda;")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.label)

        self.btnExportTemplate = QPushButton(self.widget_3)
        self.btnExportTemplate.setObjectName(u"btnExportTemplate")
        self.btnExportTemplate.setEnabled(True)
        self.btnExportTemplate.setMinimumSize(QSize(30, 30))
        self.btnExportTemplate.setMaximumSize(QSize(30, 30))
        self.btnExportTemplate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Images/Images/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportTemplate.setIcon(icon2)
        self.btnExportTemplate.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.btnExportTemplate)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.scrollArea = QScrollArea(self.widget_template)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(0, 220))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 703, 210))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QSize(16777215, 210))
        self.label_2.setPixmap(QPixmap(u":/Images/Images/student_list_template.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.widget_template)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progressBar = QProgressBar(self.verticalFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(self.verticalFrame)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.verticalFrame)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 30))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.verticalFrame)


        self.retranslateUi(SectionRegistrationDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionRegistrationDialog)
    # setupUi

    def retranslateUi(self, SectionRegistrationDialog):
        SectionRegistrationDialog.setWindowTitle(QCoreApplication.translate("SectionRegistrationDialog", u"Section Registration", None))
        self.label_windowTitle.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Section Registration", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.label_sy.setText(QCoreApplication.translate("SectionRegistrationDialog", u"School Year: 0000-0000", None))
        self.widget_1.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Name", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Adviser", None))
        self.rb_importCSV.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Import students from CSV", None))
        self.widget_CSV.setProperty(u"class", "")
        self.label_14.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Template file:", None))
        self.label_14.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"input-field", None))
        self.btnBrowseCSV.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Browse", None))
        self.label.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Template (Sample):", None))
#if QT_CONFIG(tooltip)
        self.btnExportTemplate.setToolTip(QCoreApplication.translate("SectionRegistrationDialog", u"Export Template", None))
#endif // QT_CONFIG(tooltip)
        self.btnExportTemplate.setText("")
        self.label_2.setText("")
        self.btnCancel.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"button-green", None))
    # retranslateUi

