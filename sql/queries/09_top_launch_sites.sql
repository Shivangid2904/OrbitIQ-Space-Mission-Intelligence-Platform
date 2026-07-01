-- 09_top_launch_sites.sql
-- Retrieves the top 10 individual launch sites/facilities by launch count.

SELECT 
    l.location_name,
    l.launch_country,
    COUNT(*) AS total_launches
FROM fact_launches f
JOIN dim_location l ON f.location_id = l.location_id
GROUP BY l.location_name, l.launch_country
ORDER BY total_launches DESC
LIMIT 10;
