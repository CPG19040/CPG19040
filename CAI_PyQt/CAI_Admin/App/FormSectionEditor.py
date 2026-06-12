# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormSectionEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_SectionEditorDialog(object):
    def setupUi(self, SectionEditorDialog):
        if not SectionEditorDialog.objectName():
            SectionEditorDialog.setObjectName(u"SectionEditorDialog")
        SectionEditorDialog.resize(590, 214)
        SectionEditorDialog.setMinimumSize(QSize(590, 214))
        SectionEditorDialog.setMaximumSize(QSize(590, 214))
        SectionEditorDialog.setStyleSheet(u"* {\n"
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
"*[class=\"input-field\"] QLabel, #label_8 {\n"
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
"    border: 1"
                        "px solid #3498db;\n"
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
" "
                        "   color: #ffffff;\n"
"}")
        self.verticalLayout = QVBoxLayout(SectionEditorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(SectionEditorDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#label_sectionId {\n"
"	background-color: #FFF;\n"
"	border: 1px solid #999;\n"
"	border-left: none;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(100, 16777215))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_sectionId = QLabel(self.widget_3)
        self.label_sectionId.setObjectName(u"label_sectionId")
        self.label_sectionId.setMinimumSize(QSize(100, 30))
        self.label_sectionId.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        self.label_sectionId.setFont(font)
        self.label_sectionId.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_sectionId)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget = QWidget(SectionEditorDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 30))
        self.label_9.setMaximumSize(QSize(100, 30))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.txtSectionName = QLineEdit(self.widget)
        self.txtSectionName.setObjectName(u"txtSectionName")
        self.txtSectionName.setMinimumSize(QSize(0, 30))
        self.txtSectionName.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.horizontalLayout.addWidget(self.txtSectionName)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(SectionEditorDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.cmb_teacher = QComboBox(self.widget_2)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 30))
        self.cmb_teacher.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmb_teacher.setEditable(False)

        self.horizontalLayout_3.addWidget(self.cmb_teacher)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(SectionEditorDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(SectionEditorDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SectionEditorDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionEditorDialog)
    # setupUi

    def retranslateUi(self, SectionEditorDialog):
        SectionEditorDialog.setWindowTitle(QCoreApplication.translate("SectionEditorDialog", u"Sections Editor", None))
        self.label_8.setText(QCoreApplication.translate("SectionEditorDialog", u"Sectin Id:", None))
        self.label_sectionId.setText("")
        self.widget.setProperty(u"class", QCoreApplication.translate("SectionEditorDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("SectionEditorDialog", u"Name:", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("SectionEditorDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("SectionEditorDialog", u"Teacher:", None))
        self.btnCancel.setText(QCoreApplication.translate("SectionEditorDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("SectionEditorDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("SectionEditorDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("SectionEditorDialog", u"button-green", None))
    # retranslateUi

