import os, subprocess

from App.CRUDTools import DatabaseTools
from App.Tools import Utility

from docxtpl import DocxTemplate


class StudentListReporter:
    def __init__(self):
        template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Templates")
        self.studentlist_template_path = os.path.join(template_path, "student_list.docx")
        self.classlist_template_path = os.path.join(template_path, "class_list.docx")

        self.db_tools = DatabaseTools()
        self.util = Utility()

    def generate_studentlist_report(self, section_id, output_pdf_path):
        """Fetches student data, merges using docxtpl, and converts to PDF."""

        # 1. Fetch data from PostgreSQL
        query = """
            SELECT
                s.userid,
                s.studentid,
                s.lastname,
                s.firstname,
                s.middlename,
                s.school_year,
                s.gender,

                sec.sectionname,

                st.school_id AS teacher_id,
                st.firstname AS teacher_firstname,
                st.middlename AS teacher_middlename,
                st.lastname AS teacher_lastname
            FROM
                CAI.TBL_STUDENT_INFO s
            LEFT JOIN
                cai.tbl_section sec ON s.sectionid = sec.sectionid
            LEFT JOIN
                cai.tbl_staff_info st ON sec.teacherid = st.school_id
            WHERE 1 = 1
        """
        params = []
        if section_id:
            query += """
                AND s.sectionid = %s
            """
            params.append(section_id)

        query += """
            ORDER BY sec.sectionname ASC, s.gender DESC, s.lastname ASC, s.firstname ASC;
        """

        try:
            students = self.db_tools.fetch_all(query, tuple(params))

            if not students:
                return False, "No students found in this section."

            # 2. Extract header variables
            school_year = students[0]['school_year']
            section_name = students[0]['sectionname']

            # 3. Build the student list array
            student_rows = []
            for idx, student in enumerate(students, start=1):
                student_rows.append({
                    'idx': str(idx),
                    'studentid': str(student['studentid']),
                    'fullname': self.util.formatFullname(student['firstname'], student['middlename'], student['lastname'], 1),
                    'gender': str(student['gender'] or 'N/A'),
                    'sectionname': student['sectionname']
                })

            # 4. Render the template using docxtpl
            temp_docx = os.path.abspath("temp_output.docx")

            if not section_id:
                doc = DocxTemplate(self.studentlist_template_path)
                context = {
                    'school_year': school_year,
                    'sectionname': section_name,
                    'students': student_rows
                }
                doc.render(context)
                doc.save(temp_docx)

            else:
                doc = DocxTemplate(self.classlist_template_path)
                context = {
                    'school_year': school_year,
                    'sectionname': section_name,
                    'teachername': self.util.formatFullname(student['teacher_firstname'], student['teacher_middlename'], student['teacher_lastname']),
                    'students': student_rows
                }
                doc.render(context)
                doc.save(temp_docx)

            # 5. Convert Docx to PDF via LibreOffice Headless
            try:
                output_dir = os.path.dirname(os.path.abspath(output_pdf_path))

                cmd = [
                    'soffice',
                    '--headless',
                    '--convert-to', 'pdf',
                    '--outdir', output_dir,
                    temp_docx
                ]

                subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                generated_pdf = os.path.join(output_dir, "temp_output.pdf")
                if os.path.exists(generated_pdf):
                    if os.path.exists(output_pdf_path):
                        os.remove(output_pdf_path)
                    os.rename(generated_pdf, output_pdf_path)
                else:
                    return False, "LibreOffice ran but the output PDF was not found."

            except subprocess.CalledProcessError as e:
                return False, f"LibreOffice rendering failed: {e.stderr.decode()}"

            finally:
                # Clean up temporary file
                if os.path.exists(temp_docx):
                    os.remove(temp_docx)

            return True, f"Report successfully saved to:\n{output_pdf_path}"

        except Exception as e:
            return False, f"An error occurred: {str(e)}"



class QuizReporter:
    """
        Quiz Report Automation Script (Zorin OS / Linux compatible)
        Generates styled Word Templates from DB and converts them directly to PDF.
    """
    def __init__(self):
        template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Templates")
        self.quizscores_template_path = os.path.join(template_path, "quiz_report.docx")

        self.db_tools = DatabaseTools()
        self.util = Utility()

    def generate_quizscores_report(self, studentid, remarks, output_pdf_path):
        """Fetches student data, merges using docxtpl, and converts to PDF."""

        from App.Quiz import Quiz

        model1, average_percentage1 = Quiz().get_scores(studentid, 1)
        model2, average_percentage2 = Quiz().get_scores(studentid, 2)
        model3, average_percentage3 = Quiz().get_scores(studentid, 3)
        model4, average_percentage4 = Quiz().get_scores(studentid, 4)
        
        if not (model1 and model2 and model3 and model4):
            return False, "No quiz scores record found."

        # 1. Fetch data from PostgreSQL
        query = """
            SELECT
                s.userid,
                s.studentid,
                s.lastname,
                s.firstname,
                s.middlename,
                s.school_year,
                s.gender,

                sec.sectionname,

                st.school_id AS teacher_id,
                st.firstname AS teacher_firstname,
                st.middlename AS teacher_middlename,
                st.lastname AS teacher_lastname
            FROM
                CAI.TBL_STUDENT_INFO s
            LEFT JOIN
                cai.tbl_section sec ON s.sectionid = sec.sectionid
            LEFT JOIN
                cai.tbl_staff_info st ON sec.teacherid = st.school_id
            WHERE s.studentid = %s;
        """

        try:
            students = self.db_tools.fetch_all(query, (studentid,))

            if not students:
                return False, "No students found in this section."

            # 2. Extract header variables
            first_name = students[0]['firstname']
            middle_name = students[0]['middlename']
            last_name = students[0]['lastname']
            school_year = students[0]['school_year']
            section_name = students[0]['sectionname']
            teacher_name = self.util.formatFullname(students[0]['teacher_firstname'], students[0]['teacher_middlename'], students[0]['teacher_lastname'])

            models = {1: model1, 2: model2, 3: model3, 4: model4}
            scores = {idx: [] for idx in models}

            for idx, model in models.items():
                for row in range(model.rowCount()):
                    scores[idx].append({
                        "quiz_no"      : model.index(row, 0).data(),
                        "lesson_id"    : model.index(row, 1).data(),
                        "lesson_title" : model.index(row, 2).data(),
                        "quiz_score"   : model.index(row, 3).data(),
                        "total_items"  : model.index(row, 4).data(),
                        "date_taken"   : model.index(row, 5).data()
                    })

            temp_docx = os.path.abspath("temp_output.docx")

            doc = DocxTemplate(self.quizscores_template_path)
            context = {
                'studentname': self.util.formatFullname(first_name, middle_name, last_name, 1),
                'studentid': studentid,
                'schoolyear': school_year,
                'sectionname': section_name,
                'teachername': teacher_name,
                'teacher_remark': remarks,
                'quizzes1': scores[1],
                'quizzes2': scores[2],
                'quizzes3': scores[3],
                'quizzes4': scores[4],
                'total1': average_percentage1,
                'total2': average_percentage2,
                'total3': average_percentage3,
                'total4': average_percentage4,
            }
            doc.render(context)
            doc.save(temp_docx)

            try:
                output_dir = os.path.dirname(os.path.abspath(output_pdf_path))

                cmd = [
                    'soffice',
                    '--headless',
                    '--convert-to', 'pdf',
                    '--outdir', output_dir,
                    temp_docx
                ]

                subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                generated_pdf = os.path.join(output_dir, "temp_output.pdf")
                if os.path.exists(generated_pdf):
                    if os.path.exists(output_pdf_path):
                        os.remove(output_pdf_path)
                    os.rename(generated_pdf, output_pdf_path)
                else:
                    return False, "LibreOffice ran but the output PDF was not found."

            except subprocess.CalledProcessError as e:
                return False, f"LibreOffice rendering failed: {e.stderr.decode()}"

            finally:
                # Clean up temporary file
                if os.path.exists(temp_docx):
                    os.remove(temp_docx)

            return True, f"Report successfully saved to:\n{output_pdf_path}"

        except Exception as e:
            return False, f"An error occurred: {str(e)}"


