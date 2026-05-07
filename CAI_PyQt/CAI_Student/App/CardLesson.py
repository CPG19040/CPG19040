# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CardLesson.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_CardLesson(object):
    def setupUi(self, CardLesson):
        if not CardLesson.objectName():
            CardLesson.setObjectName(u"CardLesson")
        CardLesson.resize(414, 172)
        CardLesson.setMaximumSize(QSize(16777215, 172))
        CardLesson.setFocusPolicy(Qt.StrongFocus)
        CardLesson.setStyleSheet(u"#CardLesson { background-color: transparent; }")
        self.horizontalLayout = QHBoxLayout(CardLesson)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(CardLesson)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 172))
        self.widget_2.setMaximumSize(QSize(16777215, 172))
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"	background-color: #f8e6cb;\n"
"	border-radius: 15px;\n"
"	border: 1px solid #ddd;\n"
"}\n"
"#widget_2:hover {\n"
"	border: 2px solid #946544;\n"
"	background-color: #f7fbfe;\n"
"}\n"
"/* This style applies when the custom property is true */\n"
"#widget_2[selected=\"true\"] {\n"
"	background-color: #e1f5fe;\n"
"	border: 2px solid #3498db;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.label_LessonImage = QLabel(self.widget_2)
        self.label_LessonImage.setObjectName(u"label_LessonImage")
        self.label_LessonImage.setMinimumSize(QSize(150, 150))
        self.label_LessonImage.setMaximumSize(QSize(150, 150))
        self.label_LessonImage.setStyleSheet(u"#label_LessonImage { background-color: rgb(205, 171, 143); border-radius: 10px; }")
        self.label_LessonImage.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_LessonImage)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_LessonNumber = QLabel(self.widget_3)
        self.label_LessonNumber.setObjectName(u"label_LessonNumber")
        self.label_LessonNumber.setMinimumSize(QSize(90, 50))
        self.label_LessonNumber.setMaximumSize(QSize(100, 50))
        self.label_LessonNumber.setLayoutDirection(Qt.LeftToRight)
        self.label_LessonNumber.setStyleSheet(u"font: 20pt \"Kissy Hugs\"; color: rgb(255, 255, 255); border-image: url(:/Images/Images/button_wood.png);")
        self.label_LessonNumber.setScaledContents(True)
        self.label_LessonNumber.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_LessonNumber)

        self.label_LessonName = QLabel(self.widget_3)
        self.label_LessonName.setObjectName(u"label_LessonName")
        self.label_LessonName.setMinimumSize(QSize(0, 26))
        self.label_LessonName.setMaximumSize(QSize(16777215, 26))
        self.label_LessonName.setLayoutDirection(Qt.LeftToRight)
        self.label_LessonName.setStyleSheet(u"font: 63 14pt \"Inter Medium\"; color: rgb(99, 69, 44);")
        self.label_LessonName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_LessonName)


        self.verticalLayout.addWidget(self.widget_3)

        self.label_Chapter = QLabel(self.widget)
        self.label_Chapter.setObjectName(u"label_Chapter")
        self.label_Chapter.setMinimumSize(QSize(0, 26))
        self.label_Chapter.setMaximumSize(QSize(16777215, 26))
        self.label_Chapter.setLayoutDirection(Qt.LeftToRight)
        self.label_Chapter.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(134, 94, 60);")
        self.label_Chapter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_Chapter)

        self.label_Chapter_2 = QLabel(self.widget)
        self.label_Chapter_2.setObjectName(u"label_Chapter_2")
        self.label_Chapter_2.setMinimumSize(QSize(0, 26))
        self.label_Chapter_2.setMaximumSize(QSize(16777215, 26))
        self.label_Chapter_2.setLayoutDirection(Qt.LeftToRight)
        self.label_Chapter_2.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(134, 94, 60);")
        self.label_Chapter_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_Chapter_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(CardLesson)

        QMetaObject.connectSlotsByName(CardLesson)
    # setupUi

    def retranslateUi(self, CardLesson):
        CardLesson.setWindowTitle(QCoreApplication.translate("CardLesson", u"Frame", None))
        self.label_LessonImage.setText("")
        self.label_LessonNumber.setText(QCoreApplication.translate("CardLesson", u"000", None))
        self.label_LessonName.setText(QCoreApplication.translate("CardLesson", u"Lesson Name", None))
        self.label_Chapter.setText(QCoreApplication.translate("CardLesson", u"Chapter 1", None))
        self.label_Chapter_2.setText(QCoreApplication.translate("CardLesson", u"First Grading", None))
    # retranslateUi

