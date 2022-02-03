-- Display top 3 cities temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month BETWEEN July AND August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
