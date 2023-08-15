-- The script displays the average temperature
--  by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
ORDER BY avg_temp DESC
