-- Create database and table
-- DDL query
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- set db to new db
USE hbtn_0d_usa;
-- create new table
CREATE TABLE IF NOT EXISTS states(id INT AUTO_INCREMENT UNIQUE, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
