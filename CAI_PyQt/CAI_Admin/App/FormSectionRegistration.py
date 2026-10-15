# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormSectionRegistration.ui'
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
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_SectionRegistrationDialog(object):
    def setupUi(self, SectionRegistrationDialog):
        if not SectionRegistrationDialog.objectName():
            SectionRegistrationDialog.setObjectName(u"SectionRegistrationDialog")
        SectionRegistrationDialog.resize(620, 586)
        SectionRegistrationDialog.setMinimumSize(QSize(620, 586))
        SectionRegistrationDialog.setMaximumSize(QSize(742, 586))
        SectionRegistrationDialog.setStyleSheet(u"* {\n"
"    color: #000000;\n"
"    font: 10pt \"Inter\";\n"
"}\n"
"\n"
"QDialog {\n"
"    background: transparent;\n"
"}\n"
"\n"
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
"#widget_window_buttons {\n"
"    background: transparent;\n"
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
"\n"
"#widget_body {\n"
"    background-color: #deddda;\n"
"    border: 1px solid #7a7a7a;\n"
"    border-top: none;\n"
"}\n"
"\n"
"\n"
"*[class=\""
                        "input-field\"] {\n"
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
"QLineEdit:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"*[class=\"input-field\"] QLineEdit:disabled {\n"
"    background-color: #f3f4f6;\n"
"    border: none;\n"
"    color: #999;\n"
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
"*[class=\"input-field\"] QLabel:disabled {\n"
" "
                        "   color: #999;\n"
"    border: none;\n"
"}\n"
"\n"
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
"    border-bottom-right-radius: 18px;\n"
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
"    background-color: #ffffff "
                        "!important;\n"
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
"\n"
"\n"
"QPushButton[class=\"button-green\"] {\n"
"    border: 1px solid #0a5128;\n"
"    border-radius: 15px;\n"
"    padding: 0px 10px 0px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1ebd5d, stop:1 #107f"
                        "3f);\n"
"    color: #FFF;\n"
"    font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton[class=\"button-green\"]:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2ecc71, stop:1 #27AE60);\n"
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
"    background: qlineargradient(x"
                        "1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton[class=\"button-normal\"]:disabled {\n"
"    color: #aeaeae;\n"
"    border: 1px solid #dcdcdc;\n"
"    background: #f5f5f5;\n"
"}\n"
"\n"
"\n"
"\n"
"QProgressBar {\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #007BFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
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
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
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
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: "
                        "none;\n"
"}\n"
"\n"
"\n"
"#line_1 {\n"
"    background-color: #deddda;\n"
"}\n"
"\n"
"#btnExportTemplate {\n"
"    border: 1px solid #9a9996;\n"
"    border-radius: 15px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);\n"
"}\n"
"\n"
"#btnExportTemplate:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f2f6f8);\n"
"}\n"
"\n"
"#btnExportTemplate:pressed {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);\n"
"}\n"
"\n"
"#btnExportTemplate:disabled {\n"
"    color: #aeaeae;\n"
"    border: 1px solid #dcdcdc;\n"
"    background: #f5f5f5;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] {\n"
"    background: transparent;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLabel {\n"
"    background-color: #d2d2d2;\n"
"    border: 1px solid #999;\n"
"    border-right: none;\n"
"    border-top-left-radius: 18px;\n"
"    border-bottom-left-radius: 18px;\n"
"    padding-left: 8px;\n"
""
                        "    color: #000000;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLabel:disabled {\n"
"    color: #999;\n"
"    border: none;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #999;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    padding: 0px 8px;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLineEdit:hover {\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLineEdit:focus {\n"
"    border: 1px solid #2563eb;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] QLineEdit:disabled {\n"
"    background-color: #f3f4f6;\n"
"    border: none;\n"
"    color: #999;\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] #btnBrowseCSV {\n"
"    font: 10pt \"Inter\";\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);\n"
"    border: 1px solid #9a9996;\n"
"    padding: 5px 15px;\n"
"\n"
"    border-top-right-radius: 18px;\n"
"    border-bottom-right-radius: 18px;\n"
"}\n"
"\n"
"*"
                        "[class=\"input-and-browse\"] #btnBrowseCSV:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f2f6f8);\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] #btnBrowseCSV:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);\n"
"}\n"
"\n"
"*[class=\"input-and-browse\"] #btnBrowseCSV:disabled {\n"
"    background-color: #d2d2d2;\n"
"    color: #999;\n"
"    border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(SectionRegistrationDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(SectionRegistrationDialog)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 35))
        self.frame_header.setMaximumSize(QSize(16777215, 35))
        self.frame_header.setMouseTracking(True)
        self.frame_header.setStyleSheet(u"")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 0, 0)
        self.widget_window_icon = QWidget(self.frame_header)
        self.widget_window_icon.setObjectName(u"widget_window_icon")
        self.widget_window_icon.setMinimumSize(QSize(72, 34))
        self.widget_window_icon.setMaximumSize(QSize(72, 34))
        self.widget_window_icon.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_window_icon)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.widget_window_icon)

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

        self.horizontalLayout_6.addWidget(self.label_windowTitle)

        self.widget_window_buttons = QWidget(self.frame_header)
        self.widget_window_buttons.setObjectName(u"widget_window_buttons")
        self.widget_window_buttons.setMinimumSize(QSize(72, 34))
        self.widget_window_buttons.setMaximumSize(QSize(72, 34))
        self.widget_window_buttons.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_window_buttons)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_7.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.widget_window_buttons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(24, 24))
        self.btnClose.setMaximumSize(QSize(24, 24))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Images/Images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.btnClose)


        self.horizontalLayout_6.addWidget(self.widget_window_buttons)


        self.verticalLayout.addWidget(self.frame_header)

        self.widget_body = QWidget(SectionRegistrationDialog)
        self.widget_body.setObjectName(u"widget_body")
        self.widget_body.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_body)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, 9, 12, 9)
        self.label_sy = QLabel(self.widget_body)
        self.label_sy.setObjectName(u"label_sy")

        self.verticalLayout_5.addWidget(self.label_sy)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.widget_1 = QWidget(self.widget_body)
        self.widget_1.setObjectName(u"widget_1")
        self.horizontalLayout = QHBoxLayout(self.widget_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 36))
        self.label_9.setMaximumSize(QSize(100, 36))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.txtSectionName = QLineEdit(self.widget_1)
        self.txtSectionName.setObjectName(u"txtSectionName")
        self.txtSectionName.setMinimumSize(QSize(0, 36))
        self.txtSectionName.setMaximumSize(QSize(16777215, 36))
        self.txtSectionName.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.txtSectionName)


        self.verticalLayout_2.addWidget(self.widget_1)

        self.widget_2 = QWidget(self.widget_body)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 36))
        self.label_10.setMaximumSize(QSize(100, 36))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.cmb_teacher = QComboBox(self.widget_2)
        self.cmb_teacher.setObjectName(u"cmb_teacher")
        self.cmb_teacher.setMinimumSize(QSize(0, 36))
        self.cmb_teacher.setMaximumSize(QSize(16777215, 36))
        self.cmb_teacher.setStyleSheet(u"")
        self.cmb_teacher.setEditable(False)

        self.horizontalLayout_3.addWidget(self.cmb_teacher)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line_1 = QFrame(self.widget_body)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setStyleSheet(u"")
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.rb_importCSV = QRadioButton(self.widget_body)
        self.rb_importCSV.setObjectName(u"rb_importCSV")
        self.rb_importCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rb_importCSV.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.rb_importCSV)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.widget_CSV = QWidget(self.widget_body)
        self.widget_CSV.setObjectName(u"widget_CSV")
        self.widget_CSV.setEnabled(True)
        self.widget_CSV.setMinimumSize(QSize(100, 0))
        self.widget_CSV.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_CSV)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_CSV)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 36))
        self.label_14.setMaximumSize(QSize(100, 36))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_14)

        self.txtCSVPath = QLineEdit(self.widget_CSV)
        self.txtCSVPath.setObjectName(u"txtCSVPath")
        self.txtCSVPath.setMinimumSize(QSize(0, 36))
        self.txtCSVPath.setMaximumSize(QSize(16777215, 36))
        self.txtCSVPath.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.txtCSVPath)

        self.btnBrowseCSV = QPushButton(self.widget_CSV)
        self.btnBrowseCSV.setObjectName(u"btnBrowseCSV")
        self.btnBrowseCSV.setMinimumSize(QSize(100, 36))
        self.btnBrowseCSV.setMaximumSize(QSize(100, 36))
        self.btnBrowseCSV.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBrowseCSV.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.btnBrowseCSV)


        self.verticalLayout_5.addWidget(self.widget_CSV)

        self.widget_template = QWidget(self.widget_body)
        self.widget_template.setObjectName(u"widget_template")
        self.widget_template.setEnabled(True)
        self.widget_template.setMinimumSize(QSize(0, 200))
        self.verticalLayout_3 = QVBoxLayout(self.widget_template)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.widget_template)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.label)

        self.btnExportTemplate = QPushButton(self.widget_3)
        self.btnExportTemplate.setObjectName(u"btnExportTemplate")
        self.btnExportTemplate.setEnabled(True)
        self.btnExportTemplate.setMinimumSize(QSize(30, 30))
        self.btnExportTemplate.setMaximumSize(QSize(30, 30))
        self.btnExportTemplate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Images/Images/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportTemplate.setIcon(icon2)
        self.btnExportTemplate.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.btnExportTemplate)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.scrollArea = QScrollArea(self.widget_template)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(0, 220))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 703, 210))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QSize(16777215, 210))
        self.label_2.setPixmap(QPixmap(u":/Images/Images/student_list_template.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.widget_template)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

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


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.widget_body)


        self.retranslateUi(SectionRegistrationDialog)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SectionRegistrationDialog)
    # setupUi

    def retranslateUi(self, SectionRegistrationDialog):
        SectionRegistrationDialog.setWindowTitle(QCoreApplication.translate("SectionRegistrationDialog", u"Section Registration", None))
        self.label_windowTitle.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Section Registration", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.label_sy.setText(QCoreApplication.translate("SectionRegistrationDialog", u"School Year: 0000-0000", None))
        self.widget_1.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"input-field", None))
        self.label_9.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Name", None))
        self.widget_2.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"input-field", None))
        self.label_10.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Adviser", None))
        self.rb_importCSV.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Import students from CSV", None))
        self.widget_CSV.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"input-and-browse", None))
        self.label_14.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Template file:", None))
        self.label_14.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"input-field", None))
        self.btnBrowseCSV.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Browse", None))
        self.label.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Template (Sample):", None))
#if QT_CONFIG(tooltip)
        self.btnExportTemplate.setToolTip(QCoreApplication.translate("SectionRegistrationDialog", u"Export Template", None))
#endif // QT_CONFIG(tooltip)
        self.btnExportTemplate.setText("")
        self.label_2.setText("")
        self.btnCancel.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Cancel", None))
        self.btnCancel.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"button-normal", None))
        self.btnSave.setText(QCoreApplication.translate("SectionRegistrationDialog", u"Save", None))
        self.btnSave.setProperty(u"class", QCoreApplication.translate("SectionRegistrationDialog", u"button-green", None))
    # retranslateUi

