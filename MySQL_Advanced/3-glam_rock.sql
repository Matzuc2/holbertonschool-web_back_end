-- Select the band name, lifespan where certain condition
SELECT band_name, (COALESCE(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;