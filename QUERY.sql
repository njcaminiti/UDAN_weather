SELECT year, city, avg_temp
FROM city_data
WHERE city = 'Baltimore'
UNION ALL
SELECT year, 'global' AS city, avg_temp 
FROM global_data