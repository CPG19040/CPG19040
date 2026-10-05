import csv
from passlib.hash import bcrypt
from pathlib import Path

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QHeaderView, QComboBox, QFileDialog

from App.CRUDTools import DatabaseTools
from App.Tools import CustomMessageBox, Utility
from App.FormSectionRegistration import Ui_SectionRegistrationDialog
from App.FormSectionAdviserEditor import Ui_SectionAdviserEditorDialog

class Section(QDialog, Ui_SectionRegistrationDialog):
    RESIZE_MARGIN = 8  # The clickable area around the edges (in pixels)

    def __init__(self, user):
        super().__init__()
        self.setupUi(self)

        # Remove OS default window frame
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setMouseTracking(True)

        self.user     = user
        self.utility  = Utility()
        self.db_tools = DatabaseTools()

        self.progressBar.setVisible(False)
        _, self.base_year, self.next_year = self.utility.get_dynamic_school_year_dates()
        self.label_sy.setText(f"School Year: {self.base_year} - {self.next_year}")
        self.txtCSVPath.clear()
        self.widget_CSV.setEnabled(False)
        self.widget_template.setEnabled(False)

        self.populate_teachers(self.cmb_teacher, None, True)
        self.btnExportTemplate.clicked.connect(lambda: self.utility.export_classlist_template(parent=self))
        self.rb_importCSV.toggled.connect(lambda checked: self.update_state(not checked))
        self.btnBrowseCSV.clicked.connect(self.browse_csv)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnClose.clicked.connect(self.reject)
        self.btnSave.clicked.connect(self.register)
        self.btnCancel.clicked.connect(self.reject)

    def _get_resize_edge(self, pos):
        """Determine which edge or corner the mouse is over based on RESIZE_MARGIN."""
        rect = self.rect()
        x, y = pos.x(), pos.y()
        w, h = rect.width(), rect.height()
        
        edge = None
        
        # Horizontal edges
        if x <= self.RESIZE_MARGIN:
            edge = Qt.Edge.LeftEdge
        elif x >= w - self.RESIZE_MARGIN:
            edge = Qt.Edge.RightEdge
            
        # Vertical edges
        if y <= self.RESIZE_MARGIN:
            if edge is None:
                edge = Qt.Edge.TopEdge
            else:
                edge |= Qt.Edge.TopEdge
        elif y >= h - self.RESIZE_MARGIN:
            if edge is None:
                edge = Qt.Edge.BottomEdge
            else:
                edge |= Qt.Edge.BottomEdge
                
        return edge

    def _update_cursor_shape(self, edge):
        """Update cursor appearance depending on the active resize edge/corner."""
        if edge == (Qt.Edge.TopEdge | Qt.Edge.LeftEdge) or edge == (Qt.Edge.BottomEdge | Qt.Edge.RightEdge):
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif edge == (Qt.Edge.TopEdge | Qt.Edge.RightEdge) or edge == (Qt.Edge.BottomEdge | Qt.Edge.LeftEdge):
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif edge and (edge & (Qt.Edge.LeftEdge | Qt.Edge.RightEdge)) and not (edge & (Qt.Edge.TopEdge | Qt.Edge.BottomEdge)):
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif edge and (edge & (Qt.Edge.TopEdge | Qt.Edge.BottomEdge)) and not (edge & (Qt.Edge.LeftEdge | Qt.Edge.RightEdge)):
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint()
        edge = self._get_resize_edge(pos)
        self._update_cursor_shape(edge)
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            edge = self._get_resize_edge(pos)
            
            # 1. If clicking near any edge/corner, resize the window
            if edge:
                self.windowHandle().startSystemResize(edge)
                event.accept()
                return

            # 2. If clicking inside the custom header, move the window
            if self.frame_header.geometry().contains(pos):
                self.windowHandle().startSystemMove()
                event.accept()
                return
            
        super().mousePressEvent(event)

    def get_adviser(self, sectionid=None):
        sql = """
            SELECT 
                B.school_id, B.lastname || ', ' || B.firstname || ' ' || B.middlename AS class_advisor
            FROM cai.tbl_section A
            INNER JOIN cai.tbl_staff_info B ON A.teacherid = B.school_id
            WHERE A.sectionid = %s
        """

        cursor, conn = self.db_tools.retrieve_records(sql, (sectionid,))
        class_advisor = (None, None)

        if cursor:
            record = cursor.fetchone()

            if record:
                class_advisor = record

            cursor.close()

        if conn: conn.close()
        return class_advisor

    def update_state(self, checked):
        self.widget_CSV.setEnabled(not checked)
        self.widget_template.setEnabled(not checked)

    def browse_csv(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()

            if selected_files:
                self.txtCSVPath.setText(selected_files[0])

    def import_from_csv(self, csv_path, sectionid):

        if not sectionid:
            CustomMessageBox.warning(self, "Validation Failed", "Please select a section.")
            return 1

        if not csv_path:
            CustomMessageBox.warning(self, "Validation Failed", "Please select a CSV file.")
            return 1

        if not Path(csv_path).exists():
            CustomMessageBox.warning(self, "Validation Failed", f"{csv_path}\n\nThe path does not exist.")
            return 1

        self.progressBar.setVisible(True)

        with open(csv_path, mode='r', encoding='utf-8') as f:
            total_rows = sum(1 for line in f) - 1 # Subtract 1 for header

        self.progressBar.setMaximum(total_rows)
        self.progressBar.setValue(0)

        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            query = """
                INSERT INTO cai.tbl_student_info (
                    school_year
                    ,studentid
                    ,lastname
                    ,firstname
                    ,middlename
                    ,sectionid
                    ,password
                    ,gender
                    ,contact_person
                    ,contact_number
                )
                VALUES (%s,
                    to_char(CURRENT_DATE, 'YYYY') || '-' || lpad(nextval('cai.student_id_seq')::text, 4, '0') || '-STU',
                    %s, %s, %s, %s, %s, %s, %s, %s);
            """

            skip_all         = False
            no_all           = False
            skipped_students = []

            for i, row in enumerate(reader, 1):
                name = f"{row['LAST NAME']}, {row['FIRST NAME']} {row['MIDDLE NAME']}"

                if not no_all and self.check_duplicate_student(row['LAST NAME'], row['FIRST NAME'], row['MIDDLE NAME']):
                   
                    if not skip_all:
                        dlg_res = CustomMessageBox.question(
                            self,
                            "Duplicate Entry",
                            f"Student {name} already exists. Do you want to skip it?",
                            include_all=True
                        )
                    
                        if dlg_res == CustomMessageBox.Yes:
                            skipped_students.append(name)
                            self.progressBar.setValue(i)
                            continue

                        elif dlg_res == CustomMessageBox.YesToAll:
                            skip_all = True
                            skipped_students.append(name)
                            self.progressBar.setValue(i)
                            continue

                        elif dlg_res == CustomMessageBox.NoToAll:
                            no_all = True

                    elif skip_all:
                        skipped_students.append(name)
                        self.progressBar.setValue(i)
                        continue

                self.db_tools.execute_query(query, (
                    f"{self.base_year}-{self.next_year}",
                    row['LAST NAME'],
                    row['FIRST NAME'],
                    row['MIDDLE NAME'],
                    sectionid,
                    bcrypt.hash(row['PASSWORD']),
                    self.utility.validate_gender(row['GENDER']),
                    row['CONTACT PERSON'],
                    row['CONTACT NUMBER']
                    )
                )

                self.progressBar.setValue(i)

        if skipped_students:
            skipped_list = "\n".join(skipped_students)
            CustomMessageBox.information(self, "Skipped Students", f"The following students were skipped due to duplicates:\n\n{skipped_list}")

        return 0

    def check_duplicate_student(self, last_name, first_name, middle_name):
        existing_student = self.db_tools.fetch_all(
            """
                SELECT studentid FROM cai.tbl_student_info
                WHERE UPPER(lastname) = UPPER(%s) 
                    AND UPPER(firstname) = UPPER(%s) 
                    AND UPPER(middlename) = UPPER(%s)
            """,
            (last_name, first_name, middle_name)
        )

        if existing_student:
            return True

        return False

    def register(self):
        section_name = self.txtSectionName.text().strip()
        teacher_id = self.cmb_teacher.currentData()
        is_importing = self.rb_importCSV.isChecked()
        csv_path = self.txtCSVPath.text().strip()

        if not section_name:
            CustomMessageBox.warning(self, "Input Error", "Please enter a section name.")
            return

        if is_importing and not csv_path:
            CustomMessageBox.warning(self, "Input Error", "Please select a CSV file to import.")
            return

        conn = None
        try:
            conn = self.db_tools.get_connection()
            conn.autocommit = False 
            
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT sectionid FROM cai.tbl_section WHERE UPPER(sectionname) = UPPER(%s)", 
                    (section_name,)
                )
                row = cur.fetchone()

                if row and row[0]:
                    if not is_importing:
                        CustomMessageBox.warning(self, "Duplicate Entry", f"Section '{section_name}' already exists.")
                        return
                    else:
                        new_id = row[0]
                else:
                    cur.execute(
                        "INSERT INTO cai.tbl_section (sectionname, teacherid) VALUES (%s, %s) RETURNING sectionid", 
                        (section_name, teacher_id)
                    )
                    new_id = cur.fetchone()[0]

                if is_importing:
                    ret = self.import_from_csv(csv_path, new_id)
                    if ret != 0:
                        raise Exception("Failed to import students from the CSV file.")
                    self.progressBar.setVisible(False)

                action_str = f"Registered/Updated section: {section_name} (ID: {new_id})"
                audit_sql = """
                    INSERT INTO cai.tbl_audit_trail (user_id, username, action) 
                    VALUES (%s, %s, %s)
                """
                cur.execute(audit_sql, (self.user["school_id"], self.user["username"], action_str))

            conn.commit()
            CustomMessageBox.success(self, "Success", f"Section '{section_name}' processed successfully.")
            self.refresh_section_table()
            self.accept()

        except Exception as e:
            # Rollback transaction on failure
            if conn:
                try:
                    conn.rollback()
                except Exception:
                    pass
            CustomMessageBox.critical(self, "Database Error", f"An error occurred: {str(e)}")

        finally:
            if conn:
                try:
                    conn.close()
                except Exception:
                    pass

    def refresh_section_table(self):
        sql = "SELECT\n"
        sql += "    A.sectionid AS \"Id\"\n"
        sql += "    ,A.sectionname AS \"Section Name\"\n"
        sql += "    ,B.lastname || ', ' || B.firstname || ' ' || B.middlename AS \"Class Adviser\"\n"
        sql += "FROM cai.tbl_section A\n"
        sql += "LEFT JOIN cai.tbl_staff_info B\n"
        sql += "    ON A.teacherid = B.school_id\n"
        sql += "ORDER BY A.sectionname ASC"

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
            return model

        return None

    def populate_teachers(self, combo_box:QComboBox, school_id:str, add_empty:bool):
        sql = "SELECT\n"
        sql += "    school_id AS index\n"
        sql += "    ,lastname || ', ' || firstname || ' ' || COALESCE(middlename, '') AS itemname\n"
        sql += 'FROM cai.tbl_staff_info\n'
        sql += "WHERE positionid = %s\n"
        sql += "ORDER BY lastname ASC"

        self.utility.populate_pulldown(combo_box, sql, ('2',), default_value=school_id, add_empty=add_empty)

    def populate_sections(self, combo_box:QComboBox, value:str, add_empty:bool):
        sql = 'SELECT\n'
        sql += '    sectionid AS index\n'
        sql += '    ,sectionname AS itemname\n'
        sql += 'FROM cai.tbl_section\n'
        sql += 'ORDER BY sectionname ASC'

        self.utility.populate_pulldown(combo_box, sql, default_value=value, add_empty=add_empty)

    def delete_section(self, sectionId, sectionName):
        """
        Deletes a section and all associated student data in a single transaction.

        This method performs an atomic operation to remove a section. It identifies all 
        students within the section, deletes their associated quiz scores and student 
        records, removes the section itself, and logs the action to the audit trail.
        If any step fails, the entire operation is rolled back.

        Args:
            sectionId (int/str): The unique identifier of the section to be deleted.
            sectionName (str): The display name of the section (used for logging).
            user (dict): A dictionary containing current user details. 
                Expected keys: 'school_id', 'username'.

        Returns:
            bool: True if the transaction was committed successfully, 
                False if an error occurred and changes were rolled back.

        Raises:
            Exception: Captures and logs any database or logical errors during execution.
        """
        conn = None
        
        try:
            # Create ONE connection for the entire operation
            conn = self.db_tools.get_connection()
            conn.autocommit = False # Explicitly start a transaction
            
            with conn.cursor() as cur:
                # 1. Get student IDs
                cur.execute("SELECT studentid FROM cai.tbl_student_info WHERE sectionid = %s", (sectionId,))
                records = cur.fetchall()
                
                if records:
                    student_ids = tuple(r[0] for r in records)
                    
                    move_sql = """
                        WITH moved_rows AS (
                            DELETE FROM CAI.TBL_STUDENT_INFO
                            WHERE STUDENTID IN %s
                            RETURNING *
                        )
                        INSERT INTO CAI.TBL_STUDENT_INFO_ARCHIVE (
                            SCHOOL_YEAR, USERID, STUDENTID, LASTNAME, FIRSTNAME, MIDDLENAME, 
                            SECTIONID, PASSWORD, GENDER, PROFILE_PIC, 
                            CONTACT_PERSON, CONTACT_NUMBER, ARCHIVED_BY
                        )
                        SELECT 
                            SCHOOL_YEAR, USERID, STUDENTID, LASTNAME, FIRSTNAME, MIDDLENAME, 
                            SECTIONID, PASSWORD, GENDER, PROFILE_PIC, 
                            CONTACT_PERSON, CONTACT_NUMBER, %s 
                        FROM moved_rows
                    """
                    cur.execute(move_sql, (student_ids, self.user["school_id"]))

                    # 2. Delete Answers and Quiz Scores
                    cur.execute("DELETE FROM cai.tbl_quizscores WHERE studentid IN %s", (student_ids,))
                    cur.execute("DELETE FROM cai.tbl_answers WHERE studentid IN %s", (student_ids,))

                # 3. Delete the Section
                cur.execute("DELETE FROM cai.tbl_section WHERE sectionid = %s", (sectionId,))

                # 4. Insert Audit Trail
                actionStr = f"Deleted section: {sectionId} | {sectionName}"
                sql = "INSERT INTO cai.tbl_audit_trail(user_id, username, action) VALUES (%s, %s, %s)"
                cur.execute(sql, (self.user["school_id"], self.user["username"], actionStr))

            # IF WE REACH HERE, NO ERRORS OCCURRED
            conn.commit() 
            return True
                
        except Exception as e:
            # IF ANYTHING FAILED, UNDO EVERYTHING
            if conn:
                conn.rollback()
            print(f"Transaction Rollback! Reason: {e}")
            return False
        
        finally:
            if conn:
                conn.close()


class SectionAdviserEditor(QDialog, Ui_SectionAdviserEditorDialog):
    RESIZE_MARGIN = 8

    def __init__(self, section:Section, section_id=None, school_id=None):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # Remove OS default window frame
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setMouseTracking(True)

        self.db_tools = DatabaseTools()
        self.user     = section.user
        self.section  = section
        
        model = section.refresh_section_table()

        if model:
            self.table_section.setModel(model)
            header = self.table_section.horizontalHeader()
            header.setMinimumSectionSize(100)
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

        section.populate_sections(self.cmb_section, section_id, True)
        section.populate_teachers(self.cmb_teacher, school_id, True)

        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnClose.clicked.connect(self.reject)
        self.btnSave.clicked.connect(self.save)
        self.btnCancel.clicked.connect(self.reject)

    def save(self):
        sectionid = self.cmb_section.currentData()
        sectionname = self.cmb_section.currentText()
        teacherid = self.cmb_teacher.currentData()
        teachername = self.cmb_teacher.currentText()

        try:
            # 1. Update the section adviser
            update_sql = "UPDATE cai.tbl_section SET teacherid=%s WHERE sectionid = %s"
            self.db_tools.execute_query(update_sql, (teacherid, sectionid))

            # 2. Log the action in Audit Trail
            actionStr = f"Changed adviser: {sectionname} | {teachername}"
            audit_sql = "INSERT INTO cai.tbl_audit_trail(user_id, username, action) VALUES (%s, %s, %s)"
            self.db_tools.execute_query(audit_sql, (self.user["school_id"], self.user["username"], actionStr))

            # 3. Notify User and Close
            CustomMessageBox.success(self, "Success", f"Adviser for {sectionname} updated successfully.")

            model = self.section.refresh_section_table()

            if model:
                self.table_section.setModel(model)

        except Exception as e:
            CustomMessageBox.critical(self, "Database Error", f"Failed to save changes: {str(e)}")

    def _get_resize_edge(self, pos):
        """Determine which edge or corner the mouse is over based on RESIZE_MARGIN."""
        rect = self.rect()
        x, y = pos.x(), pos.y()
        w, h = rect.width(), rect.height()
        
        edge = None
        
        # Horizontal edges
        if x <= self.RESIZE_MARGIN:
            edge = Qt.Edge.LeftEdge
        elif x >= w - self.RESIZE_MARGIN:
            edge = Qt.Edge.RightEdge
            
        # Vertical edges
        if y <= self.RESIZE_MARGIN:
            if edge is None:
                edge = Qt.Edge.TopEdge
            else:
                edge |= Qt.Edge.TopEdge
        elif y >= h - self.RESIZE_MARGIN:
            if edge is None:
                edge = Qt.Edge.BottomEdge
            else:
                edge |= Qt.Edge.BottomEdge
                
        return edge

    def _update_cursor_shape(self, edge):
        """Update cursor appearance depending on the active resize edge/corner."""
        if edge == (Qt.Edge.TopEdge | Qt.Edge.LeftEdge) or edge == (Qt.Edge.BottomEdge | Qt.Edge.RightEdge):
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif edge == (Qt.Edge.TopEdge | Qt.Edge.RightEdge) or edge == (Qt.Edge.BottomEdge | Qt.Edge.LeftEdge):
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif edge and (edge & (Qt.Edge.LeftEdge | Qt.Edge.RightEdge)) and not (edge & (Qt.Edge.TopEdge | Qt.Edge.BottomEdge)):
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif edge and (edge & (Qt.Edge.TopEdge | Qt.Edge.BottomEdge)) and not (edge & (Qt.Edge.LeftEdge | Qt.Edge.RightEdge)):
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint()
        edge = self._get_resize_edge(pos)
        self._update_cursor_shape(edge)
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            edge = self._get_resize_edge(pos)
            
            # 1. If clicking near any edge/corner, resize the window
            if edge:
                self.windowHandle().startSystemResize(edge)
                event.accept()
                return

            # 2. If clicking inside the custom header, move the window
            if self.frame_header.geometry().contains(pos):
                self.windowHandle().startSystemMove()
                event.accept()
                return
            
        super().mousePressEvent(event)

    