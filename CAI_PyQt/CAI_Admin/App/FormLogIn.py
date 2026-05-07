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
        FormLogin.resize(400, 558)
        FormLogin.setMinimumSize(QSize(400, 558))
        FormLogin.setMaximumSize(QSize(400, 558))
        FormLogin.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.centralwidget = QWidget(FormLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(75, 75))
        self.label_logo.setMaximumSize(QSize(75, 75))
        font = QFont()
        font.setFamilies([u"Inter Medium"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet(u"QLabel { font-family: 'Inter Medium'; font-weight: normal; font-size: 11pt; color: rgb(186, 186, 186); }")
        self.label_logo.setPixmap(QPixmap(u":/Images/Images/lcs logo.png"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_logo)

        self.label_schoolName1_2 = QLabel(self.centralwidget)
        self.label_schoolName1_2.setObjectName(u"label_schoolName1_2")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.label_schoolName1_2.setFont(font1)
        self.label_schoolName1_2.setAutoFillBackground(False)
        self.label_schoolName1_2.setStyleSheet(u"color: rgb(255, 255, 255); font-family: 'Ubuntu'; font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label_schoolName1_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 450))
        self.frame.setStyleSheet(u"QFrame { border: 0px; }")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel { font-family: 'Inter Medium'; font-weight: normal; font-size: 11pt; color: rgb(186, 186, 186); }")

        self.verticalLayout.addWidget(self.label)

        self.txtUsername = QLineEdit(self.frame)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setMinimumSize(QSize(0, 32))
        self.txtUsername.setMaximumSize(QSize(16777215, 32))
        font2 = QFont()
        font2.setFamilies([u"Inter Medium"])
        font2.setPointSize(11)
        self.txtUsername.setFont(font2)
        self.txtUsername.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(234, 234, 234);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: rgb(36, 31, 49);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.txtUsername)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel { font-family: 'Inter Medium'; font-weight: normal; font-size: 11pt; color: rgb(186, 186, 186); }")

        self.verticalLayout.addWidget(self.label_2)

        self.txtPassword = QLineEdit(self.frame)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(0, 32))
        self.txtPassword.setMaximumSize(QSize(16777215, 32))
        self.txtPassword.setFont(font2)
        self.txtPassword.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(234, 234, 234);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: rgb(36, 31, 49);\n"
"}")
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.txtPassword)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.btnLogin = QPushButton(self.frame)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(0, 40))
        self.btnLogin.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Inter Medium"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.btnLogin.setFont(font3)
        self.btnLogin.setMouseTracking(True)
        self.btnLogin.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	background: #FF1595;\n"
"	color: white;\n"
"	font-family: 'Inter Medium'; \n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" 	background: #ED5AB3;\n"
"}")
        self.btnLogin.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.btnLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btnForgotPassword = QPushButton(self.frame)
        self.btnForgotPassword.setObjectName(u"btnForgotPassword")
        self.btnForgotPassword.setMinimumSize(QSize(0, 40))
        self.btnForgotPassword.setFont(font)
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

        self.verticalLayout.addWidget(self.btnForgotPassword)

        self.verticalSpacer = QSpacerItem(20, 160, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame)

        FormLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormLogin)

        self.btnLogin.setDefault(True)


        QMetaObject.connectSlotsByName(FormLogin)
    # setupUi

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QCoreApplication.translate("FormLogin", u"Login", None))
        self.label_logo.setText("")
        self.label_schoolName1_2.setText(QCoreApplication.translate("FormLogin", u"La Camelle School", None))
        self.label.setText(QCoreApplication.translate("FormLogin", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("FormLogin", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("FormLogin", u"Log in", None))
        self.btnForgotPassword.setText(QCoreApplication.translate("FormLogin", u"Forgot password ?", None))
    # retranslateUi

