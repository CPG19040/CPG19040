-- ===================================================
--   Database Privilege Matrix (PostgreSQL Grants)
-- ===================================================

-- Role Initialization
CREATE ROLE cai_student;
CREATE ROLE cai_teacher;
CREATE ROLE cai_admin;

GRANT USAGE ON SCHEMA cai TO cai_student, cai_teacher, cai_admin;

-- STUDENT ROLE GRANTS
GRANT SELECT ON cai.tbl_grading_period, cai.tbl_grading_system, cai.tbl_quiz_types TO cai_student;
GRANT SELECT ON cai.tbl_lessons, cai.tbl_quiz, cai.tbl_scoremultiplier TO cai_student;
GRANT SELECT ON cai.tbl_quizidentification, cai.tbl_quizmultiplechoice, cai.tbl_quiztrueorfalse TO cai_student;
GRANT SELECT ON cai.tbl_section TO cai_student;

GRANT SELECT, INSERT ON cai.tbl_answers TO cai_student;
GRANT SELECT, INSERT, UPDATE ON cai.tbl_quizscores TO cai_student;
GRANT SELECT, INSERT, UPDATE ON cai.tbl_progress TO cai_student;
GRANT INSERT ON cai.tbl_audit_trail TO cai_student;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA cai TO cai_student;

-- TEACHER ROLE GRANTS
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_lessons TO cai_teacher;
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_quiz TO cai_teacher;
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_quizidentification TO cai_teacher;
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_quizmultiplechoice TO cai_teacher;
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_quiztrueorfalse TO cai_teacher;
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_scoremultiplier TO cai_teacher;
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_section TO cai_teacher;

GRANT SELECT, UPDATE, DELETE ON cai.tbl_answers TO cai_teacher;
GRANT SELECT, UPDATE, DELETE ON cai.tbl_quizscores TO cai_teacher;
GRANT SELECT, INSERT ON cai.tbl_quizscores_archive TO cai_teacher;
GRANT SELECT ON cai.tbl_progress TO cai_teacher;
GRANT SELECT ON cai.tbl_grading_period, cai.tbl_grading_system, cai.tbl_quiz_types TO cai_teacher;
GRANT INSERT ON cai.tbl_audit_trail TO cai_teacher;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA cai TO cai_teacher;

-- ADMIN ROLE GRANTS
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA cai TO cai_admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA cai TO cai_admin;



-- ===================================================
--   Data Isolation Policies (Row-Level Security)
-- ===================================================

-- Enable RLS on primary transactional tables
ALTER TABLE cai.tbl_quiz ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_answers ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quizscores ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_progress ENABLE ROW LEVEL SECURITY;

-- Policy 1: Quiz Publication Filtering
CREATE POLICY p_quiz_student_read ON cai.tbl_quiz
    FOR SELECT TO cai_student
    USING (publish = TRUE);

CREATE POLICY p_quiz_staff_all ON cai.tbl_quiz
    FOR ALL TO cai_teacher, cai_admin
    USING (TRUE);

-- Policy 2: Row Isolation by Session Variable (app.current_student_id)
CREATE POLICY p_answers_student_isolation ON cai.tbl_answers
    FOR ALL TO cai_student
    USING (studentid = current_setting('app.current_student_id', true))
    WITH CHECK (studentid = current_setting('app.current_student_id', true));

CREATE POLICY p_scores_student_isolation ON cai.tbl_quizscores
    FOR ALL TO cai_student
    USING (studentid = current_setting('app.current_student_id', true))
    WITH CHECK (studentid = current_setting('app.current_student_id', true));

CREATE POLICY p_progress_student_isolation ON cai.tbl_progress
    FOR ALL TO cai_student
    USING (studentid = current_setting('app.current_student_id', true))
    WITH CHECK (studentid = current_setting('app.current_student_id', true));

-- Staff Bypasses
CREATE POLICY p_answers_staff_all ON cai.tbl_answers FOR ALL TO cai_teacher, cai_admin USING (TRUE);
CREATE POLICY p_scores_staff_all ON cai.tbl_quizscores FOR ALL TO cai_teacher, cai_admin USING (TRUE);
CREATE POLICY p_progress_staff_all ON cai.tbl_progress FOR ALL TO cai_teacher, cai_admin USING (TRUE);