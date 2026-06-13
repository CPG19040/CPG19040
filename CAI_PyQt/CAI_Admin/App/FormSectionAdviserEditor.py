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
        SectionAdviserEditorDialog.resize(546, 517)
        SectionAdviserEditorDialog.setStyleSheet(u"* {\n"
"	background-color: rgb(222, 221, 218); \n"
"	color: black;\n"
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
"QPushButton[class=\"button-green\"]:disabled {\n"
"    background: #A5D6A7;\n"
"    color: #E8F5E9;\n"
"    opacity:"
                        " 0.6;\n"
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
"*[class=\"input-field\"] {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit {\n"
""
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
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QComboBox:hover, QLineEdit:hover {\n"
"    border: 1px solid #"
                        "3498db;\n"
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
"/* Hover state for items inside the dropdown */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #7eb4d7;\n"
"    color: "
                        "#ffffff;\n"
"}")
        self.verticalLayout = QVBoxLayout(SectionAdviserEditorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_24 = QLabel(SectionAdviserEditorDialog)
        self.label_24.setObjectName(u"label_24")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_24.setFont(font)

        self.verticalLayout.addWidget(self.label_24)

        self.line = QFrame(SectionAdviserEditorDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(SectionAdviserEditorDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 30))
        self.label_9.setMaximumSize(QSize(100, 30))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.cmb_section = QComboBox(self.widget_2)
        self.cmb_section.setObjectName(u"cmb_section")
        self.cmb_section.setMinimumSize(QSize(0, 30))
        self.cmb_section.setStyleSheet(u"")
        self.cmb_section.setEditable(False)

        self.horizontalLayout.addWidget(self.cmb_section)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 30))
        self.label_10.setMaximumSize(QSize(100, 30))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.cmb_teacher = QComboBox(self.widget_3)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 30))
        self.cmb_teacher.setStyleSheet(u"")
        self.cmb_teacher.setEditable(False)

        self.horizontalLayout_3.addWidget(self.cmb_teacher)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        self.table_section = QTableView(SectionAdviserEditorDialog)
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

        self.verticalLayout.addWidget(self.table_section)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(SectionAdviserEditorDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 16777215))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(SectionAdviserEditorDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 16777215))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SectionAdviserEditorDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionAdviserEditorDialog)
    # setupUi

    def retranslateUi(self, SectionAdviserEditorDialog):
        SectionAdviserEditorDialog.setWindowTitle(QCoreApplication.translate("SectionAdviserEditorDialog", u"Dialog", None))
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

