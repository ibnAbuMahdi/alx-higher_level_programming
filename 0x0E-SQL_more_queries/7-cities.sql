-- 7 create db hbtn_0d_usa and table cities

-- create db hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table cities
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
	-> state_id INTEGER NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
