-- 01_validation.sql

-- 1. Row Counts Validation
SELECT 'fact_launches' AS table_name, COUNT(*) AS row_count FROM fact_launches
UNION ALL
SELECT 'dim_company', COUNT(*) FROM dim_company
UNION ALL
SELECT 'dim_location', COUNT(*) FROM dim_location
UNION ALL
SELECT 'dim_rocket', COUNT(*) FROM dim_rocket
UNION ALL
SELECT 'dim_date', COUNT(*) FROM dim_date;

-- 2. Referential Integrity Validation (Checking for orphaned records - should return 0)
SELECT COUNT(*) AS orphaned_companies
FROM fact_launches f
LEFT JOIN dim_company c ON f.company_id = c.company_id
WHERE c.company_id IS NULL;

SELECT COUNT(*) AS orphaned_locations
FROM fact_launches f
LEFT JOIN dim_location l ON f.location_id = l.location_id
WHERE l.location_id IS NULL;

-- 3. Duplicate Records Validation (Checking if any launch record is duplicated)
SELECT date_key, company_id, location_id, rocket_id, payload_name, COUNT(*)
FROM fact_launches
GROUP BY date_key, company_id, location_id, rocket_id, payload_name
HAVING COUNT(*) > 1;

-- 4. Null Checks (Ensure critical columns do not contain nulls)
SELECT COUNT(*) AS null_dates FROM fact_launches WHERE date_key IS NULL;
SELECT COUNT(*) AS null_companies FROM fact_launches WHERE company_id IS NULL;
SELECT COUNT(*) AS null_locations FROM fact_launches WHERE location_id IS NULL;
-- Note: cost_usd_millions can be NULL, which is expected.

-- 5. Data Quality Checks (Validate range and constraints)
SELECT COUNT(*) AS invalid_success_flag FROM fact_launches WHERE is_success NOT IN (0, 1);
SELECT COUNT(*) AS negative_cost FROM fact_launches WHERE cost_usd_millions < 0;
