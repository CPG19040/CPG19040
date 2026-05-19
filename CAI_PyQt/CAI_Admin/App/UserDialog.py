import re, psycopg2
from passlib.hash import bcrypt

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from App.FormAddNewUser import Ui_AddNewUserDialog
from App.FormEditUser import Ui_EditUserDialog
from App.CRUDTools import DatabaseTools
from App.Tools import Utility

class Staff:

    def __init__(self):
        self.db_tools = DatabaseTools()
        self.util = Utility()

    def count(self):
        sql = """
            SELECT
                COUNT(*) 
            FROM 
                cai.tbl_staff_info a, cai.tbl_staff_positions b
            WHERE
                a.positionid = b.position_id AND
                b.position_name = 'Teacher';
        """
        record = self.db_tools.fetch_all(sql)

        count = 0

        if record:
            count = record[0]['count']

        return count

    def get_userid(self, school_id):
        sql = """
                SELECT user_id
                FROM cai.tbl_staff_info
                WHERE school_id = %s
            """

        cursor, conn = self.db_tools.retrieve_records(sql, (school_id,))
        userid = None

        if cursor:
            row = cursor.fetchone()

            if row:
                userid = row[0]

        if conn: conn.close()

        return userid

    def get_user_profile_pic(self, school_id, size:int=30):
        sql = """
                SELECT profile_pic
                FROM cai.tbl_staff_info
                WHERE school_id = %s
            """

        cursor, conn = self.db_tools.retrieve_records(sql, (school_id,))
        pic = None

        if cursor:
            record = cursor.fetchone()
            if record[0]:
                image = QImage.fromData(bytes(record[0]))
                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)
                    pic = self.util.makeCircularPixmap(pixmap, size)

            cursor.close()
            conn.close()
            return pic

        if conn: conn.close()
        return pic

    def get_user_info(self, school_id):
        sql = """
                SELECT
                    user_id,
                    school_id,
                    firstname,
                    middlename,
                    lastname,
                    username,
                    positionid,
                    profile_pic,
                    contact_person,
                    contact_number,
                    new_user
                FROM cai.tbl_staff_info
                WHERE school_id = %s
            """

        record = self.db_tools.fetch_all(sql, (school_id,))
        row = dict()

        if record:
            row = record[0]

        return row

    def get_user_model(self, text:str = ''):
        sql  = 'SELECT\n'
        sql += '    A.profile_pic AS " ",\n'
        sql += '    A.school_id AS "School ID",\n'
        sql += '    A.firstname AS "First Name",\n'
        sql += '    A.middlename AS "Middle Name",\n'
        sql += '    A.lastname AS "Last Name",\n'
        sql += '    A.username AS "Username",\n'
        sql += '    B.position_name AS "Position",\n'
        sql += '    A.contact_person AS "Contact Person",\n'
        sql += '    A.contact_number AS "Contact Number"\n'
        sql += 'FROM cai.tbl_staff_info A\n'
        sql += 'LEFT JOIN cai.tbl_staff_positions B\n'
        sql += 'ON A.positionid = B.position_id\n'
        sql += 'WHERE 1 = 1\n'

        params = []
        
        if text:
            sql += '    AND (\n'
            sql += '        A.school_id ILIKE %s OR\n'
            sql += '        A.firstname ILIKE %s OR\n'
            sql += '        A.middlename ILIKE %s OR\n'
            sql += '        A.lastname ILIKE %s OR\n'
            sql += '        A.username ILIKE %s OR\n'
            sql += '        B.position_name ILIKE %s OR\n'
            sql += '        A.contact_person ILIKE %s OR\n'
            sql += '        A.contact_number ILIKE %s\n'
            sql += '    )\n'

            # Append the search term 3 times to match the 3 placeholders
            search_term = f"%{text}%"
            params.extend([search_term, search_term, search_term, search_term, search_term, search_term, search_term, search_term])

        sql += 'ORDER BY lastname, firstname\n'

        cursor, conn = self.db_tools.retrieve_records(sql, tuple(params))

        if cursor:
            headers = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
            model = QStandardItemModel(len(records), len(headers))
            model.setHorizontalHeaderLabels(headers)

            for row_idx, row_data in enumerate(records):

                for col_idx, value in enumerate(row_data):
                    item = QStandardItem()

                    # Column index 0 is "profile_pic"
                    if col_idx == 0:
                        if value:
                            pixmap = QPixmap()
                            if isinstance(value, (bytes, bytearray, memoryview)):
                                pixmap.loadFromData(bytes(value))
                            else:
                                pixmap.load(str(value))

                            if not pixmap.isNull():
                                scaled = self.util.makeCircularPixmap(pixmap, 36)
                                item.setData(scaled, Qt.ItemDataRole.DecorationRole)
                    else:
                        item.setText(str(value) if value is not None else "")

                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    model.setItem(row_idx, col_idx, item)

            cursor.close()
            conn.close()
            return model

        if conn: conn.close()
        return None

    def archive_and_delete_staff(self, user:dict, staff_id):
        """
        Args:
            user (dict): The person performing the arhive.
            staff_id: The school_id of the person to be archived.
        """
        conn = None
        cur = None
        
        try:
            conn = self.db_tools.get_connection()
            cur = conn.cursor()

            sql  = "WITH moved_rows AS (\n"
            sql += "    DELETE FROM cai.tbl_staff_info\n"
            sql += "    WHERE school_id = %s\n"
            sql += "    RETURNING *\n"
            sql += ")\n"
            sql += "INSERT INTO cai.tbl_staff_info_archive (\n"
            sql += "    user_id, school_id, firstname, middlename, lastname, \n"
            sql += "    username, password, profile_pic, new_user, archived_by \n"
            sql += ")\n"
            sql += "SELECT \n"
            sql += "    user_id, school_id, firstname, middlename, lastname, \n"
            sql += "    username, password, profile_pic, new_user, %s \n"
            sql += "FROM moved_rows"
            
            userid = self.get_userid(user["school_id"])
            cur.execute(sql, (staff_id, userid))
            
            actionStr = f"Deleted user ({staff_id})"
            sql  = "INSERT INTO cai.tbl_audit_trail(user_id, username, action)\n"
            sql += "VALUES (%s, %s, %s);\n"
            cur.execute(sql, (user["school_id"], user["username"], actionStr))

            conn.commit()

            print(f"Staff {staff_id} successfully archived and removed.")

        except Exception as e:
            if conn:
                conn.rollback() # Undo everything if an error occurs
            print(f"Transaction failed: {e}")

        finally:
            if cur: cur.close()
            if conn: conn.close()



class AddUserDialog(QDialog, Ui_AddNewUserDialog):
    def __init__(self, user:dict):
        super().__init__()
        self.setupUi(self)

        self.db = DatabaseTools()
        self.util = Utility()
        self.staff = Staff()
        self.setup_ui_elements()

        self.profile_pic = None
        self.binaryImage = None

        self.btnUploadPhoto.clicked.connect(self.update_photo)
        self.btnSave.clicked.connect(lambda: self.register_user(user))
        self.btnCancel.clicked.connect(self.reject)

    def setup_ui_elements(self):
        sql = "SELECT\n"
        sql += "    position_id\n"
        sql += "    ,position_name\n"
        sql += "FROM cai.tbl_staff_positions\n"
        sql += "ORDER BY position_id ASC"
        self.util.populate_pulldown(self.comboBox_position, sql, add_empty=True)

    def update_photo(self):
        self.profile_pic, self.binaryImage = self.util.browsePhoto(self, self.label_profile_pic.width(), self.label_profile_pic.height())

        if self.profile_pic:
            w = self.label_profile_pic.width()
            self.label_profile_pic.setPixmap(self.util.makeCircularPixmap(self.profile_pic, w))

    def register_user(self, user:dict):
        # 1. Collect data
        data = {
            "fname": self.lineEdit_firstname.text().strip(),
            "mname": self.lineEdit_middlename.text().strip(),
            "lname": self.lineEdit_lastname.text().strip(),
            "uname": self.lineEdit_username.text().strip(),
            "pwd": self.lineEdit_password.text(),
            "pos": self.comboBox_position.currentData(),
            "contact_person": self.txtContactPerson.text().strip(),
            "contact_number": self.txtContactNum.text().strip()
        }

        # 2. Basic Validation: Required Fields
        required_fields = ["fname", "lname", "uname", "pwd"]
        if not all(data[field] for field in required_fields):
            QMessageBox.warning(self, "Validation Error", "All fields except Middle Name are required.")
            return

        # 3. Format Validation: Names (No numbers allowed)
        name_regex = r"^[a-zA-Z\s.-]+$"
        if not re.match(name_regex, data["fname"]) or not re.match(name_regex, data["lname"]):
            QMessageBox.warning(self, "Validation Error", "Names should only contain letters.")
            return

        # 4. Format Validation: Password Strength
        if len(data["pwd"]) < 6:
            QMessageBox.warning(self, "Validation Error", "Password must be at least 6 characters long.")
            return

        # 5. Database Validation: Duplicate Username
        check_query = "SELECT COUNT(*) FROM cai.tbl_staff_info WHERE username = %s"
        exists = self.db.fetch_all(check_query, (data["uname"],))
        if exists and exists[0]['count'] > 0:
            QMessageBox.warning(self, "Validation Error", f"Username '{data['uname']}' is already taken.")
            return

        # 6. Proceed to Registration
        try:
            sql = """
                INSERT INTO cai.tbl_staff_info(
                    school_id
                    ,firstname
                    ,middlename
                    ,lastname
                    ,username
                    ,password
                    ,positionid
                    ,profile_pic
                    ,contact_person
                    ,contact_number
                )
                VALUES ( 
                    to_char(CURRENT_DATE, 'YYYY') || '-' || lpad(nextval('cai.staff_id_seq')::text, 4, '0') || '-STA',
                    %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """

            self.db.execute_query(sql, (
                data["fname"],
                data["mname"],
                data["lname"],
                data["uname"],
                bcrypt.hash(data["pwd"]),
                data["pos"],
                psycopg2.Binary(self.binaryImage) if self.binaryImage else None,
                data["contact_person"],
                data["contact_number"]
            ))

            actionStr = f"Added a staff: {data['lname']}, {data['fname']} as {self.comboBox_position.currentText()}"
            sql  = "INSERT INTO cai.tbl_audit_trail(user_id, username, action)\n"
            sql += "VALUES (%s, %s, %s);\n"
            self.db.execute_query(sql, (user["school_id"], user["username"], actionStr))

            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to register user: {str(e)}")





class EditUserDialog(QDialog, Ui_EditUserDialog):

    def __init__(self, user:dict, school_id, mode=1):
        """
        Args:
            user (dict): The current user
            mode (int):
            1. User is updating his/her information.
            2. User is updating the information of other user.
        """
        super().__init__()
        self.setupUi(self)

        self.db = DatabaseTools()
        self.util = Utility()
        self.staff = Staff()

        sql = "SELECT\n"
        sql += "    position_id\n"
        sql += "    ,position_name\n"
        sql += "FROM cai.tbl_staff_positions\n"
        sql += "ORDER BY position_id ASC"
        self.util.populate_pulldown(self.comboBox_position, sql)

        self.binaryImage = None
        self.user = user
        self.mode = mode
        self.school_id = school_id
        self.profile_pic = self.staff.get_user_profile_pic(self.school_id, self.label_profile_pic.width())
        self.userObj = self.staff.get_user_info(self.school_id)

        if self.userObj:
            self.lineEdit_firstname.setText(self.userObj.get('firstname', ''))
            self.lineEdit_middlename.setText(self.userObj.get('middlename', ''))
            self.lineEdit_lastname.setText(self.userObj.get('lastname', ''))
            self.lineEdit_username.setText(self.userObj.get('username', ''))
            self.txtContactPerson.setText(self.userObj.get('contact_person', ''))
            self.txtContactNum.setText(self.userObj.get('contact_number', ''))

            sec_index = self.comboBox_position.findData(self.userObj.get('positionid', ''))
            if sec_index != -1:
                self.comboBox_position.setCurrentIndex(sec_index)

        if self.profile_pic:
            self.label_profile_pic.setPixmap(self.profile_pic)

        self.btnUploadPhoto.clicked.connect(self.update_photo)
        self.btnUpdate.clicked.connect(self.update_user)
        self.btnCancel.clicked.connect(self.reject)

    def update_photo(self):
        self.profile_pic, self.binaryImage = self.util.browsePhoto(self, self.label_profile_pic.width(), self.label_profile_pic.height())

        if self.profile_pic:
            w = self.label_profile_pic.width()
            self.label_profile_pic.setPixmap(self.util.makeCircularPixmap(self.profile_pic, w))

    def update_user(self):
        if self.mode == 1:
            reply = QMessageBox.question(
                self, "Profile Update",
                "Changing your profile requires a logout. Do you want to continue?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.No:
                return

        # 1. Collect data
        ui_data = {
            "fname": self.lineEdit_firstname.text().strip(),
            "mname": self.lineEdit_middlename.text().strip(),
            "lname": self.lineEdit_lastname.text().strip(),
            "uname": self.lineEdit_username.text().strip(),
            "pwd": self.lineEdit_password.text(),
            "pos": self.comboBox_position.currentData(),
            "contact_person": self.txtContactPerson.text().strip(),
            "contact_number": self.txtContactNum.text().strip()
        }

        # 2. Basic Validation: Required Fields
        required_fields = ["fname", "lname", "uname"]
        if not all(ui_data[field] for field in required_fields):
            QMessageBox.warning(self, "Validation Error", "All fields except Middle Name are required.")
            return

        # 3. Format Validation: Names (No numbers allowed)
        name_regex = r"^[a-zA-Z\s.-]+$"
        if not re.match(name_regex, ui_data["fname"]) or not re.match(name_regex, ui_data["lname"]):
            QMessageBox.warning(self, "Validation Error", "Names should only contain letters.")
            return

        # 4. Format Validation: Password Strength
        if ui_data["pwd"] and len(ui_data["pwd"]) < 6:
            QMessageBox.warning(self, "Validation Error", "Password must be at least 6 characters long.")
            return

        # 5. Database Validation: Duplicate Username
        if self.userObj["username"] != ui_data["uname"]: # When changes in username is done.
            check_query = "SELECT COUNT(*) FROM cai.tbl_staff_info WHERE username = %s"
            exists = self.db.fetch_all(check_query, (ui_data["uname"],))

            if exists and exists[0]['count'] > 0:
                QMessageBox.warning(self, "Validation Error", f"Username '{ui_data['uname']}' is already taken.")
                return

        # 6. Proceed to Registration
        try:
            sql  = 'UPDATE cai.tbl_staff_info\n'
            sql += "SET\n"
            sql += '    firstname = %s\n'
            sql += '    ,middlename = %s\n'
            sql += '    ,lastname = %s\n'

            params = [
                ui_data["fname"],
                ui_data["mname"],
                ui_data["lname"]
            ]

            if self.userObj["username"] != ui_data["uname"]:
                sql += '    ,username = %s\n'
                params.append(ui_data["uname"])

            if ui_data["pwd"]:
                sql += "    ,password = %s\n"
                params.append(bcrypt.hash(ui_data["pwd"]))

            sql += '    ,positionid = %s\n'

            params.append(ui_data["pos"])

            if self.binaryImage:
                sql += '    ,profile_pic = %s\n'
                params.append(psycopg2.Binary(self.binaryImage))

            sql += '    ,contact_person = %s\n'
            sql += '    ,contact_number = %s\n'

            params.extend([
                ui_data["contact_person"],
                ui_data["contact_number"]
            ])

            sql += "WHERE\n"
            sql += "    school_id = %s\n"

            params.append(self.userObj['school_id'])

            self.db.execute_query(sql, tuple(params))

            actionStr = f"Updated {ui_data['lname']}, {ui_data['fname']}'s information."
            sql  = "INSERT INTO cai.tbl_audit_trail(user_id, username, action)\n"
            sql += "VALUES (%s, %s, %s);\n"
            self.db.execute_query(sql, (self.user["school_id"], self.user["username"], actionStr))

            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to register user: {str(e)}")

