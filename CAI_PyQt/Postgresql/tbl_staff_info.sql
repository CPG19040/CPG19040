DROP TABLE IF EXISTS cai.tbl_staff_info CASCADE;
CREATE TABLE cai.tbl_staff_info (
    -- Set as PRIMARY KEY and auto-generate the ID
    user_id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    school_id         VARCHAR(20) UNIQUE,
    firstname         VARCHAR(50),
    middlename        VARCHAR(50),
    lastname          VARCHAR(50),
    username          VARCHAR(50) UNIQUE, -- UNIQUE for better security
    password          TEXT,               -- TEXT for hashed passwords
    positionid        INTEGER,
    profile_pic       BYTEA,
    contact_person    VARCHAR(255),
    contact_number    VARCHAR(20),
    new_user          BOOLEAN NOT NULL DEFAULT TRUE
);

DROP SEQUENCE IF EXISTS cai.staff_id_seq;
CREATE SEQUENCE cai.staff_id_seq
    START WITH 1
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9999
    CYCLE;
