CREATE DATABASE hbnb_test_db IF NOT EXISTS;
CREATE USER 'hbnb_test_user'@'localhost' IDENTIFIED BY 'hbnb_test_pwd' IF NOT EXISTS;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test_user'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_test_user'@'localhost';