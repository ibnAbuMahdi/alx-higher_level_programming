-- 9 full creation

-- create table second_table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	NAME varchar(256),
	score INT
)

-- insert values into second_table
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10), VALUES (2, "Alex", 3),
VALUES (3, "Bob", 14), VALUES (4, "George", 8)
