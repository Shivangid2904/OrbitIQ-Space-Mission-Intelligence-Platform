-- 08_cumulative_launches.sql
-- Computes the running total of space launches chronologically using SUM() OVER().

WITH yearly_launches AS (
    SELECT 
        d.launch_year,
        COUNT(*) AS yearly_count
    FROM fact_launches f
    JOIN dim_date d ON f.date_key = d.date_key
    GROUP BY d.launch_year
)
SELECT 
    launch_year,
    yearly_count,
    SUM(yearly_count) OVER (ORDER BY launch_year) AS cumulative_launches
FROM yearly_launches
ORDER BY launch_year;
