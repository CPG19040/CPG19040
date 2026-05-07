# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormEditStudent.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import resources_rc

class Ui_EditStudentDialog(object):
    def setupUi(self, EditStudentDialog):
        if not EditStudentDialog.objectName():
            EditStudentDialog.setObjectName(u"EditStudentDialog")
        EditStudentDialog.resize(890, 577)
        EditStudentDialog.setMinimumSize(QSize(890, 577))
        EditStudentDialog.setMaximumSize(QSize(890, 577))
        EditStudentDialog.setStyleSheet(u"background-color: rgb(222, 221, 218); color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(EditStudentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(EditStudentDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.spinBox_SY1 = QSpinBox(self.widget_3)
        self.spinBox_SY1.setObjectName(u"spinBox_SY1")
        self.spinBox_SY1.setMinimumSize(QSize(0, 30))
        self.spinBox_SY1.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.spinBox_SY1.setMinimum(2000)
        self.spinBox_SY1.setMaximum(3000)

        self.horizontalLayout_4.addWidget(self.spinBox_SY1)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.spinBox_SY2 = QSpinBox(self.widget_3)
        self.spinBox_SY2.setObjectName(u"spinBox_SY2")
        self.spinBox_SY2.setMinimumSize(QSize(0, 30))
        self.spinBox_SY2.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.spinBox_SY2.setMinimum(2000)
        self.spinBox_SY2.setMaximum(3000)

        self.horizontalLayout_4.addWidget(self.spinBox_SY2)

        self.btnRefreshSY = QPushButton(self.widget_3)
        self.btnRefreshSY.setObjectName(u"btnRefreshSY")
        self.btnRefreshSY.setMinimumSize(QSize(30, 30))
        self.btnRefreshSY.setMaximumSize(QSize(30, 30))
        self.btnRefreshSY.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Images/Images/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRefreshSY.setIcon(icon)
        self.btnRefreshSY.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.btnRefreshSY)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget_3)

        self.line_2 = QFrame(EditStudentDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.widget_2 = QWidget(EditStudentDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QComboBox, QLineEdit { padding: 0px 5px 0px; }")
        self.formLayout_2 = QFormLayout(self.widget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_profile_pic = QLabel(self.widget)
        self.label_profile_pic.setObjectName(u"label_profile_pic")
        self.label_profile_pic.setMinimumSize(QSize(99, 100))
        self.label_profile_pic.setMaximumSize(QSize(100, 100))
        self.label_profile_pic.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile_pic.setScaledContents(True)
        self.label_profile_pic.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_profile_pic, 0, 0, 1, 1)

        self.btnUploadPhoto = QPushButton(self.widget)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")

        self.gridLayout.addWidget(self.btnUploadPhoto, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.widget)

        self.widget_form = QWidget(self.widget_2)
        self.widget_form.setObjectName(u"widget_form")
        self.widget_form.setEnabled(True)
        self.widget_form.setStyleSheet(u"QWidget:disabled { color: rgba(0, 0, 0, 50); /* Very faded text */ background-color: rgba(200, 200, 200, 0); /* Faded background */}")
        self.formLayout = QFormLayout(self.widget_form)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.txtFirstName = QLineEdit(self.widget_form)
        self.txtFirstName.setObjectName(u"txtFirstName")
        self.txtFirstName.setMinimumSize(QSize(0, 30))
        self.txtFirstName.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtFirstName)

        self.label_9 = QLabel(self.widget_form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.txtMiddleName = QLineEdit(self.widget_form)
        self.txtMiddleName.setObjectName(u"txtMiddleName")
        self.txtMiddleName.setMinimumSize(QSize(0, 30))
        self.txtMiddleName.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtMiddleName)

        self.label_10 = QLabel(self.widget_form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.txtLastName = QLineEdit(self.widget_form)
        self.txtLastName.setObjectName(u"txtLastName")
        self.txtLastName.setMinimumSize(QSize(0, 30))
        self.txtLastName.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtLastName)

        self.label_11 = QLabel(self.widget_form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.cmbSection = QComboBox(self.widget_form)
        self.cmbSection.setObjectName(u"cmbSection")
        self.cmbSection.setMinimumSize(QSize(0, 30))
        self.cmbSection.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmbSection.setEditable(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbSection)

        self.label_13 = QLabel(self.widget_form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.cmbGender = QComboBox(self.widget_form)
        self.cmbGender.addItem("")
        self.cmbGender.addItem("")
        self.cmbGender.setObjectName(u"cmbGender")
        self.cmbGender.setMinimumSize(QSize(0, 30))
        self.cmbGender.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")
        self.cmbGender.setEditable(False)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbGender)


        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.widget_form)


        self.verticalLayout.addWidget(self.widget_2)

        self.line = QFrame(EditStudentDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_24 = QLabel(EditStudentDialog)
        self.label_24.setObjectName(u"label_24")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_24.setFont(font)

        self.verticalLayout.addWidget(self.label_24)

        self.widget_form_2 = QWidget(EditStudentDialog)
        self.widget_form_2.setObjectName(u"widget_form_2")
        self.widget_form_2.setEnabled(True)
        self.widget_form_2.setStyleSheet(u"QLineEdit { padding: 0px 5px 0px; }")
        self.formLayout_3 = QFormLayout(self.widget_form_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.txtContactPerson = QLineEdit(self.widget_form_2)
        self.txtContactPerson.setObjectName(u"txtContactPerson")
        self.txtContactPerson.setMinimumSize(QSize(0, 30))
        self.txtContactPerson.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtContactPerson)

        self.label_23 = QLabel(self.widget_form_2)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.txtContactNum = QLineEdit(self.widget_form_2)
        self.txtContactNum.setObjectName(u"txtContactNum")
        self.txtContactNum.setMinimumSize(QSize(0, 30))
        self.txtContactNum.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 10px 0px;")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtContactNum)

        self.label_22 = QLabel(self.widget_form_2)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_22)


        self.verticalLayout.addWidget(self.widget_form_2)

        self.line_3 = QFrame(EditStudentDialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.label_25 = QLabel(EditStudentDialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.verticalLayout.addWidget(self.label_25)

        self.txtPassword = QLineEdit(EditStudentDialog)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(0, 30))
        self.txtPassword.setStyleSheet(u"background-color: rgb(246, 245, 244); padding: 0px 5px 0px;")

        self.verticalLayout.addWidget(self.txtPassword)

        self.verticalSpacer = QSpacerItem(20, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(EditStudentDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnUpdate = QPushButton(EditStudentDialog)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnUpdate)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(EditStudentDialog)

        self.btnRefreshSY.setDefault(True)
        self.btnUpdate.setDefault(True)


        QMetaObject.connectSlotsByName(EditStudentDialog)
    # setupUi

    def retranslateUi(self, EditStudentDialog):
        EditStudentDialog.setWindowTitle(QCoreApplication.translate("EditStudentDialog", u"Student Information Editor", None))
        self.label_15.setText(QCoreApplication.translate("EditStudentDialog", u"School Year:", None))
        self.label_16.setText(QCoreApplication.translate("EditStudentDialog", u"-", None))
        self.btnRefreshSY.setText("")
        self.label_profile_pic.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("EditStudentDialog", u"Update photo", None))
        self.label_8.setText(QCoreApplication.translate("EditStudentDialog", u"First name", None))
        self.label_9.setText(QCoreApplication.translate("EditStudentDialog", u"Middle name", None))
        self.label_10.setText(QCoreApplication.translate("EditStudentDialog", u"Last name", None))
        self.label_11.setText(QCoreApplication.translate("EditStudentDialog", u"Section", None))
        self.label_13.setText(QCoreApplication.translate("EditStudentDialog", u"Gender", None))
        self.cmbGender.setItemText(0, QCoreApplication.translate("EditStudentDialog", u"Male", None))
        self.cmbGender.setItemText(1, QCoreApplication.translate("EditStudentDialog", u"Female", None))

        self.label_24.setText(QCoreApplication.translate("EditStudentDialog", u"Emergency contact", None))
        self.label_23.setText(QCoreApplication.translate("EditStudentDialog", u"Contact Number", None))
        self.label_22.setText(QCoreApplication.translate("EditStudentDialog", u"Contact Person", None))
        self.label_25.setText(QCoreApplication.translate("EditStudentDialog", u"Change Password", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("EditStudentDialog", u"Enter new password", None))
        self.btnCancel.setText(QCoreApplication.translate("EditStudentDialog", u"Cancel", None))
        self.btnUpdate.setText(QCoreApplication.translate("EditStudentDialog", u"Update", None))
    # retranslateUi

