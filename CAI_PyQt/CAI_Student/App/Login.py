from PySide6.QtWidgets import QWidget, QListWidgetItem, QLineEdit
from PySide6.QtCore import Qt, Signal, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve, QPoint
from PySide6.QtGui import QImage, QPixmap

from passlib.hash import bcrypt
from App.Tools import Utility, Card, CustomShapeDialog

from App.FormLogin import Ui_FormLogin
from App.CRUDTools import DatabaseTools
from App.Student import Student

class Login(QWidget, Ui_FormLogin):
    login_success = Signal(object)
    RESIZE_MARGIN = 8  # The clickable area around the edges (in pixels)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Remove OS default window frame
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setMouseTracking(True)

        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnMaximize.clicked.connect(self.toggle_maximize)

        self.btnLogin.clicked.connect(self.handle_login)
        self.btnBack.clicked.connect(lambda: self.slide_back_to_page(0))
        self.btnShowPassword.clicked.connect(self.toggle_password_visibility)
        self.db_tools = DatabaseTools()
        self.util = Utility()
        self.cards = [] # Keep a list of your card widgets
        self.last_selected_card = None

        self.student = Student()
        record = self.student.retrieve_sections()
        self.list_sections.clear()
        self.list_sections.currentItemChanged.connect(self.display_student_cards)

        for index_data, item_name in record:
            # Create the visual item
            item = QListWidgetItem(item_name)

            # Store the 'index' (UUID) in the background slot
            item.setData(Qt.ItemDataRole.UserRole, index_data)

            # Add to UI
            self.list_sections.addItem(item)

        # --- AUTO-SELECT FIRST ITEM ---
        if self.list_sections.count() > 0:
            self.list_sections.setCurrentRow(0)

            first_item = self.list_sections.item(0)
            self.display_student_cards(first_item)

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
            # Optional: Change icon back to 'maximize'
            # self.btnMaximize.setIcon(QIcon("expand.png"))
        else:
            self.showMaximized()
            # Optional: Change icon to 'restore' 
            # self.btnMaximize.setIcon(QIcon("restore.png"))

    def mouseMoveEvent(self, event):
        # Get local position of the mouse
        pos = event.position().toPoint()
        rect = self.rect()
        
        # Determine which edge the mouse is over
        edge = None
        if pos.x() >= rect.width() - self.RESIZE_MARGIN and pos.y() >= rect.height() - self.RESIZE_MARGIN:
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
            edge = Qt.Edge.RightEdge | Qt.Edge.BottomEdge
        elif pos.x() >= rect.width() - self.RESIZE_MARGIN:
            self.setCursor(Qt.CursorShape.SizeHorCursor)
            edge = Qt.Edge.RightEdge
        elif pos.y() >= rect.height() - self.RESIZE_MARGIN:
            self.setCursor(Qt.CursorShape.SizeVerCursor)
            edge = Qt.Edge.BottomEdge
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

        # If mouse is pressed and we are on an edge, start resizing
        if event.buttons() == Qt.LeftButton and edge:
            self.windowHandle().startSystemResize(edge)
        
        # Otherwise, allow your existing move logic to happen if clicking the header
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            rect = self.rect()
            
            # If NOT on a resize edge, allow moving the window
            on_edge = (pos.x() >= rect.width() - self.RESIZE_MARGIN or 
                    pos.y() >= rect.height() - self.RESIZE_MARGIN)
            
            if not on_edge:
                self.windowHandle().startSystemMove()
                event.accept()

    def handle_login(self):
        studentid = self.last_selected_card.studentid
        password = self.txtPassword.text()
        user = self.authenticate_user(studentid, password)

        if user:
            self.login_success.emit(user)

        elif not password:
            dialog = CustomShapeDialog("Please type your password.", parent=self)
            dialog.exec()

        else:
            dialog = CustomShapeDialog("Oops! Wrong password.", parent=self)
            dialog.exec()

    def authenticate_user(self, studentid, password):
        try:
            result = self.student.retrieve_one_student_info(studentid)

            if result:
                studentid, lname, fname, mname, section, gender, stored_hash, profile_pic, _, _ = result
                if bcrypt.verify(password, stored_hash):
                    user = {
                        "studentid": studentid,
                        "firstname": fname,
                        "middlename": mname,
                        "lastname": lname,
                        "section": section,
                        "gender": gender,
                        "profile_pic": profile_pic,
                    }
                    return user

            return None

        except Exception as e:
            print(f"Database error: {e}")
            return None

    def display_student_cards(self, item):
        layout = self.gridLayout
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(10)

        # 1. Efficiently clear existing cards
        while layout.count():
            # takeAt removes the layout item, allowing access to the widget
            item_to_remove = layout.takeAt(0)
            widget = item_to_remove.widget()

            if widget is not None:
                # deleteLater is safer than sip.delete for preventing crashes
                widget.deleteLater()

        # Clear the list tracking the cards
        self.cards.clear()

        # 2. Fetch data
        student = Student()
        sectionid = item.data(Qt.ItemDataRole.UserRole)
        students = student.retrieve_student_info(sectionid)

        # 3. Add new cards
        columns = 2
        for i, row in enumerate(students):
            sid, f_name, m_name, l_name, _, gender, _, img_data = row # Unpacking for clarity

            # Handle Image
            pixmap = None
            if not self.util.isEmpty(img_data):
                image = QImage.fromData(bytes(img_data))
                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)

            full_name = self.util.formatFullname(f_name, m_name, l_name)
            card = Card(full_name, sid, pixmap, "20px")

            card.clicked.connect(self.handle_card_selection)

            # Calculate row and column:
            # i=0 -> (0,0), i=1 -> (0,1), i=2 -> (1,0), etc.
            r = i // columns
            c = i % columns

            layout.addWidget(card, r, c)
            self.cards.append(card)

    def handle_card_selection(self, clicked_card, student_id):
        # 1. Store the reference and clear all other cards immediately
        self.last_selected_card = clicked_card

        for card in self.cards:
            if card != clicked_card:
                card.set_selected(False)

        # 2. Select the clicked card (Visual state)
        clicked_card.set_selected(True)

        # 3. Update Page 2 UI with the selected student's info
        # Using the attributes stored in your Card object
        self.labelFullName.setText(clicked_card.fullName)
        circular_pixmap = self.util.makeCircularPixmap(clicked_card.pixMap, size=150)
        self.label_profile_pic.setPixmap(circular_pixmap)
        
        # Optional: If you need the ID for database queries on Page 2
        self.current_student_id = student_id 

        # 4. Trigger the transition to the Math section (Page 2)
        self.slide_to_page(1)

    def slide_to_page(self, index):
        stack = self.stackedWidget
        if stack.currentIndex() == index:
            return

        # 1. Setup variables
        current_page = stack.currentWidget()
        next_page = stack.widget(index)
        width = stack.width()

        # 2. Prepare next page (move it to the right side off-screen)
        next_page.setGeometry(width, 0, width, stack.height())
        next_page.show()
        next_page.raise_()

        # 3. Create Parallel Animations
        self.anim_group = QParallelAnimationGroup()

        # Slide next page IN (from right to center)
        anim_in = QPropertyAnimation(next_page, b"pos")
        anim_in.setDuration(450)
        anim_in.setStartValue(QPoint(width, 0))
        anim_in.setEndValue(QPoint(0, 0))
        anim_in.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Slide current page OUT (from center to left)
        anim_out = QPropertyAnimation(current_page, b"pos")
        anim_out.setDuration(450)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(-width, 0))
        anim_out.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.anim_group.addAnimation(anim_in)
        self.anim_group.addAnimation(anim_out)

        # 4. On finish, update the StackedWidget index to "reset" the layout
        self.anim_group.finished.connect(lambda: stack.setCurrentIndex(index))
        self.anim_group.start()

    def slide_back_to_page(self, index):
        self.txtPassword.clear()
        stack = self.stackedWidget
        if stack.currentIndex() == index:
            return

        current_page = stack.currentWidget()
        prev_page = stack.widget(index)
        width = stack.width()

        # 1. Prepare previous page (place it to the LEFT off-screen)
        prev_page.setGeometry(-width, 0, width, stack.height())
        prev_page.show()
        prev_page.raise_()

        self.anim_group = QParallelAnimationGroup()

        # Slide previous page IN (from left to center)
        anim_in = QPropertyAnimation(prev_page, b"pos")
        anim_in.setDuration(450)
        anim_in.setStartValue(QPoint(-width, 0))
        anim_in.setEndValue(QPoint(0, 0))
        anim_in.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Slide current page OUT (from center to right)
        anim_out = QPropertyAnimation(current_page, b"pos")
        anim_out.setDuration(450)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(width, 0))
        anim_out.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.anim_group.addAnimation(anim_in)
        self.anim_group.addAnimation(anim_out)

        self.anim_group.finished.connect(lambda: stack.setCurrentIndex(index))
        self.anim_group.start()

    def toggle_password_visibility(self):
        if self.txtPassword.echoMode() == QLineEdit.EchoMode.Password:
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Normal)
            css = """
                #btnShowPassword {
                    border-image: url(:/Images/Images/eye.png);
                    border-radius: 10px;
                    color: white;
                    font-family: 'Kissy Hugs';
                    font-size: 20pt;
                    background-color: transparent;
                }
            """
            self.btnShowPassword.setStyleSheet(css)
        else:
            self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)
            css = """
                #btnShowPassword {
                    border-image: url(:/Images/Images/closed_eye.png);
                    border-radius: 10px;
                    color: white;
                    font-family: 'Kissy Hugs';
                    font-size: 20pt;
                    background-color: transparent;
                }
            """
            self.btnShowPassword.setStyleSheet(css)