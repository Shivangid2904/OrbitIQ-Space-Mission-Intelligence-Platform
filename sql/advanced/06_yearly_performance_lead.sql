-- 06_yearly_performance_lead.sql
-- Compares success rates of the current year against the subsequent year using LEAD().

WITH yearly_performance AS (
    SELECT 
        d.launch_year,
        COUNT(*) AS total_launches,
        SUM(f.is_success) AS successful_launches,
        ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage
    FROM fact_launches f
    JOIN dim_date d ON f.date_key = d.date_key
    GROUP BY d.launch_year
)
SELECT 
    launch_year,
    success_rate_percentage AS current_year_success_rate,
    LEAD(success_rate_percentage, 1) OVER (ORDER BY launch_year) AS next_year_success_rate,
    ROUND(
        LEAD(success_rate_percentage, 1) OVER (ORDER BY launch_year) - success_rate_percentage, 
        2
    ) AS success_rate_yoy_diff
FROM yearly_performance
ORDER BY launch_year;
