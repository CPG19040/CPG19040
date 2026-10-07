# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormSectionAdviserEditor.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_SectionAdviserEditorDialog(object):
    def setupUi(self, SectionAdviserEditorDialog):
        if not SectionAdviserEditorDialog.objectName():
            SectionAdviserEditorDialog.setObjectName(u"SectionAdviserEditorDialog")
        SectionAdviserEditorDialog.resize(550, 520)
        SectionAdviserEditorDialog.setMinimumSize(QSize(550, 520))
        SectionAdviserEditorDialog.setMaximumSize(QSize(900, 600))
        SectionAdviserEditorDialog.setStyleSheet(u"* {\n"
"	background-color: rgb(222, 221, 218); \n"
"	color: black;\n"
"	font: 10pt \"Inter\";\n"
"}\n"
"\n"
"#SectionAdviserEditorDialog {\n"
"	background-color: transparent;\n"
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
"QPushBut"
                        "ton[class=\"button-green\"]:disabled {\n"
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
"*[class="
                        "\"input-field\"] {\n"
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
"QComboBox {\n"
"    border: 1px solid #999;\n"
"    border-left: none;\n"
"    padding: 0px 10px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\";\n"
"    selection-background-color: #7eb4d7;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox:focus, QLineEdit:focus {\n"
""
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
"    outline: 0; /* Removes the ugly dotted focus border */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 0px 15px;\n"
"    border-radius: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hover state for items inside the "
                        "dropdown */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: #ffffff;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(SectionAdviserEditorDialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(SectionAdviserEditorDialog)
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
"	background-color: rgb(248, 228, 92);\n"
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


        self.verticalLayout_3.addWidget(self.frame_header)

        self.widget_body = QWidget(SectionAdviserEditorDialog)
        self.widget_body.setObjectName(u"widget_body")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_body.sizePolicy().hasHeightForWidth())
        self.widget_body.setSizePolicy(sizePolicy)
        self.widget_body.setMinimumSize(QSize(550, 485))
        self.widget_body.setMaximumSize(QSize(550, 485))
        self.widget_body.setStyleSheet(u"#widget_body {\n"
"	background-color: #deddda;\n"
"	border: 1px solid #7a7a7a;\n"
"	border-top: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_body)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 12, -1, -1)
        self.label_24 = QLabel(self.widget_body)
        self.label_24.setObjectName(u"label_24")
        font1 = QFont()
        font1.setFamilies([u"Inter SemiBold"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"background: transparent;\n"
"font: 11pt \"Inter SemiBold\";")

        self.verticalLayout.addWidget(self.label_24)

        self.widget_1 = QWidget(self.widget_body)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_1)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 32))
        self.label_9.setMaximumSize(QSize(100, 32))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.cmb_section = QComboBox(self.widget_2)
        self.cmb_section.setObjectName(u"cmb_section")
        self.cmb_section.setMinimumSize(QSize(0, 32))
        self.cmb_section.setStyleSheet(u"")
        self.cmb_section.setEditable(False)

        self.horizontalLayout.addWidget(self.cmb_section)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_1)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 32))
        self.label_10.setMaximumSize(QSize(100, 32))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.cmb_teacher = QComboBox(self.widget_3)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 32))
        self.cmb_teacher.setMaximumSize(QSize(16777215, 32))
        self.cmb_teacher.setStyleSheet(u"")
        self.cmb_teacher.setEditable(False)

        self.horizontalLayout_3.addWidget(self.cmb_teacher)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget_1)

        self.table_section = QTableView(self.widget_body)
        self.table_section.setObjectName(u"table_section")
        self.table_section.setEnabled(False)
        self.table_section.setStyleSheet(u"QTableView {\n"
"    background-color: #f5f5f5;          \n"
"    alternate-background-color: #eaeaea;\n"
"    color: #2b2b2b;                     \n"
"    gridline-color: #d0d0d0;            \n"
"    border: 1px solid #bcbcbc;          \n"
"    selection-background-color: #7b7b7b;\n"
"    selection-color: #ffffff;           \n"
"    outline: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #e0e0e0;\n"
"    color: #1a1a1a;\n"
"    padding: 6px;\n"
"    border: 1px solid #bcbcbc;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: #cccccc;\n"
"    border: 1px solid #bcbcbc;\n"
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
"    b"
                        "ackground: #f8f8f8;\n"
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
        self.table_section.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_section.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_section.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_section)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(self.widget_body)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 16777215))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.widget_body)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 16777215))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.widget_body)


        self.retranslateUi(SectionAdviserEditorDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionAdviserEditorDialog)
    # setupUi

    def retranslateUi(self, SectionAdviserEditorDialog):
        SectionAdviserEditorDialog.setWindowTitle(QCoreApplication.translate("SectionAdviserEditorDialog", u"Section Adviser Editor", None))
        self.label_windowTitle.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Section Adviser Editor", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.label_24.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Assign an adviser to each section", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("SectionAdviserEditorDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Section:", None))
        self.widget_3.setProperty(u"class", QCoreApplication.translate("SectionAdviserEditorDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Adviser:", None))
        self.btnCancel.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("SectionAdviserEditorDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("SectionAdviserEditorDialog", u"button-green", None))
    # retranslateUi

