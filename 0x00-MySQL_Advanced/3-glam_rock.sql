-- lists all bands with Glam rock as their
-- main style, ranked by their longevity
SELECT band_name,
	CASE
        	WHEN formed > 0 AND (split IS NULL) THEN (2022 - formed)
		WHEN formed > 0 AND split IS NOT NULL AND split <= 2022 THEN (split - formed)
		ELSE 0
	END AS lifespan
	FROM metal_bands
	WHERE style LIKE '%Glam rock%'
	ORDER BY lifespan DESC;
