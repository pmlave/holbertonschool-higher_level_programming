-- Create a database and a table with specific entry values
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE NOT NULL,
name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
