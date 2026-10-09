# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardStudent.ui'
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

class Ui_CardStudent(object):
    def setupUi(self, CardStudent):
        if not CardStudent.objectName():
            CardStudent.setObjectName(u"CardStudent")
        CardStudent.resize(174, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CardStudent.sizePolicy().hasHeightForWidth())
        CardStudent.setSizePolicy(sizePolicy)
        CardStudent.setMinimumSize(QSize(0, 100))
        CardStudent.setMaximumSize(QSize(1000, 100))
        CardStudent.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(CardStudent)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Card = QFrame(CardStudent)
        self.Card.setObjectName(u"Card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Card.sizePolicy().hasHeightForWidth())
        self.Card.setSizePolicy(sizePolicy1)
        self.Card.setStyleSheet(u"#Card {\n"
"    font: 10pt \"Inter\";\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #ddd;\n"
"}\n"
"\n"
"#Card:hover {\n"
"    border: 1px solid #3498DB;\n"
"    background-color: #E1F5FE;\n"
"}\n"
"\n"
"#Card[selected=\"true\"] {\n"
"    border: 2px solid #3498DB;\n"
"    background-color: #E1F5FE;\n"
"}\n"
"\n"
"#label_name {\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    color: #000000;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#label_studentid,\n"
"#label_section {\n"
"    color: #777777;\n"
"    font-size: 13px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#label_photo {\n"
"    background-color: transparent;\n"
"}")
        self.Card.setFrameShape(QFrame.StyledPanel)
        self.Card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Card)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_photo = QLabel(self.Card)
        self.label_photo.setObjectName(u"label_photo")
        self.label_photo.setMinimumSize(QSize(80, 80))
        self.label_photo.setMaximumSize(QSize(80, 80))
        self.label_photo.setStyleSheet(u"")
        self.label_photo.setPixmap(QPixmap(u":/Images/Images/profile.png"))
        self.label_photo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_photo)

        self.frame_2 = QFrame(self.Card)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layout_body_text = QVBoxLayout(self.frame_2)
        self.layout_body_text.setObjectName(u"layout_body_text")
        self.layout_body_text.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.frame_2)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setBold(True)
        font.setItalic(False)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"")

        self.layout_body_text.addWidget(self.label_name)

        self.label_studentid = QLabel(self.frame_2)
        self.label_studentid.setObjectName(u"label_studentid")
        self.label_studentid.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setFamilies([u"Inter SemiBold"])
        font1.setBold(False)
        font1.setItalic(False)
        self.label_studentid.setFont(font1)
        self.label_studentid.setStyleSheet(u"")

        self.layout_body_text.addWidget(self.label_studentid)

        self.label_section = QLabel(self.frame_2)
        self.label_section.setObjectName(u"label_section")
        self.label_section.setMaximumSize(QSize(16777215, 25))
        self.label_section.setFont(font1)
        self.label_section.setStyleSheet(u"")

        self.layout_body_text.addWidget(self.label_section)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.Card)


        self.retranslateUi(CardStudent)

        QMetaObject.connectSlotsByName(CardStudent)
    # setupUi

    def retranslateUi(self, CardStudent):
        CardStudent.setWindowTitle(QCoreApplication.translate("CardStudent", u"Form", None))
        self.label_photo.setText("")
        self.label_name.setText(QCoreApplication.translate("CardStudent", u"Name", None))
        self.label_studentid.setText(QCoreApplication.translate("CardStudent", u"Student ID", None))
        self.label_section.setText(QCoreApplication.translate("CardStudent", u"Section", None))
    # retranslateUi

