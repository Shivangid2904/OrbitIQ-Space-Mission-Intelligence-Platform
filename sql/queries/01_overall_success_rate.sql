-- 01_overall_success_rate.sql
-- Calculates the overall space mission success rate across all historical data.

SELECT 
    COUNT(*) AS total_launches,
    SUM(is_success) AS successful_launches,
    ROUND(100.0 * SUM(is_success) / COUNT(*), 2) AS success_rate_percentage
FROM fact_launches;
