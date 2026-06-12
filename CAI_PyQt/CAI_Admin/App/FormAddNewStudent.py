# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormAddNewStudent.ui'
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
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
import resources_rc

class Ui_AddNewStudentDialog(object):
    def setupUi(self, AddNewStudentDialog):
        if not AddNewStudentDialog.objectName():
            AddNewStudentDialog.setObjectName(u"AddNewStudentDialog")
        AddNewStudentDialog.setEnabled(True)
        AddNewStudentDialog.resize(870, 649)
        AddNewStudentDialog.setMinimumSize(QSize(870, 580))
        AddNewStudentDialog.setStyleSheet(u"* {\n"
"	background-color: rgb(222, 221, 218); \n"
"	color: black;\n"
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
"QPushButton[class=\"button-green\"] {\n"
"	border: 1px "
                        "solid #0a5128;\n"
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
"    opacity: 0.6;\n"
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
"QLabel:disabled {\n"
"	color: #aaaaaa;\n"
"	border: none;\n"
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
"*[class=\"input-field\"] QPushButton:disabled, \n"
"*[class=\"input-field\"] QLineEdit:disabled, \n"
"*[class=\"input-field\"] QComboBox:disabled  {\n"
"    background-color: #f5f5f5;\n"
"	border: none;\n"
"	color: #aeaeae"
                        ";\n"
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
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
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
""
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
"    color: #ffffff;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    color: #aaaaaa;\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/Images/Images/caret-down-disabled.png);\n"
"}\n"
"\n"
"QSpinBox {\n"
"	font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-colo"
                        "r: #ffffff;\n"
"    color: #333333;\n"
"    selection-background-color: #7eb4d7;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #007BFF;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-bottom-right-radius: 15px;\n"
"    padding: 6px 10px 6px 2px;\n"
"	color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Images/Images/caret-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}")
        self.verticalLayout = QVBoxLayout(AddNewStudentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AddNewStudentDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.spinBox_SY1 = QSpinBox(self.widget)
        self.spinBox_SY1.setObjectName(u"spinBox_SY1")
        self.spinBox_SY1.setMinimumSize(QSize(80, 30))
        self.spinBox_SY1.setMaximumSize(QSize(80, 30))
        self.spinBox_SY1.setStyleSheet(u"")
        self.spinBox_SY1.setAlignment(Qt.AlignCenter)
        self.spinBox_SY1.setMinimum(2000)
        self.spinBox_SY1.setMaximum(3000)

        self.horizontalLayout_4.addWidget(self.spinBox_SY1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.spinBox_SY2 = QSpinBox(self.widget)
        self.spinBox_SY2.setObjectName(u"spinBox_SY2")
        self.spinBox_SY2.setMinimumSize(QSize(80, 30))
        self.spinBox_SY2.setMaximumSize(QSize(80, 30))
        self.spinBox_SY2.setStyleSheet(u"")
        self.spinBox_SY2.setAlignment(Qt.AlignCenter)
        self.spinBox_SY2.setMinimum(2000)
        self.spinBox_SY2.setMaximum(3000)

        self.horizontalLayout_4.addWidget(self.spinBox_SY2)

        self.btnRefreshSY = QPushButton(self.widget)
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


        self.verticalLayout.addWidget(self.widget)

        self.line_3 = QFrame(AddNewStudentDialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.widget_stud_info = QWidget(AddNewStudentDialog)
        self.widget_stud_info.setObjectName(u"widget_stud_info")
        self.widget_stud_info.setEnabled(True)
        self.widget_stud_info.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_stud_info)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.widget_stud_info)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_profile_pic = QLabel(self.widget_3)
        self.label_profile_pic.setObjectName(u"label_profile_pic")
        self.label_profile_pic.setMinimumSize(QSize(150, 150))
        self.label_profile_pic.setMaximumSize(QSize(150, 150))
        self.label_profile_pic.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile_pic.setScaledContents(True)
        self.label_profile_pic.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_profile_pic, 0, 0, 1, 1)

        self.btnUploadPhoto = QPushButton(self.widget_3)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")
        self.btnUploadPhoto.setMinimumSize(QSize(100, 30))
        self.btnUploadPhoto.setMaximumSize(QSize(16777215, 30))
        self.btnUploadPhoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnUploadPhoto, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_form = QWidget(self.widget_stud_info)
        self.widget_form.setObjectName(u"widget_form")
        self.widget_form.setEnabled(True)
        self.widget_form.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(100, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 30))
        self.label_8.setMaximumSize(QSize(100, 30))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.txtFirstName = QLineEdit(self.widget_2)
        self.txtFirstName.setObjectName(u"txtFirstName")
        self.txtFirstName.setMinimumSize(QSize(0, 30))
        self.txtFirstName.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.txtFirstName)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget_form)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 30))
        self.label_9.setMaximumSize(QSize(100, 30))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.txtMiddleName = QLineEdit(self.widget_4)
        self.txtMiddleName.setObjectName(u"txtMiddleName")
        self.txtMiddleName.setMinimumSize(QSize(0, 30))
        self.txtMiddleName.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.txtMiddleName)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_form)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 30))
        self.label_10.setMaximumSize(QSize(100, 30))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.txtLastName = QLineEdit(self.widget_5)
        self.txtLastName.setObjectName(u"txtLastName")
        self.txtLastName.setMinimumSize(QSize(0, 30))
        self.txtLastName.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.txtLastName)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_form)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 30))
        self.label_11.setMaximumSize(QSize(100, 30))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.cmbSection = QComboBox(self.widget_6)
        self.cmbSection.setObjectName(u"cmbSection")
        self.cmbSection.setMinimumSize(QSize(0, 30))
        self.cmbSection.setStyleSheet(u"")
        self.cmbSection.setEditable(False)

        self.horizontalLayout_8.addWidget(self.cmbSection)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_form)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 30))
        self.label_12.setMaximumSize(QSize(100, 30))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.txtPassword = QLineEdit(self.widget_7)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(0, 30))
        self.txtPassword.setStyleSheet(u"")
        self.txtPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_9.addWidget(self.txtPassword)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_form)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 30))
        self.label_13.setMaximumSize(QSize(100, 30))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.cmbGender = QComboBox(self.widget_8)
        self.cmbGender.addItem("")
        self.cmbGender.addItem("")
        self.cmbGender.setObjectName(u"cmbGender")
        self.cmbGender.setMinimumSize(QSize(0, 30))
        self.cmbGender.setStyleSheet(u"")
        self.cmbGender.setEditable(False)

        self.horizontalLayout_10.addWidget(self.cmbGender)


        self.verticalLayout_2.addWidget(self.widget_8)


        self.horizontalLayout.addWidget(self.widget_form)


        self.verticalLayout.addWidget(self.widget_stud_info)

        self.line_2 = QFrame(AddNewStudentDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.widget_form_emergency = QWidget(AddNewStudentDialog)
        self.widget_form_emergency.setObjectName(u"widget_form_emergency")
        self.widget_form_emergency.setEnabled(True)
        self.widget_form_emergency.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_form_emergency)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_24 = QLabel(self.widget_form_emergency)
        self.label_24.setObjectName(u"label_24")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_24.setFont(font)

        self.verticalLayout_3.addWidget(self.label_24)

        self.widget_10 = QWidget(self.widget_form_emergency)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(120, 30))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_22)

        self.txtContactPerson = QLineEdit(self.widget_10)
        self.txtContactPerson.setObjectName(u"txtContactPerson")
        self.txtContactPerson.setMinimumSize(QSize(0, 30))
        self.txtContactPerson.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.txtContactPerson)


        self.verticalLayout_3.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_form_emergency)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(120, 30))
        self.label_23.setMaximumSize(QSize(16777215, 30))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.txtContactNum = QLineEdit(self.widget_11)
        self.txtContactNum.setObjectName(u"txtContactNum")
        self.txtContactNum.setMinimumSize(QSize(0, 30))
        self.txtContactNum.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.txtContactNum)


        self.verticalLayout_3.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_form_emergency)

        self.line = QFrame(AddNewStudentDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.rb_importCSV = QRadioButton(AddNewStudentDialog)
        self.rb_importCSV.setObjectName(u"rb_importCSV")
        self.rb_importCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.rb_importCSV)

        self.widget_CSV = QWidget(AddNewStudentDialog)
        self.widget_CSV.setObjectName(u"widget_CSV")
        self.widget_CSV.setEnabled(False)
        self.widget_CSV.setStyleSheet(u"QLineEdit {\n"
"	background-color: #ffffff;\n"
"	color: black;\n"
"	border: 1px solid #999;\n"
"	border-right: none;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	padding: 0px 10px;\n"
"}\n"
"\n"
"#btnBrowseCSV {\n"
"	font: 10pt \"Inter\";\n"
"	background-color: #e7e7e7;\n"
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
"#btnBrowseCSV:disabled, QLabel:disabled {\n"
"	background-color: rgb(192, 191, 188);\n"
"	border: none;\n"
"	color: #aeaeae;\n"
"}\n"
"\n"
"#widget_CSV QLineEdit:disabled {\n"
"	background-color: #f5f5f5;\n"
"	border: none;\n"
"	color: #aeaeae;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_CSV)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_12 = QWidget(self.widget_CSV)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_14.addWidget(self.label_14)

        self.cmbSection_2 = QComboBox(self.widget_12)
        self.cmbSection_2.setObjectName(u"cmbSection_2")
        self.cmbSection_2.setMinimumSize(QSize(0, 30))
        self.cmbSection_2.setMaximumSize(QSize(16777215, 30))
        self.cmbSection_2.setStyleSheet(u"")
        self.cmbSection_2.setEditable(False)

        self.horizontalLayout_14.addWidget(self.cmbSection_2)


        self.horizontalLayout_3.addWidget(self.widget_12)

        self.widget_9 = QWidget(self.widget_CSV)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.txtCSVPath = QLineEdit(self.widget_9)
        self.txtCSVPath.setObjectName(u"txtCSVPath")
        self.txtCSVPath.setMinimumSize(QSize(0, 30))
        self.txtCSVPath.setMaximumSize(QSize(16777215, 30))
        self.txtCSVPath.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.txtCSVPath)

        self.btnBrowseCSV = QPushButton(self.widget_9)
        self.btnBrowseCSV.setObjectName(u"btnBrowseCSV")
        self.btnBrowseCSV.setMinimumSize(QSize(100, 30))
        self.btnBrowseCSV.setMaximumSize(QSize(100, 30))
        self.btnBrowseCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBrowseCSV.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnBrowseCSV)


        self.horizontalLayout_3.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget_CSV)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progressBar = QProgressBar(AddNewStudentDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(AddNewStudentDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(AddNewStudentDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 30))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(AddNewStudentDialog)

        self.btnRefreshSY.setDefault(True)
        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(AddNewStudentDialog)
    # setupUi

    def retranslateUi(self, AddNewStudentDialog):
        AddNewStudentDialog.setWindowTitle(QCoreApplication.translate("AddNewStudentDialog", u"Student Registration", None))
        self.label_15.setText(QCoreApplication.translate("AddNewStudentDialog", u"School Year:", None))
        self.label_16.setText(QCoreApplication.translate("AddNewStudentDialog", u"-", None))
        self.btnRefreshSY.setText("")
        self.btnRefreshSY.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
#if QT_CONFIG(tooltip)
        self.label_profile_pic.setToolTip(QCoreApplication.translate("AddNewStudentDialog", u"Aspect Ratio (1:1)", None))
#endif // QT_CONFIG(tooltip)
        self.label_profile_pic.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("AddNewStudentDialog", u"Update photo", None))
        self.btnUploadPhoto.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_8.setText(QCoreApplication.translate("AddNewStudentDialog", u"First name", None))
        self.widget_4.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("AddNewStudentDialog", u"Middle name", None))
        self.widget_5.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("AddNewStudentDialog", u"Last name", None))
        self.widget_6.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_11.setText(QCoreApplication.translate("AddNewStudentDialog", u"Section", None))
        self.widget_7.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_12.setText(QCoreApplication.translate("AddNewStudentDialog", u"Password", None))
        self.widget_8.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_13.setText(QCoreApplication.translate("AddNewStudentDialog", u"Gender", None))
        self.cmbGender.setItemText(0, QCoreApplication.translate("AddNewStudentDialog", u"Male", None))
        self.cmbGender.setItemText(1, QCoreApplication.translate("AddNewStudentDialog", u"Female", None))

        self.label_24.setText(QCoreApplication.translate("AddNewStudentDialog", u"Emergency contact", None))
        self.widget_10.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_22.setText(QCoreApplication.translate("AddNewStudentDialog", u"Contact Person", None))
        self.widget_11.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_23.setText(QCoreApplication.translate("AddNewStudentDialog", u"Contact Number", None))
        self.rb_importCSV.setText(QCoreApplication.translate("AddNewStudentDialog", u"Import from CSV", None))
        self.widget_12.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_14.setText(QCoreApplication.translate("AddNewStudentDialog", u"Section", None))
        self.cmbSection_2.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"combobox-normal", None))
        self.btnBrowseCSV.setText(QCoreApplication.translate("AddNewStudentDialog", u"Browse", None))
        self.btnCancel.setText(QCoreApplication.translate("AddNewStudentDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("AddNewStudentDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-green", None))
    # retranslateUi

