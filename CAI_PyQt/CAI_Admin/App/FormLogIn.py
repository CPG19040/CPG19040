# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormLogIn.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        if not FormLogin.objectName():
            FormLogin.setObjectName(u"FormLogin")
        FormLogin.resize(486, 628)
        FormLogin.setMinimumSize(QSize(486, 628))
        FormLogin.setMaximumSize(QSize(486, 628))
        FormLogin.setStyleSheet(u"* {\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#FormLogin {\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_school_name {\n"
"	color: rgb(255, 255, 255); \n"
"	font-family: 'Ubuntu'; \n"
"	font-weight: bold;\n"
"}\n"
"")
        self.centralwidget = QWidget(FormLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 35))
        self.frame_header.setMaximumSize(QSize(16777215, 35))
        self.frame_header.setMouseTracking(True)
        self.frame_header.setStyleSheet(u"#frame_header {\n"
"	color: #FFF;\n"
"	background-color: #3d3d3d;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"	border: 1px solid #7a7a7a;\n"
"	border-bottom: none;\n"
"}")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(4, 0, 0, 0)
        self.widget_window_icon = QWidget(self.frame_header)
        self.widget_window_icon.setObjectName(u"widget_window_icon")
        self.widget_window_icon.setMinimumSize(QSize(72, 34))
        self.widget_window_icon.setMaximumSize(QSize(72, 34))
        self.widget_window_icon.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_window_icon)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.widget_window_icon)

        self.label_windowTitle = QLabel(self.frame_header)
        self.label_windowTitle.setObjectName(u"label_windowTitle")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_windowTitle.setFont(font)
        self.label_windowTitle.setStyleSheet(u"background: transparent;\n"
"color: #FFF;\n"
"font: 10pt \"Inter SemiBold\";")
        self.label_windowTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_windowTitle)

        self.widget_window_buttons = QWidget(self.frame_header)
        self.widget_window_buttons.setObjectName(u"widget_window_buttons")
        self.widget_window_buttons.setMinimumSize(QSize(72, 34))
        self.widget_window_buttons.setMaximumSize(QSize(72, 34))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_window_buttons)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.widget_window_buttons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(24, 24))
        self.btnMinimize.setMaximumSize(QSize(24, 24))
        self.btnMinimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"#btnMinimize {\n"
"	border-radius: 12px;\n"
"	background-color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"#btnMinimize:hover {\n"
"	background-color: rgb(248, 228, 92);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Images/Images/minimize-sign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QSize(12, 12))

        self.horizontalLayout_12.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.widget_window_buttons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(24, 24))
        self.btnClose.setMaximumSize(QSize(24, 24))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"#btnClose {\n"
"	border-radius: 12px;\n"
"	background-color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"#btnClose:hover {\n"
"	background-color: rgb(246, 97, 81);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)

        self.horizontalLayout_12.addWidget(self.btnClose)


        self.horizontalLayout_10.addWidget(self.widget_window_buttons)


        self.verticalLayout_3.addWidget(self.frame_header)

        self.widget_body = QWidget(self.centralwidget)
        self.widget_body.setObjectName(u"widget_body")
        self.widget_body.setStyleSheet(u"#widget_body {\n"
"	background-color: #3d3d3d;\n"
"	border: 1px solid #7a7a7a;\n"
"	border-top: none;\n"
"}\n"
"\n"
"*[class=\"input-field\"] {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLabel {\n"
"	color: #4a4a4a;\n"
"	background-color: rgb(192, 191, 188);\n"
"	border: 1px solid #999;\n"
"	border-right: none;\n"
"	border-top-left-radius: 18px;\n"
"	border-bottom-left-radius: 18px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit {\n"
"	background-color: rgb(234, 234, 234);\n"
"	border: 1px solid #ABABAB;\n"
"	border-left: none;\n"
"	border-top-right-radius: 18px;\n"
"	border-bottom-right-radius: 18px;\n"
"	padding: 0px 8px;\n"
"	color: rgb(36, 31, 49);\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit:hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit:focus {\n"
"	border: 1px solid #007BFF;\n"
"}\n"
"\n"
"#btnLogin {\n"
"	border-radius: 20px;\n"
"	background: #FF1595;\n"
"	color: white;\n"
"	font-family: 'Inter "
                        "Medium'; \n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"#btnLogin:hover {\n"
" 	background: #ED5AB3;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 9, 12, -1)
        self.widget_logo = QWidget(self.widget_body)
        self.widget_logo.setObjectName(u"widget_logo")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_logo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_logo = QLabel(self.widget_logo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(75, 75))
        self.label_logo.setMaximumSize(QSize(75, 75))
        font1 = QFont()
        font1.setFamilies([u"Inter Medium"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_logo.setFont(font1)
        self.label_logo.setStyleSheet(u"")
        self.label_logo.setPixmap(QPixmap(u":/Images/Images/lcs logo.png"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_logo)

        self.label_school_name = QLabel(self.widget_logo)
        self.label_school_name.setObjectName(u"label_school_name")
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_school_name.setFont(font2)
        self.label_school_name.setAutoFillBackground(False)
        self.label_school_name.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_school_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_logo)

        self.widget_1 = QWidget(self.widget_body)
        self.widget_1.setObjectName(u"widget_1")
        self.horizontalLayout = QHBoxLayout(self.widget_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 9)
        self.label_1 = QLabel(self.widget_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(100, 36))
        self.label_1.setMaximumSize(QSize(16777215, 36))
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.txtUsername = QLineEdit(self.widget_1)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setMinimumSize(QSize(0, 36))
        self.txtUsername.setMaximumSize(QSize(16777215, 36))
        font3 = QFont()
        font3.setFamilies([u"Inter Medium"])
        font3.setPointSize(11)
        self.txtUsername.setFont(font3)
        self.txtUsername.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.txtUsername)


        self.verticalLayout_2.addWidget(self.widget_1)

        self.widget_2 = QWidget(self.widget_body)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 14)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 36))
        self.label_2.setMaximumSize(QSize(16777215, 36))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.txtPassword = QLineEdit(self.widget_2)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(0, 32))
        self.txtPassword.setMaximumSize(QSize(16777215, 36))
        self.txtPassword.setFont(font3)
        self.txtPassword.setStyleSheet(u"")
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.txtPassword)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnLogin = QPushButton(self.widget_body)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(0, 40))
        self.btnLogin.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Inter Medium"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.btnLogin.setFont(font4)
        self.btnLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogin.setMouseTracking(True)
        self.btnLogin.setStyleSheet(u"")
        self.btnLogin.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.btnLogin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.btnForgotPassword = QPushButton(self.widget_body)
        self.btnForgotPassword.setObjectName(u"btnForgotPassword")
        self.btnForgotPassword.setMinimumSize(QSize(0, 40))
        self.btnForgotPassword.setMaximumSize(QSize(16777215, 40))
        self.btnForgotPassword.setFont(font1)
        self.btnForgotPassword.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnForgotPassword.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: transparent;\n"
"	color: White;\n"
"	font-family: 'Inter Medium'; \n"
"	font-weight: normal; \n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	color: Yellow;\n"
"}")

        self.verticalLayout_2.addWidget(self.btnForgotPassword)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_SY = QLabel(self.widget_body)
        self.label_SY.setObjectName(u"label_SY")
        self.label_SY.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_SY)


        self.verticalLayout_3.addWidget(self.widget_body)

        FormLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormLogin)

        self.btnLogin.setDefault(True)


        QMetaObject.connectSlotsByName(FormLogin)
    # setupUi

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QCoreApplication.translate("FormLogin", u"Login", None))
        self.label_windowTitle.setText(QCoreApplication.translate("FormLogin", u"Login", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.label_logo.setText("")
        self.label_school_name.setText(QCoreApplication.translate("FormLogin", u"La Camelle School", None))
        self.widget_1.setProperty(u"class", QCoreApplication.translate("FormLogin", u"input-field", None))
        self.label_1.setText(QCoreApplication.translate("FormLogin", u"Username", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("FormLogin", u"input-field", None))
        self.label_2.setText(QCoreApplication.translate("FormLogin", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("FormLogin", u"Log in", None))
        self.btnForgotPassword.setText(QCoreApplication.translate("FormLogin", u"Forgot password ?", None))
        self.label_SY.setText(QCoreApplication.translate("FormLogin", u"School Year: 0000-0000", None))
    # retranslateUi

