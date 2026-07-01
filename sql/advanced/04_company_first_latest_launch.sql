-- 04_company_first_latest_launch.sql
-- Identifies the very first and most recent launch for each space organization using ROW_NUMBER().

WITH launch_chronology AS (
    SELECT 
        c.company_name,
        f.payload_name,
        d.launch_datetime,
        ROW_NUMBER() OVER (PARTITION BY f.company_id ORDER BY d.launch_datetime ASC) AS rn_asc,
        ROW_NUMBER() OVER (PARTITION BY f.company_id ORDER BY d.launch_datetime DESC) AS rn_desc
    FROM fact_launches f
    JOIN dim_company c ON f.company_id = c.company_id
    JOIN dim_date d ON f.date_key = d.date_key
)
SELECT 
    company_name,
    MAX(CASE WHEN rn_asc = 1 THEN launch_datetime END) AS first_launch_datetime,
    MAX(CASE WHEN rn_asc = 1 THEN payload_name END) AS first_payload,
    MAX(CASE WHEN rn_desc = 1 THEN launch_datetime END) AS latest_launch_datetime,
    MAX(CASE WHEN rn_desc = 1 THEN payload_name END) AS latest_payload
FROM launch_chronology
WHERE rn_asc = 1 OR rn_desc = 1
GROUP BY company_name
ORDER BY latest_launch_datetime DESC;
