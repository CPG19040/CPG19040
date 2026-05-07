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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SectionEditorDialog(object):
    def setupUi(self, SectionEditorDialog):
        if not SectionEditorDialog.objectName():
            SectionEditorDialog.setObjectName(u"SectionEditorDialog")
        SectionEditorDialog.resize(590, 214)
        SectionEditorDialog.setMinimumSize(QSize(590, 214))
        SectionEditorDialog.setMaximumSize(QSize(590, 214))
        SectionEditorDialog.setStyleSheet(u"background-color: rgb(222, 221, 218); color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(SectionEditorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_sectionId = QLabel(SectionEditorDialog)
        self.label_sectionId.setObjectName(u"label_sectionId")
        self.label_sectionId.setMinimumSize(QSize(0, 30))
        self.label_sectionId.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        self.label_sectionId.setFont(font)
        self.label_sectionId.setStyleSheet(u"background-color: transparent;")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_sectionId)

        self.label_8 = QLabel(SectionEditorDialog)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_9 = QLabel(SectionEditorDialog)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.txtSectionName = QLineEdit(SectionEditorDialog)
        self.txtSectionName.setObjectName(u"txtSectionName")
        self.txtSectionName.setMinimumSize(QSize(0, 30))
        self.txtSectionName.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtSectionName)

        self.label_10 = QLabel(SectionEditorDialog)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.cmb_teacher = QComboBox(SectionEditorDialog)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 30))
        self.cmb_teacher.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmb_teacher.setEditable(False)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmb_teacher)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(SectionEditorDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(SectionEditorDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SectionEditorDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionEditorDialog)
    # setupUi

    def retranslateUi(self, SectionEditorDialog):
        SectionEditorDialog.setWindowTitle(QCoreApplication.translate("SectionEditorDialog", u"Sections Editor", None))
        self.label_sectionId.setText("")
        self.label_8.setText(QCoreApplication.translate("SectionEditorDialog", u"Sectin Id:", None))
        self.label_9.setText(QCoreApplication.translate("SectionEditorDialog", u"Name:", None))
        self.label_10.setText(QCoreApplication.translate("SectionEditorDialog", u"Teacher:", None))
        self.btnCancel.setText(QCoreApplication.translate("SectionEditorDialog", u"Cancel", None))
        self.btnSave.setText(QCoreApplication.translate("SectionEditorDialog", u"Save", None))
    # retranslateUi

