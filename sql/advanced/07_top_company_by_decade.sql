-- 07_top_company_by_decade.sql
-- Identifies the top performing organization in each decade (ranked by total launch volume).

WITH decade_company_stats AS (
    SELECT 
        d.launch_decade,
        c.company_name,
        COUNT(*) AS total_launches,
        SUM(f.is_success) AS successful_launches,
        ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_percentage
    FROM fact_launches f
    JOIN dim_company c ON f.company_id = c.company_id
    JOIN dim_date d ON f.date_key = d.date_key
    GROUP BY d.launch_decade, c.company_name
),
ranked_companies AS (
    SELECT 
        launch_decade,
        company_name,
        total_launches,
        success_rate_percentage,
        ROW_NUMBER() OVER (
            PARTITION BY launch_decade 
            ORDER BY total_launches DESC, success_rate_percentage DESC
        ) AS rank_by_volume
    FROM decade_company_stats
)
SELECT 
    launch_decade,
    company_name,
    total_launches,
    success_rate_percentage
FROM ranked_companies
WHERE rank_by_volume = 1
ORDER BY launch_decade;
