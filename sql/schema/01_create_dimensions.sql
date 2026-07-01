-- 01_create_dimensions.sql

CREATE TABLE dim_company (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE dim_location (
    location_id SERIAL PRIMARY KEY,
    location_name VARCHAR(500) NOT NULL UNIQUE,
    launch_country VARCHAR(100) NOT NULL
);

CREATE TABLE dim_rocket (
    rocket_id SERIAL PRIMARY KEY,
    rocket_model VARCHAR(255) NOT NULL UNIQUE,
    rocket_status VARCHAR(50) NOT NULL
);

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY, -- YYYYMMDD
    launch_datetime TIMESTAMPTZ NOT NULL,
    launch_year INT NOT NULL,
    launch_month INT NOT NULL,
    launch_decade VARCHAR(10) NOT NULL
);
