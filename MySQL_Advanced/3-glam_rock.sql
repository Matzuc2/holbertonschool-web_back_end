-- Select the band name, lifespan where certain condition
SELECT band_name, (split - formed) AS lifespan
FROM metal_bands
WHERE split <= 2024
GROUP BY band_name, lifespan
ORDER BY lifespan DESC