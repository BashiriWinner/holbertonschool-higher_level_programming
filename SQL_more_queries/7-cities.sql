-- create the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT exists hbtn_0d_usa;
CREATE TABLE IF NOT exists hbtn_0d_usa.cities(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, 
state_id INT NOT NULL , name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
