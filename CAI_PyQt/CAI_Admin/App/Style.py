

class Light_Theme:

    buttons = """
        QPushButton[class="button-green"] {
            border: 1px solid #0a5128;
            border-radius: 15px;
            padding: 0px 10px 0px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1ebd5d, stop:1 #107f3f);
            color: #FFF;
            font: 10pt "Inter SemiBold";
        }

        QPushButton[class="button-green"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2ecc71, stop:1 #27AE60);
        }

        QPushButton[class="button-green"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0b572a, stop:1 #129046); 
        }

        QPushButton[class="button-green"]:disabled {
            background: #a7f3d0;
            border: 1px solid #6ee7b7;
            color: #098f69;
        }

        QPushButton[class="button-normal"] {
            color: #000000;
            font: 10pt "Inter";
            border: 1px solid #9a9996;
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);
        }

        QPushButton[class="button-normal"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f2f6f8);
        }

        QPushButton[class="button-normal"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);
        }

        QPushButton[class="button-normal"]:disabled {
            color: #aeaeae;
            border: 1px solid #dcdcdc;
            background: #f5f5f5;
        }
    """

    check_box = """
        QCheckBox {
            background-color: transparent;
            padding: 5px 10px;
            color: #1f2937;
            font: 10pt "Inter";
        }

        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            background-color: #ffffff;
            border: 2px solid #9ca3af;
            border-radius: 4px;
        }

        QCheckBox::indicator:hover {
            border-color: #3b82f6;
        }

        QCheckBox::indicator:checked {
            background-color: #2563eb;
            border-color: #2563eb;
            image: url(:/Images/Images/check.png);
        }

        QCheckBox::indicator:disabled {
            background-color: #f3f4f6;
            border: 2px solid #d1d5db;
            image: none;
        }

        QCheckBox:disabled {
            color: #9ca3af;
        }
    """

    tool_tip = """
        QToolTip {
            background-color: #ffffff;
            color: #1f2937;
            border: 1px solid #d1d5db;
            padding: 4px 6px;
            border-radius: 6px;
            font: 10pt "Inter";
        }
    """

    progress_bar = """
        QProgressBar {
            border-radius: 10px;
            background-color: white;
        }

        QProgressBar::chunk {
            background-color: #007BFF;
            border-radius: 10px;
        }
    """

    radio_button = """
        QRadioButton {
            color: #1f2937;
            spacing: 8px;
            padding: 0px 10px;
            background: transparent;
            font: 10pt "Inter";
        }

        QRadioButton::indicator {
            background: #ffffff;
            border: 2px solid #999;
            min-width: 14px;
            min-height: 14px;
            border-radius: 7px;
        }

        QRadioButton::indicator:checked {
            border-color: #93c5fd;
            background-color: #2563eb;
        }
        """

    scrollbar = """
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

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical,
        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal {
            border: none;
            background: none;
            width: 0px;
            height: 0px;
        }

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical,
        QScrollBar::add-page:horizontal,
        QScrollBar::sub-page:horizontal {
            background: none;
        }
    """

    input_field = """
        *[class="input-field"] {
            background-color: transparent;
        }

        *[class="input-field"] QLineEdit {
            background-color: #ffffff;
            border: 1px solid #999;
            border-left: none;
            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
            padding: 0px 8px;
            color: #1f2937;
        }

        QLineEdit:focus {
            border: 1px solid #2563eb;
        }

        QLineEdit:hover {
            border: 1px solid #3b82f6;
        }

        *[class="input-field"] QLineEdit:disabled {
            background-color: #f3f4f6;
            border: none;
            color: #999;
        }

        *[class="input-field"] QLabel {
            background-color: #d2d2d2;
            border-left: 1px solid #999;
            border-top: 1px solid #999;
            border-bottom: 1px solid #999;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding-left: 8px;
            color: #000000;
        }

        *[class="input-field"] QLabel:disabled {
            color: #999;
            border: none;
        }
    """

    combo_box_input_field = """
        *[class="input-field"] QComboBox {
            border: 1px solid #999;
            border-left: none;
            padding: 0px 10px;
            background-color: #ffffff;
            color: #1f2937;
            font: 10pt "Inter Medium";
            selection-background-color: #bfdbfe;
            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
        }

        QComboBox:focus {
            border: 1px solid #2563eb;
        }

        QComboBox:hover {
            border: 1px solid #3b82f6;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
            border-left-width: 0px;
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        QComboBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            border: none;
            width: 8px;
            height: 8px;
        }

        QComboBox QAbstractItemView {
            background-color: #ffffff !important;
            border: 1px solid #999;
            selection-background-color: #bfdbfe;
            selection-color: #111827;
            outline: 0;
        }

        QComboBox QAbstractItemView::item {
            padding: 0px 15px;
            border-radius: 4px;
            color: #1f2937;
        }

        QComboBox QAbstractItemView::item:hover {
            background-color: #bfdbfe;
            color: #111827;
        }

        QComboBox:disabled {
            background-color: #f3f4f6;
            border: none;
            color: #999;
        }

        QComboBox::drop-down:disabled {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
            background-color: transparent;
        }

        QComboBox::down-arrow:disabled {
            image: url(:/Images/Images/caret-down-disabled.png);
        }
    """

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

    header_dlg = """
        #frame_header {
            background-color: #deddda;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            border: 1px solid #7a7a7a;
            border-bottom: none;
        }

        #label_windowTitle {
            background: transparent;
            font: 10pt "Inter SemiBold";
            color: #111827;
        }

        #widget_window_buttons {
            background: transparent;
        }

        #btnMinimize {
            border-radius: 12px;
            background-color: transparent;
        }

        #btnMinimize:hover {
            background-color: #f8e45c;
        }

        #btnClose {
            border-radius: 12px;
            background-color: transparent;
        }

        #btnClose:hover {
            background-color: #f66151;
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

    form_controls = """
        /*
        ==========================================================================
            FORM CONTROLS (SpinBoxes, ComboBoxes, DateEdits, RadioButtons)
        ==========================================================================
        */
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

        QComboBox:disabled {
            background-color: #f3f4f6;
            border: none;
            color: #999;
        }

        QComboBox::drop-down:disabled {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
            background-color: transparent;
        }

        QComboBox::down-arrow:disabled {
            image: url(:/Images/Images/caret-down-disabled.png);
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
    """

    widget_body = """
        /*
        ==========================================================================
                GLOBAL & BASE STYLES
        ==========================================================================
        */
        * {
            color: #000000;
            background-color: #deddda;
        }

        #widget_body {
            border: 1px solid #7a7a7a;
            border-left: none;
            border-top: none;
        }

        """ + tool_tip + """

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

       
        """ + buttons + """

        QLabel[class="accented-labels"] {
            background-color: rgb(255, 255, 255);
            padding: 0px 10px 0px;
            border-radius: 5px;
        }

        """ + check_box + """

        """ + form_controls + """

        /*
        ==========================================================================
                SEARCH WIDGETS
        ==========================================================================
        */
        *[class="widget-search-container"] {
            background-color: #ffffff;
            border: 1px solid #999999;
            border-radius: 15px;
        }

        QWidget[_focus="true"] {
            border: 1px solid #007bff;
        }

        QWidget[_hover="true"] {
            border: 1px solid #3498db;
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
                CONTAINERS & PANELS
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
                TABLES & HEADERS
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
                SCROLL AREA & SCROLLBARS
        ========================================================================== */
        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #deddda;
        }

        """ + scrollbar + """

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
        }

        #scrollArea_id #scrollAreaWidgetContents_2,
        #scrollArea_mc #scrollAreaWidgetContents_3,
        #scrollArea_tf #scrollAreaWidgetContents_4 {
            background-color: #c8c7c5;
            border-radius: 10px;
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

    widget_difficulty_toggle = """
        #widget_difficulty_toggle QPushButton {
            border: 1px solid #9ca3af;
            padding: 5px 10px;
            font: 10pt "Inter";
            background-color: #f3f4f6;
            color: #1f2937;
        }

        #widget_difficulty_toggle QPushButton:hover {
            background-color: #e5e7eb;
        }

        #widget_difficulty_toggle QPushButton:disabled {
            background-color: #f3f4f6;
            border: 1px solid #e5e7eb;
            color: #9ca3af;
        }

        QPushButton#btnEasy {
            border-top-left-radius: 15px;
            border-bottom-left-radius: 15px;
            border-right: none;
        }

        QPushButton#btnAverage {
            border-radius: 0px;
            border-right: none;
        }

        QPushButton#btnHard {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        QPushButton#btnEasy:checked {
            background-color: #86efac;
            border: 2px solid #22c55e;
            color: #14532d;
        }

        QPushButton#btnAverage:checked {
            background-color: #fef08a;
            border: 2px solid #eab308;
            color: #713f12;
        }

        QPushButton#btnHard:checked {
            background-color: #fca5a5;
            border: 2px solid #ef4444;
            color: #7f1d1d;
        }

        QPushButton#btnEasy:disabled,
        QPushButton#btnAverage:disabled {
            border-right: none; 
        }

        QPushButton#btnEasy:checked:disabled {
            background-color: #dcfce7;
            border: 2px solid #bbf7d0;
            border-right: none;
            color: #86efac;
        }

        QPushButton#btnAverage:checked:disabled {
            background-color: #fefce8;
            border: 2px solid #fef08a;
            border-right: none;
            color: #fde047;
        }

        QPushButton#btnHard:checked:disabled {
            background-color: #fee2e2;
            border: 2px solid #fecaca;
            color: #fca5a5;
        }
    """

    widget_remarks = """
        #widget_remarks { 
            border-left: 1px solid rgb(161, 161, 161);
            border-right: 1px solid rgb(161, 161, 161);
            background-color: rgb(246, 245, 244);
        }

        #plainTextEdit_remarks {
            background-color: #FFF;
            padding: 0px 5px;
        }

        #plainTextEdit_remarks:focus {
            border: 1px solid #007bff;
        }
    """

    widget_quizselector = """
        #widget_quizselector {
            background-color: rgb(192, 191, 188);
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #c6e9ff);
        }

        #widget_ReportsFilter {
            background-color: transparent;
        }
    """

    msgbox_main = """
        * {
            color: black;
            font: 10pt "Inter";
            background-color: rgb(222, 221, 218);
        }
    """

    msgbox_header = """
        #dlg_frame_header {
            background-color: #FFF;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            border: 1px solid #d6d6d6;
            border-bottom: none;
        }

        #label_windowTitle {
            background: transparent;
            color: rgb(0, 0, 0);
            font: 11pt "Inter SemiBold";
        }
    """

    msgbox_body = """
        #widget_body {
            background-color: #FFF;
            border: 1px solid #d6d6d6;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            border-top: none;
        }

        #scrollArea, #scrollArea QLabel, #widget_window_buttons {
            border: none;
            background-color: #fff;
        }

        """ + buttons + """

        """ + scrollbar

    addNewStudent = """
        * {
            color: #000000;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        #line_1,
        #line_2,
        #line_3 {
            background-color: #deddda;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        #btnBrowseCSV {
            font: 10pt "Inter";
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);
            border: 1px solid #9a9996;
            color: #1f2937;
            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
        }
        
        #btnBrowseCSV:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f2f6f8);
        }

        #btnBrowseCSV:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);
        }

        #btnBrowseCSV:disabled {
            background-color: #d2d2d2;
            color: #999;
            border: none;
        }

        #widget_CSV QLineEdit:disabled {
            background-color: #f3f4f6;
            border: none;
            color: #999;
        }

        #txtCSVPath {
            background-color: #f3f4f6;
            border: 1px solid #999;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding: 0px 10px;
        }

        #txtCSVPath:focus {
            border: 1px solid #2563eb;
        }

        #txtCSVPath:hover {
            border: 1px solid #3b82f6;
        }

        #txtCSVPath:disabled {
            background-color: #e5e7eb;
            border: none;
        }

        """ + buttons + """

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + tool_tip + """

        #label_17:disabled,
        #label_24:disabled {
            color: #999;
            border: none;
        }

        """ + progress_bar + """

        """ + radio_button + """

        QSpinBox {
            font: 10pt "Inter Medium";
            height: 30px;
            border: 1px solid #999;
            border-radius: 15px;
            padding: 0px 5px;
            background-color: #ffffff;
            color: #1f2937;
            selection-background-color: #bfdbfe;
        }

        QSpinBox:focus {
            border: 1px solid #2563eb;
        }

        QSpinBox:hover {
            border: 1px solid #3b82f6;
        }

        QSpinBox::up-button, QSpinBox::down-button {
            subcontrol-origin: border;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #6b7280;
        }

        QSpinBox::up-button {
            subcontrol-position: top right;
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button {
            subcontrol-position: bottom right;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        QSpinBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
        }
    """

    editStudent = """
        * {
            color: #000000;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        #line_1,
        #line_2,
        #line_3 {
            background-color: #deddda;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        """ + buttons + """

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + tool_tip + """

        #txtPassword {
            background-color: rgb(255, 255, 255);
            border-radius: 18px;
            border: 1px solid #999;
            padding: 0px 15px;
        }

        #txtPassword:focus {
            border: 1px solid #007BFF;
        }

        #txtPassword:hover {
            border: 1px solid #3498db;
        }

        QSpinBox {
            font: 10pt "Inter Medium";
            height: 30px;
            border: 1px solid #999;
            border-radius: 15px;
            padding: 0px 5px;
            background-color: #ffffff;
            color: #1f2937;
            selection-background-color: #bfdbfe;
        }

        QSpinBox:focus {
            border: 1px solid #2563eb;
        }

        QSpinBox:hover {
            border: 1px solid #3b82f6;
        }

        QSpinBox::up-button, QSpinBox::down-button {
            subcontrol-origin: border;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #6b7280;
        }

        QSpinBox::up-button {
            subcontrol-position: top right;
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button {
            subcontrol-position: bottom right;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        QSpinBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
        }
    """

    lesson_dialog = """
        * {
            color: #000000;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        """ + buttons + """

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + tool_tip + """

        QSpinBox {
            font: 10pt "Inter Medium";
            height: 30px;
            border: 1px solid #999;
            border-radius: 15px;
            padding: 0px 5px;
            background-color: #ffffff;
            color: #1f2937;
            selection-background-color: #bfdbfe;
        }

        QSpinBox:focus {
            border: 1px solid #2563eb;
        }

        QSpinBox:hover {
            border: 1px solid #3b82f6;
        }

        QSpinBox::up-button,
        QSpinBox::down-button {
            subcontrol-origin: border;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #6b7280;
        }

        QSpinBox::up-button {
            subcontrol-position: top right;
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button {
            subcontrol-position: bottom right;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        QSpinBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
        }

        *[class="input-and-browse"] {
            background: transparent;
        }

        *[class="input-and-browse"] QLabel {
            background-color: #c0bfbc;
            border: 1px solid #999;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding-left: 8px;
            color: #000000;
        }

        *[class="input-and-browse"] QLineEdit {
            background-color: rgb(255, 255, 255);
            border: 1px solid #999999;
            border-left: none;
            border-right: none;
            padding: 0px 8px;
        }

        *[class="input-and-browse"] QLineEdit:hover {
            border: 1px solid #3498db;
        }

        *[class="input-and-browse"] QLineEdit:focus {
            border: 1px solid #007BFF;
        }

        *[class="input-and-browse"] #btnBrowse {
            font: 10pt "Inter";
            background-color: #f0f0f0;
            border: 1px solid #999999;
            padding: 5px 15px;

            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
            border-top-left-radius: 0px;
            border-bottom-left-radius: 0px;
        }

        *[class="input-and-browse"] #btnBrowse:hover {
            background-color: #e0e0e0;
        }
    """

    user_add_dialog = """
        * {
            color: black;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + tool_tip + """

        #line_1 {
            background-color: #deddda;
        }
    """

    user_info_dialog = """
        * {
            color: black;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + tool_tip + """

        #line_1,
        #line_2 {
            background-color: #deddda;
        }
    """

    section_reg_dialog = """
        * {
            color: #000000;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + progress_bar + """

        """ + radio_button + """

        """ + scrollbar + """

        """ + tool_tip + """

        #line_1 {
            background-color: #deddda;
        }

        #btnExportTemplate {
            border: 1px solid #9a9996;
            border-radius: 15px;
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);
        }

        #btnExportTemplate:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f2f6f8);
        }

        #btnExportTemplate:pressed {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);
        }

        #btnExportTemplate:disabled {
            color: #aeaeae;
            border: 1px solid #dcdcdc;
            background: #f5f5f5;
        }

        *[class="input-and-browse"] {
            background: transparent;
        }
        
        *[class="input-and-browse"] QLabel {
            background-color: #d2d2d2;
            border: 1px solid #999;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding-left: 8px;
            color: #000000;
        }

        *[class="input-and-browse"] QLabel:disabled {
            color: #999;
            border: none;
        }

        *[class="input-and-browse"] QLineEdit {
            background-color: #ffffff;
            border: 1px solid #999;
            border-left: none;
            border-right: none;
            padding: 0px 8px;
        }

        *[class="input-and-browse"] QLineEdit:hover {
            border: 1px solid #3b82f6;
        }

        *[class="input-and-browse"] QLineEdit:focus {
            border: 1px solid #2563eb;
        }

        *[class="input-and-browse"] QLineEdit:disabled {
            background-color: #f3f4f6;
            border: none;
            color: #999;
        }

        *[class="input-and-browse"] #btnBrowseCSV {
            font: 10pt "Inter";
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #d8ecf6);
            border: 1px solid #9a9996;
            padding: 5px 15px;

            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
        }

        *[class="input-and-browse"] #btnBrowseCSV:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f2f6f8);
        }

        *[class="input-and-browse"] #btnBrowseCSV:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dce5e9, stop:1 #ffffff);
        }

        *[class="input-and-browse"] #btnBrowseCSV:disabled {
            background-color: #d2d2d2;
            color: #999;
            border: none;
        }
    """

    section_edit_dialog = """
        * {
            color: #000000;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + scrollbar + """

        """ + tool_tip + """
        
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
    """

    quiz_editor = """
        * {
            color: #000000;
            font: 10pt "Inter";
        }

        QLabel:disabled {
            color: #999;
        }

        #QuizCreatorDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #btnMaximize {
            border-radius: 12px;
            background-color: transparent;
        }

        #btnMaximize:hover {
            background-color: #3bca5c;
        }

        #widget_body {
            background-color: #deddda;
            border: 1px solid #7a7a7a;
            border-top: none;
        }

        QLabel[class="accented-labels"] {
            background-color: rgb(255, 255, 255);
            padding: 0px 10px 0px;
            border-radius: 10px;
        }

        """ + buttons + """

        """ + scrollbar + """

        """ + tool_tip + """

        #btn_save {
            border: none; 
            background: transparent;
        }

        #btn_save:hover {
            background-color: rgb(255, 255, 255);
            border-radius: 5px;
        }

        """ + widget_difficulty_toggle + """

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

        QComboBox[class="combobox-main"]:focus,
        QSpinBox:focus,
        QDoubleSpinBox:focus,
        QDateEdit:focus {
            border: 1px solid #007BFF;
        }

        QComboBox[class="combobox-main"]:disabled,
        QSpinBox:disabled,
        QDoubleSpinBox:disabled,
        QDateEdit:disabled {
            border: none;
            color: #999;
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

        QComboBox::down-arrow:disabled,
        QSpinBox::down-arrow:disabled,
        QDoubleSpinBox::down-arrow:disabled,
        QDateEdit::down-arrow:disabled {
            image: url(:/Images/Images/caret-down-disabled.png);
            width: 8px;
            height: 8px;
            border: none;
        }

        QSpinBox::up-arrow:disabled,
        QDoubleSpinBox::up-arrow:disabled,
        QDateEdit::up-arrow:disabled {
            image: url(:/Images/Images/caret-up-disabled.png);
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

        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #deddda;
        }

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
        }

        #scrollArea_id #scrollAreaWidgetContents_1,
        #scrollArea_mc #scrollAreaWidgetContents_2,
        #scrollArea_tf #scrollAreaWidgetContents_3 {
            background-color: #c8c7c5;
            border-radius: 10px;
        }

        #line_1,
        #line_2,
        #line_3 {
            background-color: #deddda;
        }

        """ + check_box + """
    """

    card_quiz_edit = """
        * {
            font: 11pt "Inter";
            color: #1f2937;
        }

        #CardQuiz_edit {
            background: transparent;
            color: #1f2937;
        }

        #Card {
            background-color: #ffffff;
            border-radius: 10px;
            border: 1px solid #e5e7eb;
        }

        #frame_2, #widget_img {
            border: none;
        }

        QLabel {
            color: #374151;
        }

        """ + tool_tip + """

        #widget_header {
            background-color: #ffffff;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }

        #label_itemno {
            font: 10pt "Inter SemiBold";
            color: #1e40af;
        }

        #btn_delete {
            background-color: transparent;
            color: #ef4444;
            font: 12pt "Inter SemiBold";
            border-radius: 15px;
        }

        #btn_delete:hover {
            color: #ffffff;
            background-color: #ef4444;
            border: 1px solid #ef4444;
        }

        #btn_q_image {
            background-color: #ffffff;
            border: none;
            border-radius: 8px;
        }

        #btn_q_image:hover {
            background-color: #eff6ff;
            border: none;
        }

        #btn_upload_img {
            border: none;
            color: #2563eb;
            background-color: transparent;
            margin: 0px 20px;
            font: 10pt "Inter Medium";
        }

        #btn_upload_img:hover {
            color: #1d4ed8;
        }

        #txt_question {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 8px 10px;
            border: 1px solid #9ca3af;
            color: #1f2937;
        }

        #txt_question:hover {
            border: 1px solid #3b82f6;
        }

        #txt_question:focus {
            border: 1px solid #2563eb;
        }
    """


class Dark_Theme:

    buttons = """
        QPushButton[class="button-green"] {
            border: 1px solid #0a5128;
            border-radius: 15px;
            padding: 0px 10px 0px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1ebd5d, stop:1 #107f3f);
            color: #FFF;
            font: 10pt "Inter SemiBold";
        }

        QPushButton[class="button-green"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2ecc71, stop:1 #27AE60);
        }

        QPushButton[class="button-green"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0b572a, stop:1 #129046); 
        }

        QPushButton[class="button-green"]:disabled {
            background: rgba(39, 174, 96, 0.2);
            border: 1px solid rgba(30, 189, 93, 0.3);
            color: #098f69;
        }

        QPushButton[class="button-normal"] {
            color: #e0e0e0;
            font: 10pt "Inter";
            border: 1px solid #4a4a50;
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3a3a40, stop:1 #2d2d32);
        }

        QPushButton[class="button-normal"]:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #484850, stop:1 #35353c);
        }

        QPushButton[class="button-normal"]:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #252529, stop:1 #35353c);
        }

        QPushButton[class="button-normal"]:disabled {
            color: #666666;
            border: 1px solid #333333;
            background: #222225;
        }
    """

    check_box = """
        QCheckBox {
            background-color: transparent;
            padding: 5px 10px;
            color: #ffffff;
            font: 10pt "Inter";
        }

        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            background-color: #1e1e1e;
            border: 2px solid #4a4a4a;
            border-radius: 4px;
        }

        QCheckBox::indicator:hover {
            border-color: #60a5fa;
        }

        QCheckBox::indicator:checked {
            background-color: #3b82f6;
            border-color: #3b82f6;
            image: url(:/Images/Images/check.png);
        }

        QCheckBox::indicator:disabled {
            background-color: #1a1a1a;
            border: 2px solid #333333;
            image: none;
        }

        QCheckBox:disabled {
            color: #666666;
        }
    """

    tool_tip = """
        QToolTip {
            background-color: #262626;
            color: #ffffff;
            border: 1px solid #4a4a4a;
            padding: 4px 6px;
            border-radius: 6px;
            font: 10pt "Inter";
        }
    """

    progress_bar = """
        QProgressBar {
            border-radius: 10px;
            background-color: #1e1e1e;
            border: 1px solid #4a4a4a;
        }

        QProgressBar::chunk {
            background-color: #3b82f6;
            border-radius: 10px;
        }
    """

    radio_button = """ 
        QRadioButton {
            color: #ffffff;
            spacing: 8px;
            padding: 0px 10px;
            background: transparent;
            font: 10pt "Inter";
        }

        QRadioButton::indicator {
            background: #1e1e1e;
            border: 2px solid #4a4a4a;
            min-width: 14px;
            min-height: 14px;
            border-radius: 7px;
        }

        QRadioButton::indicator:checked {
            border-color: #60a5fa;
            background-color: #3b82f6;
        }
    """

    scroll_bar = """
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
    """

    input_field = """
        *[class="input-field"] {
            background-color: transparent;
        }

        *[class="input-field"] QLineEdit {
            background-color: #1e1e1e;
            border: 1px solid #4a4a4a;
            border-left: none;
            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
            padding: 0px 8px;
            color: #ffffff;
        }

        *[class="input-field"] QLineEdit:disabled {
            border: none;
            color: #666666;
        }

        *[class="input-field"] QLabel {
            background-color: #262626;
            border-left: 1px solid #4a4a4a;
            border-top: 1px solid #4a4a4a;
            border-bottom: 1px solid #4a4a4a;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding-left: 8px;
            color: #a0a0a0;
        }

        *[class="input-field"] QLabel:disabled {
            color: #666666;
            border: none;
        }

        QLineEdit:focus {
            border: 1px solid #2563eb;
        }

        QLineEdit:hover {
            border: 1px solid #3b82f6;
        }
    """

    combo_box_input_field = """
        *[class="input-field"] QComboBox {
            background-color: #1e1e1e;
            border: 1px solid #4a4a4a;
            border-left: none;
            padding: 0px 10px;
            color: #ffffff;
            font: 10pt "Inter Medium";
            selection-background-color: #3b82f6;
            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
        }

        QComboBox:focus {
            border: 1px solid #3b82f6;
        }

        QComboBox:hover {
            border: 1px solid #60a5fa;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
            border-left-width: 0px;
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        QComboBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            border: none;
            width: 8px;
            height: 8px;
        }

        QComboBox QAbstractItemView {
            background-color: #1e1e1e;
            border: 1px solid #4a4a4a;
            selection-background-color: #3b82f6;
            selection-color: #ffffff;
            outline: 0;
        }

        QComboBox QAbstractItemView::item {
            padding: 0px 15px;
            border-radius: 4px;
            color: #ffffff;
        }

        QComboBox QAbstractItemView::item:hover {
            background-color: #3b82f6;
            color: #ffffff;
        }

        QComboBox:disabled {
            border: none;
            color: #666666;
        }

        QComboBox::drop-down:disabled {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
            background-color: transparent;
        }

        QComboBox::down-arrow:disabled {
            image: url(:/Images/Images/caret-down-disabled.png);
        }
    """

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

    header_dlg = """
        #frame_header {
            background-color: #2d2d2d;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            border: 1px solid #4a4a4a;
            border-bottom: none;
        }

        #label_windowTitle {
            background: transparent;
            font: 10pt "Inter SemiBold";
        }

        #widget_window_buttons {
            background: transparent;
        }

        #btnMinimize {
            border-radius: 12px;
            background-color: #77767b;
        }

        #btnMinimize:hover {
            background-color: #f8e45c;
        }

        #btnClose {
            border-radius: 12px;
            background-color: #77767b;
        }

        #btnClose:hover {
            background-color: #f66151;
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

    form_controls = """
        /*
        ==========================================================================
                FORM CONTROLS (SpinBoxes, ComboBoxes, DateEdits, RadioButtons)
        ==========================================================================
        */
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

        QComboBox:disabled {
            border: none;
            color: #666666;
        }

        QComboBox::drop-down:disabled {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
            background-color: transparent;
        }

        QComboBox::down-arrow:disabled {
            image: url(:/Images/Images/caret-down.png);
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
    """

    widget_body = """
        /* ==========================================================================
                GLOBAL & BASE STYLES
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

        """ + tool_tip + """

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

        """ + buttons + """

        QLabel[class="accented-labels"] {
            color: #ffffff;
            background-color: #2b2b30;
            padding: 0px 10px 0px;
            border-radius: 5px;
        }

        """ + check_box + """

        """ + form_controls + """

        /* ==========================================================================
                SEARCH WIDGETS
        ========================================================================== */
        *[class="widget-search-container"] {
            background-color: #2b2b30;
            border: 1px solid #4a4a50;
            border-radius: 15px;
        }

        QWidget[_focus="true"] {
            border: 1px solid #3b82f6;
        }

        QWidget[_hover="true"] {
            border: 1px solid #60a5fa;
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

        /*
        ==========================================================================
                CONTAINERS & PANELS
        ==========================================================================
        */
        *[class="gradient-header"] {
            border: 1px solid #2563eb;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1e3a8a, stop:1 #1e293b);
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
                TABLES & HEADERS
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
                SCROLL AREA & SCROLLBARS
        ========================================================================== */
        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #1e1e20;
        }

        """ + scroll_bar + """

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
        }

        #scrollArea_id #scrollAreaWidgetContents_2,
        #scrollArea_mc #scrollAreaWidgetContents_3,
        #scrollArea_tf #scrollAreaWidgetContents_4 {
            background-color: #2b2b30;
            border-radius: 10px;
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

    widget_difficulty_toggle = """
        #widget_difficulty_toggle QPushButton {
            border: 1px solid #4a4a4a;
            background-color: #1e1e1e;
            padding: 5px 10px;
            font: 10pt "Inter";
            color: #ffffff;
        }

        #widget_difficulty_toggle QPushButton:hover {
            background-color: #333333;
        }

        #widget_difficulty_toggle QPushButton:disabled {
            background-color: #1a1a1a;
            border: 1px solid #333333;
            color: #666666;
        }

        QPushButton#btnEasy {
            border-top-left-radius: 15px;
            border-bottom-left-radius: 15px;
            border-right: none;
        }

        QPushButton#btnAverage {
            border-radius: 0px;
            border-right: none;
        }

        QPushButton#btnHard {
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }

        QPushButton#btnEasy:checked {
            background-color: #166534;
            border: 2px solid #22c55e;
            color: #ffffff;
        }

        QPushButton#btnAverage:checked {
            background-color: #854d0e;
            border: 2px solid #eab308;
            color: #ffffff;
        }

        QPushButton#btnHard:checked {
            background-color: #991b1b;
            border: 2px solid #ef4444;
            color: #ffffff;
        }

        QPushButton#btnEasy:checked:disabled {
            background-color: rgba(22, 101, 52, 0.4);
            border: 2px solid rgba(34, 197, 94, 0.3);
            color: #86efac;
        }

        QPushButton#btnAverage:checked:disabled {
            background-color: rgba(133, 77, 14, 0.4);
            border: 2px solid rgba(234, 179, 8, 0.3);
            color: #fde047;
        }

        QPushButton#btnHard:checked:disabled {
            background-color: rgba(153, 27, 27, 0.4);
            border: 2px solid rgba(239, 68, 68, 0.3);
            color: #fca5a5;
        }
    """

    widget_remarks = """
        #widget_remarks { 
            border-left: 1px solid #3d3d3d;
            border-right: 1px solid #3d3d3d;
            background-color: #2d2d2d;
        }

        #plainTextEdit_remarks {
            background-color: #1e1e1e;
            color: #ffffff;
            border: 1px solid #4a4a4a;
            padding: 0px 5px;
            selection-background-color: #3b82f6;
            selection-color: #ffffff;
        }

        #plainTextEdit_remarks:focus {
            border: 1px solid #3b82f6;
        }
    """

    widget_quizselector = """
        #widget_quizselector {
            background-color: #1e293b;
            border-radius: 15px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1e293b, stop:1 #0f172a);
            border: 1px solid #3d3d3d;
        }

        #widget_ReportsFilter {
            background-color: transparent;
        }
    """

    msgbox_main = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
            background-color: #3d3d3d;
        }
    """

    msgbox_header = """
        #dlg_frame_header {
            background-color: #3d3d3d;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            border: 1px solid #A1A1A1;
            border-bottom: none;
        }

        #label_windowTitle {
            background: transparent;
            color: #ffffff;
            font: 11pt "Inter SemiBold";
        }
    """

    msgbox_body = """
        #widget_body {
            background-color: #3d3d3d;
            border: 1px solid #A1A1A1;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            border-top: none;
        }

        #scrollArea,
        #scrollArea QLabel,
        #widget_window_buttons {
            border: none;
            background-color: transparent;
        }

        """ + buttons + """

        """ + scroll_bar

    addNewStudent = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        #line_1,
        #line_2,
        #line_3 {
            background-color: #2d2d2d;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        #btnBrowseCSV {
            font: 10pt "Inter";
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #4a4a4a;
            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
        }

        #btnBrowseCSV:hover {
            background-color: #3d3d3d;
        }

        #btnBrowseCSV:disabled {
            border: none;
            color: #666666;
        }

        #widget_CSV QLineEdit:disabled {
            background-color: #1a1a1a;
            border: none;
            color: #666666;
        }

        #txtCSVPath {
            background-color: #1a1a1a;
            border: 1px solid #4a4a4a;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding: 0px 10px;
        }

        #txtCSVPath:focus {
            border: 1px solid #3b82f6;
        }

        #txtCSVPath:hover {
            border: 1px solid #60a5fa;
        }

        #txtCSVPath:disabled {
            color: #666666;
            border: none;
        }

        """ + buttons + """

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + tool_tip + """

        #label_17:disabled,
        #label_24:disabled {
            color: #666666;
            border: none;
        }

        """ + progress_bar + """

        """ + radio_button + """

        QSpinBox {
            font: 10pt "Inter Medium";
            height: 30px;
            border: 1px solid #4a4a4a;
            border-radius: 15px;
            padding: 0px 5px;
            background-color: #1e1e1e;
            color: #ffffff;
            selection-background-color: #3b82f6;
        }

        QSpinBox:focus {
            border: 1px solid #3b82f6;
        }

        QSpinBox:hover {
            border: 1px solid #60a5fa;
        }

        QSpinBox::up-button, QSpinBox::down-button {
            subcontrol-origin: border;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #a0a0a0;
        }

        QSpinBox::up-button {
            subcontrol-position: top right;
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button {
            subcontrol-position: bottom right;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        QSpinBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
        }
    """

    editStudent = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        #line_1,
        #line_2,
        #line_3 {
            background-color: #2d2d2d;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        """ + buttons + """

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + tool_tip + """

        #label_17:disabled,
        #label_24:disabled {
            color: #666666;
            border: none;
        }

        #txtPassword {
            background-color: #1e1e1e;
            border-radius: 18px;
            border: 1px solid #4a4a4a;
            padding: 0px 15px;
        }

        #txtPassword:focus {
            border: 1px solid #007BFF;
        }

        #txtPassword:hover {
            border: 1px solid #3498db;
        }

        QSpinBox {
            font: 10pt "Inter Medium";
            height: 30px;
            border: 1px solid #4a4a4a;
            border-radius: 15px;
            padding: 0px 5px;
            background-color: #1e1e1e;
            color: #ffffff;
            selection-background-color: #3b82f6;
        }

        QSpinBox:focus {
            border: 1px solid #3b82f6;
        }

        QSpinBox:hover {
            border: 1px solid #60a5fa;
        }

        QSpinBox::up-button, QSpinBox::down-button {
            subcontrol-origin: border;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #a0a0a0;
        }

        QSpinBox::up-button {
            subcontrol-position: top right;
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button {
            subcontrol-position: bottom right;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        QSpinBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
        }
    """

    lesson_dialog = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        """ + buttons + """

        """ + input_field + """
        
        """ + combo_box_input_field + """

        """ + tool_tip + """

        QSpinBox {
            font: 10pt "Inter Medium";
            height: 30px;
            border: 1px solid #999;
            border-radius: 15px;
            padding: 0px 5px;
            background-color: #ffffff;
            color: #1f2937;
            selection-background-color: #bfdbfe;
        }

        QSpinBox:focus {
            border: 1px solid #2563eb;
        }

        QSpinBox:hover {
            border: 1px solid #3b82f6;
        }

        QSpinBox::up-button,
        QSpinBox::down-button {
            subcontrol-origin: border;
            width: 8px;
            height: 8px;
            padding: 6px 10px 6px 2px;
            color: #6b7280;
        }

        QSpinBox::up-button {
            subcontrol-position: top right;
            border-top-right-radius: 15px;
        }

        QSpinBox::down-button {
            subcontrol-position: bottom right;
            border-bottom-right-radius: 15px;
        }

        QSpinBox::up-arrow {
            image: url(:/Images/Images/caret-up.png);
            width: 8px;
            height: 8px;
        }

        QSpinBox::down-arrow {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
        }

        *[class="input-and-browse"] {
            background: transparent;
        }

        *[class="input-and-browse"] QLabel {
            background-color: #262626;
            border: 1px solid #4a4a4a;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding-left: 8px;
            color: #a0a0a0;
        }

        *[class="input-and-browse"] QLineEdit {
            background-color: #1e1e1e;
            border: 1px solid #4a4a4a;
            border-left: none;
            border-right: none;
            padding: 0px 8px;
        }

        *[class="input-and-browse"] QLineEdit:hover {
            border: 1px solid #3b82f6;
        }

        *[class="input-and-browse"] QLineEdit:focus {
            border: 1px solid #007BFF;
        }

        *[class="input-and-browse"] #btnBrowse {
            font: 10pt "Inter";
            background-color: #262626;
            border: 1px solid #4a4a4a;
            padding: 5px 15px;

            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
        }

        *[class="input-and-browse"] #btnBrowse:hover {
            background-color: #363636;
        }
    """

    user_add_dialog = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + tool_tip + """

        #line_1,
        #line_2 {
            background-color: #2d2d2d;
        }
    """

    user_info_dialog = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + tool_tip + """

        #line_1 {
            background-color: #2d2d2d;
        }
    """

    section_reg_dialog = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + progress_bar + """

        """ + radio_button + """

        """ + scroll_bar + """

        """ + tool_tip + """

        #line_1 {
            background-color: #2d2d2d;
        }

        #btnExportTemplate {
            border: 1px solid #4a4a50;
            border-radius: 15px;
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3a3a40, stop:1 #2d2d32);
        }

        #btnExportTemplate:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #484850, stop:1 #35353c);
        }

        #btnExportTemplate:pressed {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #252529, stop:1 #35353c);
        }

        #btnExportTemplate:disabled {
            color: #666666;
            border: 1px solid #333333;
            background: #222225;
        }

        *[class="input-and-browse"] {
            background: transparent;
        }

        *[class="input-and-browse"] QLabel {
            background-color: #262626;
            border: 1px solid #4a4a4a;
            border-right: none;
            border-top-left-radius: 18px;
            border-bottom-left-radius: 18px;
            padding-left: 8px;
            color: #a0a0a0;
        }

        *[class="input-and-browse"] QLabel:disabled {
            color: #666666;
            border: none;
        }

        *[class="input-and-browse"] QLineEdit {
            background-color: #1e1e1e;
            border: 1px solid #4a4a4a;
            border-left: none;
            border-right: none;
            padding: 0px 8px;
        }

        *[class="input-and-browse"] QLineEdit:hover {
            border: 1px solid #3b82f6;
        }

        *[class="input-and-browse"] QLineEdit:focus {
            border: 1px solid #007BFF;
        }

        *[class="input-and-browse"] QLineEdit:disabled {
            border: none;
            color: #666666;
        }

        *[class="input-and-browse"] #btnBrowseCSV {
            font: 10pt "Inter";
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3a3a40, stop:1 #2d2d32);
            border: 1px solid #4a4a4a;
            padding: 5px 15px;

            border-top-right-radius: 18px;
            border-bottom-right-radius: 18px;
        }

        *[class="input-and-browse"] #btnBrowseCSV:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #484850, stop:1 #35353c);
        }

        *[class="input-and-browse"] #btnBrowseCSV:pressed {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #252529, stop:1 #35353c);
        }

        *[class="input-and-browse"] #btnBrowseCSV:disabled {
            color: #666666;
            border: none;
            background: #222225;
        }
    """

    section_edit_dialog = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QDialog {
            background: transparent;
        }

        """ + header_dlg + """

        """ + tool_tip + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        """ + input_field + """

        """ + combo_box_input_field + """

        """ + buttons + """

        """ + scroll_bar + """

        """ + tool_tip + """
        
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
    """

    quiz_editor = """
        * {
            color: #ffffff;
            font: 10pt "Inter";
        }

        QLabel:disabled {
            color: #666666;
        }

        #QuizCreatorDialog {
            background: transparent;
        }

        """ + header_dlg + """

        """ + tool_tip + """

        #widget_body {
            background-color: #2d2d2d;
            border: 1px solid #4a4a4a;
            border-top: none;
        }

        #btnMaximize {
            border-radius: 12px;
            background-color: #77767b;
        }

        #btnMaximize:hover {
            background-color: #3bca5c;
        }

        QLabel[class="accented-labels"] {
            color: #ffffff;
            background-color: #1e1e1e;
            padding: 0px 10px 0px;
            border-radius: 5px;
        }

        QLabel[class="accented-labels"]:disabled {
            background-color: #242424;
            color: #666666;
        }

        """ + buttons + """

        """ + scroll_bar + """

        #btn_save {
            border: none; 
            background: transparent;
        }

        #btn_save:hover {
            background-color: #484850;
            border-radius: 5px;
        }

        """ + widget_difficulty_toggle + """

        QScrollArea { 
            border: none;
            border-radius: 20px;
            background-color: #1e1e20;
        }

        QScrollArea QWidget #qt_scrollarea_corner {
            background: transparent;
            border: none;
        }

        #scrollArea_id #scrollAreaWidgetContents_1,
        #scrollArea_mc #scrollAreaWidgetContents_2,
        #scrollArea_tf #scrollAreaWidgetContents_3 {
            background-color: #1e1e1e;
            border-radius: 10px;
        }

        #line_1,
        #line_2,
        #line_3 {
            background-color: #2d2d2d;
        }

        QComboBox[class="combobox-main"],
        QSpinBox,
        QDoubleSpinBox,
        QDateEdit {
            height: 30px;
            padding: 0px 5px 0px 10px;
            color: #ffffff;
            font: 10pt "Inter SemiBold";
            border: 1px solid #4a4a4a;
            background-color: #1e1e1e;
            border-radius: 15px;
            selection-background-color: #3b82f6;
            selection-color: #ffffff;
        }

        QComboBox[class="combobox-main"]:hover,
        QSpinBox:hover,
        QDoubleSpinBox:hover,
        QDateEdit:hover {
            border: 1px solid #3b82f6;
        }

        QComboBox[class="combobox-main"]:focus,
        QSpinBox:focus,
        QDoubleSpinBox:focus,
        QDateEdit:focus {
            border: 1px solid #007BFF;
        }

        QComboBox[class="combobox-main"]:disabled,
        QSpinBox:disabled,
        QDoubleSpinBox:disabled,
        QDateEdit:disabled {
            background-color: #242424;
            border: 1px solid #333333;
            color: #666666;
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
            image: url(:/Images/Images/caret-down-disabled.png);
            width: 8px;
            height: 8px;
            border: none;
        }

        QSpinBox::up-arrow,
        QDoubleSpinBox::up-arrow,
        QDateEdit::up-arrow {
            image: url(:/Images/Images/caret-up-disabled.png);
            width: 8px;
            height: 8px;
        }

        QComboBox::down-arrow:disabled,
        QSpinBox::down-arrow:disabled,
        QDoubleSpinBox::down-arrow:disabled,
        QDateEdit::down-arrow:disabled {
            image: url(:/Images/Images/caret-down.png);
            width: 8px;
            height: 8px;
            border: none;
        }

        QSpinBox::up-arrow:disabled,
        QDoubleSpinBox::up-arrow:disabled,
        QDateEdit::up-arrow:disabled {
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

        """ + check_box + """
    """

    card_quiz_edit = """
        * {
            font: 11pt "Inter";
            color: #ffffff;
        }

        #CardQuiz_edit {
            background: transparent;
            color: #ffffff;
        }

        #Card {
            background-color: #2a2c2e;
            border-radius: 10px;
            border: 1px solid #4a4a4a;
        }

        #frame_2, #widget_img {
            border: none;
        }

        QLabel {
            color: #e0e0e0;
        }

        """ + tool_tip + """

        #widget_header {
            background-color: #2a2c2e;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }

        #label_itemno {
            font: 10pt "Inter SemiBold";
            color: #93c5fd;
        }

        #btn_delete {
            background-color: transparent;
            color: #f87171;
            font: 12pt "Inter SemiBold";
            border-radius: 15px;
        }

        #btn_delete:hover {
            color: #ffffff;
            background-color: #dc2626;
            border: 1px solid #dc2626;
        }

        #btn_q_image {
            background-color: #262626;
            border: none;
            border-radius: 8px;
        }

        #btn_q_image:hover {
            background-color: #1e293b;
            border: none;
        }

        #btn_upload_img {
            border: none;
            color: #60a5fa;
            background-color: transparent;
            margin: 0px 20px;
            font: 10pt "Inter Medium";
        }

        #btn_upload_img:hover {
            color: #93c5fd;
        }

        #txt_question {
            background-color: #1e1e1e;
            border-radius: 15px;
            padding: 8px 10px;
            border: 1px solid #4a4a4a;
            color: #ffffff;
        }

        #txt_question:hover {
            border: 1px solid #60a5fa;
        }

        #txt_question:focus {
            border: 1px solid #3b82f6;
        }
    """


