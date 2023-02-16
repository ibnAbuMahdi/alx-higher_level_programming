-- 6 create db hbtn_0d_usa and table states

-- create db hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL,
	name VARCHAR(256),
	UNIQUE (id),
	PRIMARY KEY (id)
)
