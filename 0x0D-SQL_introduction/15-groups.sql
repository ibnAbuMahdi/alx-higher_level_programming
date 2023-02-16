--15 groups

--list scores grouped and sorted by frequency in second_table
SELECT score, COUNT(score) AS number GROUP BY score, number ORDER BY number DESC
