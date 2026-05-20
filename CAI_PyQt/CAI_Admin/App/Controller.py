import os

# PyQt Imports
from PySide6.QtCore import QSettings, QTimer, QDateTime, QPoint, QEasingCurve, QPropertyAnimation, QParallelAnimationGroup, Qt, QDate
from PySide6.QtWidgets import QMainWindow, QHeaderView, QDialog, QStyledItemDelegate, QWidget, QMessageBox, QApplication, QButtonGroup
from PySide6.QtGui import QFontDatabase, QImage, QPixmap, QGuiApplication, QStandardItemModel, QStandardItem
from shiboken6 import isValid

# Core App Logic/Main Windows
from App.FormHome import Ui_Home
from App.Login import Login
from App.Tools import Card, Utility
from App.CRUDTools import DatabaseTools

# Dialogs
from App.StudentDialog import Student, AddNewStudentDialog, StudentEditorDialog
from App.UserDialog import Staff, AddUserDialog, EditUserDialog
from App.SectionDialog import Section
from App.Lessons import Lesson, LessonDialog

class Controller:
    def __init__(self, script_dir=''):
        self.script_dir = script_dir
        self.settings = QSettings("CAI_System", "CAI_Admin_App")
        self.util = Utility()
        self.db_tools = DatabaseTools()

        self.login_win = Login()
        self.login_win.txtUsername.returnPressed.connect(self.login_win.btnLogin.click)
        self.login_win.txtPassword.returnPressed.connect(self.login_win.btnLogin.click)
        self.login_win.login_success.connect(self.on_login_success)

        self.cards = [] # Keep a list of your card widgets
        self.last_selected_card = None

        self.load_fonts()
        self.check_session()

    def check_session(self):
        sid = self.settings.value("school_id")
        if sid:
            user = {
                "school_id": sid,
                "username": self.settings.value("username"),
                "firstname": self.settings.value("firstname"),
                "lastname": self.settings.value("lastname"),
                "position_id": self.settings.value("position_id"),
                "position_name": self.settings.value("position_name")
            }
            self.show_home(user)
        else:
            self.login_win.show()

    def on_login_success(self, user):
        for key, val in user.items():
            self.settings.setValue(key, val)

        self.settings.sync()
        self.show_home(user)

    def show_home(self, user:dict):
        self.home_win = QMainWindow()
        self.ui = Ui_Home()
        self.ui.setupUi(self.home_win)
        # self.home_win.showMaximized()

        # Setup UI
        self.card_layout = self.ui.verticalLayout_9
        self.card_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.card_layout.setSpacing(10)
        self.get_dynamic_school_year_dates()

        # Search Box: Pass the text directly
        self.ui.txt_classList_search.textChanged.connect(self.display_student_cards)

        # Spin Boxes: Used a lambda to ignore the 'value' integer they send
        self.ui.spinBox_SY1.valueChanged.connect(lambda: self.handle_student_searching())
        self.ui.spinBox_SY2.valueChanged.connect(lambda: self.handle_student_searching())

        self.ui.btnUserName.setText(f"{user['firstname']} {user['lastname']}")
        self.ui.labelPosition.setText(user['position_name'])

        # Timer for Clock
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.displayDashboard()

        self.nav_group = QButtonGroup(self.home_win)
        self.nav_group.setExclusive(True)

        # Navigation
        self.nav_map = {
            self.ui.btnHome: 0,
            self.ui.btnStudentList: 1,
            self.ui.btnLesson: 2,
            self.ui.btnQuiz: 3,
            self.ui.btnExercise: 4,
            self.ui.btnSections: 5,
            self.ui.btnReports: 6,
            self.ui.btnUsers: 7,
            self.ui.btnUtility: 8,
        }

        for btn, idx in self.nav_map.items():
            btn.setCheckable(True)
            self.nav_group.addButton(btn)
            btn.clicked.connect(lambda checked, i=idx: self.handle_nav_click(i))

        # Optional: Set the initial active button (Home)
        self.ui.btnHome.setChecked(True)

        pic = Staff().get_user_profile_pic(user["school_id"])
        
        if pic:
            self.ui.btnUserName.setIcon(pic)

        self.ui.btnRefreshSY.clicked.connect(self.get_dynamic_school_year_dates)
        self.ui.btnAddStudent.clicked.connect(self.register_student)
        self.ui.btnDeleteStudent.clicked.connect(lambda: self.delete_student(user))
        self.ui.btnEditStudent.clicked.connect(lambda: self.edit_student(user))

        self.ui.btnAddNewUser.clicked.connect(lambda: self.add_user(user))
        self.ui.btnEditUserInfo.clicked.connect(lambda: self.update_user(user, 2))
        self.ui.btnUserName.clicked.connect(lambda: self.update_user(user))
        self.ui.btnLogout.clicked.connect(self.logout)

        self.ui.comboBox_Section.currentIndexChanged.connect(self.display_section_info)
        self.sectionObj = Section(user)
        self.sectionObj.populate_sections(self.ui.comboBox_Section, False)
        self.sectionObj.populate_sections(self.ui.cmb_studSection, True)

        self.ui.cmb_studSection.currentIndexChanged.connect(self.handle_student_searching)

        self.ui.btnSectionAdd.clicked.connect(self.register_section)
        self.ui.btnSectionDelete.clicked.connect(self.delete_selected_sections)
        self.ui.btnSectionEdit.clicked.connect(self.section_edit)

        self.ui.btnLessonView.clicked.connect(self.view_lesson)
        self.ui.btnLessonAdd.clicked.connect(lambda: self.showLessonDialog(1))
        self.ui.btnLessonEdit.clicked.connect(lambda: self.showLessonDialog(2))
        self.ui.txtSearchLesson.textChanged.connect(lambda searchText: self.displayLessons(searchText))
        self.ui.btnRefreshLessonTable.clicked.connect(self.displayLessons)

        self.ui.txt_search_user.textChanged.connect(lambda text: self.displayUsers(text))
        self.ui.btnRefreshUsers.clicked.connect(lambda: self.displayUsers())
        self.ui.btnDeleteUser.clicked.connect(lambda: self.delete_user(user))

        self.difficulty_group = QButtonGroup(self.home_win)
        self.difficulty_group.setExclusive(True)
        self.level_map = { 1: self.ui.btnEasy, 2: self.ui.btnAverage, 3: self.ui.btnHard }

        for idx, btn in self.level_map.items():
            btn.setCheckable(True)
            self.difficulty_group.addButton(btn, idx)
            btn.clicked.connect(lambda checked, i=idx: self.handle_level_click(i))

        self.ui.btnEasy.setChecked(True)

        self.ui.quiz_no.valueChanged.connect(self.display_quiz)
        self.ui.cbGradingPeriod.currentIndexChanged.connect(self.handle_quiz_filter)
        self.ui.cbLessonName.currentIndexChanged.connect(self.cbLesson_selection_change)
        self.ui.checkBoxPublish.clicked.connect(self.save_quiz_publishing)
        self.ui.checkBoxPublish.setVisible(False)
        self.ui.btnQuizAdd.clicked.connect(self.showQuizDialog)

        self.reports_selectedRow_idv = None
        self.ui.table_student_score_idv.clicked.connect(lambda row: self.handle_report_student_click(row))
        self.ui.cb_gp_quiz_idv.currentIndexChanged.connect(lambda: self.handle_report_student_click(self.reports_selectedRow_idv))

        self.ui.btnSaveSettings_SY.clicked.connect(self.saveSchoolYear_gradingPeriod)

        #=============================================================
        #  Application-Level Privileges (Role-Based Access Control)
        #=============================================================

        role = user.get("position_name")

        if role == "Admin":
           pass
            
        elif role == "Teacher":
            self.ui.btnEditUserInfo.setVisible(False)
            self.ui.btnDeleteUser.setVisible(False)

        else:
            self.ui.btnUsers.setVisible(False)
            self.ui.btnUtility.setVisible(False)

            self.ui.btnAddStudent.setVisible(False)
            self.ui.btnLessonAdd.setVisible(False)
            self.ui.btnQuizAdd.setVisible(False)
            self.ui.btnExerciseAdd.setVisible(False)
            self.ui.btnSectionAdd.setVisible(False)

            self.ui.btnEditStudent.setVisible(False)
            self.ui.btnLessonEdit.setVisible(False)
            self.ui.btnSectionEdit.setVisible(False)
            self.ui.btnExerciseEdit.setVisible(False)

            self.ui.btnDeleteStudent.setVisible(False)
            self.ui.btnSectionDelete.setVisible(False)
            self.ui.btnDeleteUser.setVisible(False)

            self.ui.btnShowPwdStudent.setVisible(False)

        self.login_win.close()
        self.home_win.show()

    def displayDashboard(self):
        self.ui.label_lessons_total.setText(f"{Lesson().count()}")
        self.ui.label_student_total.setText(f"{Student().count()}")
        self.ui.label_teachers_total.setText(f"{Staff().count()}")

    def handle_student_searching(self):
        searchStr = self.ui.txt_classList_search.text().strip()
        self.display_student_cards(searchStr)

    def slide_to_page(self, index):
        stack = self.ui.stackedWidget
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

    def handle_nav_click(self, index):
        self.slide_to_page(index)

        if index == 0:
            self.displayDashboard()
            self.get_dynamic_school_year_dates()

        elif index == 1: # Student List
            self.sectionObj.populate_sections(self.ui.cmb_studSection, True)
            self.display_student_cards()
            self.display_student_info()

        elif index == 2: # Lesson
            self.ui.txtSearchLesson.clear()
            self.displayLessons()

        elif index == 3: # Quiz
            self.util.populate_pulldowns(self.ui.cbGradingPeriod, self.ui.cbLessonName)
            self.display_quiz()

        elif index == 5:
            self.display_section_info()

        elif index == 6: # Reports
            self.util.populate_pulldowns(self.ui.cb_gp_quiz_idv)

            stud = Student()
            new_model = stud.refresh_student_table(None)
            self.ui.table_student_score_idv.sortByColumn(-1, Qt.AscendingOrder)
            self.ui.table_quiz_score_idv.sortByColumn(-1, Qt.AscendingOrder)

            if new_model:
                self.ui.table_student_score_idv.setModel(new_model)
                header = self.ui.table_student_score_idv.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                # header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
                # header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
                self.ui.table_student_score_idv.setColumnHidden(5, True) # Hide 'Gender' column

        elif index == 7: # Users
            self.displayUsers()

        elif index == 8: # Utilities
            self.displayAuditTrail()
            self.displayArchive()
            self.get_dynamic_school_year_dates()
            self.display_grading_periods()

    def update_clock(self):
        now = QDateTime.currentDateTime()
        timeNow = now.toString("hh:mm AP")
        time, ap = timeNow.split()
        self.ui.label_day.setText(now.toString("d"))
        self.ui.label_time.setText(time)
        self.ui.label_timeAP.setText(ap)

    def logout(self):
        confirm_msg = f"Are you sure you want to log out?"
        confirm = QMessageBox.question(self.home_win, "Confirm Logout", confirm_msg,
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.No:
            return
        
        # 1. Clear the persistent session from QSettings
        self.settings.clear()
        self.settings.sync()

        # 2. Close all top-level windows (Home, Dialogs, etc.)
        # We use [:] to create a snapshot of the list to avoid iteration errors
        for widget in QApplication.topLevelWidgets()[:]:
            widget.close()

        # 3. Reset the Login Window fields (Security best practice)
        self.login_win.txtUsername.clear()
        self.login_win.txtPassword.clear()
        self.login_win.txtUsername.setFocus()

        # 4. Show the login window again
        self.login_win.show()

    def load_fonts(self):
        path = os.path.join(self.script_dir, "fonts")
        loaded_count = 0

        if os.path.exists(path):
            for f in os.listdir(path):
                if f.endswith((".ttf", ".otf")):
                    font_path = os.path.join(path, f)
                    font_id = QFontDatabase.addApplicationFont(font_path)

                    if font_id != -1:
                        loaded_count += 1
                    else:
                        print(f"❌ Failed to load font: {f}")

            if loaded_count > 0:
                print(f"✅ {loaded_count} font(s) loaded successfully.")
            else:
                print("⚠️ Font folder found, but no valid fonts were loaded.")
        else:
            print(f"⚠️ Font directory not found at: {path}")

    def add_user(self, user):

        if AddUserDialog(user).exec() == QDialog.DialogCode.Accepted:
            self.displayUsers()

    def update_user(self, user:dict, mode:int=1):
        """
        Args:
            user (dict): The current user
            mode (int): 
            1. User is updating his/her information.
            2. User is updating the information of other user.
        """

        if mode == 1:
            if EditUserDialog(user, user["school_id"], mode).exec() == QDialog.DialogCode.Accepted:
                self.logout()

        else: # mode = 2
            selection_model = self.ui.table_users.selectionModel()

            if not selection_model.hasSelection():
                QMessageBox.information(self.home_win, "No Selection", f"Select a user to update.")
                return

            selected_indices = selection_model.selectedRows()

            if selected_indices:
                row_index = selected_indices[0].row()
                model = self.ui.table_users.model()
                school_id = model.index(row_index, 1).data()

                if EditUserDialog(user, school_id, mode).exec() == QDialog.DialogCode.Accepted:
                    self.displayUsers()

    def register_student(self):
        studDialog = AddNewStudentDialog(self.script_dir)

        if studDialog.exec() == QDialog.DialogCode.Accepted:
            self.display_student_cards()

    def display_student_cards(self, text=''):
        # Ensure 'text' is always a string, defaulting to the textbox if empty
        if not text: 
            text = self.ui.txt_classList_search.text().strip()

        schoolYear = f"{self.ui.spinBox_SY1.value()}-{self.ui.spinBox_SY2.value()}"
        sectionid = self.ui.cmb_studSection.currentData()
        params = (schoolYear, sectionid, text)

        # UI Optimization: Stop painting until the loop is done
        self.ui.scrollArea_classlist.setUpdatesEnabled(False)

        try:
            # 1. Clear existing cards
            while self.card_layout.count():
                item = self.card_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.cards.clear()

            # 2. Fetch data
            stud = Student()
            students = stud.refresh_student_cards(params)

            # Update count label
            count = len(students)
            self.ui.label_totalStudCount.setText(f"{count} {'item' if count <= 1 else 'items'}")

            # 3. Add new cards
            for row in students:
                # Unpacking based on your SQL order
                sid, f_name, m_name, l_name, _, _, _, img_data = row 

                pixmap = None
                if img_data:
                    image = QImage.fromData(bytes(img_data))
                    if not image.isNull():
                        pixmap = QPixmap.fromImage(image)

                full_name = self.util.formatFullname(f_name, m_name, l_name)
                card = Card(full_name, sid, pixmap)
                card.clicked.connect(self.handle_card_selection)

                self.card_layout.addWidget(card)
                self.cards.append(card)

        finally:
            # Resume painting the UI
            self.ui.scrollArea_classlist.setUpdatesEnabled(True)

    def display_student_info(self, clicked_card=None, student_id=None):
        studDialog = AddNewStudentDialog(self.script_dir)
        total, boys, girls = studDialog.update_section_stats(student_id)
        selected_row = studDialog.refresh_student_info(student_id)
        sid = lname = fname = mname = section = gender = contact_person = contact_num = "N/A"
        self.last_selected_card = None # Reset

        if selected_row:
            sid, lname, fname, mname, section, gender, *_, contact_person, contact_num = selected_row

        # 1. Unselect the previous card
        if self.last_selected_card:
            # shiboken.isValid(obj) checks if the C++ object still exists
            if isValid(self.last_selected_card):
                self.last_selected_card.set_selected(False)
            else:
                # If it's gone, clear the reference
                self.last_selected_card = None

        # 2. Select the new card
        if clicked_card:
            clicked_card.set_selected(True)
            self.last_selected_card = clicked_card

        self.ui.label_section.setText(section)
        self.ui.label_studentCount.setText(f"{total}")
        self.ui.label_boyCount.setText(f"{boys}")
        self.ui.label_girlCount.setText(f"{girls}")

        self.ui.label_studentId.setText(f"{sid}")
        self.ui.label_studentLastName.setText(f"{lname}")
        self.ui.label_studentFirstName.setText(f"{fname}")
        self.ui.label_studentMiddleName.setText(f"{mname}")
        self.ui.label_studentGender.setText(f"{gender}")

        self.ui.label_contact_person.setText(f"{contact_person}")
        self.ui.label_contact_number.setText(f"{contact_num}")

        # if not self.util.isEmpty(sid):
        #     layout = self.ui.verticalLayout_14
        #     layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        #     layout.setSpacing(10)

        #     while layout.count():
        #         item = layout.takeAt(0)
        #         widget = item.widget()
        #         if widget:
        #             widget.deleteLater()

        #     student = Student()
        #     progressBar = student.get_student_progress(sid, 1)
        #     progressBar.setFixedSize(120, 120)

        #     layout.addWidget(progressBar)

    def edit_student(self, user):
        student_id = self.ui.label_studentId.text().strip()
        if self.util.isEmpty(student_id):
            QMessageBox.warning(None, "Warning", f"Select a student to update the information.")
            return

        editor = StudentEditorDialog(user, student_id)
        if editor.exec() == QDialog.DialogCode.Accepted:
            self.display_student_cards()
            QMessageBox.information(editor, "Updated", f"Student {student_id} information has been updated.")

    def delete_student(self, user):
        # Gather all selected student IDs
        selected_ids = [card.label_studentid.text() for card in self.cards if card.property("selected")]

        if not selected_ids:
            QMessageBox.warning(None, "Warning", "Please select at least one student card to delete.")
            return

        # Confirm deletion with the user
        count = len(selected_ids)
        confirm_msg = f"Are you sure you want to delete {count} selected student(s)?"
        confirm = QMessageBox.question(None, "Confirm Delete", confirm_msg,
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes:
            stud = Student()

            # Pass the list (converted to tuple) to your DB method
            if stud.delete_student(tuple(selected_ids), user):
                self.display_student_cards()
                self.display_student_info() # Reset labels
                QMessageBox.information(None, "Deleted", f"Successfully removed {count} students.")
            else:
                QMessageBox.warning(None, "Error", "Could not delete students from the database.")

    def register_section(self):
        self.sectionObj.txtSectionName.clear()
        self.sectionObj.cmb_teacher.setCurrentIndex(0)

        if self.sectionObj.exec() == QDialog.DialogCode.Accepted:
            self.sectionObj.populate_sections(self.ui.comboBox_Section, False)
            self.display_section_info()

    def display_section_info(self):
        section_id = self.ui.comboBox_Section.currentData()

        if section_id:
            stud = Student()
            new_model = stud.refresh_student_table(section_id)

            if new_model:
                self.ui.table_section.setModel(new_model)

        else:
            self.ui.table_section.setModel(QStandardItemModel())

        self.ui.table_section.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        class_adviser = self.sectionObj.get_adviser(section_id)
        self.ui.label_Adviser.setText(class_adviser)

    def delete_selected_sections(self):
        sectionId = self.ui.comboBox_Section.currentData()
        sectionName = self.ui.comboBox_Section.currentText()
        dialog = QMessageBox.warning(None, "Delete Section", 
                             f"Deleting ({sectionName}) section will also remove all associated students.",
                             QMessageBox.Ok | QMessageBox.Cancel)

        if dialog == QMessageBox.Ok:
            self.sectionObj.delete_section(sectionId, sectionName)
            self.sectionObj.populate_sections(self.ui.comboBox_Section, False)
            self.display_section_info()

    def section_edit(self):
        from App.SectionDialog import SectionAdviserEditor
        sectionEditor = SectionAdviserEditor(self.sectionObj)

        sectionEditor.exec()

        section_id = self.ui.comboBox_Section.currentData()
        class_adviser = self.sectionObj.get_adviser(section_id)
        self.ui.label_Adviser.setText(class_adviser)

    def handle_card_selection(self, clicked_card, student_id):
        # Check if the Control key is currently held down
        modifiers = QGuiApplication.keyboardModifiers()
        is_ctrl_pressed = modifiers == Qt.KeyboardModifier.ControlModifier

        if is_ctrl_pressed:
            # Toggle selection for the clicked card (Multi-select mode)
            current_state = clicked_card.property("selected")
            clicked_card.set_selected(not current_state)
        else:
            # Single select mode: Unselect all other cards first
            for card in self.cards:
                if card != clicked_card:
                    card.set_selected(False)
            # Select the clicked card
            clicked_card.set_selected(True)

        # Always update the info panel with the most recent click
        self.display_student_info(clicked_card, student_id)

    def displayLessons(self, searchText:str=""):
        lesson = Lesson()
        model = lesson.retrieve_lessons_table(searchText)

        if model:
            self.ui.table_lesson.setModel(model)
            self.ui.table_lesson.setColumnHidden(0, True)
            header = self.ui.table_lesson.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
            self.ui.table_lesson.verticalHeader().setVisible(False)
            self.ui.table_lesson.sortByColumn(-1, Qt.AscendingOrder)

            suffix = "item" if model.rowCount() <= 1 else "items"
            self.ui.label_lessonTotalCount.setText(f"{model.rowCount()} {suffix}")

    def cbLesson_selection_change(self):
        self.display_quiz()

        if self.ui.label_totalScore.text() in ['', '0', '000']:
            self.ui.checkBoxPublish.setVisible(False)

        else:
            self.ui.checkBoxPublish.setVisible(True)

    def showLessonDialog(self, mode):
        """mode: 1 Add, 2 Edit"""
        lesson_id = None

        if mode == 2:
            selection = self.ui.table_lesson.selectionModel()
            if selection.hasSelection():
                row_index = selection.selectedRows()[0]
                lesson_id = self.ui.table_lesson.model().data(row_index)

            if not lesson_id:
                QMessageBox.information(self.ui.table_lesson.window(), "No Selection", f"Select a lesson to update.")
                return

        lessonDialog = LessonDialog(mode, lesson_id)

        if lessonDialog.exec() == QDialog.DialogCode.Accepted:
            self.displayLessons() # Refresh the main table

    def showQuizDialog(self):
        from App.Quiz import QuizCreatorDialog

        q_num = self.ui.quiz_no.value()
        g_period = self.ui.cbGradingPeriod.currentData()
        lesson_id = self.ui.cbLessonName.currentData()
        diff_level = self.difficulty_group.checkedId()

        quiz = QuizCreatorDialog(q_num, g_period, lesson_id, diff_level)

        if quiz.exec() == QDialog.DialogCode.Accepted:
            self.display_quiz()

    def handle_quiz_filter(self):
        self.ui.cbLessonName.clear()
        selected_period = self.ui.cbGradingPeriod.currentData()

        if selected_period:
            sql = 'SELECT\n'
            sql += '    lesson_id\n'
            sql += '    ,title\n'
            sql += 'FROM cai.tbl_lessons\n'
            sql += 'WHERE gradingperiod = %s\n'
            sql += 'ORDER BY chapter, lessonnum ASC'
            self.util.populate_pulldown(self.ui.cbLessonName, sql, params=(selected_period,), add_empty=True)

        self.display_quiz()

    def display_quiz(self):
        from App.Quiz import Quiz, CardQuiz
        quiz = Quiz()

        q_num = self.ui.quiz_no.value()
        g_period = self.ui.cbGradingPeriod.currentData()
        lesson_id = self.ui.cbLessonName.currentData()
        diff_level = self.difficulty_group.checkedId()

        record_id, record_mc, record_tf, quiz_record, multipliers, scores = quiz.retrieve_quiz(q_num, g_period, lesson_id, diff_level)
        _, publish = quiz_record
        easy_score, average_score, hard_score, total_score = scores

        self.ui.label_totalScore.setText(f"{total_score}")
        score_per_level = ""

        match diff_level:
            case 1:
                score_per_level = f"{easy_score}"
            case 2:
                score_per_level = f"{average_score}"
            case 3:
                score_per_level = f"{hard_score}"

        self.ui.label_scoreperlevel.setText(score_per_level)
        self.ui.checkBoxPublish.setChecked(publish)

        self.ui.multiplier_easy.setText('1')
        self.ui.multiplier_average.setText('1')
        self.ui.multiplier_hard.setText('1')

        if multipliers:
            self.ui.multiplier_easy.setText(f'{multipliers[4]}')
            self.ui.multiplier_average.setText(f'{multipliers[5]}')
            self.ui.multiplier_hard.setText(f'{multipliers[6]}')

        layout_id = self.ui.verticalLayout_11
        layout_mc = self.ui.verticalLayout_12
        layout_tf = self.ui.verticalLayout_13

        for layout in [layout_id, layout_mc, layout_tf]:
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            layout.setSpacing(5)

        self.clear_layout(layout_id)
        self.clear_layout(layout_mc)
        self.clear_layout(layout_tf)

        for row in record_id:
            card = CardQuiz("Identification")
            card.idKey = row["idkey"]
            card.itemno = row["itemno"]
            card.question = row["question"]
            card.answer = row["correct_answer"]
            card.imageQ = row["imagequestion"]
            card.displayAttributes()

            layout_id.addWidget(card)

        for row in record_mc:
            card = CardQuiz("Mutiple Choice")
            card.idKey = row["mckey"]
            card.itemno = row["itemno"]
            card.question = row["question"]
            card.choices = f"A. {row["choice_a"]} | B. {row["choice_b"]} | C. {row["choice_c"]}"
            card.answer = row["correct_answer"]
            card.imageQ = row["imagequestion"]
            card.displayAttributes()

            layout_mc.addWidget(card)

        for row in record_tf:
            card = CardQuiz("True or False")
            card.idKey = row["tfkey"]
            card.itemno = row["itemno"]
            card.question = row["question"]
            card.answer = row["correct_answer"]
            card.imageQ = row["imagequestion"]
            card.displayAttributes()

            layout_tf.addWidget(card)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if widget := item.widget():
                widget.deleteLater()

    def handle_level_click(self, idx):
        self.display_quiz()

    def save_quiz_publishing(self, checked):
        lessonId = self.ui.cbLessonName.currentData()

        if self.ui.label_totalScore.text() == "0" or not lessonId:
            return

        try:

            sql = """
                UPDATE cai.tbl_quiz
                SET PUBLISH = CASE 
                    WHEN quiznumber = %s AND gradingperiod = %s AND lessonid = %s THEN %s
                    ELSE false
                END;
            """

            self.db_tools.execute_query(sql, (self.ui.quiz_no.value(), self.ui.cbGradingPeriod.currentData(), lessonId, checked))

            if checked:
                QMessageBox.information(self.home_win, "Publishing", "This quiz is published. Students can see this.")
            else:
                QMessageBox.information(self.home_win, "Publishing", "This quiz is unpublished. Students cannot see this.")

        except Exception as e:
            print(f"Error saving to database: {e}")

    def displayUsers(self, text:str = ''):
        staff = Staff()
        model = staff.get_user_model(text)

        if model:
            self.ui.table_users.setModel(model)

            header = self.ui.table_users.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def delete_user(self, user):
        selection = self.ui.table_users.selectionModel()

        if not selection.hasSelection():
            QMessageBox.information(self.ui.table_users.window(), "No Selection", "Select a user to delete.")
            return

        # Get the index of the first selected row
        selected_row_index = selection.selectedRows()[0].row()
        model = self.ui.table_users.model()
        school_id = model.index(selected_row_index, 1).data()
        staff = Staff()
        staff.archive_and_delete_staff(user, school_id)
        self.displayUsers()

    def displayAuditTrail(self):
        sql  = 'SELECT\n'
        sql += '    user_id AS "User Id",\n'
        sql += '    username AS "User Name",\n'
        sql += '    TO_CHAR(date_logged, \'YYYY/MM/DD, HH12:MI AM\') AS "Date Logged",\n'
        sql += '    action AS "Action"\n'
        sql += 'FROM cai.tbl_audit_trail\n'
        sql += 'ORDER BY date_logged DESC'
        cursor, conn = self.db_tools.retrieve_records(sql)

        if cursor:
            headers = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
            model = QStandardItemModel(len(records), len(headers))
            model.setHorizontalHeaderLabels(headers)

            for row_idx, row_data in enumerate(records):

                for col_idx, value in enumerate(row_data):
                    item = QStandardItem(str(value) if value is not None else "")
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    model.setItem(row_idx, col_idx, item)

            cursor.close()
            conn.close()

            self.ui.table_AuditTrail.setModel(model)
            self.ui.table_AuditTrail.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        if conn: conn.close()

    def displayArchive(self):
        sql = """
            SELECT
                school_year AS "School Year",
                studentid AS "Student ID",
                lastname AS "Last Name",
                firstname AS "First Name",
                middlename AS "Middle Name",
                sectionid AS "Section ID",
                gender AS "Gender",
                contact_person AS "Contact Person",
                contact_number AS "Contact Number",
                TO_CHAR(archived_at, 'YYYY/MM/DD, HH12:MI AM') AS "Date Archived",
                archived_by AS "Archived By"
            FROM cai.TBL_STUDENT_INFO_ARCHIVE
            ORDER BY archived_at DESC
        """
        cursor, conn = self.db_tools.retrieve_records(sql)

        if cursor:
            headers = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
            model = QStandardItemModel(len(records), len(headers))
            model.setHorizontalHeaderLabels(headers)

            for row_idx, row_data in enumerate(records):

                for col_idx, value in enumerate(row_data):
                    item = QStandardItem(str(value) if value is not None else "")
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    model.setItem(row_idx, col_idx, item)

            cursor.close()
            conn.close()

            self.ui.table_student_archive.setModel(model)
            self.ui.table_student_archive.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        if conn: conn.close()

    def view_lesson(self):
        selection = self.ui.table_lesson.selectionModel()

        if not selection.hasSelection():
            QMessageBox.information(self.ui.table_lesson.window(), "No Selection", "Select a lesson to view.")
            return

        # Get the index of the first selected row
        selected_row_index = selection.selectedRows()[0].row()
        model = self.ui.table_lesson.model()

        # Column 0 is lesson_id (Hidden), Column 2 is Lesson Title
        lesson_id = model.index(selected_row_index, 0).data()
        lesson_title = model.index(selected_row_index, 2).data()

        if not lesson_id:
            return

        lesson_obj = Lesson()
        # Unpack the 8-tuple from retrieve_lesson_info method
        info = lesson_obj.retrieve_lesson_info(lesson_id)
        path_str = info[5] # path_str is the 6th element

        if path_str:
            file_to_open = lesson_obj.get_absolute_lesson_path(path_str)
            
            if file_to_open.exists():
                from App.Tools import WickPlayer 
                self.lesson_window = WickPlayer(str(file_to_open))
                self.lesson_window.show()
            else:
                QMessageBox.warning(self.ui.table_lesson.window(), "File Not Found", 
                                    f"The file does not exist at:\n{file_to_open}")
        else:
            QMessageBox.warning(self.ui.table_lesson.window(), "Missing Path", 
                                f"No file path associated with: {lesson_title}")
            
    def handle_report_student_click(self, row=None):
        if row is not None:
            self.reports_selectedRow_idv = row

        if row == None:
            return
        
        row = self.reports_selectedRow_idv
        gradingperiod = self.ui.cb_gp_quiz_idv.currentData()
        studentId = row.siblingAtColumn(0).data()
        lastName = row.siblingAtColumn(1).data()
        firstName = row.siblingAtColumn(2).data()
        middleName = row.siblingAtColumn(3).data()
        stud_name = self.util.formatFullname(firstName, middleName, lastName)
        self.ui.label_student_name.setText(stud_name)

        stud = Student()
        s = self.ui.label_student_icon.width()
        pixmap = stud.get_student_picture(studentId, True, s)
        self.ui.label_student_icon.setPixmap(pixmap)

        from App.Quiz import Quiz
        quiz = Quiz()
        model, average_percentage = quiz.get_scores(studentId, gradingperiod)

        if model:
            self.ui.table_quiz_score_idv.setModel(model)
            self.ui.table_quiz_score_idv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.ui.table_quiz_score_idv.sortByColumn(-1, Qt.AscendingOrder)

        self.ui.label_average_percentage.setText(f'{average_percentage:.0f}%')

    def get_dynamic_school_year_dates(self):
        today = QDate.currentDate()
        current_year = today.year()
        current_month = today.month()
        
        # If today is between Jan and May, the next school year begins in June of THIS year.
        # If today is between June and Dec, the next school year begins in June of NEXT year.
        if current_month < 6:
            base_year = current_year
        else:
            base_year = current_year + 1
            
        next_year = base_year + 1

        self.ui.label_SY.setText(f"School Year {base_year}-{next_year}")
        self.ui.spinBox_SY_start.setValue(base_year)
        self.ui.spinBox_SY_end.setValue(next_year)

        self.ui.spinBox_SY1.setValue(base_year)
        self.ui.spinBox_SY2.setValue(next_year)
        
        # Generate the exact 4-Quarter DepEd standard milestones dynamically
        quarters = {
            1: {"start": f"{base_year}-06-16", "end": f"{base_year}-08-22"},
            2: {"start": f"{base_year}-08-26", "end": f"{base_year}-10-24"},
            3: {"start": f"{base_year}-11-03", "end": f"{next_year}-01-23"},
            4: {"start": f"{next_year}-01-26", "end": f"{next_year}-03-20"}
        }

        # Determine and display the active grading period
        active_quarter = "Off-season / Break"
        is_break = True

        for q_num, dates in quarters.items():
            start_date = QDate.fromString(dates["start"], "yyyy-MM-dd")
            end_date = QDate.fromString(dates["end"], "yyyy-MM-dd")
            
            if start_date <= today <= end_date:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(q_num, "th")
                active_quarter = f"{q_num}{suffix} Grading Period"
                is_break = False
                break
                
        self.ui.label_gradingperiod.setText(active_quarter)

        qss = 'font: 10pt "Inter Medium"; border-radius: 12px; padding: 0px 10px 0px;'

        if is_break:
            qss += 'background-color: #E5254B; color: white;'
            self.ui.label_gradingperiod.setStyleSheet(qss)
        else:
            qss += 'background-color: #038100; color: white;'
            self.ui.label_gradingperiod.setStyleSheet(qss)
        
        return quarters

    def saveSchoolYear_gradingPeriod(self):
        schedule = self.get_dynamic_school_year_dates()
        sql = ""
        params = []
        
        for gpid, dates in schedule.items():
            sql += """
                UPDATE cai.tbl_grading_period 
                SET startdate = %s, enddate = %s
                WHERE gpid = %s;
            """
            params.extend([dates["start"], dates["end"], gpid])

        if sql:
            self.db_tools.execute_query(sql, tuple(params))

    def display_grading_periods(self):
        sql = """
            SELECT gpid, gpname, startdate, enddate
	        FROM cai.tbl_grading_period;
        """

        rows = self.db_tools.fetch_all(sql)

        if rows:
            for row in rows:
                start = QDate.fromString(str(row['startdate']), "yyyy-MM-dd")
                end = QDate.fromString(str(row['enddate']), "yyyy-MM-dd")

                if row['gpid'] == 1:
                    self.ui.dateEdit_firstgrading_start.setDate(start)
                    self.ui.dateEdit_firstgrading_end.setDate(end)

                elif row['gpid'] == 2:
                    self.ui.dateEdit_secondgrading_start.setDate(start)
                    self.ui.dateEdit_secondgrading_end.setDate(end)

                elif row['gpid'] == 3:
                    self.ui.dateEdit_thirdgrading_start.setDate(start)
                    self.ui.dateEdit_thirdgrading_end.setDate(end)

                else:
                    self.ui.dateEdit_fourthgrading_start.setDate(start)
                    self.ui.dateEdit_fourthgrading_end.setDate(end)
    
