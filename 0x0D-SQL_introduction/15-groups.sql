--15 groups

--list scores grouped and sorted by frequency in second_table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY COUNT(score) DESC
