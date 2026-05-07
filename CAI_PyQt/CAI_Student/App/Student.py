from App.CRUDTools import DatabaseTools
from App.Tools import Utility

class Student:
    def __init__(self):
        self.util = Utility()
        self.profile_pic = None
        self.binaryImage = None
        self.db_tools = DatabaseTools()

    def retrieve_sections(self):
        sql = 'SELECT\n'
        sql += '    sectionid AS index\n'
        sql += '    ,sectionname AS itemname\n'
        sql += 'FROM cai.tbl_section\n'
        sql += 'ORDER BY sectionname ASC'
        cursor, conn = self.db_tools.retrieve_records(sql)

        if cursor:
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records

        conn.close()
        return list()

    def retrieve_student_info(self, sectionid):
        sql = 'SELECT\n'
        sql += '    studentid\n'
        sql += '    ,firstname \n'
        sql += '    ,middlename\n'
        sql += '    ,lastname\n'
        sql += '    ,sectionid\n'
        sql += '    ,gender\n'
        sql += '    ,password\n'
        sql += '    ,profile_pic\n'
        sql += 'FROM cai.tbl_student_info\n'
        sql += 'WHERE sectionid = %s\n'
        sql += 'ORDER BY lastname ASC'
        cursor, conn = self.db_tools.retrieve_records(sql, (sectionid,))

        if cursor:
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records

        conn.close()
        return list()  # Return an empty list if no records are found

    def retrieve_one_student_info(self, student_id):
        """tuple(studentid, lastname, firstname, middlename, sectionname, gender, password, profile_pic, contact_person, contact_number)"""
        
        if not student_id:
            return tuple([""] * 10)  # Return a tuple with 10 empty string values if no record is found
            
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

        conn.close()
        return tuple([""] * 10)
