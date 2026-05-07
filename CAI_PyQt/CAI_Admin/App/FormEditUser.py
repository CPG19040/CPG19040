# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormEditUser.ui'
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
    QVBoxLayout, QWidget)
import resources_rc

class Ui_EditUserDialog(object):
    def setupUi(self, EditUserDialog):
        if not EditUserDialog.objectName():
            EditUserDialog.setObjectName(u"EditUserDialog")
        EditUserDialog.resize(790, 604)
        EditUserDialog.setMinimumSize(QSize(790, 604))
        EditUserDialog.setMaximumSize(QSize(790, 604))
        EditUserDialog.setStyleSheet(u"background-color: rgb(222, 221, 218); color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(EditUserDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(EditUserDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QComboBox, QLineEdit { padding: 0px 5px 0px; }")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_profile_pic = QLabel(self.widget_3)
        self.label_profile_pic.setObjectName(u"label_profile_pic")
        self.label_profile_pic.setMinimumSize(QSize(160, 160))
        self.label_profile_pic.setMaximumSize(QSize(160, 160))
        self.label_profile_pic.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile_pic.setScaledContents(True)
        self.label_profile_pic.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_profile_pic, 0, 0, 1, 1)

        self.btnUploadPhoto = QPushButton(self.widget_3)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")

        self.gridLayout.addWidget(self.btnUploadPhoto, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)

        self.grp_info = QWidget(self.widget)
        self.grp_info.setObjectName(u"grp_info")
        self.formLayout_3 = QFormLayout(self.grp_info)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.grp_info)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.lineEdit_firstname = QLineEdit(self.grp_info)
        self.lineEdit_firstname.setObjectName(u"lineEdit_firstname")
        self.lineEdit_firstname.setMinimumSize(QSize(0, 30))
        self.lineEdit_firstname.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_firstname)

        self.label_9 = QLabel(self.grp_info)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.lineEdit_middlename = QLineEdit(self.grp_info)
        self.lineEdit_middlename.setObjectName(u"lineEdit_middlename")
        self.lineEdit_middlename.setMinimumSize(QSize(0, 30))
        self.lineEdit_middlename.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_middlename)

        self.label_10 = QLabel(self.grp_info)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.lineEdit_lastname = QLineEdit(self.grp_info)
        self.lineEdit_lastname.setObjectName(u"lineEdit_lastname")
        self.lineEdit_lastname.setMinimumSize(QSize(0, 30))
        self.lineEdit_lastname.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_lastname)

        self.label_11 = QLabel(self.grp_info)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.lineEdit_username = QLineEdit(self.grp_info)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMinimumSize(QSize(0, 30))
        self.lineEdit_username.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_username)

        self.comboBox_position = QComboBox(self.grp_info)
        self.comboBox_position.setObjectName(u"comboBox_position")
        self.comboBox_position.setMinimumSize(QSize(0, 30))
        self.comboBox_position.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.comboBox_position.setEditable(True)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboBox_position)

        self.label_13 = QLabel(self.grp_info)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_13)


        self.horizontalLayout.addWidget(self.grp_info)


        self.verticalLayout.addWidget(self.widget)

        self.line = QFrame(EditUserDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.grp_recovery = QWidget(EditUserDialog)
        self.grp_recovery.setObjectName(u"grp_recovery")
        self.grp_recovery.setStyleSheet(u"QComboBox, QLineEdit { padding: 0px 5px 0px; }")
        self.formLayout_4 = QFormLayout(self.grp_recovery)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_14 = QLabel(self.grp_recovery)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.comboBox_recoveryQuestion = QComboBox(self.grp_recovery)
        self.comboBox_recoveryQuestion.setObjectName(u"comboBox_recoveryQuestion")
        self.comboBox_recoveryQuestion.setMinimumSize(QSize(0, 30))
        self.comboBox_recoveryQuestion.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.comboBox_recoveryQuestion.setEditable(True)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_recoveryQuestion)

        self.labelAnswer_2 = QLabel(self.grp_recovery)
        self.labelAnswer_2.setObjectName(u"labelAnswer_2")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelAnswer_2)

        self.lineEdit_Answer = QLineEdit(self.grp_recovery)
        self.lineEdit_Answer.setObjectName(u"lineEdit_Answer")
        self.lineEdit_Answer.setMinimumSize(QSize(0, 30))
        self.lineEdit_Answer.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_Answer)


        self.verticalLayout.addWidget(self.grp_recovery)

        self.widget_form_3 = QWidget(EditUserDialog)
        self.widget_form_3.setObjectName(u"widget_form_3")
        self.widget_form_3.setEnabled(True)
        self.widget_form_3.setStyleSheet(u"QLineEdit { padding: 0px 5px 0px; }")
        self.formLayout_6 = QFormLayout(self.widget_form_3)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_25 = QLabel(self.widget_form_3)
        self.label_25.setObjectName(u"label_25")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_25.setFont(font)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.label_12 = QLabel(self.widget_form_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.lineEdit_password = QLineEdit(self.widget_form_3)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 30))
        self.lineEdit_password.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_password)


        self.verticalLayout.addWidget(self.widget_form_3)

        self.widget_form_2 = QWidget(EditUserDialog)
        self.widget_form_2.setObjectName(u"widget_form_2")
        self.widget_form_2.setEnabled(True)
        self.widget_form_2.setStyleSheet(u"QWidget:disabled { color: rgba(0, 0, 0, 50); /* Very faded text */ background-color: rgba(200, 200, 200, 0); /* Faded background */}\n"
"QLineEdit { padding: 0px 5px 0px; }")
        self.formLayout_5 = QFormLayout(self.widget_form_2)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_24 = QLabel(self.widget_form_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.txtContactPerson = QLineEdit(self.widget_form_2)
        self.txtContactPerson.setObjectName(u"txtContactPerson")
        self.txtContactPerson.setMinimumSize(QSize(0, 30))
        self.txtContactPerson.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtContactPerson)

        self.label_23 = QLabel(self.widget_form_2)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.txtContactNum = QLineEdit(self.widget_form_2)
        self.txtContactNum.setObjectName(u"txtContactNum")
        self.txtContactNum.setMinimumSize(QSize(0, 30))
        self.txtContactNum.setStyleSheet(u"background-color: rgb(246, 245, 244);")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtContactNum)

        self.label_22 = QLabel(self.widget_form_2)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_22)


        self.verticalLayout.addWidget(self.widget_form_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(EditUserDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnUpdate = QPushButton(EditUserDialog)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnUpdate)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(EditUserDialog)

        self.btnUpdate.setDefault(True)


        QMetaObject.connectSlotsByName(EditUserDialog)
    # setupUi

    def retranslateUi(self, EditUserDialog):
        EditUserDialog.setWindowTitle(QCoreApplication.translate("EditUserDialog", u"User Information", None))
        self.label_profile_pic.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("EditUserDialog", u"Update photo", None))
        self.label_8.setText(QCoreApplication.translate("EditUserDialog", u"First name", None))
        self.label_9.setText(QCoreApplication.translate("EditUserDialog", u"Middle name", None))
        self.label_10.setText(QCoreApplication.translate("EditUserDialog", u"Last name", None))
        self.label_11.setText(QCoreApplication.translate("EditUserDialog", u"User name", None))
        self.label_13.setText(QCoreApplication.translate("EditUserDialog", u"Position", None))
        self.label_14.setText(QCoreApplication.translate("EditUserDialog", u"Recovery question", None))
        self.labelAnswer_2.setText(QCoreApplication.translate("EditUserDialog", u"Answer", None))
        self.label_25.setText(QCoreApplication.translate("EditUserDialog", u"Change Password", None))
        self.label_12.setText(QCoreApplication.translate("EditUserDialog", u"Password", None))
        self.label_24.setText(QCoreApplication.translate("EditUserDialog", u"Emergency contact", None))
        self.label_23.setText(QCoreApplication.translate("EditUserDialog", u"Contact Number", None))
        self.label_22.setText(QCoreApplication.translate("EditUserDialog", u"Contact Person", None))
        self.btnCancel.setText(QCoreApplication.translate("EditUserDialog", u"Cancel", None))
        self.btnUpdate.setText(QCoreApplication.translate("EditUserDialog", u"Update", None))
    # retranslateUi

