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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_EditUserDialog(object):
    def setupUi(self, EditUserDialog):
        if not EditUserDialog.objectName():
            EditUserDialog.setObjectName(u"EditUserDialog")
        EditUserDialog.resize(790, 525)
        EditUserDialog.setMinimumSize(QSize(790, 525))
        EditUserDialog.setMaximumSize(QSize(790, 525))
        EditUserDialog.setStyleSheet(u"* {\n"
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
        EditUserDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(EditUserDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(EditUserDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
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
        self.btnUploadPhoto.setMinimumSize(QSize(0, 30))
        self.btnUploadPhoto.setMaximumSize(QSize(16777215, 30))
        self.btnUploadPhoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnUploadPhoto, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)

        self.grp_info = QWidget(self.widget)
        self.grp_info.setObjectName(u"grp_info")
        self.verticalLayout_2 = QVBoxLayout(self.grp_info)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.grp_info)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 30))
        self.label_8.setMaximumSize(QSize(120, 30))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.lineEdit_firstname = QLineEdit(self.widget_2)
        self.lineEdit_firstname.setObjectName(u"lineEdit_firstname")
        self.lineEdit_firstname.setMinimumSize(QSize(0, 30))
        self.lineEdit_firstname.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lineEdit_firstname)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.grp_info)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(120, 30))
        self.label_9.setMaximumSize(QSize(120, 30))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.lineEdit_middlename = QLineEdit(self.widget_4)
        self.lineEdit_middlename.setObjectName(u"lineEdit_middlename")
        self.lineEdit_middlename.setMinimumSize(QSize(0, 30))
        self.lineEdit_middlename.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.lineEdit_middlename)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.grp_info)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(120, 30))
        self.label_10.setMaximumSize(QSize(120, 30))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.lineEdit_lastname = QLineEdit(self.widget_5)
        self.lineEdit_lastname.setObjectName(u"lineEdit_lastname")
        self.lineEdit_lastname.setMinimumSize(QSize(0, 30))
        self.lineEdit_lastname.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lineEdit_lastname)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.grp_info)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(120, 30))
        self.label_11.setMaximumSize(QSize(120, 30))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.lineEdit_username = QLineEdit(self.widget_6)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMinimumSize(QSize(0, 30))
        self.lineEdit_username.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.lineEdit_username)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.grp_info)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(120, 30))
        self.label_13.setMaximumSize(QSize(120, 30))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.comboBox_position = QComboBox(self.widget_7)
        self.comboBox_position.setObjectName(u"comboBox_position")
        self.comboBox_position.setMinimumSize(QSize(0, 30))
        self.comboBox_position.setStyleSheet(u"")
        self.comboBox_position.setEditable(True)

        self.horizontalLayout_7.addWidget(self.comboBox_position)


        self.verticalLayout_2.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.grp_info)


        self.verticalLayout.addWidget(self.widget)

        self.line = QFrame(EditUserDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget_form_3 = QWidget(EditUserDialog)
        self.widget_form_3.setObjectName(u"widget_form_3")
        self.widget_form_3.setEnabled(True)
        self.widget_form_3.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_form_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_25 = QLabel(self.widget_form_3)
        self.label_25.setObjectName(u"label_25")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_25.setFont(font)

        self.verticalLayout_3.addWidget(self.label_25)

        self.widget_8 = QWidget(self.widget_form_3)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.lineEdit_password = QLineEdit(self.widget_8)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 30))
        self.lineEdit_password.setStyleSheet(u"")
        self.lineEdit_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_8.addWidget(self.lineEdit_password)


        self.verticalLayout_3.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.widget_form_3)

        self.widget_form_2 = QWidget(EditUserDialog)
        self.widget_form_2.setObjectName(u"widget_form_2")
        self.widget_form_2.setEnabled(True)
        self.widget_form_2.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_form_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_24 = QLabel(self.widget_form_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.verticalLayout_4.addWidget(self.label_24)

        self.widget_9 = QWidget(self.widget_form_2)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(120, 30))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_22)

        self.txtContactPerson = QLineEdit(self.widget_9)
        self.txtContactPerson.setObjectName(u"txtContactPerson")
        self.txtContactPerson.setMinimumSize(QSize(0, 30))
        self.txtContactPerson.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.txtContactPerson)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.widget_11 = QWidget(self.widget_form_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(120, 30))
        self.label_23.setMaximumSize(QSize(16777215, 30))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_23)

        self.txtContactNum = QLineEdit(self.widget_11)
        self.txtContactNum.setObjectName(u"txtContactNum")
        self.txtContactNum.setMinimumSize(QSize(0, 30))
        self.txtContactNum.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.txtContactNum)


        self.verticalLayout_4.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_form_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(EditUserDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnUpdate = QPushButton(EditUserDialog)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setMinimumSize(QSize(100, 30))
        self.btnUpdate.setMaximumSize(QSize(100, 30))
        self.btnUpdate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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
        self.btnUploadPhoto.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"button-normal", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_8.setText(QCoreApplication.translate("EditUserDialog", u"First name", None))
        self.widget_4.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("EditUserDialog", u"Middle name", None))
        self.widget_5.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("EditUserDialog", u"Last name", None))
        self.widget_6.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_11.setText(QCoreApplication.translate("EditUserDialog", u"User name", None))
        self.widget_7.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_13.setText(QCoreApplication.translate("EditUserDialog", u"Position", None))
        self.label_25.setText(QCoreApplication.translate("EditUserDialog", u"Change Password", None))
        self.widget_8.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_12.setText(QCoreApplication.translate("EditUserDialog", u"Password", None))
        self.label_24.setText(QCoreApplication.translate("EditUserDialog", u"Emergency contact", None))
        self.widget_9.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_22.setText(QCoreApplication.translate("EditUserDialog", u"Contact Person", None))
        self.widget_11.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"input-field", None))
        self.label_23.setText(QCoreApplication.translate("EditUserDialog", u"Contact Number", None))
        self.btnCancel.setText(QCoreApplication.translate("EditUserDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"button-normal", None))
        self.btnUpdate.setText(QCoreApplication.translate("EditUserDialog", u"Update", None))
        self.btnUpdate.setProperty(u"class", QCoreApplication.translate("EditUserDialog", u"button-green", None))
    # retranslateUi

