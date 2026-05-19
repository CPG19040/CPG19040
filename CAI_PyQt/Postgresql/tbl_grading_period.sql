DROP TABLE IF EXISTS cai.tbl_grading_period;

CREATE TABLE cai.tbl_grading_period
(
    gpid       INTEGER NOT NULL PRIMARY KEY,
    gpname     VARCHAR(50) NOT NULL,
    startdate  DATE
);

INSERT INTO cai.tbl_grading_period (GPID, GPNAME) VALUES 
(1, 'First Grading'),
(2, 'Second Grading'),
(3, 'Third Grading'),
(4, 'Fourth Grading');