-- 10_decade_wise_summary.sql
-- Generates a decade-wise space mission performance summary utilizing CTEs.

WITH decade_stats AS (
    SELECT 
        d.launch_decade,
        COUNT(*) AS total_launches,
        SUM(f.is_success) AS successful_launches,
        ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage,
        ROUND(AVG(f.cost_usd_millions), 2) AS avg_cost_millions,
        SUM(CASE WHEN f.cost_usd_millions IS NOT NULL THEN 1 ELSE 0 END) AS launches_with_cost
    FROM fact_launches f
    JOIN dim_date d ON f.date_key = d.date_key
    GROUP BY d.launch_decade
)
SELECT 
    launch_decade,
    total_launches,
    successful_launches,
    success_rate_percentage,
    avg_cost_millions,
    launches_with_cost
FROM decade_stats
ORDER BY launch_decade ASC;
