-- list all records of the table second_table of the database hbtn-0c_0 in your MySQL server
-- Don't list rows withour a name value
SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL ORDER BY `score` DESC;
