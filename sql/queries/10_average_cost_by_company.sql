-- 10_average_cost_by_company.sql
-- Calculates the average mission cost in millions of USD for each company, excluding null values.

SELECT 
    c.company_name,
    COUNT(*) AS total_launches,
    COUNT(f.cost_usd_millions) AS launches_with_cost_data,
    ROUND(AVG(f.cost_usd_millions), 2) AS average_cost_usd_millions
FROM fact_launches f
JOIN dim_company c ON f.company_id = c.company_id
WHERE f.cost_usd_millions IS NOT NULL
GROUP BY c.company_name
ORDER BY average_cost_usd_millions DESC;
