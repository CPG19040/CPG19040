DROP TABLE IF EXISTS cai.tbl_staff_info_archive CASCADE;
CREATE TABLE cai.tbl_staff_info_archive (
    user_id           UUID PRIMARY KEY,
    school_id         VARCHAR(20),
    firstname         VARCHAR(50),
    middlename        VARCHAR(50),
    lastname          VARCHAR(50),
    username          VARCHAR(50),
    password          TEXT,
    position          VARCHAR(50),
    profile_pic       BYTEA,
    new_user          BOOLEAN,
    -- Essential metadata
    archived_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    archived_by       UUID
);
