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
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_SectionAdviserEditorDialog(object):
    def setupUi(self, SectionAdviserEditorDialog):
        if not SectionAdviserEditorDialog.objectName():
            SectionAdviserEditorDialog.setObjectName(u"SectionAdviserEditorDialog")
        SectionAdviserEditorDialog.resize(546, 517)
        SectionAdviserEditorDialog.setStyleSheet(u"background-color: rgb(222, 221, 218); color: rgb(0, 0, 0);")
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

        self.widget = QWidget(SectionAdviserEditorDialog)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.cmb_section = QComboBox(self.widget)
        self.cmb_section.setObjectName(u"cmb_section")
        self.cmb_section.setMinimumSize(QSize(0, 30))
        self.cmb_section.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmb_section.setEditable(False)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmb_section)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.cmb_teacher = QComboBox(self.widget)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 30))
        self.cmb_teacher.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmb_teacher.setEditable(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmb_teacher)


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
        self.btnCancel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(SectionAdviserEditorDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SectionAdviserEditorDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionAdviserEditorDialog)
    # setupUi

    def retranslateUi(self, SectionAdviserEditorDialog):
        SectionAdviserEditorDialog.setWindowTitle(QCoreApplication.translate("SectionAdviserEditorDialog", u"Dialog", None))
        self.label_24.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Assign an adviser to each section", None))
        self.label_9.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Section:", None))
        self.label_10.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Adviser:", None))
        self.btnCancel.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Cancel", None))
        self.btnSave.setText(QCoreApplication.translate("SectionAdviserEditorDialog", u"Save", None))
    # retranslateUi

