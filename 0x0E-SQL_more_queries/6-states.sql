-- creates the database hbtn_0d_usa
-- creates the table hbtn_0d_usa

CREATE DATABASE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT unique PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL)