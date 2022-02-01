-- displays the top 3 of cities temperature during July and August ordered by temprature
-- cities with the highest tempratures
SELECT `city`, AVG(`value`) 'avg_temp' FROM `temperatures` WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
