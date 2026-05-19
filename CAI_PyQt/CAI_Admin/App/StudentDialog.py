import psycopg2, csv
from passlib.hash import bcrypt

from PySide6.QtGui import QStandardItemModel, QStandardItem, QImage, QPixmap
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide6.QtCore import Qt, QByteArray, QBuffer, QIODevice, QDate

from App.FormAddNewStudent import Ui_AddNewStudentDialog
from App.FormEditStudent import Ui_EditStudentDialog

from App.Tools import Utility, CircularProgress
from App.CRUDTools import DatabaseTools

class Student:

    def __init__(self):
        self.db_tools = DatabaseTools()
        self.util = Utility()
        self.circular_bar = CircularProgress()

    def count(self):
        sql = "SELECT COUNT(*) FROM cai.tbl_student_info;"
        record = self.db_tools.fetch_all(sql)

        count = 0

        if record:
            count = record[0]['count']

        return count

    def get_student_picture(self, studentid, isCircular=False, size=80):
        sql = """
            SELECT profile_pic
            FROM cai.tbl_student_info
            WHERE studentid = %s
        """
        record = self.db_tools.fetch_all(sql, (studentid,))
        pixmap = QPixmap(u":/Images/Images/profile_gray.png")

        if record:
            img_data = record[0]['profile_pic']

            if img_data:
                image = QImage.fromData(bytes(img_data))

                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)

        if isCircular:
            pixmap = self.util.makeCircularPixmap(pixmap, size)

        return pixmap

    def refresh_student_table(self, sectionid):
        sql = 'SELECT\n'
        sql += '    stud.studentid AS "STUDENT ID"\n'
        sql += '    ,stud.lastname AS "LAST NAME"\n'
        sql += '    ,stud.firstname AS "FIRST NAME"\n'
        sql += '    ,stud.middlename AS "MIDDLE NAME"\n'
        sql += '    ,sec.sectionname AS "SECTION"\n'
        sql += '    ,stud.gender AS "GENDER"\n'
        sql += 'FROM\n'
        sql += '    cai.tbl_student_info stud\n'
        sql += 'INNER JOIN\n'
        sql += '    cai.tbl_section sec\n'
        sql += '    ON stud.sectionid = sec.sectionid\n'

        params = []

        if sectionid:
            sql += '    AND stud.sectionid = %s\n'
            params.append(sectionid)

        sql += 'ORDER BY\n'
        sql += '    stud.lastname, stud.firstname ASC'

        params = tuple(params) if params else None

        cursor, conn = self.db_tools.retrieve_records(sql, params)
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

        if conn: conn.close()
        return None
    
    def refresh_student_cards(self, params):
        schoolYear, sectionid, text = params

        sql = 'SELECT\n'
        sql += '    studentid\n'
        sql += '    ,firstname\n'
        sql += '    ,middlename\n'
        sql += '    ,lastname\n'
        sql += '    ,sectionid\n'
        sql += '    ,gender\n'
        sql += '    ,password\n'
        sql += '    ,profile_pic\n'
        sql += 'FROM cai.tbl_student_info\n'
        sql += 'WHERE school_year = %s\n'

        params2 = [schoolYear]

        if sectionid:
            sql += '    AND sectionid = %s\n'
            params2.append(sectionid)

        # Global search across multiple columns
        if text:
            sql += '    AND (\n'
            sql += '        studentid ILIKE %s OR\n'
            sql += '        firstname ILIKE %s OR\n'
            sql += '        lastname ILIKE %s\n'
            sql += '    )\n'
            
            # Append the search term 3 times to match the 3 placeholders
            search_term = f"%{text}%"
            params2.extend([search_term, search_term, search_term])

        sql += 'ORDER BY lastname ASC'

        cursor, conn = self.db_tools.retrieve_records(sql, tuple(params2))
        if cursor:
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records

        if conn: conn.close()
        return list()

    def getStudentMastery(self):
        """
            This calculates the percentage for every quiz and adds a "Status" label based on their performance.
        """
        sql  = "SELECT\n"
        sql += "    studentid,\n"
        sql += "    lessonid,\n"
        sql += "    quizscore,\n"
        sql += "    totalitems,\n"
        sql += "    ROUND((quizscore::numeric / totalitems) * 100, 2) AS percentage,\n"
        sql += "    CASE\n"
        sql += "        WHEN (quizscore::numeric / totalitems) >= 0.85 THEN 'Mastered'\n"
        sql += "        WHEN (quizscore::numeric / totalitems) >= 0.70 THEN 'Developing'\n"
        sql += "        ELSE 'Needs Review'\n"
        sql += "    END AS status,\n"
        sql += "    datetaken::DATE AS date_only\n"
        sql += "FROM cai.tbl_quizscores\n"
        sql += "WHERE studentid = %s\n"
        sql += "ORDER BY datetaken DESC;\n"

    def getProgressOvertime(self):
        """
            To show if a student is improving across a specific grading period, you can group their average
            scores by date. This data is ideal for a line graph.
        """
        sql  = "SELECT\n"
        sql += "    datetaken::DATE as day,\n"
        sql += "    AVG((quizscore::numeric / totalitems) * 100) as daily_avg\n"
        sql += "FROM cai.tbl_quizscores\n"
        sql += "WHERE studentid = %s AND gradingperiod = %s\n"
        sql += "GROUP BY datetaken::DATE\n"
        sql += "ORDER BY day ASC;\n"

    def get_student_progress(self, studentid, gradingperiod):
        sql  = "SELECT\n"
        sql += "    AVG((quizscore::numeric / totalitems) * 100) as overall_avg\n"
        sql += "FROM cai.tbl_quizscores\n"
        sql += "WHERE studentid = %s AND gradingperiod = %s;\n"

        cur, conn = self.db_tools.retrieve_records(sql, (studentid, gradingperiod))
        result = cur.fetchone()

        if result and result[0] is not None:
            score_avg = float(result[0])
            self.circular_bar.set_value(score_avg)

        else:
            self.circular_bar.set_value(0)

        return self.circular_bar
    
    def delete_student(self, ids, user):

        if isinstance(ids, list):
            ids = tuple(ids)
        elif not isinstance(ids, tuple):
            ids = (ids,)

        try:
            sql  = "WITH moved_rows AS (\n"
            sql += "    DELETE FROM CAI.TBL_STUDENT_INFO\n"
            sql += "    WHERE STUDENTID IN %s\n"
            sql += "    RETURNING *\n"
            sql += ")\n"
            sql += "INSERT INTO CAI.TBL_STUDENT_INFO_ARCHIVE (\n"
            sql += "    SCHOOL_YEAR, USERID, STUDENTID, LASTNAME, FIRSTNAME, MIDDLENAME, \n"
            sql += "    SECTIONID, PASSWORD, GENDER, PROFILE_PIC, \n"
            sql += "    CONTACT_PERSON, CONTACT_NUMBER, ARCHIVED_BY\n"
            sql += ")\n"
            sql += "SELECT \n"
            sql += "    SCHOOL_YEAR, USERID, STUDENTID, LASTNAME, FIRSTNAME, MIDDLENAME, \n"
            sql += "    SECTIONID, PASSWORD, GENDER, PROFILE_PIC, \n"
            sql += "    CONTACT_PERSON, CONTACT_NUMBER, %s \n"
            sql += "FROM moved_rows"

            self.db_tools.execute_query(sql, (ids, user["school_id"]))

            actionStr = f"Deleted students: {ids}"
            sql  = "INSERT INTO cai.tbl_audit_trail(user_id, username, action)\n"
            sql += "VALUES (%s, %s, %s);\n"
            self.db_tools.execute_query(sql, (user["school_id"], user["username"], actionStr))

            return True

        except Exception as e:
            print(f"Failed to delete students {ids}. Error: {str(e)}")
            return False


class AddNewStudentDialog(QDialog, Ui_AddNewStudentDialog):
    def __init__(self, script_dir):
        super().__init__()
        self.setupUi(self)

        self.displaySchoolYear()
        self.util = Utility()
        self.script_dir = script_dir
        self.profile_pic = None
        self.binaryImage = None
        self.db_tools = DatabaseTools()
        self.btnUploadPhoto.clicked.connect(self.update_photo)
        self.btnSave.clicked.connect(self.register)
        self.btnCancel.clicked.connect(self.reject)
        self.rb_importCSV.toggled.connect(lambda checked: self.update_state(not checked))
        self.btnBrowseCSV.clicked.connect(self.browse_csv)
        self.btnRefreshSY.clicked.connect(self.displaySchoolYear)
        self.progressBar.setVisible(False)

        sql = 'SELECT\n'
        sql += '    sectionid AS index\n'
        sql += '    ,sectionname AS itemname\n'
        sql += 'FROM cai.tbl_section\n'
        sql += 'ORDER BY sectionname ASC'

        self.util.populate_pulldown(self.cmbSection, sql, add_empty=True)
        self.util.populate_pulldown(self.cmbSection_2, sql, add_empty=True)

    def displaySchoolYear(self):
        current_date = QDate.currentDate()
        current_year = current_date.year()
        self.spinBox_SY1.setValue(current_year)
        self.spinBox_SY2.setValue(current_year + 1)

    def update_state(self, checked):
        self.widget_stud_info.setEnabled(checked)
        self.widget_form_emergency.setEnabled(checked)
        self.widget_CSV.setEnabled(not checked)

    def browse_csv(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()

            if selected_files:
                self.txtCSVPath.setText(selected_files[0])

    def update_photo(self):
        self.profile_pic, self.binaryImage = self.util.browsePhoto(self, self.label_profile_pic.width(), self.label_profile_pic.height())

        if self.profile_pic:
            self.label_profile_pic.setPixmap(self.profile_pic)

    def register(self):
        if self.rb_importCSV.isChecked():
            ret = self.import_from_csv(self.txtCSVPath.text())
            if ret == 0:
                QMessageBox.information(self, "Success", "Students imported successfully!")
                self.accept()
            return

        sy1 = self.spinBox_SY1.value()
        sy2 = self.spinBox_SY2.value()
        firstname = self.txtFirstName.text().strip()
        middlename = self.txtMiddleName.text().strip()
        lastname = self.txtLastName.text().strip()
        section = self.cmbSection.currentData()
        password = self.txtPassword.text()
        gender = self.cmbGender.currentText()
        contact_person = self.txtContactPerson.text().strip()
        contact_number = self.txtContactNum.text().strip()

        errors = []

        if not sy1 or not sy2:
            errors.append("❌ School year cannot be empty.")
        if not firstname:
            errors.append("❌ First name cannot be empty.")
        if not lastname:
            errors.append("❌ Last name cannot be empty.")
        if not section:
            errors.append("❌ Please select a section.")
        if len(password) < 6:
            errors.append("❌ Password must be at least 6 characters long.")
        if not gender:
            errors.append("❌ Please select a gender.")

        if errors:
            QMessageBox.warning(self, "Validation Error", "\n".join(errors))
            return

        sql = 'INSERT INTO cai.tbl_student_info(\n'
        sql += '    school_year\n'
        sql += "    ,studentid\n"
        sql += '    ,firstname\n'
        sql += '    ,middlename\n'
        sql += '    ,lastname\n'
        sql += '    ,sectionid\n'
        sql += '    ,password\n'
        sql += '    ,gender\n'
        sql += '    ,profile_pic\n'
        sql += '    ,contact_person\n'
        sql += '    ,contact_number\n'
        sql += ')\n'
        sql += "VALUES (%s, \n"
        sql += "    to_char(CURRENT_DATE, 'YYYY') || '-' || lpad(nextval('cai.student_id_seq')::text, 4, '0') || '-STU', \n"
        sql += "    %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        self.db_tools.execute_query(sql, (
            f"{sy1}-{sy2}",
            firstname,
            middlename,
            lastname,
            section,
            bcrypt.hash(password),
            gender,
            psycopg2.Binary(self.binaryImage) if self.binaryImage else None,
            contact_person,
            contact_number
            )
        )
        QMessageBox.information(self, "Success", "Student registered successfully!")
        self.accept()

    def import_from_csv(self, csv_path):
        section = self.cmbSection_2.currentData()

        if not section:
            QMessageBox.warning(self, "Validation Error", "Please select a section.")
            return 1

        if not csv_path:
            QMessageBox.warning(self, "Validation Error", "Please select a CSV file.")
            return 1
        
        sy1 = self.spinBox_SY1.value()
        sy2 = self.spinBox_SY2.value()

        if not sy1 or not sy2:
            QMessageBox.warning(self, "Validation Error", "School year cannot be empty.")
            return 1

        self.progressBar.setVisible(True)

        with open(csv_path, mode='r', encoding='utf-8') as f:
            total_rows = sum(1 for line in f) - 1 # Subtract 1 for header

        self.progressBar.setMaximum(total_rows)
        self.progressBar.setValue(0)

        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            sql = 'INSERT INTO cai.tbl_student_info(\n'
            sql += '    school_year\n'
            sql += '    ,studentid\n'
            sql += '    ,lastname\n'
            sql += '    ,firstname\n'
            sql += '    ,middlename\n'
            sql += '    ,sectionid\n'
            sql += '    ,password\n'
            sql += '    ,gender\n'
            sql += '    ,contact_person\n'
            sql += '    ,contact_number\n'
            sql += ')\n'
            sql += 'VALUES (%s, \n'
            sql += "    to_char(CURRENT_DATE, 'YYYY') || '-' || lpad(nextval('cai.student_id_seq')::text, 4, '0') || '-STU',\n"
            sql += '    %s, %s, %s, %s, %s, %s, %s, %s);'

            for i, row in enumerate(reader, 1):
                self.db_tools.execute_query(sql, (
                    f"{sy1}-{sy2}",
                    row['LAST NAME'],
                    row['FIRST NAME'],
                    row['MIDDLE NAME'],
                    section,
                    bcrypt.hash(row['PASSWORD']),
                    self.validateGender(row['GENDER']),
                    row['CONTACT PERSON'],
                    row['CONTACT NUMBER']
                    )
                )

                self.progressBar.setValue(i)

        return 0

    def validateGender(self, gender):
        if not gender:
            return ""
        
        clean_gender = str(gender).strip().upper()
        
        lookup = {
            'M': 'Male', 
            'MALE': 'Male',
            'F': 'Female', 
            'FEMALE': 'Female'
        }
        
        return lookup.get(clean_gender, "")
    
    def refresh_student_info(self, student_id):
        sql = 'SELECT\n'
        sql += '    stud.studentid\n'
        sql += '    ,stud.lastname\n'
        sql += '    ,stud.firstname \n'
        sql += '    ,stud.middlename\n'
        sql += '    ,sec.sectionname\n'
        sql += '    ,stud.gender\n'
        sql += '    ,stud.password\n'
        sql += '    ,stud.profile_pic\n'
        sql += '    ,stud.contact_person\n'
        sql += '    ,stud.contact_number\n'
        sql += 'FROM\n'
        sql += '    cai.tbl_student_info stud\n'
        sql += 'LEFT JOIN\n'
        sql += '    cai.tbl_section sec\n'
        sql += '    ON stud.sectionid = sec.sectionid\n'
        sql += 'WHERE\n'
        sql += '    stud.studentid = %s\n'

        cursor, conn = self.db_tools.retrieve_records(sql, (student_id,))

        if cursor:
            record = cursor.fetchone()
            cursor.close()
            conn.close()
            return record

        return tuple([""] * 10)  # Return a tuple with 10 empty string values if no record is found

    def update_section_stats(self, student_id):
        if not student_id:
            return tuple([0, 0, 0])

        sql = "SELECT\n"
        sql += "    COUNT(*),\n"
        sql += "    COUNT(*) FILTER (WHERE UPPER(gender) = 'MALE'),\n"
        sql += "    COUNT(*) FILTER (WHERE UPPER(gender) = 'FEMALE')\n"
        sql += "FROM\n"
        sql += "    cai.tbl_student_info\n"
        sql += "WHERE sectionid = (\n"
        sql += "    SELECT sectionid FROM cai.tbl_student_info WHERE studentid = %s\n"
        sql += ")"

        cur, conn = self.db_tools.retrieve_records(sql, (student_id,))
        if cur:
            record = cur.fetchone()
            conn.close()
            return record

        conn.close()
        return tuple([0, 0, 0])

    


class StudentEditorDialog(QDialog, Ui_EditStudentDialog):
    def __init__(self, user, studentid=None):
        super().__init__()
        self.setupUi(self)
        self.db_tools = DatabaseTools()
        self.util = Utility()

        if self.util.isEmpty(studentid) or self.util.isEmpty(user):
            self.reject()

        self.image_data = None
        self.user = user

        self.displaySchoolYear()

        self.btnUpdate.clicked.connect(lambda: self.edit(studentid))
        self.btnCancel.clicked.connect(self.reject)
        self.btnUploadPhoto.clicked.connect(self.update_photo)
        self.btnRefreshSY.clicked.connect(self.displaySchoolYear)

        sql = 'SELECT\n'
        sql += '    sectionid AS index\n'
        sql += '    ,sectionname AS itemname\n'
        sql += 'FROM cai.tbl_section\n'
        sql += 'ORDER BY sectionname ASC'

        self.util.populate_pulldown(self.cmbSection, sql, add_empty=True)
        sid = lname = fname = mname = sectionid = gender = contact_person = contact_num = ""
        record = self.get_student_info(studentid)

        if record:
            sid, lname, fname, mname, sectionid, gender, _, self.image_data, contact_person, contact_num = record

            # --- Add Profile Picture Logic Here ---
            if self.image_data:
                image = QImage.fromData(bytes(self.image_data))
                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)
                    # Scale it to fit your label while keeping aspect ratio
                    scaled_pixmap = pixmap.scaled(
                        self.label_profile_pic.width(),
                        self.label_profile_pic.height(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    self.label_profile_pic.setPixmap(scaled_pixmap)
                else:
                    self.label_profile_pic.setText("Invalid Image")

        self.txtFirstName.setText(f"{fname}")
        self.txtMiddleName.setText(f"{mname}")
        self.txtLastName.setText(f"{lname}")

        sec_index = self.cmbSection.findData(sectionid)
        if sec_index != -1:
            self.cmbSection.setCurrentIndex(sec_index)

        gen_index = self.cmbGender.findText(gender)
        if gen_index != -1:
            self.cmbGender.setCurrentIndex(gen_index)

        self.txtContactPerson.setText(f"{contact_person}")
        self.txtContactNum.setText(f"{contact_num}")

    def displaySchoolYear(self):
        current_date = QDate.currentDate()
        current_year = current_date.year()
        self.spinBox_SY1.setValue(current_year)
        self.spinBox_SY2.setValue(current_year + 1)

    def get_student_info(self, studentid):
        sql = 'SELECT\n'
        sql += '    stud.studentid\n'
        sql += '    ,stud.lastname\n'
        sql += '    ,stud.firstname \n'
        sql += '    ,stud.middlename\n'
        sql += '    ,sec.sectionid\n'
        sql += '    ,stud.gender\n'
        sql += '    ,stud.password\n'
        sql += '    ,stud.profile_pic\n'
        sql += '    ,stud.contact_person\n'
        sql += '    ,stud.contact_number\n'
        sql += 'FROM\n'
        sql += '    cai.tbl_student_info stud\n'
        sql += 'LEFT JOIN\n'
        sql += '    cai.tbl_section sec\n'
        sql += '    ON stud.sectionid = sec.sectionid\n'
        sql += 'WHERE\n'
        sql += '    stud.studentid = %s\n'

        cursor, conn = self.db_tools.retrieve_records(sql, (studentid,))

        if cursor:
            record = cursor.fetchone()
            cursor.close()
            conn.close()
            return record

        conn.close()
        return tuple([""] * 10) # Return a tuple with 10 empty string values if no record is found

    def edit(self, studentid):
        try:
            sy1 = self.spinBox_SY1.value()
            sy2 = self.spinBox_SY2.value()
            firstname = self.txtFirstName.text().strip()
            middlename = self.txtMiddleName.text().strip()
            lastname = self.txtLastName.text().strip()
            section = self.cmbSection.currentData()
            password = self.txtPassword.text()
            gender = self.cmbGender.currentText()
            contact_person = self.txtContactPerson.text().strip()
            contact_number = self.txtContactNum.text().strip()

            errors = []

            if not sy1 or not sy2:
                errors.append("❌ School year cannot be empty.")
            if not firstname:
                errors.append("❌ First name cannot be empty.")
            if not lastname:
                errors.append("❌ Last name cannot be empty.")
            if not section:
                errors.append("❌ Please select a section.")
            if password and len(password) < 6:
                errors.append("❌ Password must be at least 6 characters long.")
            if not gender:
                errors.append("❌ Please select a gender.")

            if errors:
                QMessageBox.warning(self, "Validation Error", "\n".join(errors))
                return

            sql  = "UPDATE cai.tbl_student_info\n"
            sql += "SET\n"
            sql += "    school_year = %s\n"
            sql += "    ,firstname = %s\n"
            sql += "    ,middlename = %s\n"
            sql += "    ,lastname = %s\n"
            sql += "    ,sectionid = %s\n"

            params = [
                f"{sy1}-{sy2}",
                firstname,
                middlename,
                lastname,
                section
            ]

            if password:
                sql += "    ,password = %s\n"
                params.append(bcrypt.hash(password))

            sql += "    ,gender = %s\n"
            sql += "    ,contact_person = %s\n"
            sql += "    ,contact_number = %s\n"
            sql += "    ,profile_pic = %s\n"
            sql += "WHERE\n"
            sql += "    studentid = %s\n"

            params.extend([
                gender,
                contact_person,
                contact_number,
                self.image_data,
                studentid
            ])

            self.db_tools.execute_query(sql, tuple(params))

            # Log
            actionStr = f"Edited: {studentid}"
            sql  = "INSERT INTO cai.tbl_audit_trail(user_id, username, action)\n"
            sql += "VALUES (%s, %s, %s);\n"
            self.db_tools.execute_query(sql, (self.user["school_id"], self.user["username"], actionStr))

            self.accept()

        except Exception as e:
            print(f"Error: {e}")
            return

    def update_photo(self):
        pixmap, binaryImage = self.util.browsePhoto(self, self.label_profile_pic.width(), self.label_profile_pic.height())

        if pixmap:
            self.label_profile_pic.setPixmap(pixmap)

        if binaryImage:
            self.image_data = binaryImage


