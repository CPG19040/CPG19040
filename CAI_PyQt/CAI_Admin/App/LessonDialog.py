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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_LessonDialog(object):
    def setupUi(self, LessonDialog):
        if not LessonDialog.objectName():
            LessonDialog.setObjectName(u"LessonDialog")
        LessonDialog.resize(939, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LessonDialog.sizePolicy().hasHeightForWidth())
        LessonDialog.setSizePolicy(sizePolicy)
        LessonDialog.setMinimumSize(QSize(939, 500))
        LessonDialog.setMaximumSize(QSize(1000, 500))
        LessonDialog.setStyleSheet(u"* {\n"
"    color: #000000;\n"
"    font: 10pt \"Inter\";\n"
"}\n"
"\n"
"QDialog {\n"
"    background: transparent;\n"
"}\n"
"\n"
"#frame_header {\n"
"    background-color: #deddda;\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border: 1px solid #7a7a7a;\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"#label_windowTitle {\n"
"    background: transparent;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"    color: #111827;\n"
"}\n"
"\n"
"#widget_body {\n"
"    background-color: #deddda;\n"
"    border: 1px solid #7a7a7a;\n"
"    border-top: none;\n"
"}\n"
"\n"
"\n"
"QPushButton[class=\"button-green\"] {\n"
"    border: 1px solid #0a5128;\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px 0px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1ebd5d, stop:1 #107f3f);\n"
"    color: #FFF;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2ecc71, sto"
                        "p:1 #27AE60);\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0b572a, stop:1 #129046);\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:disabled {\n"
"    background: #A5D6A7;\n"
"    color: #E8F5E9;\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"QPushButton[class=\"button-normal\"] {\n"
"    color: #000000;\n"
"    font: 10pt \"Inter\";\n"
"    border: 1px solid #9a9996;\n"
"    border-radius: 15px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);\n"
"}\n"
"\n"
"QPushButton[class=\"button-normal\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f2f6f8);\n"
"}\n"
"\n"
"QPushButton[class=\"button-normal\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton[class=\"button-normal\"]:disabled {\n"
"    color: #aeaeae;\n"
"    border: 1px solid #dcdcdc;\n"
"    background: #f5f5"
                        "f5;\n"
"}\n"
"\n"
"\n"
"*[class=\"input-field\"] {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #999;\n"
"    border-left: none;\n"
"    border-top-right-radius: 18px;\n"
"    border-bottom-right-radius: 18px;\n"
"    padding: 0px 8px;\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLabel,\n"
"*[class=\"input-and-browse\"] QLabel {\n"
"    background-color: #c0bfbc;\n"
"    border: 1px solid #999;\n"
"    border-right: none;\n"
"    border-top-left-radius: 18px;\n"
"    border-bottom-left-radius: 18px;\n"
"    padding-left: 8px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"\n"
"*[class=\"input-field\"] QComboBox {\n"
"    border: 1px solid #999;\n"
"    border-left: none;\n"
"    padding: 0px 10px;\n"
"    background-color: #ffffff;\n"
"    color: #1f2937;\n"
"    font: 10pt \"Inter Medium\";\n"
"    selection-background-color: #bfdbfe;\n"
"    border-top-right-radius: 18px;\n"
"    border-bott"
                        "om-right-radius: 18px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    border: none;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff !important;\n"
"    border: 1px solid #999;\n"
"    selection-background-color: #bfdbfe;\n"
"    selection-color: #111827;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 0px 15px;\n"
"    border-radius: 4px;\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #bfdbfe;\n"
"    color: #1118"
                        "27;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #f3f4f6;\n"
"    border: none;\n"
"    color: #999;\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/Images/Images/caret-down-disabled.png);\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    font: 10pt \"Inter Medium\";\n"
"    height: 30px;\n"
"    border: 1px solid #999;\n"
"    border-radius: 15px;\n"
"    padding: 0px 5px;\n"
"    background-color: #ffffff;\n"
"    color: #1f2937;\n"
"    selection-background-color: #bfdbfe;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button {\n"
"    subcontr"
                        "ol-origin: border;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    padding: 6px 10px 6px 2px;\n"
"    color: #6b7280;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom right;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/Images/Images/caret-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/Images/Images/caret-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"#btnMinimize {\n"
"    border-radius: 12px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#btnMinimize:hover {\n"
"    background-color: #f8e45c;\n"
"}\n"
"\n"
"#btnClose {\n"
"    border-radius: 12px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#btnClose:hover {\n"
"    background-color: #f66151;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] {\n"
"    background: transpare"
                        "nt;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #999999;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    padding: 0px 8px;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLineEdit:hover {\n"
"    border: 1px solid #3498db;\n"
"    border-right: none;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLineEdit:focus {\n"
"    border: 1px solid #007BFF;\n"
"    border-right: none;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] #btnBrowse {\n"
"    font: 10pt \"Inter\";\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #999999;\n"
"    padding: 5px 15px;\n"
"\n"
"    border-top-right-radius: 18px;\n"
"    border-bottom-right-radius: 18px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] #btnBrowse:hover {\n"
"    background-color: #e0e0e0;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(LessonDialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(LessonDialog)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 35))
        self.frame_header.setMaximumSize(QSize(16777215, 35))
        self.frame_header.setMouseTracking(True)
        self.frame_header.setStyleSheet(u"")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(4, 0, 0, 0)
        self.widget_window_icon = QWidget(self.frame_header)
        self.widget_window_icon.setObjectName(u"widget_window_icon")
        self.widget_window_icon.setMinimumSize(QSize(72, 34))
        self.widget_window_icon.setMaximumSize(QSize(72, 34))
        self.widget_window_icon.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_window_icon)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.widget_window_icon)

        self.label_windowTitle = QLabel(self.frame_header)
        self.label_windowTitle.setObjectName(u"label_windowTitle")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_windowTitle.setFont(font)
        self.label_windowTitle.setStyleSheet(u"")
        self.label_windowTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_windowTitle)

        self.widget_window_buttons = QWidget(self.frame_header)
        self.widget_window_buttons.setObjectName(u"widget_window_buttons")
        self.widget_window_buttons.setMinimumSize(QSize(72, 34))
        self.widget_window_buttons.setMaximumSize(QSize(72, 34))
        self.widget_window_buttons.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_window_buttons)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.widget_window_buttons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(24, 24))
        self.btnMinimize.setMaximumSize(QSize(24, 24))
        self.btnMinimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Images/Images/minimize-sign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QSize(12, 12))

        self.horizontalLayout_13.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.widget_window_buttons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(24, 24))
        self.btnClose.setMaximumSize(QSize(24, 24))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)

        self.horizontalLayout_13.addWidget(self.btnClose)


        self.horizontalLayout_9.addWidget(self.widget_window_buttons)


        self.verticalLayout_3.addWidget(self.frame_header)

        self.widget_body = QWidget(LessonDialog)
        self.widget_body.setObjectName(u"widget_body")
        self.widget_body.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_body)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(12, -1, 12, -1)
        self.widget_4 = QWidget(self.widget_body)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_img = QLabel(self.widget_4)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setMinimumSize(QSize(300, 300))
        self.label_img.setMaximumSize(QSize(300, 300))
        self.label_img.setStyleSheet(u"background-color: rgb(246, 245, 244); border-radius: 20px;")
        self.label_img.setPixmap(QPixmap(u":/Images/Images/no-image2.png"))
        self.label_img.setScaledContents(True)
        self.label_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_img)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 0)
        self.btnUploadPhoto = QPushButton(self.widget_4)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")
        self.btnUploadPhoto.setMinimumSize(QSize(200, 30))
        self.btnUploadPhoto.setMaximumSize(QSize(200, 30))
        self.btnUploadPhoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btnUploadPhoto)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_10.addWidget(self.widget_4)

        self.widget_right = QWidget(self.widget_body)
        self.widget_right.setObjectName(u"widget_right")
        self.verticalLayout_2 = QVBoxLayout(self.widget_right)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 30, 0, 0)
        self.widget_6 = QWidget(self.widget_right)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(132, 36))
        self.label.setMaximumSize(QSize(132, 36))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.txtLessonTitle = QLineEdit(self.widget_6)
        self.txtLessonTitle.setObjectName(u"txtLessonTitle")
        self.txtLessonTitle.setMinimumSize(QSize(0, 36))
        self.txtLessonTitle.setMaximumSize(QSize(16777215, 36))
        self.txtLessonTitle.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.txtLessonTitle)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_right)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(132, 36))
        self.label_2.setMaximumSize(QSize(132, 36))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.cmbGradingPeriod = QComboBox(self.widget_7)
        self.cmbGradingPeriod.setObjectName(u"cmbGradingPeriod")
        self.cmbGradingPeriod.setMinimumSize(QSize(0, 36))
        self.cmbGradingPeriod.setMaximumSize(QSize(16777215, 36))
        self.cmbGradingPeriod.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.cmbGradingPeriod)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_right)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(132, 36))
        self.label_3.setMaximumSize(QSize(132, 36))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.txtChapter = QLineEdit(self.widget_8)
        self.txtChapter.setObjectName(u"txtChapter")
        self.txtChapter.setMinimumSize(QSize(0, 36))
        self.txtChapter.setMaximumSize(QSize(16777215, 36))
        self.txtChapter.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.txtChapter)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_right)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(132, 36))
        self.label_4.setMaximumSize(QSize(132, 36))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.txtLessonNumber = QLineEdit(self.widget_9)
        self.txtLessonNumber.setObjectName(u"txtLessonNumber")
        self.txtLessonNumber.setMinimumSize(QSize(0, 36))
        self.txtLessonNumber.setMaximumSize(QSize(16777215, 36))
        self.txtLessonNumber.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.txtLessonNumber)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_path = QWidget(self.widget_right)
        self.widget_path.setObjectName(u"widget_path")
        self.widget_path.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_path)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_path)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(132, 36))
        self.label_5.setMaximumSize(QSize(132, 36))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.txtLessonPath = QLineEdit(self.widget_path)
        self.txtLessonPath.setObjectName(u"txtLessonPath")
        self.txtLessonPath.setMinimumSize(QSize(0, 36))
        self.txtLessonPath.setMaximumSize(QSize(16777215, 36))
        self.txtLessonPath.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.txtLessonPath)

        self.btnBrowse = QPushButton(self.widget_path)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setMinimumSize(QSize(50, 36))
        self.btnBrowse.setMaximumSize(QSize(16777215, 36))
        self.btnBrowse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnBrowse)


        self.verticalLayout_2.addWidget(self.widget_path)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.widget_footer = QWidget(self.widget_right)
        self.widget_footer.setObjectName(u"widget_footer")
        self.widget_footer.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_footer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, 12, -1)
        self.horizontalSpacer = QSpacerItem(436, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.widget_footer)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.widget_footer)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 30))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_2.addWidget(self.widget_footer)


        self.horizontalLayout_10.addWidget(self.widget_right)


        self.verticalLayout_3.addWidget(self.widget_body)


        self.retranslateUi(LessonDialog)

        QMetaObject.connectSlotsByName(LessonDialog)
    # setupUi

    def retranslateUi(self, LessonDialog):
        LessonDialog.setWindowTitle(QCoreApplication.translate("LessonDialog", u"Lesson Editor", None))
        self.label_windowTitle.setText(QCoreApplication.translate("LessonDialog", u"Lesson Editor", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.label_img.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("LessonDialog", u"Update photo", None))
        self.btnUploadPhoto.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"button-normal", None))
        self.label_6.setText(QCoreApplication.translate("LessonDialog", u"Aspect ratio (1:1)", None))
        self.widget_6.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label.setText(QCoreApplication.translate("LessonDialog", u"Lesson Title", None))
        self.widget_7.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label_2.setText(QCoreApplication.translate("LessonDialog", u"Grading Period", None))
        self.widget_8.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label_3.setText(QCoreApplication.translate("LessonDialog", u"Chapter", None))
        self.widget_9.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-field", None))
        self.label_4.setText(QCoreApplication.translate("LessonDialog", u"Lesson Number", None))
        self.widget_path.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"input-and-browse", None))
        self.label_5.setText(QCoreApplication.translate("LessonDialog", u"Path", None))
        self.btnBrowse.setText(QCoreApplication.translate("LessonDialog", u"\u2022\u2022\u2022", None))
        self.btnCancel.setText(QCoreApplication.translate("LessonDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("LessonDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("LessonDialog", u"button-green", None))
    # retranslateUi

