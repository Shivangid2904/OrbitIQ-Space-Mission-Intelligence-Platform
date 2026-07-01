-- 03_top_organizations.sql
-- Retrieves the top 10 organizations by total number of launches.

SELECT 
    c.company_name,
    COUNT(*) AS total_launches
FROM fact_launches f
JOIN dim_company c ON f.company_id = c.company_id
GROUP BY c.company_name
ORDER BY total_launches DESC
LIMIT 10;
