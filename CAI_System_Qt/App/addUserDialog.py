import datetime, re
from PyQt6.QtWidgets import QDialog, QMessageBox
from passlib.hash import bcrypt
from FormAddNewUser import Ui_AddNewUserDialog
from ClassStaff import Staff

class AddUserDialog(QDialog, Ui_AddNewUserDialog):
    def __init__(self, database_tools):
        super().__init__()
        self.setupUi(self)
        self.db = database_tools
        self.setup_ui_elements()
        self.btnSave.clicked.connect(self.register_user)

    def setup_ui_elements(self):
        positions = self.db.fetch_all("SELECT DISTINCT position_id, position_name FROM cai.staff_positions ORDER BY position_id ASC")
        for pos in positions:
            self.comboBox_position.addItem(pos['position_name'], pos['position_id'])

        self.comboBox_recoveryQuestion.addItems([
            "What is your mother's maiden name?",
            "What was the name of your first pet?",
            "What was the make of your first car?"
        ])

    def register_user(self):
        # 1. Collect data
        data = {
            "fname": self.lineEdit_firstname.text().strip(),
            "mname": self.lineEdit_middlename.text().strip(),
            "lname": self.lineEdit_lastname.text().strip(),
            "uname": self.lineEdit_username.text().strip(),
            "pwd": self.lineEdit_password.text(),
            "pos": self.comboBox_position.currentText(),
            "q": self.comboBox_recoveryQuestion.currentText(),
            "a": self.lineEdit_Answer.text().strip()
        }

        # 2. Basic Validation: Required Fields
        required_fields = ["fname", "lname", "uname", "pwd", "a"]
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
            cur = self.db.retrieve_records("SELECT COUNT(*) FROM cai.tbl_staff_info")
            count = cur.fetchone()[0] if cur else 0

            new_staff = Staff(
                school_id=self.generate_id(count),
                firstname=data["fname"],
                middlename=data["mname"],
                lastname=data["lname"],
                username=data["uname"],
                password=bcrypt.hash(data["pwd"]),
                position=data["pos"],
                RecoveryQuestion=data["q"],
                RecoveryAnswer=data["a"]
            )

            new_staff.register()
            QMessageBox.information(self, "Success", "User registered successfully!")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to register user: {str(e)}")

    def generate_id(self, count):
        return f"{datetime.datetime.now().year}-{(count + 1):04d}-STA"