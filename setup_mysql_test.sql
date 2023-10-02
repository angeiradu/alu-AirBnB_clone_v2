--script to create database hbnb_test_db
--also creates user hbnb_test_user on localhost
--grants all privileges to user on hbnb_test_db
--grants select access to user on performance_schema database
CREATE DATABASE hbnb_test_db IF NOT EXISTS;
CREATE USER 'hbnb_test_user'@'localhost' IDENTIFIED BY 'hbnb_test_pwd' IF NOT EXISTS;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test_user'@'localhost';