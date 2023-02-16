-- 4 never empty

-- create table id_not_null
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 AUTO_INCREMENT,
	name VARCHAR(256),
	UNIQUE (id)
)
