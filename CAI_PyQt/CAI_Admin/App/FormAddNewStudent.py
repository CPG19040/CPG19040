# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormAddNewStudent.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import resources_rc

class Ui_AddNewStudentDialog(object):
    def setupUi(self, AddNewStudentDialog):
        if not AddNewStudentDialog.objectName():
            AddNewStudentDialog.setObjectName(u"AddNewStudentDialog")
        AddNewStudentDialog.setEnabled(True)
        AddNewStudentDialog.resize(870, 711)
        AddNewStudentDialog.setMinimumSize(QSize(870, 711))
        AddNewStudentDialog.setMaximumSize(QSize(870, 711))
        AddNewStudentDialog.setStyleSheet(u"* {\n"
"    color: #000000;\n"
"    font: 10pt \"Inter\";\n"
"}\n"
"\n"
"#AddNewStudentDialog {\n"
"    background: transparent;\n"
"}\n"
"\n"
"#line_1,\n"
"#line_2,\n"
"#line_3 {\n"
"    background-color: #deddda;\n"
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
"#btnBrowseCSV {\n"
"    font: 10pt \"Inter\";\n"
"    background-color: #f3f4f6;\n"
"    color: #1f2937;\n"
"    border: 1px solid #999;\n"
"    border-top-right-radius: 18px;\n"
"    border-bottom-right-radius: 18px;\n"
"}\n"
"\n"
"#btnBrowseCSV:hover {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"#btnBrowseCSV:disabled {\n"
""
                        "    background-color: #e5e7eb;\n"
"    border: none;\n"
"    color: #999;\n"
"}\n"
"\n"
"#widget_CSV QLineEdit:disabled {\n"
"    background-color: #f3f4f6;\n"
"    border: none;\n"
"    color: #999;\n"
"}\n"
"\n"
"#txtCSVPath {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #999;\n"
"    border-right: none;\n"
"    border-top-left-radius: 18px;\n"
"    border-bottom-left-radius: 18px;\n"
"    padding: 0px 10px;\n"
"}\n"
"\n"
"#txtCSVPath:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"#txtCSVPath:hover {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"#txtCSVPath:disabled {\n"
"    background-color: #e5e7eb;\n"
"    border: none;\n"
"}\n"
"\n"
"*[class=\"button-normal\"] {\n"
"    color: #000000;\n"
"    font: 10pt \"Inter\";\n"
"    border: 1px solid #9a9996;\n"
"    border-radius: 15px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y"
                        "2:1, stop:0 #ffffff, stop:1 #f2f6f8);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);\n"
"}\n"
"\n"
"*[class=\"button-normal\"]:disabled {\n"
"    color: #aeaeae;\n"
"    border: 1px solid #dcdcdc;\n"
"    background: #f5f5f5;\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"] {\n"
"    border: 1px solid #059669;\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #10b981, stop:1 #059669);\n"
"    color: #ffffff;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34d399, stop:1 #10b981);\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #047857, stop:1 #059669); \n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:disabled {\n"
"    background: #a7f3d0;\n"
""
                        "    color: #065f46;\n"
"    opacity: 0.6;\n"
"}\n"
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
"*[class=\"input-field\"] QLabel {\n"
"    background-color: #d2d2d2;\n"
"    border-left: 1px solid #999;\n"
"    border-top: 1px solid #999;\n"
"    border-bottom: 1px solid #999;\n"
"    border-right: none;\n"
"    border-top-left-radius: 18px;\n"
"    border-bottom-left-radius: 18px;\n"
"    padding-left: 8px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLabel:disabled,\n"
"#label_17:disabled,\n"
"#label_24:disabled {\n"
"    color: #999;\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QProgressBar::c"
                        "hunk {\n"
"    background-color: #007BFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QPushButton:disabled, \n"
"*[class=\"input-field\"] QLineEdit:disabled, \n"
"*[class=\"input-field\"] QComboBox:disabled {\n"
"    background-color: #f3f4f6;\n"
"    border: none;\n"
"    color: #999;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #1f2937;\n"
"    spacing: 8px;\n"
"    padding: 0px 10px;\n"
"    background: transparent;\n"
"    font: 10pt \"Inter\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    background: #ffffff;\n"
"    border: 2px solid #999;\n"
"    min-width: 14px;\n"
"    min-height: 14px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #93c5fd;\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #999;\n"
"    border-left: none;\n"
"    padding: 0px 10px;\n"
"    background-color: #ffffff;\n"
"    color: #1f2937;\n"
"    font: 10pt \"Inter Medium\";\n"
"    selection-background-color: #bfdbf"
                        "e;\n"
"    border-top-right-radius: 18px;\n"
"    border-bottom-right-radius: 18px;\n"
"}\n"
"\n"
"QComboBox:focus, QLineEdit:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"QComboBox:hover, QLineEdit:hover {\n"
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
"QC"
                        "omboBox QAbstractItemView::item:hover {\n"
"    background-color: #bfdbfe;\n"
"    color: #111827;\n"
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
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    width: 8px;\n"
"    hei"
                        "ght: 8px;\n"
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
"}")
        self.verticalLayout_5 = QVBoxLayout(AddNewStudentDialog)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(AddNewStudentDialog)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 35))
        self.frame_header.setMaximumSize(QSize(16777215, 35))
        self.frame_header.setMouseTracking(True)
        self.frame_header.setStyleSheet(u"")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(4, 0, 0, 0)
        self.widget_window_icon = QWidget(self.frame_header)
        self.widget_window_icon.setObjectName(u"widget_window_icon")
        self.widget_window_icon.setMinimumSize(QSize(72, 34))
        self.widget_window_icon.setMaximumSize(QSize(72, 34))
        self.widget_window_icon.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_window_icon)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_15.addWidget(self.widget_window_icon)

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

        self.horizontalLayout_15.addWidget(self.label_windowTitle)

        self.widget_window_buttons = QWidget(self.frame_header)
        self.widget_window_buttons.setObjectName(u"widget_window_buttons")
        self.widget_window_buttons.setMinimumSize(QSize(72, 34))
        self.widget_window_buttons.setMaximumSize(QSize(72, 34))
        self.widget_window_buttons.setStyleSheet(u"")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_window_buttons)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_17.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.widget_window_buttons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(24, 24))
        self.btnClose.setMaximumSize(QSize(24, 24))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)

        self.horizontalLayout_17.addWidget(self.btnClose)


        self.horizontalLayout_15.addWidget(self.widget_window_buttons)


        self.verticalLayout_5.addWidget(self.frame_header)

        self.widget_body = QWidget(AddNewStudentDialog)
        self.widget_body.setObjectName(u"widget_body")
        self.widget_body.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_body)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, -1, 12, -1)
        self.widget = QWidget(self.widget_body)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.spinBox_SY1 = QSpinBox(self.widget)
        self.spinBox_SY1.setObjectName(u"spinBox_SY1")
        self.spinBox_SY1.setMinimumSize(QSize(80, 30))
        self.spinBox_SY1.setMaximumSize(QSize(80, 30))
        self.spinBox_SY1.setStyleSheet(u"")
        self.spinBox_SY1.setAlignment(Qt.AlignCenter)
        self.spinBox_SY1.setMinimum(2000)
        self.spinBox_SY1.setMaximum(3000)

        self.horizontalLayout_4.addWidget(self.spinBox_SY1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.spinBox_SY2 = QSpinBox(self.widget)
        self.spinBox_SY2.setObjectName(u"spinBox_SY2")
        self.spinBox_SY2.setMinimumSize(QSize(80, 30))
        self.spinBox_SY2.setMaximumSize(QSize(80, 30))
        self.spinBox_SY2.setStyleSheet(u"")
        self.spinBox_SY2.setAlignment(Qt.AlignCenter)
        self.spinBox_SY2.setMinimum(2000)
        self.spinBox_SY2.setMaximum(3000)

        self.horizontalLayout_4.addWidget(self.spinBox_SY2)

        self.btnRefreshSY = QPushButton(self.widget)
        self.btnRefreshSY.setObjectName(u"btnRefreshSY")
        self.btnRefreshSY.setMinimumSize(QSize(30, 30))
        self.btnRefreshSY.setMaximumSize(QSize(30, 30))
        self.btnRefreshSY.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Images/Images/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRefreshSY.setIcon(icon2)
        self.btnRefreshSY.setIconSize(QSize(22, 22))

        self.horizontalLayout_4.addWidget(self.btnRefreshSY)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget)

        self.line_1 = QFrame(self.widget_body)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setStyleSheet(u"")
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_1)

        self.widget_stud_info = QWidget(self.widget_body)
        self.widget_stud_info.setObjectName(u"widget_stud_info")
        self.widget_stud_info.setEnabled(True)
        self.widget_stud_info.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_stud_info)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.widget_stud_info)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_profile_pic = QLabel(self.widget_3)
        self.label_profile_pic.setObjectName(u"label_profile_pic")
        self.label_profile_pic.setMinimumSize(QSize(150, 150))
        self.label_profile_pic.setMaximumSize(QSize(150, 150))
        self.label_profile_pic.setPixmap(QPixmap(u":/Images/Images/profile.png"))
        self.label_profile_pic.setScaledContents(True)
        self.label_profile_pic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_profile_pic)

        self.btnUploadPhoto = QPushButton(self.widget_3)
        self.btnUploadPhoto.setObjectName(u"btnUploadPhoto")
        self.btnUploadPhoto.setMinimumSize(QSize(100, 30))
        self.btnUploadPhoto.setMaximumSize(QSize(16777215, 30))
        self.btnUploadPhoto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btnUploadPhoto)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_17)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_form = QWidget(self.widget_stud_info)
        self.widget_form.setObjectName(u"widget_form")
        self.widget_form.setEnabled(True)
        self.widget_form.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_form)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(100, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 36))
        self.label_8.setMaximumSize(QSize(100, 36))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.txtFirstName = QLineEdit(self.widget_2)
        self.txtFirstName.setObjectName(u"txtFirstName")
        self.txtFirstName.setMinimumSize(QSize(0, 36))
        self.txtFirstName.setMaximumSize(QSize(16777215, 36))
        self.txtFirstName.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.txtFirstName)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget_form)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 36))
        self.label_9.setMaximumSize(QSize(100, 36))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.txtMiddleName = QLineEdit(self.widget_4)
        self.txtMiddleName.setObjectName(u"txtMiddleName")
        self.txtMiddleName.setMinimumSize(QSize(0, 36))
        self.txtMiddleName.setMaximumSize(QSize(16777215, 36))
        self.txtMiddleName.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.txtMiddleName)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_form)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 36))
        self.label_10.setMaximumSize(QSize(100, 36))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.txtLastName = QLineEdit(self.widget_5)
        self.txtLastName.setObjectName(u"txtLastName")
        self.txtLastName.setMinimumSize(QSize(0, 36))
        self.txtLastName.setMaximumSize(QSize(16777215, 36))
        self.txtLastName.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.txtLastName)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_form)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 36))
        self.label_11.setMaximumSize(QSize(100, 36))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_11)

        self.cmbSection = QComboBox(self.widget_6)
        self.cmbSection.setObjectName(u"cmbSection")
        self.cmbSection.setMinimumSize(QSize(0, 36))
        self.cmbSection.setMaximumSize(QSize(16777215, 36))
        self.cmbSection.setStyleSheet(u"")
        self.cmbSection.setEditable(False)

        self.horizontalLayout_8.addWidget(self.cmbSection)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_form)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 36))
        self.label_12.setMaximumSize(QSize(100, 36))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.txtPassword = QLineEdit(self.widget_7)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setMinimumSize(QSize(0, 36))
        self.txtPassword.setMaximumSize(QSize(16777215, 36))
        self.txtPassword.setStyleSheet(u"")
        self.txtPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_9.addWidget(self.txtPassword)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_form)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 36))
        self.label_13.setMaximumSize(QSize(100, 36))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.cmbGender = QComboBox(self.widget_8)
        self.cmbGender.addItem("")
        self.cmbGender.addItem("")
        self.cmbGender.setObjectName(u"cmbGender")
        self.cmbGender.setMinimumSize(QSize(0, 36))
        self.cmbGender.setMaximumSize(QSize(16777215, 36))
        self.cmbGender.setStyleSheet(u"")
        self.cmbGender.setEditable(False)

        self.horizontalLayout_10.addWidget(self.cmbGender)


        self.verticalLayout_2.addWidget(self.widget_8)


        self.horizontalLayout.addWidget(self.widget_form)


        self.verticalLayout.addWidget(self.widget_stud_info)

        self.line_2 = QFrame(self.widget_body)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.widget_form_emergency = QWidget(self.widget_body)
        self.widget_form_emergency.setObjectName(u"widget_form_emergency")
        self.widget_form_emergency.setEnabled(True)
        self.widget_form_emergency.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_form_emergency)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_24 = QLabel(self.widget_form_emergency)
        self.label_24.setObjectName(u"label_24")
        font1 = QFont()
        font1.setFamilies([u"Inter SemiBold"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"font: 11pt \"Inter SemiBold\";")

        self.verticalLayout_3.addWidget(self.label_24)

        self.widget_10 = QWidget(self.widget_form_emergency)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(120, 36))
        self.label_22.setMaximumSize(QSize(16777215, 36))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_22)

        self.txtContactPerson = QLineEdit(self.widget_10)
        self.txtContactPerson.setObjectName(u"txtContactPerson")
        self.txtContactPerson.setMinimumSize(QSize(0, 36))
        self.txtContactPerson.setMaximumSize(QSize(16777215, 36))
        self.txtContactPerson.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.txtContactPerson)


        self.verticalLayout_3.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_form_emergency)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(120, 36))
        self.label_23.setMaximumSize(QSize(16777215, 36))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.txtContactNum = QLineEdit(self.widget_11)
        self.txtContactNum.setObjectName(u"txtContactNum")
        self.txtContactNum.setMinimumSize(QSize(0, 36))
        self.txtContactNum.setMaximumSize(QSize(16777215, 36))
        self.txtContactNum.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.txtContactNum)


        self.verticalLayout_3.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_form_emergency)

        self.line_3 = QFrame(self.widget_body)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.rb_importCSV = QRadioButton(self.widget_body)
        self.rb_importCSV.setObjectName(u"rb_importCSV")
        self.rb_importCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rb_importCSV.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.rb_importCSV)

        self.widget_CSV = QWidget(self.widget_body)
        self.widget_CSV.setObjectName(u"widget_CSV")
        self.widget_CSV.setEnabled(False)
        self.widget_CSV.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_CSV)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_12 = QWidget(self.widget_CSV)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 36))
        self.label_14.setMaximumSize(QSize(100, 36))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_14)

        self.cmbSection_2 = QComboBox(self.widget_12)
        self.cmbSection_2.setObjectName(u"cmbSection_2")
        self.cmbSection_2.setMinimumSize(QSize(0, 36))
        self.cmbSection_2.setMaximumSize(QSize(16777215, 36))
        self.cmbSection_2.setStyleSheet(u"")
        self.cmbSection_2.setEditable(False)

        self.horizontalLayout_14.addWidget(self.cmbSection_2)


        self.horizontalLayout_3.addWidget(self.widget_12)

        self.widget_9 = QWidget(self.widget_CSV)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.txtCSVPath = QLineEdit(self.widget_9)
        self.txtCSVPath.setObjectName(u"txtCSVPath")
        self.txtCSVPath.setMinimumSize(QSize(0, 36))
        self.txtCSVPath.setMaximumSize(QSize(16777215, 36))
        self.txtCSVPath.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.txtCSVPath)

        self.btnBrowseCSV = QPushButton(self.widget_9)
        self.btnBrowseCSV.setObjectName(u"btnBrowseCSV")
        self.btnBrowseCSV.setMinimumSize(QSize(100, 36))
        self.btnBrowseCSV.setMaximumSize(QSize(100, 36))
        self.btnBrowseCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBrowseCSV.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnBrowseCSV)


        self.horizontalLayout_3.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget_CSV)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progressBar = QProgressBar(self.widget_body)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnCancel = QPushButton(self.widget_body)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 30))
        self.btnCancel.setMaximumSize(QSize(100, 30))
        self.btnCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.widget_body)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 30))
        self.btnSave.setMaximumSize(QSize(100, 30))
        self.btnSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.widget_body)


        self.retranslateUi(AddNewStudentDialog)

        self.btnRefreshSY.setDefault(True)
        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(AddNewStudentDialog)
    # setupUi

    def retranslateUi(self, AddNewStudentDialog):
        AddNewStudentDialog.setWindowTitle(QCoreApplication.translate("AddNewStudentDialog", u"Student Registration", None))
        self.label_windowTitle.setText(QCoreApplication.translate("AddNewStudentDialog", u"Student Registration", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.label_15.setText(QCoreApplication.translate("AddNewStudentDialog", u"School Year:", None))
        self.label_16.setText(QCoreApplication.translate("AddNewStudentDialog", u"-", None))
        self.btnRefreshSY.setText("")
        self.btnRefreshSY.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
#if QT_CONFIG(tooltip)
        self.label_profile_pic.setToolTip(QCoreApplication.translate("AddNewStudentDialog", u"Aspect Ratio (1:1)", None))
#endif // QT_CONFIG(tooltip)
        self.label_profile_pic.setText("")
        self.btnUploadPhoto.setText(QCoreApplication.translate("AddNewStudentDialog", u"Update photo", None))
        self.btnUploadPhoto.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
        self.label_17.setText(QCoreApplication.translate("AddNewStudentDialog", u"Aspect ratio (1:1)", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_8.setText(QCoreApplication.translate("AddNewStudentDialog", u"First name", None))
        self.widget_4.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("AddNewStudentDialog", u"Middle name", None))
        self.widget_5.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("AddNewStudentDialog", u"Last name", None))
        self.widget_6.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_11.setText(QCoreApplication.translate("AddNewStudentDialog", u"Section", None))
        self.widget_7.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_12.setText(QCoreApplication.translate("AddNewStudentDialog", u"Password", None))
        self.widget_8.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_13.setText(QCoreApplication.translate("AddNewStudentDialog", u"Gender", None))
        self.cmbGender.setItemText(0, QCoreApplication.translate("AddNewStudentDialog", u"Male", None))
        self.cmbGender.setItemText(1, QCoreApplication.translate("AddNewStudentDialog", u"Female", None))

        self.label_24.setText(QCoreApplication.translate("AddNewStudentDialog", u"Emergency contact", None))
        self.widget_10.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_22.setText(QCoreApplication.translate("AddNewStudentDialog", u"Contact Person", None))
        self.widget_11.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_23.setText(QCoreApplication.translate("AddNewStudentDialog", u"Contact Number", None))
        self.rb_importCSV.setText(QCoreApplication.translate("AddNewStudentDialog", u"Import from CSV", None))
        self.widget_12.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"input-field", None))
        self.label_14.setText(QCoreApplication.translate("AddNewStudentDialog", u"Section", None))
        self.cmbSection_2.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"combobox-normal", None))
        self.btnBrowseCSV.setText(QCoreApplication.translate("AddNewStudentDialog", u"Browse", None))
        self.btnCancel.setText(QCoreApplication.translate("AddNewStudentDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("AddNewStudentDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("AddNewStudentDialog", u"button-green", None))
    # retranslateUi

