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
        EditStudentDialog.setStyleSheet(u"* {\n"
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
"*[class=\"button-normal\"]:disabled {\n"
"    background-color: #bdc3c7;\n"
"    color: #7f8c8d;\n"
"    border: 1px solid #95a5a6;\n"
"}\n"
"\n"
"*[class=\"input-field\"] {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit {\n"
"	background-color: #ffffff;\n"
"	border: 1px solid #ABABAB;\n"
"	border-left: none;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	padding: 0px 8px;\n"
"	color: black;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLabel {\n"
"	background-color: rgb(192, 191, 188);\n"
"	border-right: none;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	padding-le"
                        "ft: 8px;\n"
"	color: black;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #999;\n"
"	border-left: none;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	padding: 0px 15px 0px;\n"
"	background-color: #ffffff;\n"
"	color: #333333;\n"
"	font: 10pt \"Inter Medium\"; /* Consolidated font settings */\n"
"	selection-background-color: #7eb4d7;\n"
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
""
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
"    subcontrol-origin: bord"
                        "er;\n"
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
        self.spinBox_SY1.setMinimumSize(QSize(80, 30))
        self.spinBox_SY1.setMaximumSize(QSize(80, 30))
        self.spinBox_SY1.setStyleSheet(u"")
        self.spinBox_SY1.setAlignment(Qt.AlignCenter)
        self.spinBox_SY1.setMinimum(2000)
        self.spinBox_SY1.setMaximum(3000)

        self.horizontalLayout_4.addWidget(self.spinBox_SY1)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.spinBox_SY2 = QSpinBox(self.widget_3)
        self.spinBox_SY2.setObjectName(u"spinBox_SY2")
        self.spinBox_SY2.setMinimumSize(QSize(80, 30))
        self.spinBox_SY2.setMaximumSize(QSize(80, 30))
        self.spinBox_SY2.setStyleSheet(u"")
        self.spinBox_SY2.setAlignment(Qt.AlignCenter)
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
        self.widget_2.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_profile_pic = QLabel(self.widget)
        self.label_profile_pic.setObjectName(u"label_profile_pic")
        self.label_profile_pic.setMinimumSize(QSize(150, 150))
        self.label_profile_pic.setMaximumSize(QSize(150, 150))
        self.label_profile_pic.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile_pic.setScaledContents(True)
        self.label_profile_pic.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_profile_pic, 0, 0, 1, 1)

        self.btnUploadPhoto = QPushButton(self.widget)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")
        self.btnUploadPhoto.setMinimumSize(QSize(100, 30))
        self.btnUploadPhoto.setMaximumSize(QSize(16777215, 30))
        self.btnUploadPhoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnUploadPhoto, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.widget)

        self.widget_form = QWidget(self.widget_2)
        self.widget_form.setObjectName(u"widget_form")
        self.widget_form.setEnabled(True)
        self.widget_form.setStyleSheet(u"QWidget:disabled { color: rgba(0, 0, 0, 50); /* Very faded text */ background-color: rgba(200, 200, 200, 0); /* Faded background */}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_form)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.txtFirstName = QLineEdit(self.widget_4)
        self.txtFirstName.setObjectName(u"txtFirstName")
        self.txtFirstName.setMinimumSize(QSize(0, 30))
        self.txtFirstName.setMaximumSize(QSize(16777215, 30))
        self.txtFirstName.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.txtFirstName)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_form)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.txtMiddleName = QLineEdit(self.widget_5)
        self.txtMiddleName.setObjectName(u"txtMiddleName")
        self.txtMiddleName.setMinimumSize(QSize(0, 30))
        self.txtMiddleName.setMaximumSize(QSize(16777215, 30))
        self.txtMiddleName.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.txtMiddleName)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_form)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.txtLastName = QLineEdit(self.widget_6)
        self.txtLastName.setObjectName(u"txtLastName")
        self.txtLastName.setMinimumSize(QSize(0, 30))
        self.txtLastName.setMaximumSize(QSize(16777215, 30))
        self.txtLastName.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.txtLastName)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_form)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 30))
        self.label_11.setMaximumSize(QSize(100, 30))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.cmbSection = QComboBox(self.widget_7)
        self.cmbSection.setObjectName(u"cmbSection")
        self.cmbSection.setMinimumSize(QSize(0, 30))
        self.cmbSection.setMaximumSize(QSize(16777215, 30))
        self.cmbSection.setStyleSheet(u"")
        self.cmbSection.setEditable(False)

        self.horizontalLayout_6.addWidget(self.cmbSection)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_form)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 30))
        self.label_13.setMaximumSize(QSize(100, 30))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.cmbGender = QComboBox(self.widget_8)
        self.cmbGender.addItem("")
        self.cmbGender.addItem("")
        self.cmbGender.setObjectName(u"cmbGender")
        self.cmbGender.setMinimumSize(QSize(0, 30))
        self.cmbGender.setMaximumSize(QSize(16777215, 30))
        self.cmbGender.setStyleSheet(u"")
        self.cmbGender.setEditable(False)

        self.horizontalLayout_7.addWidget(self.cmbGender)


        self.verticalLayout_2.addWidget(self.widget_8)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.widget_form)


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
        self.widget_form_2.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_form_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_9 = QWidget(self.widget_form_2)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(130, 30))
        self.label_22.setMaximumSize(QSize(130, 30))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_22)

        self.txtContactPerson = QLineEdit(self.widget_9)
        self.txtContactPerson.setObjectName(u"txtContactPerson")
        self.txtContactPerson.setMinimumSize(QSize(0, 30))
        self.txtContactPerson.setMaximumSize(QSize(16777215, 30))
        self.txtContactPerson.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.txtContactPerson)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_form_2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(130, 30))
        self.label_23.setMaximumSize(QSize(130, 30))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_23)

        self.txtContactNum = QLineEdit(self.widget_10)
        self.txtContactNum.setObjectName(u"txtContactNum")
        self.txtContactNum.setMinimumSize(QSize(0, 30))
        self.txtContactNum.setMaximumSize(QSize(16777215, 30))
        self.txtContactNum.setStyleSheet(u"")
        self.txtContactNum.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.txtContactNum)


        self.verticalLayout_3.addWidget(self.widget_10)


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
        self.txtPassword.setMaximumSize(QSize(16777215, 30))
        self.txtPassword.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: 1px solid #999;\n"
"	padding: 0px 15px;\n"
"}")
        self.txtPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.txtPassword)

        self.verticalSpacer = QSpacerItem(20, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(EditStudentDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnUpdate = QPushButton(EditStudentDialog)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setMinimumSize(QSize(100, 30))
        self.btnUpdate.setMaximumSize(QSize(100, 30))
        self.btnUpdate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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
        self.btnRefreshSY.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"button-normal", None))
#if QT_CONFIG(tooltip)
        self.label_profile_pic.setToolTip(QCoreApplication.translate("EditStudentDialog", u"Aspect Ratio (1:1)", None))
#endif // QT_CONFIG(tooltip)
        self.label_profile_pic.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("EditStudentDialog", u"Update photo", None))
        self.btnUploadPhoto.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"button-normal", None))
        self.widget_4.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"input-field", None))
        self.label_8.setText(QCoreApplication.translate("EditStudentDialog", u"First name", None))
        self.widget_5.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("EditStudentDialog", u"Middle name", None))
        self.widget_6.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("EditStudentDialog", u"Last name", None))
        self.widget_7.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"input-field", None))
        self.label_11.setText(QCoreApplication.translate("EditStudentDialog", u"Section", None))
        self.widget_8.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"input-field", None))
        self.label_13.setText(QCoreApplication.translate("EditStudentDialog", u"Gender", None))
        self.cmbGender.setItemText(0, QCoreApplication.translate("EditStudentDialog", u"Male", None))
        self.cmbGender.setItemText(1, QCoreApplication.translate("EditStudentDialog", u"Female", None))

        self.label_24.setText(QCoreApplication.translate("EditStudentDialog", u"Emergency contact", None))
        self.widget_9.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"input-field", None))
        self.label_22.setText(QCoreApplication.translate("EditStudentDialog", u"Contact Person", None))
        self.widget_10.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"input-field", None))
        self.label_23.setText(QCoreApplication.translate("EditStudentDialog", u"Contact Number", None))
        self.txtContactNum.setInputMask(QCoreApplication.translate("EditStudentDialog", u"0999 999 9999;*", None))
        self.label_25.setText(QCoreApplication.translate("EditStudentDialog", u"Change Password", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("EditStudentDialog", u"Enter new password", None))
        self.btnCancel.setText(QCoreApplication.translate("EditStudentDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"button-normal", None))
        self.btnUpdate.setText(QCoreApplication.translate("EditStudentDialog", u"Update", None))
        self.btnUpdate.setProperty(u"class", QCoreApplication.translate("EditStudentDialog", u"button-normal", None))
    # retranslateUi

