# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomizedDialog.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_CustomDialog(object):
    def setupUi(self, CustomDialog):
        if not CustomDialog.objectName():
            CustomDialog.setObjectName(u"CustomDialog")
        CustomDialog.resize(415, 306)
        CustomDialog.setMinimumSize(QSize(415, 306))
        CustomDialog.setMaximumSize(QSize(415, 306))
        CustomDialog.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(CustomDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(CustomDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#widget { border-image: url(:/Images/Images/slab.png); }")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 30)
        self.widget_WindowsButtons = QWidget(self.widget)
        self.widget_WindowsButtons.setObjectName(u"widget_WindowsButtons")
        self.widget_WindowsButtons.setMinimumSize(QSize(0, 40))
        self.widget_WindowsButtons.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_WindowsButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.btnClose = QPushButton(self.widget_WindowsButtons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(40, 40))
        self.btnClose.setMaximumSize(QSize(40, 40))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"#btnClose { border-image: url(:/Images/Images/wood_round_ex.png); }\n"
"#btnClose:hover { border-image: url(:/Images/Images/wood_round_ex2.png); }")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout_2.addWidget(self.widget_WindowsButtons)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"#widget_2 { border-image: url(:/Images/Images/paper.svg); margin: 0px 20px 0px; }")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 9, -1)
        self.label_message = QLabel(self.widget_2)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setStyleSheet(u"padding: 10px 30px 10px; font: 13pt \"Inter Medium\"; color: green;")
        self.label_message.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_message.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_message)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(CustomDialog)

        QMetaObject.connectSlotsByName(CustomDialog)
    # setupUi

    def retranslateUi(self, CustomDialog):
        CustomDialog.setWindowTitle(QCoreApplication.translate("CustomDialog", u"Dialog", None))
        self.btnClose.setText("")
        self.label_message.setText(QCoreApplication.translate("CustomDialog", u"Hello World", None))
    # retranslateUi

