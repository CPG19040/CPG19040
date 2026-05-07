import os

# PyQt Imports
from PySide6.QtCore import QSettings, QTimer, QDateTime, QPoint, QEasingCurve, QPropertyAnimation, QParallelAnimationGroup, Qt, QDate
from PySide6.QtWidgets import QMainWindow, QHeaderView, QDialog, QVBoxLayout, QWidget, QMessageBox, QApplication, QButtonGroup
from PySide6.QtGui import QFontDatabase, QImage, QPixmap, QGuiApplication, QStandardItemModel, QStandardItem
from shiboken6 import isValid

# Core App Logic/Main Windows
from App.FormHome import Ui_Home
from App.Login import Login
from App.Tools import Card, Utility

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
        self.displaySchoolYear()

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

        self.ui.btnRefreshSY.clicked.connect(self.displaySchoolYear)
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

        self.difficulty_group = QButtonGroup(self.home_win)
        self.difficulty_group.setExclusive(True)
        self.level_map = { 1: self.ui.btnEasy, 2: self.ui.btnAverage, 3: self.ui.btnHard }

        for idx, btn in self.level_map.items():
            btn.setCheckable(True)
            self.difficulty_group.addButton(btn, idx)
            btn.clicked.connect(lambda checked, i=idx: self.handle_level_click(i))

        self.ui.btnEasy.setChecked(True)

        self.ui.quiz_no.valueChanged.connect(self.display_quiz)
        self.ui.cbGradingPeriod.currentIndexChanged.connect(self.display_quiz)
        self.ui.cbLessonName.currentIndexChanged.connect(self.cbLesson_selection_change)
        self.ui.checkBoxLockQuiz.clicked.connect(self.save_quiz_lock_status)
        self.ui.checkBoxLockQuiz.setVisible(False)
        self.ui.btnQuizAdd.clicked.connect(self.showQuizDialog)

        self.login_win.close()
        self.home_win.show()

    def displaySchoolYear(self):
        current_date = QDate.currentDate()
        current_year = current_date.year()
        self.ui.spinBox_SY1.setValue(current_year)
        self.ui.spinBox_SY2.setValue(current_year + 1)

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

        if index == 1: # Student List
            self.sectionObj.populate_sections(self.ui.cmb_studSection, True)
            self.display_student_cards()
            self.display_student_info()

        elif index == 2: # Lesson
            self.displayLessons()

        elif index == 3: # Quiz
            sql =  "SELECT 1 AS index, 'First Grading' AS itemname\n"
            sql += "UNION ALL\n"
            sql += "SELECT 2, 'Second Grading'\n"
            sql += "UNION ALL\n"
            sql += "SELECT 3, 'Third Grading'\n"
            sql += "UNION ALL\n"
            sql += "SELECT 4, 'Fourth Grading'\n"
            self.util.populate_pulldown(self.ui.cbGradingPeriod, sql)

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

        elif index == 5:
            self.display_section_info()

        elif index == 7:
            self.displayUsers()

        elif index == 8:
            self.displayAuditTrail()
            self.displayArchive()

    def update_clock(self):
        now = QDateTime.currentDateTime()
        timeNow = now.toString("hh:mm AP")
        time, ap = timeNow.split()
        self.ui.label_day.setText(now.toString("d"))
        self.ui.label_time.setText(time)
        self.ui.label_timeAP.setText(ap)

    def logout(self):
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
        self.ui.scrollArea.setUpdatesEnabled(False)

        try:
            # 1. Clear existing cards
            while self.card_layout.count():
                item = self.card_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.cards.clear()

            # 2. Fetch data
            studDialog = AddNewStudentDialog(self.script_dir)
            students = studDialog.refresh_student_cards(params)

            # Update count label
            count = len(students)
            self.ui.label_totalStudCount.setText(f"{count} {'item' if count == 1 else 'items'}")

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
            self.ui.scrollArea.setUpdatesEnabled(True)

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
            studDialog = AddNewStudentDialog(self.script_dir)
            new_model = studDialog.refresh_student_table(section_id)

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

    def cbLesson_selection_change(self):
        self.display_quiz()

        if self.ui.label_totalScore.text() == "0":
            self.ui.checkBoxLockQuiz.setVisible(False)

        else:
            self.ui.checkBoxLockQuiz.setVisible(True)

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

    def display_quiz(self):
        from App.Quiz import Quiz, CardQuiz
        quiz = Quiz()

        q_num = self.ui.quiz_no.value()
        g_period = self.ui.cbGradingPeriod.currentData()
        lesson_id = self.ui.cbLessonName.currentData()
        diff_level = self.difficulty_group.checkedId()

        record_id, record_mc, record_tf, quiz_record, multipliers = quiz.retrieve_quiz(q_num, g_period, lesson_id, diff_level)
        total_items, quizlock = quiz_record

        self.ui.label_totalScore.setText(f"{total_items}")
        self.ui.checkBoxLockQuiz.setChecked(quizlock)

        self.ui.multiplier_easy.setValue(1)
        self.ui.multiplier_average.setValue(1)
        self.ui.multiplier_hard.setValue(1)

        if multipliers:
            self.ui.multiplier_easy.setValue(multipliers[4])
            self.ui.multiplier_average.setValue(multipliers[5])
            self.ui.multiplier_hard.setValue(multipliers[6])

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
            card.answer = row["correct_answer_1"]
            card.imageQ = row["imagequestion"]
            card.setAttributes()

            layout_id.addWidget(card)

        for row in record_mc:
            card = CardQuiz("Mutiple Choice")
            card.idKey = row["mckey"]
            card.itemno = row["itemno"]
            card.question = row["question"]
            card.answer = f"A. {row["choice_a"]} | B. {row["choice_b"]} | C. {row["choice_c"]}\nCorrect: {row["correct_answer"]}"
            card.imageQ = row["imagequestion"]
            card.setAttributes()

            layout_mc.addWidget(card)

        for row in record_tf:
            card = CardQuiz("True or False")
            card.idKey = row["tfkey"]
            card.itemno = row["itemno"]
            card.question = row["question"]
            card.answer = row["correct_answer"]
            card.imageQ = row["imagequestion"]
            card.setAttributes()

            layout_tf.addWidget(card)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if widget := item.widget():
                widget.deleteLater()

    def handle_level_click(self, idx):
        self.display_quiz()

    def save_quiz_lock_status(self, checked):
        lessonId = self.ui.cbLessonName.currentData()

        if self.ui.label_totalScore.text() == "0" or not lessonId:
            return

        from App.CRUDTools import DatabaseTools
        db_tools = DatabaseTools()

        try:

            sql  = "UPDATE cai.tbl_quiz\n"
            sql += "    SET QUIZLOCK = %s\n"
            sql += "WHERE quiznumber = %s\n"
            sql += "    AND gradingperiod = %s\n"
            sql += "    AND lessonid = %s"

            db_tools.execute_query(sql, (checked, self.ui.quiz_no.value(), self.ui.cbGradingPeriod.currentData(), lessonId))

            if checked:
                QMessageBox.information(self.home_win, "Publishing", "This quiz is locked. Students cannot see this.")
            else:
                QMessageBox.information(self.home_win, "Publishing", "This quiz is unlocked. Students can see this.")

        except Exception as e:
            print(f"Error saving to database: {e}")

    def displayUsers(self, text:str = ''):
        staff = Staff()
        model = staff.get_user_model(text)

        if model:
            self.ui.table_users.setModel(model)

            header = self.ui.table_users.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def displayAuditTrail(self):
        from App.CRUDTools import DatabaseTools
        db_tools = DatabaseTools()

        sql  = 'SELECT\n'
        sql += '    user_id AS "User Id",\n'
        sql += '    username AS "User Name",\n'
        sql += '    TO_CHAR(date_logged, \'Mon DD, YYYY, HH12:MI AM\') AS "Date Logged",\n'
        sql += '    action AS "Action"\n'
        sql += 'FROM cai.tbl_audit_trail\n'
        sql += 'ORDER BY date_logged DESC'
        cursor, conn = db_tools.retrieve_records(sql)

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
        from App.CRUDTools import DatabaseTools
        db_tools = DatabaseTools()

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
                TO_CHAR(archived_at, \'Mon DD, YYYY, HH12:MI AM\') AS "Date Archived",
                archived_by AS "Archived By"
            FROM cai.TBL_STUDENT_INFO_ARCHIVE
            ORDER BY archived_at DESC
        """
        cursor, conn = db_tools.retrieve_records(sql)

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

    
