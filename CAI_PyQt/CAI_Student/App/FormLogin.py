# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormLogin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        if not FormLogin.objectName():
            FormLogin.setObjectName(u"FormLogin")
        FormLogin.resize(968, 665)
        FormLogin.setMinimumSize(QSize(0, 0))
        FormLogin.setStyleSheet(u"QWidget { background-color: #ffdaa5; }")
        self.verticalLayout_3 = QVBoxLayout(FormLogin)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(FormLogin)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.btnMinimize = QPushButton(self.widget_8)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(40, 40))
        self.btnMinimize.setMaximumSize(QSize(40, 40))
        self.btnMinimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"#btnMinimize { border-image: url(:/Images/Images/wood_round_min.png); }\n"
"#btnMinimize:hover { border-image: url(:/Images/Images/wood_round_min2.png); }")

        self.horizontalLayout_2.addWidget(self.btnMinimize)

        self.btnMaximize = QPushButton(self.widget_8)
        self.btnMaximize.setObjectName(u"btnMaximize")
        self.btnMaximize.setMinimumSize(QSize(40, 40))
        self.btnMaximize.setMaximumSize(QSize(40, 40))
        self.btnMaximize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMaximize.setStyleSheet(u"#btnMaximize { border-image: url(:/Images/Images/wood_round_max.png); }\n"
"#btnMaximize:hover { border-image: url(:/Images/Images/wood_round_max2.png); }")

        self.horizontalLayout_2.addWidget(self.btnMaximize)

        self.btnClose = QPushButton(self.widget_8)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(40, 40))
        self.btnClose.setMaximumSize(QSize(40, 40))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"#btnClose { border-image: url(:/Images/Images/wood_round_ex.png); }\n"
"#btnClose:hover { border-image: url(:/Images/Images/wood_round_ex2.png); }")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.stackedWidget = QStackedWidget(FormLogin)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.horizontalLayout = QHBoxLayout(self.page1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.page1)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_20 = QWidget(self.widget)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(6, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.widget_20)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setFamilies([u"Kissy Hugs"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(5, 28, 84); border-image: url(:/Images/Images/blue-button.png);")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.label = QLabel(self.widget_20)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Kissy Hugs"])
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #88490f;")

        self.horizontalLayout_10.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(6, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_20)

        self.list_sections = QListWidget(self.widget)
        QListWidgetItem(self.list_sections)
        QListWidgetItem(self.list_sections)
        QListWidgetItem(self.list_sections)
        QListWidgetItem(self.list_sections)
        self.list_sections.setObjectName(u"list_sections")
        self.list_sections.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Inter Medium"])
        font2.setPointSize(13)
        self.list_sections.setFont(font2)
        self.list_sections.setStyleSheet(u"border-radius: 20px; background-color: rgb(248, 230, 203); padding: 10px; color: rgb(84, 51, 51); border: 5px solid #fff;")
        self.list_sections.setFlow(QListView.TopToBottom)
        self.list_sections.setSpacing(5)

        self.verticalLayout.addWidget(self.list_sections)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_18 = QWidget(self.page1)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_10 = QVBoxLayout(self.widget_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.widget_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 50))
        self.label_3.setMaximumSize(QSize(50, 50))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(5, 28, 84); border-image: url(:/Images/Images/blue-button.png);")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.label_26 = QLabel(self.widget_19)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(300, 16777215))
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"color: #88490f;")
        self.label_26.setMargin(4)

        self.horizontalLayout_7.addWidget(self.label_26)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addWidget(self.widget_19)

        self.scrollArea = QScrollArea(self.widget_18)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* 1. THE MAIN CONTAINER */\n"
"#scrollArea { \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* 2. THE VIEWPORT (Crucial for transparency/backgrounds) */\n"
"#scrollArea QWidget #qt_scrollarea_viewport {\n"
"    background: transparent;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* 3. VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #7a7a7a;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 4. HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    height: 10px; /* Note: height, not width */\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #7"
                        "a7a7a;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 5. REMOVE BUTTONS & TRACK BACKGROUNDS */\n"
"/* This handles both horizontal and vertical arrows/tracks */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* 6. THE CORNER WIDGET \n"
"   (The small square where both bars meet) */\n"
"#scrollArea QWidget #qt_scrollarea_corner {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 644, 545))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.widget_18)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.horizontalLayout_5 = QHBoxLayout(self.page2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(195, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.widget_3 = QWidget(self.page2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setLayoutDirection(Qt.LeftToRight)
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnBack = QPushButton(self.widget_3)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setMinimumSize(QSize(100, 50))
        self.btnBack.setMaximumSize(QSize(100, 50))
        font3 = QFont()
        font3.setFamilies([u"Kissy Hugs"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.btnBack.setFont(font3)
        self.btnBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBack.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/Images/Images/leftArrowWood.png);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	font-family: 'Kissy Hugs';\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	border-image: url(:/Images/Images/leftArrowWoodGlow.png);\n"
"}")

        self.verticalLayout_2.addWidget(self.btnBack)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_profile_pic = QLabel(self.widget_7)
        self.label_profile_pic.setObjectName(u"label_profile_pic")
        self.label_profile_pic.setMinimumSize(QSize(150, 150))
        self.label_profile_pic.setMaximumSize(QSize(150, 150))
        self.label_profile_pic.setFont(font)
        self.label_profile_pic.setStyleSheet(u"color: rgb(5, 28, 84); border-image: url(:/Images/Images/profile_gray.png);")
        self.label_profile_pic.setTextFormat(Qt.PlainText)
        self.label_profile_pic.setScaledContents(True)
        self.label_profile_pic.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_profile_pic)


        self.horizontalLayout_8.addWidget(self.widget_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.labelFullName = QLabel(self.widget_3)
        self.labelFullName.setObjectName(u"labelFullName")
        self.labelFullName.setMaximumSize(QSize(500, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Kissy Hugs"])
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        self.labelFullName.setFont(font4)
        self.labelFullName.setStyleSheet(u"font: 63 20pt \"Kissy Hugs\"; color: rgb(165, 29, 45);")
        self.labelFullName.setAlignment(Qt.AlignCenter)
        self.labelFullName.setMargin(4)

        self.verticalLayout_2.addWidget(self.labelFullName)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(5, 28, 84); border-image: url(:/Images/Images/blue-button.png);")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(300, 16777215))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"color: #88490f;")
        self.label_27.setMargin(4)

        self.horizontalLayout_3.addWidget(self.label_27)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 60))
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.widget_4.setStyleSheet(u"#widget_4 { background-color: rgb(246, 245, 244); border-radius: 20px; padding: 20px; border: 5px solid rgb(206, 152, 115); color: rgb(54, 37, 26); }")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.txtPassword = QLineEdit(self.widget_4)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(350, 40))
        self.txtPassword.setMaximumSize(QSize(1000, 40))
        font5 = QFont()
        font5.setFamilies([u"Inter SemiBold"])
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setItalic(False)
        self.txtPassword.setFont(font5)
        self.txtPassword.setStyleSheet(u"#txtPassword {\n"
"	border: none;\n"
"	background: transparent;\n"
"	outline: none; /* Removes the focus rectangle on some systems */\n"
"	font: 63 20pt \"Inter SemiBold\";\n"
"	color: rgb(99, 69, 44);\n"
"}\n"
"#txtPassword:focus {\n"
"	border: none;\n"
"	background: transparent;\n"
"	outline: none;\n"
"}")
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.txtPassword)

        self.btnShowPassword = QPushButton(self.widget_4)
        self.btnShowPassword.setObjectName(u"btnShowPassword")
        self.btnShowPassword.setMinimumSize(QSize(50, 50))
        self.btnShowPassword.setMaximumSize(QSize(50, 50))
        font6 = QFont()
        font6.setFamilies([u"Kissy Hugs"])
        font6.setPointSize(20)
        font6.setBold(False)
        self.btnShowPassword.setFont(font6)
        self.btnShowPassword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnShowPassword.setStyleSheet(u"#btnShowPassword {\n"
"	border-image: url(:/Images/Images/closed_eye.png);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	font-family: 'Kissy Hugs';\n"
"	font-size: 20pt;\n"
"	background-color: transparent;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btnShowPassword)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnLogin = QPushButton(self.widget_5)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(200, 60))
        self.btnLogin.setMaximumSize(QSize(200, 16777215))
        self.btnLogin.setFont(font6)
        self.btnLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogin.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/Images/Images/btnWood.png);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	font-family: 'Kissy Hugs';\n"
"	font-size: 20pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	border-image: url(:/Images/Images/btnWoodGlow.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" 	border-image: url(:/Images/Images/btnWood.png);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btnLogin)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.horizontalSpacer_8 = QSpacerItem(195, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.retranslateUi(FormLogin)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormLogin)
    # setupUi

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QCoreApplication.translate("FormLogin", u"Login", None))
        self.btnMinimize.setText("")
        self.btnMaximize.setText("")
        self.btnClose.setText("")
        self.label_2.setText(QCoreApplication.translate("FormLogin", u"1", None))
        self.label.setText(QCoreApplication.translate("FormLogin", u"Select your section", None))

        __sortingEnabled = self.list_sections.isSortingEnabled()
        self.list_sections.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_sections.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("FormLogin", u"Clarity", None))
        ___qlistwidgetitem1 = self.list_sections.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("FormLogin", u"Hope", None))
        ___qlistwidgetitem2 = self.list_sections.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("FormLogin", u"Humility", None))
        ___qlistwidgetitem3 = self.list_sections.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("FormLogin", u"Honesty", None))
        self.list_sections.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("FormLogin", u"2", None))
        self.label_26.setText(QCoreApplication.translate("FormLogin", u"Select your name", None))
        self.btnBack.setText(QCoreApplication.translate("FormLogin", u"Back", None))
        self.label_profile_pic.setText("")
        self.labelFullName.setText(QCoreApplication.translate("FormLogin", u"Juan De La Cruz", None))
        self.label_4.setText(QCoreApplication.translate("FormLogin", u"3", None))
        self.label_27.setText(QCoreApplication.translate("FormLogin", u"What's your password?", None))
        self.btnShowPassword.setText("")
        self.btnLogin.setText(QCoreApplication.translate("FormLogin", u"Enter", None))
    # retranslateUi

