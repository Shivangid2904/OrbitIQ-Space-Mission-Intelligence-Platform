-- 02_success_rate_by_company.sql
-- Calculates the mission success rate for each organization/company.

SELECT 
    c.company_name,
    COUNT(*) AS total_launches,
    SUM(f.is_success) AS successful_launches,
    ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage
FROM fact_launches f
JOIN dim_company c ON f.company_id = c.company_id
GROUP BY c.company_name
ORDER BY total_launches DESC, success_rate_percentage DESC;
