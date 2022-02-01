-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
-- list in descending order sort
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
