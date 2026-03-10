from CRUDTools import DatabaseTools

class Student:
    def __init__(self, student_id=None, firstname=None, middlename=None, lastname=None, section=None, gender=None):
        self.db_tools = DatabaseTools()

        self.student_id = student_id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.section = section
        self.gender = gender


    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.firstname} {self.middlename} {self.lastname}, Section: {self.section}, Gender: {self.gender})"

    def __repr__(self):
        return self.__str__()

    def register(self):
        self.db_tools.execute_query(
            "INSERT INTO cai.tbl_student_info (studentID, firstname, middlename, lastname, section, gender) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.student_id, self.firstname, self.middlename, self.lastname, self.section, self.gender)
        )

    def retrieve_student_info(self):
        query = "SELECT studentID, firstname, middlename, lastname, section, gender FROM cai.tbl_student_info WHERE studentID = %s"
        result = self.db_tools.fetch_all(query, (self.student_id,))
        
        if result:
            student_data = result[0]
            self.student_id = student_data['studentID']
            self.firstname = student_data['firstname']
            self.middlename = student_data['middlename']
            self.lastname = student_data['lastname']
            self.section = student_data['section']
            self.gender = student_data['gender']
        else:
            print(f"No student found with ID: {self.student_id}")
        
        self.db_tools.close_connection()

