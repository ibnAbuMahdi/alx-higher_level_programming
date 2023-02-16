-- 8 cities of California

-- get cities California from cities with id from states
SELECT id, name FROM cities WHERE state_id=(
	SELECT id FROM states WHERE name='California';
)
 ORDER BY cities.id ASC
