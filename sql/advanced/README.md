# OrbitIQ Advanced SQL Analytics

This directory contains production-ready PostgreSQL queries demonstrating advanced SQL analytics concepts, designed to answer key business questions for the OrbitIQ Space Mission Intelligence Platform.

## Query Catalog & Concepts Demonstrated

1. **[01_rank_organizations_success.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/01_rank_organizations_success.sql)**
   * **Business Metric:** Ranks organizations by launch success rate.
   * **Advanced Concepts:** `CTEs`, `RANK()`, `OVER (ORDER BY ... DESC)` window function, and `HAVING` aggregation filters.

2. **[02_yoy_launch_volume.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/02_yoy_launch_volume.sql)**
   * **Business Metric:** Yearly launch volume and year-over-year comparison.
   * **Advanced Concepts:** `LAG()`, `NULLIF()` to avoid division-by-zero errors, and delta change calculations.

3. **[03_rolling_average_launches.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/03_rolling_average_launches.sql)**
   * **Business Metric:** 3-year rolling average launches over time.
   * **Advanced Concepts:** `AVG() OVER()`, `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` frame specification.

4. **[04_company_first_latest_launch.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/04_company_first_latest_launch.sql)**
   * **Business Metric:** First and latest launch payload and datetime for each organization.
   * **Advanced Concepts:** Dual `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` evaluations and conditional aggregation (`CASE WHEN`).

5. **[05_rank_launch_sites_reliability.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/05_rank_launch_sites_reliability.sql)**
   * **Business Metric:** Ranks launch sites by mission success rate.
   * **Advanced Concepts:** `DENSE_RANK()`, `OVER (ORDER BY ...)` which avoids skipping ranks on identical values.

6. **[06_yearly_performance_lead.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/06_yearly_performance_lead.sql)**
   * **Business Metric:** Yearly performance success rate compared to the subsequent year.
   * **Advanced Concepts:** `LEAD()`, lookahead calculations, and temporal metrics comparison.

7. **[07_top_company_by_decade.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/07_top_company_by_decade.sql)**
   * **Business Metric:** Top-performing organization in each decade by volume.
   * **Advanced Concepts:** `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` and filtering ranking metrics using outer queries.

8. **[08_cumulative_launches.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/08_cumulative_launches.sql)**
   * **Business Metric:** Cumulative/running total launches over time.
   * **Advanced Concepts:** `SUM() OVER (ORDER BY ...)` running aggregation.

9. **[09_consistent_operational_performance.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/09_consistent_operational_performance.sql)**
   * **Business Metric:** Identifies companies maintaining high operational standard across active decades.
   * **Advanced Concepts:** Multi-layer `CTEs`, nested aggregate summaries (`MIN`, `MAX`, `AVG`), and multi-dimension filtering.

10. **[10_decade_wise_summary.sql](file:///c:/Users/SHIVANGI/OneDrive/Documents/Desktop/Projects/OrbitIQ-Space-Mission-Intelligence-Platform/sql/advanced/10_decade_wise_summary.sql)**
    * **Business Metric:** Decade-wise summary containing metrics and average mission costs.
    * **Advanced Concepts:** `CTEs`, conditional counting, and composite grouping metrics.
