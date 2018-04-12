SELECT *
FROM city_data
WHERE city IN ('Baltimore', 'San Francisco')
UNION ALL
SELECT year, 'global' AS city, 'global' AS country, avg_temp 
FROM global_data