-- 07_success_by_rocket_status.sql
-- Analyzes mission success rates grouped by the status of the rocket (Active vs Retired).

SELECT 
    r.rocket_status,
    COUNT(*) AS total_launches,
    SUM(f.is_success) AS successful_launches,
    ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage
FROM fact_launches f
JOIN dim_rocket r ON f.rocket_id = r.rocket_id
GROUP BY r.rocket_status;
