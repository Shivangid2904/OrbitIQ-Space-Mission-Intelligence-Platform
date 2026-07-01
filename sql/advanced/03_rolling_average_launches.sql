-- 03_rolling_average_launches.sql
-- Calculates a 3-year rolling average of space launches over time using AVG() OVER().

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
    ROUND(AVG(launch_count) OVER (ORDER BY launch_year ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS rolling_avg_3_years
FROM yearly_launches
ORDER BY launch_year;
