DROP TABLE IF EXISTS cai.tbl_staff_positions;

CREATE TABLE cai.tbl_staff_positions (
    position_id SERIAL PRIMARY KEY,
    position_name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO cai.tbl_staff_positions (position_name) 
VALUES ('Admin'), ('Teacher'), ('Substitute'), ('Others');
