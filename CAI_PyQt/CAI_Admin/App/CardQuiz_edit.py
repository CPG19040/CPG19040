# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardQuiz_edit.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_CardQuiz_edit(object):
    def setupUi(self, CardQuiz_edit):
        if not CardQuiz_edit.objectName():
            CardQuiz_edit.setObjectName(u"CardQuiz_edit")
        CardQuiz_edit.resize(216, 365)
        CardQuiz_edit.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(CardQuiz_edit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Card = QFrame(CardQuiz_edit)
        self.Card.setObjectName(u"Card")
        self.Card.setStyleSheet(u"* {\n"
"	font: 10pt \"Inter\";\n"
"}\n"
"\n"
"#Card {\n"
"	background-color: #FFF;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #ddd;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #333;\n"
"}\n"
"\n"
"#widget_header {\n"
"	background-color: rgb(153, 193, 241);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#label_itemno {\n"
"	font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"#btn_delete {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: red; \n"
"	font-weight: bold;\n"
"	font: 12pt \"Inter\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#btn_delete:hover {\n"
"	color: white;\n"
"	background-color: red;\n"
"}\n"
"\n"
"#btn_q_image {\n"
"	background-color: white;\n"
"	border: none;\n"
"}\n"
"\n"
"#btn_q_image:hover {\n"
"	background-color: rgb(208, 236, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"#btn_upload_img {\n"
"	border: none;\n"
"	color: blue;\n"
"	background-color: transparent; \n"
"	margin: 0px 20px 0px;\n"
"}\n"
"\n"
"#txt_question {\n"
"	background-color: white;\n"
"	border"
                        "-radius: 15px;\n"
"	padding: 0px 10px 0px;\n"
"	border: 1px solid #ABABAB;\n"
"}\n"
"\n"
"#txt_question:hover {\n"
"	border: 1px solid #3498db;\n"
"}\n"
"\n"
"#txt_question:focus {\n"
"	border: 1px solid #007BFF;\n"
"}")
        self.Card.setFrameShape(QFrame.StyledPanel)
        self.Card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Card)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.frame_2 = QFrame(self.Card)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layout_card_body = QVBoxLayout(self.frame_2)
        self.layout_card_body.setSpacing(0)
        self.layout_card_body.setObjectName(u"layout_card_body")
        self.layout_card_body.setContentsMargins(0, 0, 0, 0)
        self.widget_header = QWidget(self.frame_2)
        self.widget_header.setObjectName(u"widget_header")
        self.widget_header.setMinimumSize(QSize(0, 35))
        self.widget_header.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 2, 0)
        self.label_itemno = QLabel(self.widget_header)
        self.label_itemno.setObjectName(u"label_itemno")
        self.label_itemno.setMinimumSize(QSize(0, 30))
        self.label_itemno.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_itemno.setFont(font)
        self.label_itemno.setStyleSheet(u"")
        self.label_itemno.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_itemno)

        self.btn_delete = QPushButton(self.widget_header)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(30, 30))
        self.btn_delete.setMaximumSize(QSize(30, 30))
        self.btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_delete)


        self.layout_card_body.addWidget(self.widget_header)

        self.widget_img = QWidget(self.frame_2)
        self.widget_img.setObjectName(u"widget_img")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_img)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_q_image = QLabel(self.widget_img)
        self.label_q_image.setObjectName(u"label_q_image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_q_image.sizePolicy().hasHeightForWidth())
        self.label_q_image.setSizePolicy(sizePolicy)
        self.label_q_image.setMinimumSize(QSize(200, 200))
        self.label_q_image.setMaximumSize(QSize(200, 200))
        self.label_q_image.setPixmap(QPixmap(u":/Images/Images/no-image2.png"))
        self.label_q_image.setScaledContents(True)
        self.label_q_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_q_image)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.layout_card_body.addWidget(self.widget_img)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_upload_img = QPushButton(self.widget)
        self.btn_upload_img.setObjectName(u"btn_upload_img")
        self.btn_upload_img.setMinimumSize(QSize(0, 30))
        self.btn_upload_img.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_upload_img.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.btn_upload_img)


        self.layout_card_body.addWidget(self.widget)

        self.widget_q_a = QWidget(self.frame_2)
        self.widget_q_a.setObjectName(u"widget_q_a")
        self.layout_inputs = QVBoxLayout(self.widget_q_a)
        self.layout_inputs.setObjectName(u"layout_inputs")
        self.txt_question = QPlainTextEdit(self.widget_q_a)
        self.txt_question.setObjectName(u"txt_question")
        self.txt_question.setMinimumSize(QSize(0, 50))

        self.layout_inputs.addWidget(self.txt_question)


        self.layout_card_body.addWidget(self.widget_q_a)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.Card)


        self.retranslateUi(CardQuiz_edit)

        QMetaObject.connectSlotsByName(CardQuiz_edit)
    # setupUi

    def retranslateUi(self, CardQuiz_edit):
        CardQuiz_edit.setWindowTitle(QCoreApplication.translate("CardQuiz_edit", u"Form", None))
        self.label_itemno.setText(QCoreApplication.translate("CardQuiz_edit", u"ITEM 1", None))
        self.btn_delete.setText(QCoreApplication.translate("CardQuiz_edit", u"\u2716", None))
        self.label_q_image.setText("")
        self.btn_upload_img.setText(QCoreApplication.translate("CardQuiz_edit", u"Upload Image", None))
        self.txt_question.setPlaceholderText(QCoreApplication.translate("CardQuiz_edit", u"Enter Question (e.g. 1 + 5 = ?)", None))
    # retranslateUi

