-- create the database hbtn_0d_usa and the table states
-- states with description and id is unique
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
Use hbtn_0d_usa;
-- create the table with description
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id))
