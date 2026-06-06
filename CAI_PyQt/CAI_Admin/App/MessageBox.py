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
from PySide6.QtWidgets import (QApplication, QDialog, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        if not MessageBox.objectName():
            MessageBox.setObjectName(u"MessageBox")
        MessageBox.resize(683, 325)
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
        self.verticalLayout_2 = QVBoxLayout(MessageBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit = QPlainTextEdit(MessageBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.retranslateUi(MessageBox)

        QMetaObject.connectSlotsByName(MessageBox)
    # setupUi

    def retranslateUi(self, MessageBox):
        MessageBox.setWindowTitle(QCoreApplication.translate("MessageBox", u"Message", None))
    # retranslateUi

