# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LessonDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_LessonDialog(object):
    def setupUi(self, LessonDialog):
        if not LessonDialog.objectName():
            LessonDialog.setObjectName(u"LessonDialog")
        LessonDialog.resize(900, 351)
        LessonDialog.setMinimumSize(QSize(697, 351))
        LessonDialog.setMaximumSize(QSize(900, 351))
        LessonDialog.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(0, 0, 0); background-color: rgb(222, 221, 218);")
        self.verticalLayout = QVBoxLayout(LessonDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(LessonDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_img = QLabel(self.widget_4)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setMinimumSize(QSize(200, 200))
        self.label_img.setMaximumSize(QSize(200, 200))
        self.label_img.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.label_img.setPixmap(QPixmap(u":/Images/Images/no-image2.png"))
        self.label_img.setScaledContents(True)
        self.label_img.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_img, 0, 0, 1, 1)

        self.btnUploadPhoto = QPushButton(self.widget_4)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")
        self.btnUploadPhoto.setMinimumSize(QSize(0, 30))
        self.btnUploadPhoto.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.btnUploadPhoto, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_4)

        self.widget_right = QWidget(self.widget)
        self.widget_right.setObjectName(u"widget_right")
        self.formLayout = QFormLayout(self.widget_right)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget_right)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(0, 0, 0);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.txtLessonTitle = QLineEdit(self.widget_right)
        self.txtLessonTitle.setObjectName(u"txtLessonTitle")
        self.txtLessonTitle.setMinimumSize(QSize(0, 30))
        self.txtLessonTitle.setMaximumSize(QSize(16777215, 30))
        self.txtLessonTitle.setStyleSheet(u"font: 11pt \"Inter\"; padding: 0px 10px 0px; color: rgb(0, 0, 0); background-color: rgb(246, 245, 244);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtLessonTitle)

        self.label_2 = QLabel(self.widget_right)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(0, 0, 0);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.cmbGradingPeriod = QComboBox(self.widget_right)
        self.cmbGradingPeriod.setObjectName(u"cmbGradingPeriod")
        self.cmbGradingPeriod.setMinimumSize(QSize(0, 30))
        self.cmbGradingPeriod.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbGradingPeriod)

        self.label_3 = QLabel(self.widget_right)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(0, 0, 0);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.txtChapter = QLineEdit(self.widget_right)
        self.txtChapter.setObjectName(u"txtChapter")
        self.txtChapter.setMinimumSize(QSize(0, 30))
        self.txtChapter.setMaximumSize(QSize(16777215, 30))
        self.txtChapter.setStyleSheet(u"font: 11pt \"Inter\"; padding: 0px 10px 0px; color: rgb(0, 0, 0); background-color: rgb(246, 245, 244);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtChapter)

        self.label_4 = QLabel(self.widget_right)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(0, 0, 0);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.txtLessonNumber = QLineEdit(self.widget_right)
        self.txtLessonNumber.setObjectName(u"txtLessonNumber")
        self.txtLessonNumber.setMinimumSize(QSize(0, 30))
        self.txtLessonNumber.setMaximumSize(QSize(16777215, 30))
        self.txtLessonNumber.setStyleSheet(u"font: 11pt \"Inter\"; padding: 0px 10px 0px; color: rgb(0, 0, 0); background-color: rgb(246, 245, 244);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtLessonNumber)

        self.label_5 = QLabel(self.widget_right)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 11pt \"Inter\"; color: rgb(0, 0, 0);")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.widget_3 = QWidget(self.widget_right)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.txtLessonPath = QLineEdit(self.widget_3)
        self.txtLessonPath.setObjectName(u"txtLessonPath")
        self.txtLessonPath.setMinimumSize(QSize(0, 30))
        self.txtLessonPath.setMaximumSize(QSize(16777215, 30))
        self.txtLessonPath.setStyleSheet(u"font: 11pt \"Inter\"; padding: 0px 10px 0px; color: rgb(0, 0, 0); background-color: rgb(246, 245, 244);")

        self.horizontalLayout_2.addWidget(self.txtLessonPath)

        self.btnBrowse = QPushButton(self.widget_3)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setMinimumSize(QSize(30, 30))
        self.btnBrowse.setMaximumSize(QSize(30, 30))
        self.btnBrowse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnBrowse)


        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.widget_3)


        self.horizontalLayout_3.addWidget(self.widget_right)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(LessonDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(436, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.widget_2)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(80, 30))
        self.btnCancel.setMaximumSize(QSize(80, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.widget_2)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(80, 30))
        self.btnSave.setMaximumSize(QSize(80, 30))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(LessonDialog)

        QMetaObject.connectSlotsByName(LessonDialog)
    # setupUi

    def retranslateUi(self, LessonDialog):
        LessonDialog.setWindowTitle(QCoreApplication.translate("LessonDialog", u"Dialog", None))
        self.label_img.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("LessonDialog", u"Update photo", None))
        self.label.setText(QCoreApplication.translate("LessonDialog", u"Lesson Title", None))
        self.label_2.setText(QCoreApplication.translate("LessonDialog", u"Grading Period", None))
        self.cmbGradingPeriod.setStyleSheet(QCoreApplication.translate("LessonDialog", u"font: 11pt \"Inter\"; padding: 0px 10px 0px; color: rgb(0, 0, 0); background-color: rgb(246, 245, 244);", None))
        self.label_3.setText(QCoreApplication.translate("LessonDialog", u"Chapter", None))
        self.label_4.setText(QCoreApplication.translate("LessonDialog", u"Lesson Number", None))
        self.label_5.setText(QCoreApplication.translate("LessonDialog", u"Path", None))
        self.btnBrowse.setText(QCoreApplication.translate("LessonDialog", u"...", None))
        self.btnCancel.setText(QCoreApplication.translate("LessonDialog", u"Cancel", None))
        self.btnSave.setText(QCoreApplication.translate("LessonDialog", u"Save", None))
    # retranslateUi

