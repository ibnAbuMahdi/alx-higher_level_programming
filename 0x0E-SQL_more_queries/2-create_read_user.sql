-- 2 create read user

-- create db hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- drop user if exists
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- create user user_0d_2
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant select privilege to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;


