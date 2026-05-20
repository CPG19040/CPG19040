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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_AddNewStudentDialog(object):
    def setupUi(self, AddNewStudentDialog):
        if not AddNewStudentDialog.objectName():
            AddNewStudentDialog.setObjectName(u"AddNewStudentDialog")
        AddNewStudentDialog.resize(870, 590)
        AddNewStudentDialog.setMinimumSize(QSize(870, 580))
        AddNewStudentDialog.setStyleSheet(u"* {\n"
"	background-color: rgb(222, 221, 218); \n"
"	color: black;\n"
"}\n"
"\n"
"*[class=\"button-normal\"] {\n"
"	font: 10pt \"Inter\";\n"
"	background-color: #e7e7e7;\n"
"	color: black;\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(154, 153, 150);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:hover {\n"
"	background-color: white;\n"
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
"QPushButton:disabled, QLineEdit:disabled, QComboBox:disabled {\n"
"    background-color: #d5d6d7;\n"
"    color: #7f8c8d;\n"
"    border: 1px solid #95a5a6;\n"
"}\n"
"\n"
"#widget_CSV:disabled, #widget_stud_info:disabled, QComboBox:disabled { \n"
"	color: rgba(0, 0, 0, 50); \n"
"	background-color: rgba(200, 200, 200, 0); \n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(255, 255, 255); \n"
"	border-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	padding: 0px 15px;\n"
"}\n"
"\n"
"QC"
                        "omboBox {\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px; /* Fully rounded pills */\n"
"    padding: 0px 15px 0px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font: 10pt \"Inter Medium\"; /* Consolidated font settings */\n"
"    selection-background-color: #7eb4d7;\n"
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
"    background-color: white !important;"
                        "\n"
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
"    color: #ffffff;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px 0px;\n"
"    background-color: #ffffff;\n"
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
"    h"
                        "eight: 8px;\n"
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
        self.widget_form.setStyleSheet(u"QWidget:disabled { color: rgba(0, 0, 0, 50); /* Very faded text */ background-color: rgba(200, 200, 200, 0); /* Faded background */}")
        self.formLayout_2 = QFormLayout(self.widget_form)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.txtFirstName = QLineEdit(self.widget_form)
        self.txtFirstName.setObjectName(u"txtFirstName")
        self.txtFirstName.setMinimumSize(QSize(0, 30))
        self.txtFirstName.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtFirstName)

        self.label_9 = QLabel(self.widget_form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.txtMiddleName = QLineEdit(self.widget_form)
        self.txtMiddleName.setObjectName(u"txtMiddleName")
        self.txtMiddleName.setMinimumSize(QSize(0, 30))
        self.txtMiddleName.setStyleSheet(u"")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtMiddleName)

        self.label_10 = QLabel(self.widget_form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.txtLastName = QLineEdit(self.widget_form)
        self.txtLastName.setObjectName(u"txtLastName")
        self.txtLastName.setMinimumSize(QSize(0, 30))
        self.txtLastName.setStyleSheet(u"")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtLastName)

        self.label_11 = QLabel(self.widget_form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.cmbSection = QComboBox(self.widget_form)
        self.cmbSection.setObjectName(u"cmbSection")
        self.cmbSection.setMinimumSize(QSize(0, 30))
        self.cmbSection.setStyleSheet(u"")
        self.cmbSection.setEditable(False)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbSection)

        self.label_12 = QLabel(self.widget_form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.txtPassword = QLineEdit(self.widget_form)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(0, 30))
        self.txtPassword.setStyleSheet(u"")
        self.txtPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtPassword)

        self.label_13 = QLabel(self.widget_form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.cmbGender = QComboBox(self.widget_form)
        self.cmbGender.addItem("")
        self.cmbGender.addItem("")
        self.cmbGender.setObjectName(u"cmbGender")
        self.cmbGender.setMinimumSize(QSize(0, 30))
        self.cmbGender.setStyleSheet(u"")
        self.cmbGender.setEditable(False)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbGender)


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
        self.formLayout_5 = QFormLayout(self.widget_form_emergency)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_24 = QLabel(self.widget_form_emergency)
        self.label_24.setObjectName(u"label_24")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_24.setFont(font)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.txtContactPerson = QLineEdit(self.widget_form_emergency)
        self.txtContactPerson.setObjectName(u"txtContactPerson")
        self.txtContactPerson.setMinimumSize(QSize(0, 30))
        self.txtContactPerson.setStyleSheet(u"")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtContactPerson)

        self.label_23 = QLabel(self.widget_form_emergency)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.txtContactNum = QLineEdit(self.widget_form_emergency)
        self.txtContactNum.setObjectName(u"txtContactNum")
        self.txtContactNum.setMinimumSize(QSize(0, 30))
        self.txtContactNum.setStyleSheet(u"")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtContactNum)

        self.label_22 = QLabel(self.widget_form_emergency)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_22)


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
        self.widget_CSV.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_CSV)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.widget_CSV)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label_14)

        self.cmbSection_2 = QComboBox(self.widget_CSV)
        self.cmbSection_2.setObjectName(u"cmbSection_2")
        self.cmbSection_2.setMinimumSize(QSize(0, 30))
        self.cmbSection_2.setStyleSheet(u"")
        self.cmbSection_2.setEditable(False)

        self.horizontalLayout_3.addWidget(self.cmbSection_2)

        self.txtCSVPath = QLineEdit(self.widget_CSV)
        self.txtCSVPath.setObjectName(u"txtCSVPath")
        self.txtCSVPath.setMinimumSize(QSize(0, 30))
        self.txtCSVPath.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.txtCSVPath)

        self.btnBrowseCSV = QPushButton(self.widget_CSV)
        self.btnBrowseCSV.setObjectName(u"btnBrowseCSV")
        self.btnBrowseCSV.setMinimumSize(QSize(100, 30))
        self.btnBrowseCSV.setMaximumSize(QSize(100, 30))
        self.btnBrowseCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btnBrowseCSV)


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
        self.label_8.setText(QCoreApplication.translate("AddNewStudentDialog", u"First name", None))
        self.label_9.setText(QCoreApplication.translate("AddNewStudentDialog", u"Middle name", None))
        self.label_10.setText(QCoreApplication.translate("AddNewStudentDialog", u"Last name", None))
        self.label_11.setText(QCoreApplication.translate("AddNewStudentDialog", u"Section", None))
        self.label_12.setText(QCoreApplication.translate("AddNewStudentDialog", u"Password", None))
        self.label_13.setText(QCoreApplication.translate("AddNewStudentDialog", u"Gender", None))
        self.cmbGender.setItemText(0, QCoreApplication.translate("AddNewStudentDialog", u"Male", None))
        self.cmbGender.setItemText(1, QCoreApplication.translate("AddNewStudentDialog", u"Female", None))

        self.label_24.setText(QCoreApplication.translate("AddNewStudentDialog", u"Emergency contact", None))
        self.label_23.setText(QCoreApplication.translate("AddNewStudentDialog", u"Contact Number", None))
        self.label_22.setText(QCoreApplication.translate("AddNewStudentDialog", u"Contact Person", None))
        self.rb_importCSV.setText(QCoreApplication.translate("AddNewStudentDialog", u"Import from CSV", None))
        self.label_14.setText(QCoreApplication.translate("AddNewStudentDialog", u"Section", None))
        self.btnBrowseCSV.setText(QCoreApplication.translate("AddNewStudentDialog", u"Browse", None))
        self.btnBrowseCSV.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
        self.btnCancel.setText(QCoreApplication.translate("AddNewStudentDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("AddNewStudentDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
    # retranslateUi

