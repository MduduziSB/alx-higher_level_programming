-- This script creates the table id_not_null
-- This script does not fail if i_not_null table already exists
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
