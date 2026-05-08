CREATE TABLE cai.tbl_lessons (
    lesson_id       SERIAL PRIMARY KEY,
    chapter         INT,
    lessonnum       INT,
    gradingperiod   INT,
    title           TEXT,
    path_str        TEXT,
    lessonimages    BYTEA,
    lessonfilename  TEXT
);
