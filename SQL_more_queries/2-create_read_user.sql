-- create the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT exists hbtn_0d_2;
CREATE USER IF NOT exists "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
