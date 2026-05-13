from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView, QComboBox
from App.CRUDTools import DatabaseTools
from App.Tools import Utility
from App.FormSectionRegistration import Ui_SectionRegistrationDialog
from App.FormSectionAdviserEditor import Ui_SectionAdviserEditorDialog

class Section(QDialog, Ui_SectionRegistrationDialog):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)

        self.user = user
        self.utility = Utility()
        self.db_tools = DatabaseTools()
        self.populate_teachers(self.cmb_teacher, True)
        self.btnSave.clicked.connect(self.register)
        self.btnCancel.clicked.connect(self.reject)

    def get_adviser(self, sectionid=None):
        sql = """
            SELECT 
                B.lastname || ', ' || B.firstname || ' ' || B.middlename AS class_advisor
            FROM cai.tbl_section A
            INNER JOIN cai.tbl_staff_info B ON A.teacherid = B.school_id
            WHERE A.sectionid = %s
        """

        cursor, conn = self.db_tools.retrieve_records(sql, (sectionid,))
        class_advisor = ""

        if cursor:
            record = cursor.fetchone()
            if record:
                class_advisor = record[0]

            cursor.close()

        if conn: conn.close()
        return class_advisor

    def register(self):
        section_name = self.txtSectionName.text().strip()
        teacher_id = self.cmb_teacher.currentData()

        # 1. Validation
        if not section_name:
            QMessageBox.warning(self, "Input Error", "Please enter a section name.")
            return

        if not teacher_id:
            QMessageBox.warning(self, "Input Error", "Please select a class advisor.")
            return

        conn = None
        try:
            # 2. Get connection and start transaction
            conn = self.db_tools.get_connection()
            conn.autocommit = False 
            
            with conn.cursor() as cur:
                # 3. Check for duplicates (Case-Insensitive)
                cur.execute("SELECT 1 FROM cai.tbl_section WHERE UPPER(sectionname) = UPPER(%s)", (section_name,))
                if cur.fetchone():
                    QMessageBox.warning(self, "Duplicate Entry", f"Section '{section_name}' already exists.")
                    return

                # 4. Insert Section
                cur.execute(
                    "INSERT INTO cai.tbl_section (sectionname, teacherid) VALUES (%s, %s) RETURNING sectionid", 
                    (section_name, teacher_id)
                )
                new_id = cur.fetchone()[0]

                # 5. Insert Audit Trail
                action_str = f"Registered new section: {section_name} (ID: {new_id})"
                audit_sql = """
                    INSERT INTO cai.tbl_audit_trail (user_id, username, action) 
                    VALUES (%s, %s, %s)
                """
                cur.execute(audit_sql, (self.user["school_id"], self.user["username"], action_str))

            # 6. Commit if everything succeeded
            conn.commit()
            QMessageBox.information(self, "Success", f"Section '{section_name}' added successfully.")
            self.refresh_section_table()
            self.accept()

        except Exception as e:
            # 7. Rollback if anything failed
            if conn: conn.rollback()
            QMessageBox.critical(self, "Error", f"Failed to register section: {e}")

        finally:
            if conn: conn.close()

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

    def populate_teachers(self, combo_box:QComboBox, add_empty:bool):
        sql = "SELECT\n"
        sql += "    school_id AS index\n"
        sql += "    ,lastname || ', ' || firstname || ' ' || COALESCE(middlename, '') AS itemname\n"
        sql += 'FROM cai.tbl_staff_info\n'
        sql += "WHERE positionid = %s\n"
        sql += "ORDER BY lastname ASC"

        self.utility.populate_pulldown(combo_box, sql, ('2',), add_empty=add_empty)

    def populate_sections(self, combo_box:QComboBox, add_empty:bool):
        sql = 'SELECT\n'
        sql += '    sectionid AS index\n'
        sql += '    ,sectionname AS itemname\n'
        sql += 'FROM cai.tbl_section\n'
        sql += 'ORDER BY sectionname ASC'

        self.utility.populate_pulldown(combo_box, sql, add_empty=add_empty)

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

    def __init__(self, section:Section):
        super().__init__()
        self.setupUi(self)

        self.db_tools = DatabaseTools()
        self.user = section.user
        self.section = section

        self.table_section.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        model = section.refresh_section_table()

        if model:
            self.table_section.setModel(model)

        section.populate_sections(self.cmb_section, True)
        section.populate_teachers(self.cmb_teacher, True)

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
            QMessageBox.information(self, "Success", f"Adviser for {sectionname} updated successfully.")

            model = self.section.refresh_section_table()

            if model:
                self.table_section.setModel(model)

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to save changes: {str(e)}")



    