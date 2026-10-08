

class Light_Theme:

    home_win = """
        * {
            color: black;
            font: 10pt "Inter";
        }

        QMainWindow, #centralwidget {
            background: transparent;
        }
    """

    centralWidget = """
        * {
            color: black;
            font: 10pt "Inter";
        }

        #contentWindow {
            background-color: transparent;
        }

        QTabWidget, QTabWidget * {
            background-color: #deddda;
        }
    """

    frame_header = """
        #frame_header {
            background-color: #deddda;
            border-top-right-radius: 12px;
            border: 1px solid #7a7a7a;
            border-left: none;
            border-bottom: none;
        }

        #label_windowTitle {
            background: transparent;
            color: rgb(0, 0, 0);
            font: 10pt "Inter SemiBold";
        }

        #widget_window_buttons {
            background: transparent;
        }

        #btnMinimize {
            border-radius: 12px;
            background-color: transparent;
        }

        #btnMinimize:hover {
            background-color: rgb(248, 228, 92);
        }

        #btnMaximize {
            border-radius: 12px;
            background-color: transparent;
        }

        #btnMaximize:hover {
            background-color: #3bca5c;
        }

        #btnClose {
            border-radius: 12px;
            background-color: transparent;
        }

        #btnClose:hover {
            background-color: rgb(246, 97, 81);
        }
    """

    widget_header_welcome = """
        * {
            color: #241f31;
        }

        #widget_header_welcome {
            background-color: rgb(246, 245, 244);
            padding: 0px 10px;
            border-radius: 20px;
        }

        #label_welcome {
            background-color: transparent;
            font: 12pt "Inter Medium";
        }

        #label_gradingperiod {
            font: 10pt "Inter Medium";
            border-radius: 15px;
            padding: 0px 10px 0px;
        }

        #label_SY {
            background-color: transparent;
            font: 12pt "Inter Medium";
        }
    """

    frame_ranking_title = """
        * {
            color: rgb(36, 31, 49);
        }

        #frame_ranking_title {
            background-color: transparent;
            border-bottom: 1px solid rgb(146, 146, 146);
        }

        QLabel {
            background-color: transparent;
            font: 12pt "Inter Medium";
        }
    """

    navigationBar = """
        #navigationBar {
            border-top-left-radius: 12px;
        }

        #navigationBar, #line, #line_2 {
            background-color: rgb(61, 61, 61); /* Dark Gray or Storm Dust */
        }

        QPushButton[class="button-left-nav"] {
            border-radius: 0px;
            background: transparent;
            color: white;
            text-align: left;
            padding: 0px 10px;
            font: 57 10pt "Inter Medium";
        }

        QPushButton[class="button-left-nav"]:hover {
            background: #5d5d5d;
        }

        QPushButton[class="button-left-nav"]:checked {
            background-color: #5d5d5d;
            color: white;
            border-left: 5px solid #FF00FF;
        }

        QPushButton[class="button-left-nav"]:hover:!checked {
            background-color: #5d5d5d;
        }
    """

    widget_body = """
        * {
            background-color: #deddda;
        }

        #widget_body {
            border: 1px solid #7a7a7a;
            border-left: none;
            border-top: none;
        }

        QPushButton[class="button-green"] {
            border: 1px solid #0a5128;
            border-radius: 15px;
            padding: 0px 10px 0px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #1ebd5d, 
                                        stop:1 #107f3f);
            color: #FFF;
            font: 10pt "Inter SemiBold";
        }

        QPushButton[class="button-green"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #2ecc71, 
                                        stop:1 #27AE60);
        }

        QPushButton[class="button-green"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #0b572a, 
                                        stop:1 #129046); 
        }

        QPushButton[class="button-green"]:disabled {
            background: #A5D6A7;
            color: #E8F5E9;
            opacity: 0.6;
        }

        *[class="button-normal"] {
            font: 10pt "Inter";
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #ffffff, 
                                        stop:1 #d8ecf6);
            color: black;
            border-radius: 15px;
            border: 1px solid rgb(154, 153, 150);
        }

        *[class="button-normal"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #ffffff, 
                                        stop:1 #f2f6f8);
        }

        *[class="button-normal"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #dce5e9, 
                                        stop:1 #ffffff);
        }

        *[class="button-normal"]:disabled {
            background: #f5f5f5;
            border: 1px solid #dcdcdc;
            color: #aeaeae;
        }

        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #deddda;
        }

        QScrollArea QWidget #qt_scrollarea_viewport {
            background: transparent;
            border-radius: 20px;
        }

        QScrollBar:vertical {
            border: none;
            background: #ffffff;
            width: 10px;
            margin: 0px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            background: #7a7a7a;
            min-height: 20px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical:hover {
            background: #574939;
        }

        QScrollBar:horizontal {
            border: none;
            background: #ffffff;
            height: 10px;
            margin: 0px;
            border-radius: 5px;
        }

        QScrollBar::handle:horizontal {
            background: #7a7a7a;
            min-width: 20px;
            border-radius: 5px;
        }

        QScrollBar::handle:horizontal:hover {
            background: #574939;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
            width: 0px;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
        }

        QDateEdit {
            background-color: #fff;
        }

        QLabel {
            background: transparent;
        }
    """

    widget_datetime = """
        #label_day {
            color: #241f31;
            background-color: transparent;
            font: 50pt "Inter Medium";
        }

        #label_month {
            color: rgb(255, 255, 255);
            background-color: transparent; font: 57 18pt "Inter Medium";
            margin-bottom: 3px;
        }

        #label_time {
            color: rgb(36, 31, 49);
            background-color: transparent;
            font: 57 30pt "Inter Medium";
        }

        #label_timeAP {
            color: rgb(36, 31, 49);
            background-color: transparent;
            font: 57 14pt "Inter Medium";
        }
    """

    stackedWidget = """
        * {
            color: black;
        }

        *[class="group-box"] {
            border-radius: 15px;
            background-color: rgb(255, 255, 255);
        }

        *[class="label-faded"] {
            color: rgb(124, 124, 124);
            background-color: transparent;
        }

        #grp_SectionInfo QLabel,
        #frame_student_info QLabel,
        #frame_contact_info QLabel {
            font: 11pt "Inter";
        }

        *[class="widget-search-container"] {
            background-color: #FFF;
            border: 1px solid #999;
            border-radius: 15px;
        }

        *[class="label-magnifying-search"] {
            background: transparent;
            border: none;
        }

        *[class="textbox-search"] {
            border: none;
            background: transparent;
        }

        *[class="button-clear-search"] {
            background: transparent;
            border-radius: 10px;
        }

        *[class="button-clear-search"]:hover {
            background-color: #ffc0c0;
        }

        *[class="button-clear-search"]:pressed {
            background-color: #ffd2d2;
        }

        QComboBox[class="combobox-main"],
        QSpinBox,
        QDoubleSpinBox,
        QDateEdit {
            height: 30px;
            padding: 0px 5px 0px 10px;
            font: 10pt "Inter SemiBold";
            color: #333333;
            background-color: #ffffff;
            border: 1px solid #999999;
            border-radius: 15px;
            selection-background-color: #7eb4d7;
        }

        QComboBox[class="combobox-main"]:hover,
        QSpinBox:hover,
        QDoubleSpinBox:hover,
        QDateEdit:hover {
            border: 1px solid #3498db;
        }

        QComboBox[class="combobox-main"]:focus,
        QSpinBox:focus,
        QDoubleSpinBox:focus,
        QDateEdit:focus {
            border: 1px solid #007BFF;
        }

        /* Subcontrol Dropdown Buttons */
        QComboBox::drop-down,
        QDoubleSpinBox::drop-down,
        QDateEdit::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
            border-left-width: 0px;
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-button,
        QDoubleSpinBox::up-button,
        QDateEdit::up-button {
            subcontrol-origin: border;
            subcontrol-position: top right;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: rgb(119, 118, 123);
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button,
        QDoubleSpinBox::down-button,
        QDateEdit::down-button {
            subcontrol-origin: border;
            subcontrol-position: bottom right;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: rgb(119, 118, 123);
            border-bottom-right-radius: 15px;
        }

        /* Subcontrol Arrows */
        QComboBox::down-arrow,
        QSpinBox::down-arrow,
        QDoubleSpinBox::down-arrow,
        QDateEdit::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
            border: none;
        }

        QSpinBox::up-arrow,
        QDoubleSpinBox::up-arrow,
        QDateEdit::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        /* ComboBox Dropdown Menu Item View */
        QComboBox QAbstractItemView {
            background-color: #ffffff !important;
            border: 1px solid #999999;
            selection-background-color: #7eb4d7;
            selection-color: #ffffff;
            outline: 0;
        }

        QComboBox QAbstractItemView::item {
            padding-left: 10px;
            color: #333333;
            border-radius: 4px;
        }

        QComboBox[class="combobox-main"] QAbstractItemView::item:hover {
            background-color: #7eb4d7;
            color: #ffffff;
        }

        QTableView {
            background-color: #ffffff;
            border: 1px solid #ff7d87;
            gridline-color: #f0f0f0;
            selection-background-color: rgba(255, 125, 135, 0.2);
            selection-color: #000000;
            outline: none;
        }

        /* Hide Vertical Headers (Row Numbers) */
        QHeaderView:vertical,
        QHeaderView::section:vertical {
            width: 0px;
            border: none;
        }

        /* Horizontal Header */
        QHeaderView::section:horizontal {
            background-color: #ff7d87;
            color: #ffffff;
            padding: 6px;
            font-weight: bold;
            font-size: 11pt;
            border: none;
        }

        /* Top-Left Header Corner */
        QTableCornerButton::section {
            background-color: #ff7d87;
            border: none;
        }

        QScrollBar:vertical {
            background: #fdfdfd;
            width: 10px;
            border: none;
        }

        QScrollBar::handle:vertical {
            background: #ff7d87;
            min-height: 30px;
            border-radius: 3px;
            margin: 2px;
        }

        QScrollBar::handle:vertical:hover {
            background: #e66a74;
        }

        QScrollBar:horizontal {
            background: #fdfdfd;
            height: 10px;
            border: none;
        }

        QScrollBar::handle:horizontal {
            background: #ff7d87;
            min-width: 30px;
            border-radius: 3px;
            margin: 2px;
        }

        QScrollBar::handle:horizontal:hover {
            background: #e66a74;
        }

        /* Scrollbar Buttons & Page Track */
        QScrollBar::add-line,
        QScrollBar::sub-line {
            width: 0px;
            height: 0px;
            background: none;
            border: none;
        }

        QScrollBar::add-page,
        QScrollBar::sub-page {
            background: none;
        }

        * [class="gradient-header"] {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #c6e9ff);
            border: 1px solid rgb(98, 160, 234);
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }

        * [class="gradient-body-1"],
        * [class="gradient-body-2"] {
            background-color: #fff;
            border: 1px solid #999;
            border-top: none;
        }

        * [class="gradient-body-2"] QDateEdit:disabled {
            background-color: rgb(192, 191, 188);
        }

        QRadioButton {
            color: black;
            spacing: 8px;
            padding: 0px 10px;
            background: transparent;
            font: 10pt "Inter Medium";
        }

        QRadioButton::indicator {
            border: 1px solid #999;
            border-radius: 6px;
        }

        QRadioButton::indicator:hover {
            border-color: #3b82f6;
        }

        QRadioButton::indicator:checked {
            border-color: #3b82f6;
            background-color: blue;
        }
    """

    widget_toggle_gp = """
        #widget_toggle_gp {
            background: transparent;
        }

        QPushButton {
            border: 1px solid #999;
            padding: 4px 14px;
            font: 10pt "Inter";
            background-color: #f0f0f0;
        }

        QPushButton:hover {
            background-color: #e0e0e0;
        }

        #btn_manual {
            border-top-left-radius: 15px;
            border-bottom-left-radius: 15px;
            border-right: none;
        }

        #btn_manual:checked {
            background-color: #72D582;
            border: 2px solid #448D50;
            color: #000;
        }

        #btn_auto {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        #btn_auto:checked {
            background-color: #72D582;
            border: 2px solid #448D50;
            color: #000;
        }
    """


class Dark_Theme:

    home_win = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QMainWindow, #centralwidget {
            background: transparent;
        }
    """

    centralWidget = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        #contentWindow {
            background-color: transparent;
        }

        QTabWidget, QTabWidget * {
            background-color: #1e1e1e;
        }
    """

    frame_header = """
        #frame_header {
            background-color: #1e1e1e;
            border-top-right-radius: 12px;
            border: 1px solid #3d3d3d;
            border-left: none;
            border-bottom: none;
        }

        #label_windowTitle {
            background: transparent;
            color: #ffffff;
            font: 10pt "Inter SemiBold";
        }

        #widget_window_buttons {
            background: transparent;
        }

        #btnMinimize {
            border-radius: 12px;
            background-color: #404040;
        }

        #btnMinimize:hover {
            background-color: rgb(248, 228, 92);
        }

        #btnMaximize {
            border-radius: 12px;
            background-color: #404040;
        }

        #btnMaximize:hover {
            background-color: #3bca5c;
        }

        #btnClose {
            border-radius: 12px;
            background-color: #404040;
        }

        #btnClose:hover {
            background-color: rgb(246, 97, 81);
        }
    """

    widget_header_welcome = """
        * {
            color: #ffffff;
        }

        #widget_header_welcome {
            background-color: #2d2d2d;
            padding: 0px 10px;
            border-radius: 20px;
        }

        #label_welcome {
            background-color: transparent;
            font: 12pt "Inter Medium";
            color: #ffffff;
        }

        #label_gradingperiod {
            font: 10pt "Inter Medium";
            background-color: #3d3d3d;
            color: #e0e0e0;
            border-radius: 15px;
            padding: 0px 10px 0px;
        }

        #label_SY {
            background-color: transparent;
            font: 12pt "Inter Medium";
            color: #b0b0b0;
        }
    """

    frame_ranking_title = """
        * {
            color: #ffffff;
        }

        #frame_ranking_title {
            background-color: transparent;
            border-bottom: 1px solid #3d3d3d;
        }

        QLabel {
            background-color: transparent;
            font: 12pt "Inter Medium";
            color: #ffffff;
        }
    """

    navigationBar = """
        #navigationBar {
            border-top-left-radius: 12px;
        }

        #navigationBar, #line, #line_2 {
            background-color: #121212; /* Deep Dark Accent */
        }

        QPushButton[class="button-left-nav"] {
            border-radius: 0px;
            background: transparent;
            color: #b0b0b0;
            text-align: left;
            padding: 0px 10px;
            font: 57 10pt "Inter Medium";
        }

        QPushButton[class="button-left-nav"]:hover {
            background: #2a2a2a;
            color: #ffffff;
        }

        QPushButton[class="button-left-nav"]:checked {
            background-color: #2a2a2a;
            color: #ffffff;
            border-left: 5px solid #FF00FF;
        }

        QPushButton[class="button-left-nav"]:hover:!checked {
            background-color: #2a2a2a;
        }
    """

    widget_body = """
        * {
            background-color: #1e1e1e;
            color: #ffffff;
        }

        #widget_body {
            border: 1px solid #3d3d3d;
            border-left: none;
            border-top: none;
        }

        QPushButton[class="button-green"] {
            border: 1px solid #084020;
            border-radius: 15px;
            padding: 0px 10px 0px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #107f3f, 
                                        stop:1 #0a5128);
            color: #ffffff;
            font: 10pt "Inter SemiBold";
        }

        QPushButton[class="button-green"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #1ebd5d, 
                                        stop:1 #107f3f);
        }

        QPushButton[class="button-green"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #083c1d, 
                                        stop:1 #0a5128); 
        }

        QPushButton[class="button-green"]:disabled {
            background: #1b3827;
            color: #4e735b;
            border: 1px solid #14291d;
        }

        *[class="button-normal"] {
            font: 10pt "Inter";
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #333333, 
                                        stop:1 #242424);
            color: #ffffff;
            border-radius: 15px;
            border: 1px solid #4a4a4a;
        }

        *[class="button-normal"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #444444, 
                                        stop:1 #333333);
            border: 1px solid #666666;
        }

        *[class="button-normal"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #1a1a1a, 
                                        stop:1 #282828);
        }

        *[class="button-normal"]:disabled {
            background: #222222;
            border: 1px solid #333333;
            color: #666666;
        }

        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #1e1e1e;
        }

        QScrollArea QWidget #qt_scrollarea_viewport {
            background: transparent;
            border-radius: 20px;
        }

        QScrollBar:vertical {
            border: none;
            background: #121212;
            width: 10px;
            margin: 0px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            background: #4a4a4a;
            min-height: 20px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical:hover {
            background: #6e6e6e;
        }

        QScrollBar:horizontal {
            border: none;
            background: #121212;
            height: 10px;
            margin: 0px;
            border-radius: 5px;
        }

        QScrollBar::handle:horizontal {
            background: #4a4a4a;
            min-width: 20px;
            border-radius: 5px;
        }

        QScrollBar::handle:horizontal:hover {
            background: #6e6e6e;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
            width: 0px;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
        }

        QDateEdit {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 1px solid #3d3d3d;
            border-radius: 4px;
            padding: 2px 4px;
        }

        QLabel {
            background: transparent;
            color: #ffffff;
        }
    """

    widget_datetime = """
        #label_day {
            color: #241f31;
            background-color: transparent;
            font: 50pt "Inter Medium";
        }

        #label_month {
            color: #e0e0e0;
            background-color: transparent; 
            font: 57 18pt "Inter Medium";
            margin-bottom: 3px;
        }

        #label_time {
            color: #ffffff;
            background-color: transparent;
            font: 57 30pt "Inter Medium";
        }

        #label_timeAP {
            color: #b0b0b0;
            background-color: transparent;
            font: 57 14pt "Inter Medium";
        }
    """

    stackedWidget = """
        * {
            color: #ffffff;
        }

        *[class="group-box"] {
            border-radius: 15px;
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
        }

        QLabel[class="label-faded"] {
            color: #858585;
            background-color: transparent;
        }

        *[class="group-box"] QLabel {
            font: 11pt "Inter";
        }

        *[class="widget-search-container"] {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-radius: 15px;
        }

        *[class="label-magnifying-search"] {
            border: none;
            background: transparent;
        }

        *[class="textbox-search"] {
            border: none;
            background: transparent;
        }

        *[class="button-clear-search"] {
            background: #404040;
            border-radius: 10px;
        }

        *[class="button-clear-search"]:hover {
            background-color: rgba(255, 100, 100, 0.50);
        }

        *[class="button-clear-search"]:pressed {
            background-color: rgba(255, 100, 100, 0.4);
        }

        QComboBox[class="combobox-main"], 
        QSpinBox,
        QDoubleSpinBox,
        QDateEdit {
            height: 30px;
            padding: 0px 5px 0px 10px;
            font: 10pt "Inter SemiBold";
            color: #ffffff;
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-radius: 15px;
            selection-background-color: #3b82f6;
        }

        QComboBox[class="combobox-main"]:hover,
        QSpinBox:hover,
        QDoubleSpinBox:hover,
        QDateEdit:hover {
            border: 1px solid #60a5fa;
        }

        QComboBox[class="combobox-main"]:focus,
        QSpinBox:focus,
        QDoubleSpinBox:focus,
        QDateEdit:focus {
            border: 1px solid #3b82f6;
        }

        /* Subcontrol Dropdown Buttons */
        QComboBox::drop-down,
        QDoubleSpinBox::drop-down,
        QDateEdit::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
            border-left-width: 0px;
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-button,
        QDoubleSpinBox::up-button,
        QDateEdit::up-button {
            subcontrol-origin: border;
            subcontrol-position: top right;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #a0a0a0;
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button,
        QDoubleSpinBox::down-button,
        QDateEdit::down-button {
            subcontrol-origin: border;
            subcontrol-position: bottom right;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #a0a0a0;
            border-bottom-right-radius: 15px;
        }

        /* Subcontrol Arrows */
        QComboBox::down-arrow,
        QSpinBox::down-arrow,
        QDoubleSpinBox::down-arrow,
        QDateEdit::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
            border: none;
        }

        QSpinBox::up-arrow,
        QDoubleSpinBox::up-arrow,
        QDateEdit::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        /* ComboBox Dropdown Menu Item View */
        QComboBox QAbstractItemView {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            selection-background-color: #3b82f6;
            selection-color: #ffffff;
            outline: 0;
        }

        QComboBox QAbstractItemView::item {
            padding-left: 10px;
            color: #ffffff;
            border-radius: 4px;
        }

        QComboBox[class="combobox-main"] QAbstractItemView::item:hover {
            background-color: #3b82f6;
            color: #ffffff;
        }

        QTableView {
            background-color: #1e1e1e;
            border: 1px solid #d8525e;
            gridline-color: #2d2d2d;
            selection-background-color: rgba(216, 82, 94, 0.35);
            selection-color: #ffffff;
            outline: none;
        }

        /* Hide Vertical Headers (Row Numbers) */
        QHeaderView:vertical,
        QHeaderView::section:vertical {
            width: 0px;
            border: none;
        }

        /* Horizontal Header */
        QHeaderView::section:horizontal {
            background-color: #b83845;  
            color: #ffffff;
            padding: 6px;
            font-weight: bold;
            font-size: 11pt;
            border: none;
        }

        /* Top-Left Header Corner */
        QTableCornerButton::section {
            background-color: #b83845;
            border: none;
        }

        QScrollBar:vertical {
            background: #121212;
            width: 10px;
            border: none;
        }

        QScrollBar::handle:vertical {
            background: #b83845;
            min-height: 30px;
            border-radius: 3px; 
            margin: 2px;
        }

        QScrollBar::handle:vertical:hover {
            background: #d8525e;
        }

        QScrollBar:horizontal {
            background: #121212;
            height: 10px;
            border: none;
        }

        QScrollBar::handle:horizontal {
            background: #b83845;
            min-width: 30px;
            border-radius: 3px;
            margin: 2px;
        }

        QScrollBar::handle:horizontal:hover {
            background: #d8525e;
        }

        /* Scrollbar Buttons & Page Track */
        QScrollBar::add-line, 
        QScrollBar::sub-line {
            width: 0px;
            height: 0px;
            background: none;
            border: none;
        }

        QScrollBar::add-page, 
        QScrollBar::sub-page {
            background: none;
        }
        
        *[class="gradient-header"] {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1e293b, stop:1 #0f172a);
            border: 1px solid #3b82f6;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            color: #ffffff;
        }

        *[class="gradient-body-1"],
        *[class="gradient-body-2"] {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
            color: #ffffff;
        }

        *[class="gradient-body-2"] QDateEdit:disabled {
            background-color: #1a1a1a;
            color: #666666;
            border: 1px solid #333333;
        }

        QRadioButton {
            color: #ffffff;
            spacing: 8px;
            padding: 0px 10px;
            background: transparent;
            font: 10pt "Inter Medium";
        }

        QRadioButton::indicator {
            border: 1px solid #666666;
            background-color: #2d2d2d;
            border-radius: 6px;
        }

        QRadioButton::indicator:hover {
            border-color: #60a5fa;
        }

        QRadioButton::indicator:checked {
            border-color: #3b82f6;
            background-color: #2563eb;
        }
    """

    widget_toggle_gp = """
        #widget_toggle_gp {
            background: transparent;
        }

        QPushButton {
            border: 1px solid #4a4a4a;
            padding: 4px 14px;
            font: 10pt "Inter";
            background-color: #2d2d2d;
            color: #ffffff;
        }

        QPushButton:hover {
            background-color: #3d3d3d;
        }

        #btn_manual {
            border-top-left-radius: 15px;
            border-bottom-left-radius: 15px;
            border-right: none;
        }

        #btn_manual:checked {
            background-color: #27ae60;
            border: 2px solid #1ebd5d;
            color: #ffffff;
        }

        #btn_auto {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        #btn_auto:checked {
            background-color: #27ae60;
            border: 2px solid #1ebd5d;
            color: #ffffff;
        }
    """