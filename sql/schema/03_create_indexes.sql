-- 03_create_indexes.sql

-- Foreign Key Indexes on Fact Table (speeds up joins)
CREATE INDEX idx_fact_launches_date ON fact_launches(date_key);
CREATE INDEX idx_fact_launches_company ON fact_launches(company_id);
CREATE INDEX idx_fact_launches_location ON fact_launches(location_id);
CREATE INDEX idx_fact_launches_rocket ON fact_launches(rocket_id);

-- Filter & Group By Indexes
CREATE INDEX idx_dim_date_year_month ON dim_date(launch_year, launch_month);
CREATE INDEX idx_dim_location_country ON dim_location(launch_country);
CREATE INDEX idx_fact_launches_success ON fact_launches(is_success);
