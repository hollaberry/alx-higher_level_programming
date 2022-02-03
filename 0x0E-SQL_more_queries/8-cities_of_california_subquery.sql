-- lists all the cities of california that can be found in the database hbtn_0d_usa
-- id can be different as states table contain only one record where name = cal
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
