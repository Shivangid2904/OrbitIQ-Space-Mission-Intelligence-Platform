-- 01_rank_organizations_success.sql
-- Ranks organizations by mission success rate using RANK(), filtering for companies with >= 5 launches.

WITH company_stats AS (
    SELECT 
        c.company_name,
        COUNT(*) AS total_launches,
        SUM(f.is_success) AS successful_launches,
        ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage
    FROM fact_launches f
    JOIN dim_company c ON f.company_id = c.company_id
    GROUP BY c.company_name
    HAVING COUNT(*) >= 5
)
SELECT 
    company_name,
    total_launches,
    successful_launches,
    success_rate_percentage,
    RANK() OVER (ORDER BY success_rate_percentage DESC, total_launches DESC) AS success_rank
FROM company_stats;
