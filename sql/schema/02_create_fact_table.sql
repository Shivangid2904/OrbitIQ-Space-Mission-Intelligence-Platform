-- 02_create_fact_table.sql

CREATE TABLE fact_launches (
    launch_id SERIAL PRIMARY KEY,
    date_key INT NOT NULL REFERENCES dim_date(date_key),
    company_id INT NOT NULL REFERENCES dim_company(company_id),
    location_id INT NOT NULL REFERENCES dim_location(location_id),
    rocket_id INT NOT NULL REFERENCES dim_rocket(rocket_id),
    payload_name VARCHAR(500) NOT NULL,
    cost_usd_millions NUMERIC(10, 2),
    mission_status VARCHAR(50) NOT NULL,
    is_success INT NOT NULL CHECK (is_success IN (0, 1))
);
