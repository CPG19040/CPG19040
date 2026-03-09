from CRUDTools import DatabaseTools

class Staff:
    def __init__(self, school_id=None, firstname=None, middlename=None, lastname=None, username=None, password=None, position=None, RecoveryQuestion=None, RecoveryAnswer=None):
        self.db_tools = DatabaseTools()

        self.school_id = school_id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.username = username
        self.password = password
        self.position = position
        self.RecoveryQuestion = RecoveryQuestion
        self.RecoveryAnswer = RecoveryAnswer


    def __str__(self):
        return f"Staff(ID: {self.school_id}, Name: {self.firstname} {self.middlename} {self.lastname}, Position: {self.position})"

    def __repr__(self):
        return self.__str__()

    def register(self):
        self.db_tools.execute_query(
            "INSERT INTO cai.tbl_staff_info (school_id, firstname, middlename, lastname, username, password, position, recovery_question, answer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (self.school_id, self.firstname, self.middlename, self.lastname, self.username, self.password, self.position, self.RecoveryQuestion, self.RecoveryAnswer)   )  
