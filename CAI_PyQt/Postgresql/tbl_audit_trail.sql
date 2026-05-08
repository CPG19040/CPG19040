-- Remove the table and its associated indexes if they already exist
DROP TABLE IF EXISTS cai.tbl_audit_trail CASCADE;

-- Create the table
CREATE TABLE cai.tbl_audit_trail (
    audit_id    INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id     VARCHAR(50), 
    username    VARCHAR(50),
    date_logged TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    action      TEXT NOT NULL
);

-- Re-create the indexes
CREATE INDEX idx_audit_date ON cai.tbl_audit_trail (date_logged);
CREATE INDEX idx_audit_user ON cai.tbl_audit_trail (user_id);