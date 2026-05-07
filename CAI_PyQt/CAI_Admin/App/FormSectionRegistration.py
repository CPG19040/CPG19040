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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SectionRegistrationDialog(object):
    def setupUi(self, SectionRegistrationDialog):
        if not SectionRegistrationDialog.objectName():
            SectionRegistrationDialog.setObjectName(u"SectionRegistrationDialog")
        SectionRegistrationDialog.resize(590, 187)
        SectionRegistrationDialog.setMinimumSize(QSize(590, 187))
        SectionRegistrationDialog.setMaximumSize(QSize(590, 187))
        SectionRegistrationDialog.setStyleSheet(u"background-color: rgb(222, 221, 218); color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(SectionRegistrationDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_9 = QLabel(SectionRegistrationDialog)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.txtSectionName = QLineEdit(SectionRegistrationDialog)
        self.txtSectionName.setObjectName(u"txtSectionName")
        self.txtSectionName.setMinimumSize(QSize(0, 30))
        self.txtSectionName.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtSectionName)

        self.label_10 = QLabel(SectionRegistrationDialog)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.cmb_teacher = QComboBox(SectionRegistrationDialog)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 30))
        self.cmb_teacher.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmb_teacher.setEditable(False)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmb_teacher)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(SectionRegistrationDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(SectionRegistrationDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SectionRegistrationDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionRegistrationDialog)
    # setupUi

    def retranslateUi(self, SectionRegistrationDialog):
        SectionRegistrationDialog.setWindowTitle(QCoreApplication.translate("SectionRegistrationDialog", u"Section Registration", None))
        self.label_9.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Name:", None))
        self.label_10.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Adviser:", None))
        self.btnCancel.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Cancel", None))
        self.btnSave.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Save", None))
    # retranslateUi

