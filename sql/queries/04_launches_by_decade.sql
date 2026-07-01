-- 04_launches_by_decade.sql
-- Group and count launches by decade, including success rates.

SELECT 
    d.launch_decade,
    COUNT(*) AS total_launches,
    SUM(f.is_success) AS successful_launches,
    ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage
FROM fact_launches f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.launch_decade
ORDER BY d.launch_decade ASC;
