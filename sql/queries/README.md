# OrbitIQ Analytical SQL Queries

This directory contains the production-ready PostgreSQL analytical SQL queries designed to answer key business questions using the star schema.

## Query Catalog

1. **[01_overall_success_rate.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/01_overall_success_rate.sql)**
   * **Purpose:** Calculates the overall mission success rate percentage across all historical launch records.

2. **[02_success_rate_by_company.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/02_success_rate_by_company.sql)**
   * **Purpose:** Calculates total launches, successful launches, and success rate percentage grouped by launching company.

3. **[03_top_organizations.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/03_top_organizations.sql)**
   * **Purpose:** Ranks the top 10 space organizations based on their total launch counts.

4. **[04_launches_by_decade.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/04_launches_by_decade.sql)**
   * **Purpose:** Identifies launch volume and success rates grouped by the decade of the launch.

5. **[05_launches_by_year.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/05_launches_by_year.sql)**
   * **Purpose:** Shows chronological launch trend volume grouped by year.

6. **[06_active_vs_retired_rockets.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/06_active_vs_retired_rockets.sql)**
   * **Purpose:** Determines the proportional usage and total counts of active vs. retired rockets.

7. **[07_success_by_rocket_status.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/07_success_by_rocket_status.sql)**
   * **Purpose:** Compares success rates of active rockets against retired ones.

8. **[08_top_launch_countries.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/08_top_launch_countries.sql)**
   * **Purpose:** Ranks countries by their volume of space launches and shows their percentage share of global launches.

9. **[09_top_launch_sites.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/09_top_launch_sites.sql)**
   * **Purpose:** Identifies and ranks the top 10 individual launch pads and locations.

10. **[10_average_cost_by_company.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/queries/10_average_cost_by_company.sql)**
    * **Purpose:** Calculates average mission costs in millions of USD for each space organization (ignoring null/missing values).
