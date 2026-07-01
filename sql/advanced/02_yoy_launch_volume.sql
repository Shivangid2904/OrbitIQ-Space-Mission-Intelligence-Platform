-- 02_yoy_launch_volume.sql
-- Compares annual launch volumes year-over-year (YoY) using the LAG() window function.

WITH yearly_launches AS (
    SELECT 
        d.launch_year,
        COUNT(*) AS launch_count
    FROM fact_launches f
    JOIN dim_date d ON f.date_key = d.date_key
    GROUP BY d.launch_year
)
SELECT 
    launch_year,
    launch_count,
    LAG(launch_count, 1) OVER (ORDER BY launch_year) AS previous_year_launches,
    (launch_count - LAG(launch_count, 1) OVER (ORDER BY launch_year)) AS yoy_change,
    ROUND(100.0 * (launch_count - LAG(launch_count, 1) OVER (ORDER BY launch_year)) / NULLIF(LAG(launch_count, 1) OVER (ORDER BY launch_year), 0), 2) AS yoy_growth_percentage
FROM yearly_launches
ORDER BY launch_year;
