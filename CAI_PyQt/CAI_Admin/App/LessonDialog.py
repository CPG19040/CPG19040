# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LessonDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_LessonDialog(object):
    def setupUi(self, LessonDialog):
        if not LessonDialog.objectName():
            LessonDialog.setObjectName(u"LessonDialog")
        LessonDialog.resize(900, 351)
        LessonDialog.setMinimumSize(QSize(697, 351))
        LessonDialog.setMaximumSize(QSize(900, 351))
        LessonDialog.setStyleSheet(u"* {\n"
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
        self.verticalLayout = QVBoxLayout(LessonDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(LessonDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_img = QLabel(self.widget_4)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setMinimumSize(QSize(200, 200))
        self.label_img.setMaximumSize(QSize(200, 200))
        self.label_img.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.label_img.setPixmap(QPixmap(u":/Images/Images/no-image2.png"))
        self.label_img.setScaledContents(True)
        self.label_img.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_img, 0, 0, 1, 1)

        self.btnUploadPhoto = QPushButton(self.widget_4)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")
        self.btnUploadPhoto.setMinimumSize(QSize(0, 30))
        self.btnUploadPhoto.setMaximumSize(QSize(16777215, 30))
        self.btnUploadPhoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.btnUploadPhoto, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_4)

        self.widget_right = QWidget(self.widget)
        self.widget_right.setObjectName(u"widget_right")
        self.verticalLayout_2 = QVBoxLayout(self.widget_right)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.widget_6 = QWidget(self.widget_right)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(132, 30))
        self.label.setMaximumSize(QSize(132, 30))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.txtLessonTitle = QLineEdit(self.widget_6)
        self.txtLessonTitle.setObjectName(u"txtLessonTitle")
        self.txtLessonTitle.setMinimumSize(QSize(0, 30))
        self.txtLessonTitle.setMaximumSize(QSize(16777215, 30))
        self.txtLessonTitle.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.txtLessonTitle)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_right)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(132, 30))
        self.label_2.setMaximumSize(QSize(132, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.cmbGradingPeriod = QComboBox(self.widget_7)
        self.cmbGradingPeriod.setObjectName(u"cmbGradingPeriod")
        self.cmbGradingPeriod.setMinimumSize(QSize(0, 30))
        self.cmbGradingPeriod.setMaximumSize(QSize(16777215, 30))
        self.cmbGradingPeriod.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.cmbGradingPeriod)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_right)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(132, 30))
        self.label_3.setMaximumSize(QSize(132, 30))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.txtChapter = QLineEdit(self.widget_8)
        self.txtChapter.setObjectName(u"txtChapter")
        self.txtChapter.setMinimumSize(QSize(0, 30))
        self.txtChapter.setMaximumSize(QSize(16777215, 30))
        self.txtChapter.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.txtChapter)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_right)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(132, 30))
        self.label_4.setMaximumSize(QSize(132, 30))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.txtLessonNumber = QLineEdit(self.widget_9)
        self.txtLessonNumber.setObjectName(u"txtLessonNumber")
        self.txtLessonNumber.setMinimumSize(QSize(0, 30))
        self.txtLessonNumber.setMaximumSize(QSize(16777215, 30))
        self.txtLessonNumber.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.txtLessonNumber)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_3 = QWidget(self.widget_right)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_3 {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(255, 255, 255); \n"
"	border: 1px solid #999999;\n"
"	border-left: none;\n"
"	border-right: none;\n"
"	padding: 0px 15px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 1px solid #3498db;\n"
"	border-right: none;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #007BFF;\n"
"	border-right: none;\n"
"}\n"
"\n"
"#btnBrowse {\n"
"	font: 10pt \"Inter\";\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #999999;\n"
"	padding: 5px 15px;\n"
"	\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"#btnBrowse:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgb(192, 191, 188);\n"
"	border-left: 1px solid #999;\n"
"	border-top: 1px solid #999;\n"
"	border-bottom: 1px solid #999;\n"
"	border-right: none;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius"
                        ": 15px;\n"
"	padding-left: 8px;\n"
"	color: black;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(132, 30))
        self.label_5.setMaximumSize(QSize(132, 30))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.txtLessonPath = QLineEdit(self.widget_3)
        self.txtLessonPath.setObjectName(u"txtLessonPath")
        self.txtLessonPath.setMinimumSize(QSize(0, 30))
        self.txtLessonPath.setMaximumSize(QSize(16777215, 30))
        self.txtLessonPath.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.txtLessonPath)

        self.btnBrowse = QPushButton(self.widget_3)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setMinimumSize(QSize(50, 30))
        self.btnBrowse.setMaximumSize(QSize(16777215, 30))
        self.btnBrowse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnBrowse)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.widget_right)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(LessonDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(436, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.widget_2)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.widget_2)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 30))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(LessonDialog)

        QMetaObject.connectSlotsByName(LessonDialog)
    # setupUi

    def retranslateUi(self, LessonDialog):
        LessonDialog.setWindowTitle(QCoreApplication.translate("LessonDialog", u"Lesson Editor", None))
        self.label_img.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("LessonDialog", u"Update photo", None))
        self.btnUploadPhoto.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"button-normal", None))
        self.widget_6.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label.setText(QCoreApplication.translate("LessonDialog", u"Lesson Title", None))
        self.widget_7.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label_2.setText(QCoreApplication.translate("LessonDialog", u"Grading Period", None))
        self.widget_8.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label_3.setText(QCoreApplication.translate("LessonDialog", u"Chapter", None))
        self.widget_9.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label_4.setText(QCoreApplication.translate("LessonDialog", u"Lesson Number", None))
        self.label_5.setText(QCoreApplication.translate("LessonDialog", u"Path", None))
        self.btnBrowse.setText(QCoreApplication.translate("LessonDialog", u"\u2022\u2022\u2022", None))
        self.btnCancel.setText(QCoreApplication.translate("LessonDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("LessonDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"button-green", None))
    # retranslateUi

