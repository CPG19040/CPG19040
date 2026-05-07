# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardQuiz.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_CardQuiz(object):
    def setupUi(self, CardQuiz):
        if not CardQuiz.objectName():
            CardQuiz.setObjectName(u"CardQuiz")
        CardQuiz.resize(558, 220)
        CardQuiz.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(CardQuiz)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Card = QFrame(CardQuiz)
        self.Card.setObjectName(u"Card")
        self.Card.setStyleSheet(u"#Card {\n"
"	font: 15pt \"Inter\";\n"
"	background-color: #FFF;\n"
"	color: rgb(54, 37, 26);\n"
"	border-radius: 10px;\n"
"	border: 1px solid #ddd;\n"
"}\n"
"#Card:hover {\n"
"	border: 3px solid #3498db;\n"
"	background-color: #f7fbfe;\n"
"}\n"
"/* This style applies when the custom property is true */\n"
"#Card[selected=\"true\"] {\n"
"	background-color: #e1f5fe;\n"
"	border: 2px solid #3498db;\n"
"}\n"
"QLabel {\n"
"	color: #333;\n"
"}")
        self.Card.setFrameShape(QFrame.StyledPanel)
        self.Card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Card)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.Card)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_itemno = QLabel(self.frame_2)
        self.label_itemno.setObjectName(u"label_itemno")
        self.label_itemno.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamilies([u"Kissy Hugs"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label_itemno.setFont(font)
        self.label_itemno.setStyleSheet(u"font: 11pt \"Kissy Hugs\"; border-radius: 0px;")

        self.verticalLayout_2.addWidget(self.label_itemno)

        self.label_question = QLabel(self.frame_2)
        self.label_question.setObjectName(u"label_question")
        self.label_question.setStyleSheet(u"padding: 0px 10px 0px; font: 11pt \"Inter\";")
        self.label_question.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_question.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_question)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.label_q_image = QLabel(self.Card)
        self.label_q_image.setObjectName(u"label_q_image")
        self.label_q_image.setMinimumSize(QSize(200, 200))
        self.label_q_image.setMaximumSize(QSize(200, 200))
        self.label_q_image.setStyleSheet(u"border-image: url(:/Images/Images/no-image2.png);")
        self.label_q_image.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_q_image)


        self.horizontalLayout.addWidget(self.Card)


        self.retranslateUi(CardQuiz)

        QMetaObject.connectSlotsByName(CardQuiz)
    # setupUi

    def retranslateUi(self, CardQuiz):
        CardQuiz.setWindowTitle(QCoreApplication.translate("CardQuiz", u"Form", None))
        self.label_itemno.setText(QCoreApplication.translate("CardQuiz", u"ITEM 1", None))
        self.label_question.setText(QCoreApplication.translate("CardQuiz", u"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.", None))
        self.label_q_image.setText("")
    # retranslateUi

