-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id PRIMARY KEY INT NOT NULL AUTO_INCREMENT,
state_id INT FOREIGN KEY REFERENCES hbtn_0d_usa.states(id)  NOT NULL,
name VARCHAR(256) NOT NULL);
