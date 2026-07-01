-- 08_top_launch_countries.sql
-- Lists the top launch countries by volume of launches and their percentage share.

SELECT 
    l.launch_country,
    COUNT(*) AS total_launches,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM fact_launches), 2) AS share_percentage
FROM fact_launches f
JOIN dim_location l ON f.location_id = l.location_id
GROUP BY l.launch_country
ORDER BY total_launches DESC;
