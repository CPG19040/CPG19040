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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QFrame,
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        if not MessageBox.objectName():
            MessageBox.setObjectName(u"MessageBox")
        MessageBox.setWindowModality(Qt.NonModal)
        MessageBox.resize(700, 287)
        MessageBox.setMinimumSize(QSize(500, 0))
        MessageBox.setStyleSheet(u"* {\n"
"    color: black;\n"
"    font: 10pt \"Inter\";\n"
"    background-color: rgb(222, 221, 218);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: #fff;\n"
"}")
        MessageBox.setModal(True)
        self.verticalLayout = QVBoxLayout(MessageBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dlg_frame_header = QFrame(MessageBox)
        self.dlg_frame_header.setObjectName(u"dlg_frame_header")
        self.dlg_frame_header.setMinimumSize(QSize(0, 35))
        self.dlg_frame_header.setMaximumSize(QSize(16777215, 35))
        self.dlg_frame_header.setMouseTracking(True)
        self.dlg_frame_header.setStyleSheet(u"#dlg_frame_header {\n"
"	background-color: #deddda;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"	border: 1px solid #7a7a7a;\n"
"	border-bottom: none;\n"
"}")
        self.dlg_frame_header.setFrameShape(QFrame.StyledPanel)
        self.dlg_frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.dlg_frame_header)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(13, 0, 4, 0)
        self.widget_window_icon = QWidget(self.dlg_frame_header)
        self.widget_window_icon.setObjectName(u"widget_window_icon")
        self.widget_window_icon.setMinimumSize(QSize(0, 34))
        self.widget_window_icon.setMaximumSize(QSize(16777215, 34))
        self.widget_window_icon.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_window_icon)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_icon = QLabel(self.widget_window_icon)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setMinimumSize(QSize(30, 30))
        self.label_icon.setMaximumSize(QSize(30, 30))
        self.label_icon.setPixmap(QPixmap(u":/Images/Images/information.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_icon)

        self.label_windowTitle = QLabel(self.widget_window_icon)
        self.label_windowTitle.setObjectName(u"label_windowTitle")
        self.label_windowTitle.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label_windowTitle.setFont(font)
        self.label_windowTitle.setStyleSheet(u"background: transparent;\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"Inter SemiBold\";")
        self.label_windowTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_windowTitle)


        self.horizontalLayout_6.addWidget(self.widget_window_icon)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.dlg_frame_header)

        self.widget_body = QWidget(MessageBox)
        self.widget_body.setObjectName(u"widget_body")
        self.widget_body.setStyleSheet(u"#widget_body {\n"
"	background-color: #deddda;\n"
"	border: 1px solid #7a7a7a;\n"
"	border-bottom-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"	border-top: none;\n"
"}\n"
"\n"
"#plainTextEdit {\n"
"	border: none;\n"
"	background-color: #deddda;\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"] {\n"
"	border: 1px solid #0a5128;\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px 0px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #1ebd5d, \n"
"                                stop:1 #107f3f);\n"
"    color: #FFF;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #2ecc71, \n"
"                                stop:1 #27AE60);\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 "
                        "#0b572a, \n"
"                                stop:1 #129046); \n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:disabled {\n"
"    background: #A5D6A7;\n"
"    color: #E8F5E9;\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"*[class=\"button-normal\"] {\n"
"	font: 10pt \"Inter\";\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #d8ecf6);\n"
"	color: black;\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(154, 153, 150);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:hover {\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #ffffff, \n"
"                                stop:1 #f2f6f8);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #dce5e9, \n"
"                                stop:1 #ffffff);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:disabled {\n"
"	background"
                        ": #f5f5f5;\n"
"	border: 1px solid #dcdcdc;\n"
"	color: #aeaeae;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #7a7a7a;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 4. HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #7a7a7a;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #574939;\n"
"}\n"
"\n"
"/* 5. REMOVE BUTTONS & TRACK BACKGROUNDS */\n"
"/* This handles both horizontal and vertical arrows/tracks */\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical"
                        ",\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, -1, 12, -1)
        self.plainTextEdit = QPlainTextEdit(self.widget_body)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.widget_window_buttons = QWidget(self.widget_body)
        self.widget_window_buttons.setObjectName(u"widget_window_buttons")
        self.widget_window_buttons.setMinimumSize(QSize(0, 36))
        self.widget_window_buttons.setMaximumSize(QSize(16777215, 36))
        self.widget_window_buttons.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_window_buttons)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.btnYes = QPushButton(self.widget_window_buttons)
        self.btnYes.setObjectName(u"btnYes")
        self.btnYes.setMinimumSize(QSize(100, 30))
        self.btnYes.setMaximumSize(QSize(100, 30))
        self.btnYes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnYes.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.btnYes)

        self.btnYesAll = QPushButton(self.widget_window_buttons)
        self.btnYesAll.setObjectName(u"btnYesAll")
        self.btnYesAll.setMinimumSize(QSize(100, 30))
        self.btnYesAll.setMaximumSize(QSize(100, 30))
        self.btnYesAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnYesAll.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.btnYesAll)

        self.btnOk = QPushButton(self.widget_window_buttons)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setMinimumSize(QSize(100, 30))
        self.btnOk.setMaximumSize(QSize(100, 30))
        self.btnOk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnOk.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.btnOk)

        self.btnNo = QPushButton(self.widget_window_buttons)
        self.btnNo.setObjectName(u"btnNo")
        self.btnNo.setMinimumSize(QSize(100, 30))
        self.btnNo.setMaximumSize(QSize(100, 30))
        self.btnNo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNo.setStyleSheet(u"")
        self.btnNo.setIconSize(QSize(12, 12))

        self.horizontalLayout_13.addWidget(self.btnNo)

        self.btnNoAll = QPushButton(self.widget_window_buttons)
        self.btnNoAll.setObjectName(u"btnNoAll")
        self.btnNoAll.setMinimumSize(QSize(100, 30))
        self.btnNoAll.setMaximumSize(QSize(100, 30))
        self.btnNoAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnNoAll.setStyleSheet(u"")
        self.btnNoAll.setIconSize(QSize(12, 12))

        self.horizontalLayout_13.addWidget(self.btnNoAll)

        self.btnCancel = QPushButton(self.widget_window_buttons)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCancel.setStyleSheet(u"")
        self.btnCancel.setIconSize(QSize(12, 12))

        self.horizontalLayout_13.addWidget(self.btnCancel)


        self.verticalLayout_2.addWidget(self.widget_window_buttons)


        self.verticalLayout.addWidget(self.widget_body)


        self.retranslateUi(MessageBox)

        QMetaObject.connectSlotsByName(MessageBox)
    # setupUi

    def retranslateUi(self, MessageBox):
        MessageBox.setWindowTitle(QCoreApplication.translate("MessageBox", u"Message", None))
        self.label_icon.setText("")
        self.label_windowTitle.setText("")
        self.btnYes.setText(QCoreApplication.translate("MessageBox", u"Yes", None))
        self.btnYes.setProperty(u"class", QCoreApplication.translate("MessageBox", u"button-green", None))
        self.btnYesAll.setText(QCoreApplication.translate("MessageBox", u"Yes to All", None))
        self.btnYesAll.setProperty(u"class", QCoreApplication.translate("MessageBox", u"button-green", None))
        self.btnOk.setText(QCoreApplication.translate("MessageBox", u"OK", None))
        self.btnOk.setProperty(u"class", QCoreApplication.translate("MessageBox", u"button-green", None))
        self.btnNo.setText(QCoreApplication.translate("MessageBox", u"No", None))
        self.btnNo.setProperty(u"class", QCoreApplication.translate("MessageBox", u"button-normal", None))
        self.btnNoAll.setText(QCoreApplication.translate("MessageBox", u"No to All", None))
        self.btnNoAll.setProperty(u"class", QCoreApplication.translate("MessageBox", u"button-normal", None))
        self.btnCancel.setText(QCoreApplication.translate("MessageBox", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("MessageBox", u"button-normal", None))
    # retranslateUi

