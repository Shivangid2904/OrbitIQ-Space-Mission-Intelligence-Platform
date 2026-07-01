-- 09_consistent_operational_performance.sql
-- Identifies organizations maintaining a high success rate (min 80% per decade) across all decades they launched, with >= 10 total launches.

WITH company_decade_stats AS (
    SELECT 
        c.company_name,
        d.launch_decade,
        COUNT(*) AS launches_in_decade,
        SUM(f.is_success) AS success_in_decade,
        ROUND(100.0 * SUM(f.is_success) / COUNT(*), 2) AS success_rate_decade
    FROM fact_launches f
    JOIN dim_company c ON f.company_id = c.company_id
    JOIN dim_date d ON f.date_key = d.date_key
    GROUP BY c.company_name, d.launch_decade
),
company_summaries AS (
    SELECT 
        company_name,
        SUM(launches_in_decade) AS total_launches,
        AVG(success_rate_decade) AS avg_decade_success_rate,
        MIN(success_rate_decade) AS min_decade_success_rate,
        MAX(success_rate_decade) AS max_decade_success_rate,
        COUNT(DISTINCT launch_decade) AS decades_active
    FROM company_decade_stats
    GROUP BY company_name
)
SELECT 
    company_name,
    total_launches,
    decades_active,
    ROUND(avg_decade_success_rate, 2) AS avg_decade_success_rate,
    ROUND(min_decade_success_rate, 2) AS worst_decade_success_rate,
    ROUND(max_decade_success_rate, 2) AS best_decade_success_rate,
    ROUND(max_decade_success_rate - min_decade_success_rate, 2) AS success_rate_variance
FROM company_summaries
WHERE total_launches >= 10 AND min_decade_success_rate >= 80.0
ORDER BY avg_decade_success_rate DESC, success_rate_variance ASC;
