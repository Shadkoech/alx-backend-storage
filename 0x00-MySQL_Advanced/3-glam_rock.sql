-- SQL script that lists all bands with Glam rock as their main style
-- Ranking is by longevity

SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
FROM metal_bands
/*WHERE style = 'Glam rock'*/
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;