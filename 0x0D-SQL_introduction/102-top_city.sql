-- The script displays the top 3 of cities temperature
-- during July and August
-- ordered by temperature (descending)
SELECT `city`, `value` AS `avg_temp`
FROM `temperatures`
WHERE `month` IN (7,8)
ORDER BY `avg_temp` DESC
LIMIT 3;
