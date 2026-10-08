

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
        /* ==========================================================================
        1. GLOBAL & BASE STYLES
        ========================================================================== */
        * {
            color: #000000;
            background-color: #deddda;
        }

        #widget_body {
            border: 1px solid #7a7a7a;
            border-left: none;
            border-top: none;
        }

        QLabel {
            background: transparent;
        }

        *[class="label-faded"] {
            color: #7c7c7c;
            background-color: transparent;
        }

        *[class="group-box"] {
            border-radius: 15px;
            background-color: #ffffff;
        }

        #grp_SectionInfo QLabel,
        #frame_student_info QLabel,
        #frame_contact_info QLabel {
            font: 11pt "Inter";
        }

        /* ==========================================================================
        2. BUTTONS
        ========================================================================== */
        /* Green Action Buttons */
        QPushButton[class="button-green"] {
            color: #ffffff;
            font: 10pt "Inter SemiBold";
            padding: 0px 10px;
            border: 1px solid #0a5128;
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #1ebd5d, 
                                        stop:1 #107f3f);
        }

        QPushButton[class="button-green"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #2ecc71, 
                                        stop:1 #27ae60);
        }

        QPushButton[class="button-green"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #0b572a, 
                                        stop:1 #129046); 
        }

        QPushButton[class="button-green"]:disabled {
            color: #e8f5e9;
            background: #a5d6a7;
            opacity: 0.6;
        }

        /* Normal / Default Buttons */
        *[class="button-normal"] {
            color: #000000;
            font: 10pt "Inter";
            border: 1px solid #9a9996;
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #ffffff, 
                                        stop:1 #d8ecf6);
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
            color: #aeaeae;
            border: 1px solid #dcdcdc;
            background: #f5f5f5;
        }

        /* ==========================================================================
        3. FORM CONTROLS (SpinBoxes, ComboBoxes, DateEdits, RadioButtons)
        ========================================================================== */
        QComboBox[class="combobox-main"],
        QSpinBox,
        QDoubleSpinBox,
        QDateEdit {
            height: 30px;
            padding: 0px 5px 0px 10px;
            color: #333333;
            font: 10pt "Inter SemiBold";
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
            border: 1px solid #007bff;
        }

        /* Dropdown Subcontrols */
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
            color: #77767b;
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
            color: #77767b;
            border-bottom-right-radius: 15px;
        }

        /* Control Arrows */
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

        /* ComboBox Item View Popup */
        QComboBox QAbstractItemView {
            outline: 0;
            border: 1px solid #999999;
            background-color: #ffffff !important;
            selection-color: #ffffff;
            selection-background-color: #7eb4d7;
        }

        QComboBox QAbstractItemView::item {
            padding-left: 10px;
            color: #333333;
            border-radius: 4px;
        }

        QComboBox[class="combobox-main"] QAbstractItemView::item:hover {
            color: #ffffff;
            background-color: #7eb4d7;
        }

        /* Radio Buttons */
        QRadioButton {
            color: #000000;
            font: 10pt "Inter Medium";
            spacing: 8px;
            padding: 0px 10px;
            background: transparent;
        }

        QRadioButton::indicator {
            border: 1px solid #999999;
            border-radius: 6px;
        }

        QRadioButton::indicator:hover {
            border-color: #3b82f6;
        }

        QRadioButton::indicator:checked {
            border-color: #3b82f6;
            background-color: #0000ff;
        }

        /* ==========================================================================
        4. SEARCH WIDGETS
        ========================================================================== */
        *[class="widget-search-container"] {
            background-color: #ffffff;
            border: 1px solid #999999;
            border-radius: 15px;
        }

        *[class="label-magnifying-search"] {
            background: transparent;
            border: none;
        }

        *[class="textbox-search"] {
            background: transparent;
            border: none;
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

        /* ==========================================================================
        5. CONTAINERS & PANELS
        ========================================================================== */
        *[class="gradient-header"] {
            border: 1px solid #62a0ea;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #ffffff, 
                                        stop:1 #c6e9ff);
        }

        *[class="gradient-body-1"],
        *[class="gradient-body-2"] {
            background-color: #ffffff;
            border: 1px solid #999999;
            border-top: none;
        }

        *[class="gradient-body-2"] QDateEdit:disabled {
            background-color: #c0bfbc;
        }

        /* ==========================================================================
        6. TABLES & HEADERS
        ========================================================================== */
        QTableView {
            outline: none;
            border: 1px solid #a1a1a1;
            gridline-color: #f0f0f0;
            background-color: #ffffff;
            selection-color: #000000;
            selection-background-color: rgba(38, 162, 105, 0.2);
        }

        /* Hide Vertical Headers (Row Numbers) */
        QHeaderView:vertical,
        QHeaderView::section:vertical {
            width: 0px;
            border: none;
        }

        /* Horizontal Header */
        QHeaderView::section:horizontal {
            padding: 6px;
            color: #000000;
            font-weight: bold;
            background-color: #f6f5f4;
        }

        /* ==========================================================================
        7. SCROLL AREA & SCROLLBARS
        ========================================================================== */
        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #deddda;
        }

        QScrollBar:vertical {
            width: 10px;
            margin: 0px;
            border: none;
            border-radius: 5px;
            background: #ffffff;
        }

        QScrollBar::handle:vertical {
            min-height: 20px;
            border-radius: 5px;
            background: #7a7a7a;
        }

        QScrollBar::handle:vertical:hover {
            background: #574939;
        }

        QScrollBar:horizontal {
            height: 10px;
            margin: 0px;
            border: none;
            border-radius: 5px;
            background: #ffffff;
        }

        QScrollBar::handle:horizontal {
            min-width: 20px;
            border-radius: 5px;
            background: #7a7a7a;
        }

        QScrollBar::handle:horizontal:hover {
            background: #574939;
        }

        QScrollBar::add-line:vertical, 
        QScrollBar::sub-line:vertical,
        QScrollBar::add-line:horizontal, 
        QScrollBar::sub-line:horizontal {
            width: 0px;
            height: 0px;
            border: none;
            background: none;
        }

        QScrollBar::add-page:vertical, 
        QScrollBar::sub-page:vertical,
        QScrollBar::add-page:horizontal, 
        QScrollBar::sub-page:horizontal {
            background: none;
        }

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
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
        /* ==========================================================================
        1. GLOBAL & BASE STYLES
        ========================================================================== */
        * {
            color: #e0e0e0;
            background-color: #1e1e20;
        }

        #widget_body {
            border: 1px solid #3d3d42;
            border-left: none;
            border-top: none;
        }

        QLabel {
            background: transparent;
        }

        *[class="label-faded"] {
            color: #9e9e9e;
            background-color: transparent;
        }

        *[class="group-box"] {
            border-radius: 15px;
            background-color: #28282c;
        }

        #grp_SectionInfo QLabel,
        #frame_student_info QLabel,
        #frame_contact_info QLabel {
            font: 11pt "Inter";
        }

        /* ==========================================================================
        2. BUTTONS
        ========================================================================== */
        /* Green Action Buttons */
        QPushButton[class="button-green"] {
            color: #ffffff;
            font: 10pt "Inter SemiBold";
            padding: 0px 10px;
            border: 1px solid #107f3f;
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #107f3f, 
                                        stop:1 #0a5128);
        }

        QPushButton[class="button-green"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #1ed760, 
                                        stop:1 #107f3f);
        }

        QPushButton[class="button-green"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #083c1e, 
                                        stop:1 #0a5128); 
        }

        QPushButton[class="button-green"]:disabled {
            color: #4a6b55;
            background: #1c3325;
            border-color: #1c3325;
            opacity: 0.6;
        }

        /* Normal / Default Buttons */
        *[class="button-normal"] {
            color: #e0e0e0;
            font: 10pt "Inter";
            border: 1px solid #4a4a50;
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #3a3a40, 
                                        stop:1 #2d2d32);
        }

        *[class="button-normal"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #484850, 
                                        stop:1 #35353c);
        }

        *[class="button-normal"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #252529, 
                                        stop:1 #35353c);
        }

        *[class="button-normal"]:disabled {
            color: #666666;
            border: 1px solid #333333;
            background: #222225;
        }

        /* ==========================================================================
        3. FORM CONTROLS (SpinBoxes, ComboBoxes, DateEdits, RadioButtons)
        ========================================================================== */
        QComboBox[class="combobox-main"],
        QSpinBox,
        QDoubleSpinBox,
        QDateEdit {
            height: 30px;
            padding: 0px 5px 0px 10px;
            color: #ffffff;
            font: 10pt "Inter SemiBold";
            background-color: #2b2b30;
            border: 1px solid #4a4a50;
            border-radius: 15px;
            selection-background-color: #3b82f6;
            selection-color: #ffffff;
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

        /* Dropdown Subcontrols */
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

        /* Control Arrows */
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

        /* ComboBox Item View Popup */
        QComboBox QAbstractItemView {
            outline: 0;
            border: 1px solid #4a4a50;
            background-color: #2b2b30 !important;
            selection-color: #ffffff;
            selection-background-color: #3b82f6;
        }

        QComboBox QAbstractItemView::item {
            padding-left: 10px;
            color: #e0e0e0;
            border-radius: 4px;
        }

        QComboBox[class="combobox-main"] QAbstractItemView::item:hover {
            color: #ffffff;
            background-color: #3b82f6;
        }

        /* Radio Buttons */
        QRadioButton {
            color: #e0e0e0;
            font: 10pt "Inter Medium";
            spacing: 8px;
            padding: 0px 10px;
            background: transparent;
        }

        QRadioButton::indicator {
            border: 1px solid #666666;
            border-radius: 6px;
            background-color: #2b2b30;
        }

        QRadioButton::indicator:hover {
            border-color: #60a5fa;
        }

        QRadioButton::indicator:checked {
            border-color: #60a5fa;
            background-color: #3b82f6;
        }

        /* ==========================================================================
        4. SEARCH WIDGETS
        ========================================================================== */
        *[class="widget-search-container"] {
            background-color: #2b2b30;
            border: 1px solid #4a4a50;
            border-radius: 15px;
        }

        *[class="label-magnifying-search"] {
            background: transparent;
            border: none;
        }

        *[class="textbox-search"] {
            background: transparent;
            border: none;
            color: #ffffff;
        }

        *[class="button-clear-search"] {
            background: #404040;
            border-radius: 10px;
        }

        *[class="button-clear-search"]:hover {
            background-color: #BF3636;
        }

        *[class="button-clear-search"]:pressed {
            background-color: #a83232;
        }

        /* ==========================================================================
        5. CONTAINERS & PANELS
        ========================================================================== */
        *[class="gradient-header"] {
            border: 1px solid #2563eb;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                                        stop:0 #1e3a8a, 
                                        stop:1 #1e293b);
        }

        *[class="gradient-body-1"],
        *[class="gradient-body-2"] {
            background-color: #28282c;
            border: 1px solid #4a4a50;
            border-top: none;
        }

        *[class="gradient-body-2"] QDateEdit:disabled {
            background-color: #1a1a1c;
            color: #666666;
        }

        /* ==========================================================================
        6. TABLES & HEADERS
        ========================================================================== */
        QTableView {
            outline: none;
            border: 1px solid #3d3d42;
            gridline-color: #333338;
            background-color: #232326;
            selection-color: #ffffff;
            selection-background-color: rgba(38, 162, 105, 0.4);
        }

        /* Hide Vertical Headers (Row Numbers) */
        QHeaderView:vertical,
        QHeaderView::section:vertical {
            width: 0px;
            border: none;
        }

        /* Horizontal Header */
        QHeaderView::section:horizontal {
            padding: 6px;
            color: #e0e0e0;
            font-weight: bold;
            background-color: #2d2d32;
            border: none;
            border-bottom: 1px solid #3d3d42;
        }

        /* ==========================================================================
        7. SCROLL AREA & SCROLLBARS
        ========================================================================== */
        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #1e1e20;
        }

        QScrollBar:vertical {
            width: 10px;
            margin: 0px;
            border: none;
            border-radius: 5px;
            background: #18181a;
        }

        QScrollBar::handle:vertical {
            min-height: 20px;
            border-radius: 5px;
            background: #4a4a50;
        }

        QScrollBar::handle:vertical:hover {
            background: #6a6a72;
        }

        QScrollBar:horizontal {
            height: 10px;
            margin: 0px;
            border: none;
            border-radius: 5px;
            background: #18181a;
        }

        QScrollBar::handle:horizontal {
            min-width: 20px;
            border-radius: 5px;
            background: #4a4a50;
        }

        QScrollBar::handle:horizontal:hover {
            background: #6a6a72;
        }

        QScrollBar::add-line:vertical, 
        QScrollBar::sub-line:vertical,
        QScrollBar::add-line:horizontal, 
        QScrollBar::sub-line:horizontal {
            width: 0px;
            height: 0px;
            border: none;
            background: none;
        }

        QScrollBar::add-page:vertical, 
        QScrollBar::sub-page:vertical,
        QScrollBar::add-page:horizontal, 
        QScrollBar::sub-page:horizontal {
            background: none;
        }

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
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