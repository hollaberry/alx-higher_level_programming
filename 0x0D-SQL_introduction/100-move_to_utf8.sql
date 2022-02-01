-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
-- converts database to utf8
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- convert table to 'first_table'
USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- converts a field in a table to utf8
USE hbtn_0c_0;
ALTER TABLE first_table
CHANGE name name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
