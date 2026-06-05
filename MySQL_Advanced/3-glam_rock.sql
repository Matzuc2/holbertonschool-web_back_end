-- Select the band name and lifespan of bands with Glam rock style
SELECT band_name, (COALESCE(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;