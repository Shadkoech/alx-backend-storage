-- SQL script that ranks country origins of bands
-- Order is by the number of (non-unique) fans
-- Column names must be: origin and nb_fans

SELECT origin, SUM(fans) AS nb_fans -- Calculate the total number of fans for each country origin
FROM metal_bands 
GROUP BY origin
ORDER BY nb_fans DESC;