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
        CardStudent.resize(423, 100)
        CardStudent.setMinimumSize(QSize(0, 100))
        CardStudent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        CardStudent.setFocusPolicy(Qt.StrongFocus)
        CardStudent.setStyleSheet(u"#CardStudent {\n"
"	border-image: url(:/Images/Images/name_tag_1.svg)\n"
"}\n"
"\n"
"#CardStudent:hover {\n"
"	border-image: url(:/Images/Images/name_tag_2.svg);\n"
"}\n"
"\n"
"#CardStudent[selected=\"true\"] {\n"
"	border-image: url(:/Images/Images/name_tag_2.svg);\n"
"}")
        self.horizontalLayout = QHBoxLayout(CardStudent)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(CardStudent)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 100))
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_profile = QLabel(self.widget_2)
        self.label_profile.setObjectName(u"label_profile")
        self.label_profile.setMinimumSize(QSize(100, 100))
        self.label_profile.setMaximumSize(QSize(100, 100))
        self.label_profile.setStyleSheet(u"#label_profile {\n"
"	background-color: #FFF;\n"
"	border-radius: 50px;\n"
"	border: 5px solid #664733;\n"
"}")
        self.label_profile.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_profile)

        self.widget_1 = QWidget(self.widget_2)
        self.widget_1.setObjectName(u"widget_1")
        self.info_layout = QVBoxLayout(self.widget_1)
        self.info_layout.setSpacing(0)
        self.info_layout.setObjectName(u"info_layout")
        self.info_layout.setContentsMargins(-1, 9, 16, 9)
        self.label_student_name = QLabel(self.widget_1)
        self.label_student_name.setObjectName(u"label_student_name")
        self.label_student_name.setLayoutDirection(Qt.LeftToRight)
        self.label_student_name.setStyleSheet(u"#label_student_name {\n"
"	font: 20pt \"Biscuit Glitch\";\n"
"	color: rgb(99, 69, 44)\n"
"}")
        self.label_student_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.info_layout.addWidget(self.label_student_name)

        self.label_student_id = QLabel(self.widget_1)
        self.label_student_id.setObjectName(u"label_student_id")
        self.label_student_id.setMinimumSize(QSize(0, 26))
        self.label_student_id.setMaximumSize(QSize(16777215, 26))
        self.label_student_id.setLayoutDirection(Qt.LeftToRight)
        self.label_student_id.setStyleSheet(u"font: 11pt \"Inter SemiBold\"; color: rgb(99, 69, 44);")
        self.label_student_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.info_layout.addWidget(self.label_student_id)


        self.horizontalLayout_3.addWidget(self.widget_1)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(CardStudent)

        QMetaObject.connectSlotsByName(CardStudent)
    # setupUi

    def retranslateUi(self, CardStudent):
        CardStudent.setWindowTitle(QCoreApplication.translate("CardStudent", u"Frame", None))
        self.label_profile.setText("")
        self.label_student_name.setText(QCoreApplication.translate("CardStudent", u"FirstName A. LastName", None))
        self.label_student_id.setText(QCoreApplication.translate("CardStudent", u"2026-0000-STU", None))
    # retranslateUi

