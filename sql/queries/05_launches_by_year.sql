-- 05_launches_by_year.sql
-- Group and count launches by year.

SELECT 
    d.launch_year,
    COUNT(*) AS total_launches
FROM fact_launches f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.launch_year
ORDER BY d.launch_year ASC;
