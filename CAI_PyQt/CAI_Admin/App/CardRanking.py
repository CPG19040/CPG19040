# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardRanking.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_CardRanking(object):
    def setupUi(self, CardRanking):
        if not CardRanking.objectName():
            CardRanking.setObjectName(u"CardRanking")
        CardRanking.resize(144, 200)
        CardRanking.setMinimumSize(QSize(0, 200))
        CardRanking.setMaximumSize(QSize(16777215, 200))
        CardRanking.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(CardRanking)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(CardRanking)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setStyleSheet(u"#widget_27 {\n"
"	background-color: #34a25b;\n"
"	border-radius: 18px;\n"
"}\n"
"\n"
"#widget_26 {\n"
"	background: transparent;\n"
"}\n"
"\n"
"#label_stud_name {\n"
"	color: #FFF;\n"
"	background-color: transparent;\n"
"	font: 12pt \"Inter Medium\";\n"
"}\n"
"\n"
"#label_student_score {\n"
"	font: 20pt \"Inter SemiBold\";\n"
"	background: transparent;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#label_student_place {\n"
"	font: 12pt \"Inter SemiBold\";\n"
"	border-radius: 12px;\n"
"	background-color: #57c27b;\n"
"	color: #FFF;\n"
"}")
        self.verticalLayout_37 = QVBoxLayout(self.widget_27)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 10, -1, 10)
        self.widget_26 = QWidget(self.widget_27)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_13)

        self.label_profile = QLabel(self.widget_26)
        self.label_profile.setObjectName(u"label_profile")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_profile.sizePolicy().hasHeightForWidth())
        self.label_profile.setSizePolicy(sizePolicy)
        self.label_profile.setMinimumSize(QSize(80, 80))
        self.label_profile.setMaximumSize(QSize(80, 80))
        self.label_profile.setStyleSheet(u"background-color: transparent;")
        self.label_profile.setPixmap(QPixmap(u":/Images/Images/profile_gray.png"))
        self.label_profile.setScaledContents(True)
        self.label_profile.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_profile)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_14)


        self.verticalLayout_37.addWidget(self.widget_26)

        self.label_stud_name = QLabel(self.widget_27)
        self.label_stud_name.setObjectName(u"label_stud_name")
        font = QFont()
        font.setFamilies([u"Inter Medium"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_stud_name.setFont(font)
        self.label_stud_name.setStyleSheet(u"")
        self.label_stud_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_stud_name)

        self.label_student_score = QLabel(self.widget_27)
        self.label_student_score.setObjectName(u"label_student_score")
        font1 = QFont()
        font1.setFamilies([u"Inter SemiBold"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_student_score.setFont(font1)
        self.label_student_score.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_student_score)

        self.label_student_place = QLabel(self.widget_27)
        self.label_student_place.setObjectName(u"label_student_place")
        self.label_student_place.setMinimumSize(QSize(0, 26))
        font2 = QFont()
        font2.setFamilies([u"Inter SemiBold"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_student_place.setFont(font2)
        self.label_student_place.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_student_place)


        self.horizontalLayout.addWidget(self.widget_27)


        self.retranslateUi(CardRanking)

        QMetaObject.connectSlotsByName(CardRanking)
    # setupUi

    def retranslateUi(self, CardRanking):
        CardRanking.setWindowTitle(QCoreApplication.translate("CardRanking", u"Form", None))
        self.label_profile.setText("")
        self.label_stud_name.setText(QCoreApplication.translate("CardRanking", u"Juan De La Cruz", None))
        self.label_student_score.setText(QCoreApplication.translate("CardRanking", u"00.00%", None))
        self.label_student_place.setText(QCoreApplication.translate("CardRanking", u"1st", None))
    # retranslateUi

