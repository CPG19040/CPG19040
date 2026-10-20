-- Run as the database owner or a role with CREATEROLE and grant privileges.
-- These are capability roles, not login accounts. Never connect the desktop apps
-- as postgres, a table owner, or a role with BYPASSRLS.
--
-- IMPORTANT: app.current_student_id and app.current_staff_id are client-settable
-- PostgreSQL settings. They are defense-in-depth only, not authenticated identity.
-- Do not treat these policies as tenant isolation until identity is supplied by a
-- trusted server-side API/database function. The current desktop clients connect
-- directly and must be updated before this policy can safely replace broad access.

BEGIN;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = 'cai_student') THEN
        CREATE ROLE cai_student;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = 'cai_teacher') THEN
        CREATE ROLE cai_teacher;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = 'cai_admin') THEN
        CREATE ROLE cai_admin;
    END IF;
END
$$;

ALTER ROLE cai_student NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS NOINHERIT;
ALTER ROLE cai_teacher NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS NOINHERIT;
ALTER ROLE cai_admin NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS NOINHERIT;

REVOKE ALL ON SCHEMA cai FROM PUBLIC;
REVOKE CREATE ON SCHEMA cai FROM cai_student, cai_teacher, cai_admin;
GRANT USAGE ON SCHEMA cai TO cai_student, cai_teacher, cai_admin;

REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA cai
    FROM PUBLIC, cai_student, cai_teacher, cai_admin;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA cai
    FROM PUBLIC, cai_student, cai_teacher, cai_admin;
REVOKE EXECUTE ON ALL FUNCTIONS IN SCHEMA cai FROM PUBLIC;

-- Students may read published lessons/quizzes and non-answer quiz content.
GRANT SELECT ON cai.tbl_grading_period, cai.tbl_grading_system, cai.tbl_quiz_types,
    cai.tbl_lessons, cai.tbl_quiz, cai.tbl_scoremultiplier, cai.tbl_section
    TO cai_student;
GRANT SELECT (idkey, itemno, question, imagequestion, difficultylevel)
    ON cai.tbl_quizidentification TO cai_student;
GRANT SELECT (mckey, itemno, question, imagequestion, choice_a, choice_b, choice_c, difficultylevel)
    ON cai.tbl_quizmultiplechoice TO cai_student;
GRANT SELECT (tfkey, itemno, question, imagequestion, difficultylevel)
    ON cai.tbl_quiztrueorfalse TO cai_student;
GRANT SELECT, INSERT, DELETE ON cai.tbl_answers TO cai_student;
GRANT SELECT ON cai.tbl_quizscores TO cai_student;
GRANT SELECT, INSERT, UPDATE ON cai.tbl_progress TO cai_student;
GRANT USAGE ON SEQUENCE cai.tbl_answers_answerid_seq, cai.tbl_progress_pid_seq
    TO cai_student;
GRANT SELECT (school_year, studentid, lastname, firstname, middlename, sectionid,
    gender, profile_pic) ON cai.tbl_student_info TO cai_student;

-- Teachers manage instructional content and their assigned section rosters.
GRANT SELECT ON cai.tbl_grading_period, cai.tbl_grading_system, cai.tbl_quiz_types,
    cai.tbl_staff_positions TO cai_teacher;
GRANT SELECT, INSERT, UPDATE, DELETE ON cai.tbl_lessons, cai.tbl_quiz,
    cai.tbl_quizidentification, cai.tbl_quizmultiplechoice,
    cai.tbl_quiztrueorfalse, cai.tbl_scoremultiplier, cai.tbl_section,
    cai.tbl_student_info TO cai_teacher;
GRANT SELECT (school_id, firstname, middlename, lastname, username, positionid,
    profile_pic, contact_person, contact_number, new_user)
    ON cai.tbl_staff_info TO cai_teacher;
GRANT SELECT, UPDATE, DELETE ON cai.tbl_answers TO cai_teacher;
GRANT SELECT, UPDATE, DELETE ON cai.tbl_quizscores TO cai_teacher;
GRANT SELECT ON cai.tbl_progress TO cai_teacher;
GRANT INSERT ON cai.tbl_student_info_archive, cai.tbl_staff_info_archive,
    cai.tbl_audit_trail TO cai_teacher;
GRANT SELECT, INSERT ON cai.tbl_quizscores_archive TO cai_teacher;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA cai TO cai_teacher;

-- Keep staff/account administration and archive reads with the admin capability.
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA cai TO cai_admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA cai TO cai_admin;

-- Enable and force RLS so table owners are subject to policies too.
ALTER TABLE cai.tbl_quiz ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quiz FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quizidentification ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quizidentification FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quizmultiplechoice ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quizmultiplechoice FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quiztrueorfalse ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quiztrueorfalse FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_answers ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_answers FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quizscores ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_quizscores FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_progress FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_staff_info ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_staff_info FORCE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_student_info ENABLE ROW LEVEL SECURITY;
ALTER TABLE cai.tbl_student_info FORCE ROW LEVEL SECURITY;

-- Make reruns safe and replace the previous, incomplete policy definitions.
DROP POLICY IF EXISTS p_quiz_student_read ON cai.tbl_quiz;
DROP POLICY IF EXISTS p_quiz_staff_all ON cai.tbl_quiz;
DROP POLICY IF EXISTS p_quizid_student_published ON cai.tbl_quizidentification;
DROP POLICY IF EXISTS p_quizid_staff_all ON cai.tbl_quizidentification;
DROP POLICY IF EXISTS p_quizmc_student_published ON cai.tbl_quizmultiplechoice;
DROP POLICY IF EXISTS p_quizmc_staff_all ON cai.tbl_quizmultiplechoice;
DROP POLICY IF EXISTS p_quiztf_student_published ON cai.tbl_quiztrueorfalse;
DROP POLICY IF EXISTS p_quiztf_staff_all ON cai.tbl_quiztrueorfalse;
DROP POLICY IF EXISTS p_answers_student_isolation ON cai.tbl_answers;
DROP POLICY IF EXISTS p_answers_staff_all ON cai.tbl_answers;
DROP POLICY IF EXISTS p_scores_student_isolation ON cai.tbl_quizscores;
DROP POLICY IF EXISTS p_scores_staff_all ON cai.tbl_quizscores;
DROP POLICY IF EXISTS p_progress_student_isolation ON cai.tbl_progress;
DROP POLICY IF EXISTS p_progress_staff_all ON cai.tbl_progress;
DROP POLICY IF EXISTS staff_isolation_policy ON cai.tbl_staff_info;
DROP POLICY IF EXISTS p_staff_teacher_self ON cai.tbl_staff_info;
DROP POLICY IF EXISTS p_staff_admin_all ON cai.tbl_staff_info;
DROP POLICY IF EXISTS student_teacher_isolation ON cai.tbl_student_info;
DROP POLICY IF EXISTS p_student_self ON cai.tbl_student_info;
DROP POLICY IF EXISTS student_admin_all ON cai.tbl_student_info;

CREATE POLICY p_quiz_student_read ON cai.tbl_quiz
    FOR SELECT TO cai_student USING (publish IS TRUE);
CREATE POLICY p_quiz_staff_all ON cai.tbl_quiz
    FOR ALL TO cai_teacher, cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY p_quizid_student_published ON cai.tbl_quizidentification
    FOR SELECT TO cai_student
    USING (EXISTS (
        SELECT 1 FROM cai.tbl_quiz q
                WHERE q.quiznumber = tbl_quizidentification.quiznumber
                    AND q.gradingperiod = tbl_quizidentification.gradingperiod
                    AND q.lessonid = tbl_quizidentification.lessonid
          AND q.publish IS TRUE
    ));
CREATE POLICY p_quizid_staff_all ON cai.tbl_quizidentification
    FOR ALL TO cai_teacher, cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY p_quizmc_student_published ON cai.tbl_quizmultiplechoice
    FOR SELECT TO cai_student
    USING (EXISTS (
        SELECT 1 FROM cai.tbl_quiz q
                WHERE q.quiznumber = tbl_quizmultiplechoice.quiznumber
                    AND q.gradingperiod = tbl_quizmultiplechoice.gradingperiod
                    AND q.lessonid = tbl_quizmultiplechoice.lessonid
          AND q.publish IS TRUE
    ));
CREATE POLICY p_quizmc_staff_all ON cai.tbl_quizmultiplechoice
    FOR ALL TO cai_teacher, cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY p_quiztf_student_published ON cai.tbl_quiztrueorfalse
    FOR SELECT TO cai_student
    USING (EXISTS (
        SELECT 1 FROM cai.tbl_quiz q
                WHERE q.quiznumber = tbl_quiztrueorfalse.quiznumber
                    AND q.gradingperiod = tbl_quiztrueorfalse.gradingperiod
                    AND q.lessonid = tbl_quiztrueorfalse.lessonid
          AND q.publish IS TRUE
    ));
CREATE POLICY p_quiztf_staff_all ON cai.tbl_quiztrueorfalse
    FOR ALL TO cai_teacher, cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY p_answers_student_isolation ON cai.tbl_answers
    FOR ALL TO cai_student
    USING (studentid = NULLIF(current_setting('app.current_student_id', TRUE), ''))
    WITH CHECK (studentid = NULLIF(current_setting('app.current_student_id', TRUE), ''));
CREATE POLICY p_answers_staff_all ON cai.tbl_answers
    FOR ALL TO cai_teacher, cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY p_scores_student_isolation ON cai.tbl_quizscores
    FOR SELECT TO cai_student
    USING (studentid = NULLIF(current_setting('app.current_student_id', TRUE), ''));
CREATE POLICY p_scores_staff_all ON cai.tbl_quizscores
    FOR ALL TO cai_teacher, cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY p_progress_student_isolation ON cai.tbl_progress
    FOR ALL TO cai_student
    USING (studentid = NULLIF(current_setting('app.current_student_id', TRUE), ''))
    WITH CHECK (studentid = NULLIF(current_setting('app.current_student_id', TRUE), ''));
CREATE POLICY p_progress_staff_all ON cai.tbl_progress
    FOR ALL TO cai_teacher, cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY p_staff_teacher_self ON cai.tbl_staff_info
    FOR SELECT TO cai_teacher
    USING (school_id = NULLIF(current_setting('app.current_staff_id', TRUE), ''));
CREATE POLICY p_staff_admin_all ON cai.tbl_staff_info
    FOR ALL TO cai_admin USING (TRUE) WITH CHECK (TRUE);

CREATE POLICY student_teacher_isolation ON cai.tbl_student_info
    FOR ALL TO cai_teacher
    USING (sectionid IN (
        SELECT sectionid FROM cai.tbl_section
        WHERE teacherid = NULLIF(current_setting('app.current_staff_id', TRUE), '')
    ))
    WITH CHECK (sectionid IN (
        SELECT sectionid FROM cai.tbl_section
        WHERE teacherid = NULLIF(current_setting('app.current_staff_id', TRUE), '')
    ));
CREATE POLICY p_student_self ON cai.tbl_student_info
    FOR SELECT TO cai_student
    USING (studentid = NULLIF(current_setting('app.current_student_id', TRUE), ''));
CREATE POLICY student_admin_all ON cai.tbl_student_info
    FOR ALL TO cai_admin USING (TRUE) WITH CHECK (TRUE);

COMMIT;