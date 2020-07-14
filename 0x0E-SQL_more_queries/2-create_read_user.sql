-- script that creates the database hbtn_0d_2 and the user user_0d_2.

CREATE DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_od_2_pwd@'localhost';
