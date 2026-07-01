-- 05_rank_launch_sites_reliability.sql
-- Ranks launch locations by their launch success rate using DENSE_RANK() for locations with >= 5 launches.

WITH site_reliability AS (
    SELECT 
        l.location_name,
        l.launch_country,
        COUNT(*) AS total_launches,
        SUM(f.is_success) AS successful_launches,
        ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage
    FROM fact_launches f
    JOIN dim_location l ON f.location_id = l.location_id
    GROUP BY l.location_name, l.launch_country
    HAVING COUNT(*) >= 5
)
SELECT 
    location_name,
    launch_country,
    total_launches,
    successful_launches,
    success_rate_percentage,
    DENSE_RANK() OVER (ORDER BY success_rate_percentage DESC, total_launches DESC) AS reliability_rank
FROM site_reliability;
