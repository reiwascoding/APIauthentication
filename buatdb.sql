CREATE DATABASE loguserapp;
CREATE USER 'userapp'@'localhost' IDENTIFIED BY 'user1234';
GRANT ALL PRIVILEGES ON loguserapp.* TO 'userapp'@'localhost';
FLUSH PRIVILEGES;