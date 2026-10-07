# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MessageBox.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        if not MessageBox.objectName():
            MessageBox.setObjectName(u"MessageBox")
        MessageBox.resize(348, 297)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MessageBox.sizePolicy().hasHeightForWidth())
        MessageBox.setSizePolicy(sizePolicy)
        MessageBox.setMinimumSize(QSize(348, 297))
        MessageBox.setMaximumSize(QSize(420, 390))
        MessageBox.setStyleSheet(u"#MessageBox { \n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#widget { \n"
"	border: 5px solid #91404b;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5f2a31, stop:1 #91404b);;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#widget_body { \n"
"	border: 5px solid #91404b;\n"
"	background: #dabe8f;\n"
"	border-radius: 20px;\n"
"	margin: 0px 20px 0px; \n"
"}\n"
"\n"
"#label_message {\n"
"	padding: 10px 30px 10px; \n"
"	font: 16pt \"Biscuit Glitch\"; \n"
"	color: Brown;\n"
"}")
        self.verticalLayout = QVBoxLayout(MessageBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(MessageBox)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 10)
        self.widget_header = QWidget(self.widget)
        self.widget_header.setObjectName(u"widget_header")
        self.widget_header.setMinimumSize(QSize(0, 40))
        self.widget_header.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_header)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(40, 40))
        self.widget_5.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.widget_5)

        self.label_windowTitle = QLabel(self.widget_header)
        self.label_windowTitle.setObjectName(u"label_windowTitle")
        self.label_windowTitle.setMinimumSize(QSize(0, 35))
        self.label_windowTitle.setMaximumSize(QSize(16777215, 35))
        self.label_windowTitle.setStyleSheet(u"#label_windowTitle {\n"
"	font: 13pt \"Kissy Hugs\"; \n"
"	color: #fff;\n"
"}")
        self.label_windowTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_windowTitle)

        self.btnClose = QPushButton(self.widget_header)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(40, 40))
        self.btnClose.setMaximumSize(QSize(40, 40))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"#btnClose { border-image: url(:/Images/Images/wood_round_ex.png); }\n"
"#btnClose:hover { border-image: url(:/Images/Images/wood_round_ex2.png); }")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout_2.addWidget(self.widget_header)

        self.widget_body = QWidget(self.widget)
        self.widget_body.setObjectName(u"widget_body")
        self.widget_body.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_body)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_gif = QLabel(self.widget_3)
        self.label_gif.setObjectName(u"label_gif")
        self.label_gif.setMinimumSize(QSize(120, 120))
        self.label_gif.setMaximumSize(QSize(120, 120))
        self.label_gif.setScaledContents(True)
        self.label_gif.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_gif)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.label_message = QLabel(self.widget_body)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setStyleSheet(u"")
        self.label_message.setAlignment(Qt.AlignCenter)
        self.label_message.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_message)


        self.verticalLayout_2.addWidget(self.widget_body)

        self.widget_buttons = QWidget(self.widget)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.widget_buttons.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnOk = QPushButton(self.widget_buttons)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setMinimumSize(QSize(100, 40))
        self.btnOk.setMaximumSize(QSize(100, 40))
        self.btnOk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnOk.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/Images/Images/button_wood_skyblue.png);\n"
"	font: 13pt \"Kissy Hugs\"; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-image: url(:/Images/Images/button_wood_skyblue_glow.png);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btnOk)

        self.btnYes = QPushButton(self.widget_buttons)
        self.btnYes.setObjectName(u"btnYes")
        self.btnYes.setMinimumSize(QSize(100, 40))
        self.btnYes.setMaximumSize(QSize(100, 40))
        self.btnYes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnYes.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/Images/Images/button_wood_skyblue.png);\n"
"	font: 13pt \"Kissy Hugs\"; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-image: url(:/Images/Images/button_wood_skyblue_glow.png);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btnYes)

        self.btnNo = QPushButton(self.widget_buttons)
        self.btnNo.setObjectName(u"btnNo")
        self.btnNo.setMinimumSize(QSize(100, 40))
        self.btnNo.setMaximumSize(QSize(100, 40))
        self.btnNo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNo.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/Images/Images/button_wood.png);\n"
"	font: 13pt \"Kissy Hugs\"; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-image: url(:/Images/Images/button_wood_glow.png);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btnNo)


        self.verticalLayout_2.addWidget(self.widget_buttons)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(MessageBox)

        QMetaObject.connectSlotsByName(MessageBox)
    # setupUi

    def retranslateUi(self, MessageBox):
        MessageBox.setWindowTitle(QCoreApplication.translate("MessageBox", u"Dialog", None))
        self.label_windowTitle.setText(QCoreApplication.translate("MessageBox", u"Title", None))
        self.btnClose.setText("")
        self.label_gif.setText("")
        self.label_message.setText(QCoreApplication.translate("MessageBox", u"Hello World", None))
        self.btnOk.setText(QCoreApplication.translate("MessageBox", u"OK", None))
        self.btnYes.setText(QCoreApplication.translate("MessageBox", u"Yes", None))
        self.btnNo.setText(QCoreApplication.translate("MessageBox", u"No", None))
    # retranslateUi

