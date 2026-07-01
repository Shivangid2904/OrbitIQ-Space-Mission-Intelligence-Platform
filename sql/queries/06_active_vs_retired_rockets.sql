-- 06_active_vs_retired_rockets.sql
-- Compares the usage and share of active vs retired rockets.

SELECT 
    r.rocket_status,
    COUNT(*) AS total_launches,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM fact_launches), 2) AS usage_percentage
FROM fact_launches f
JOIN dim_rocket r ON f.rocket_id = r.rocket_id
GROUP BY r.rocket_status;
