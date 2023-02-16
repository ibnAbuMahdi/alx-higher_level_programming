-- 1 create user

-- create user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- create grant permissions
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
