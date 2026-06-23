# OrbitIQ-Space-Mission-Intelligence-Platform
Project Type

Data Analytics + Business Intelligence + SQL

Difficulty Level

Intermediate to Advanced

Duration

4–5 Weeks

Goal

Build a Space Mission Intelligence Platform that analyzes global space missions from major agencies such as ISRO, NASA, ESA, SpaceX, CNSA, and Roscosmos.

The platform will use SQL, PostgreSQL, Power BI, and Python to identify mission trends, compare agency performance, evaluate reliability, and provide strategic insights into the global space ecosystem.

The project will include a dedicated ISRO analytics section to benchmark India's space program against leading international agencies.

Problem Statement

Space agencies launch thousands of missions over decades, but understanding long-term mission success, reliability, strategic focus, and operational performance requires large-scale analytics.

Current public datasets contain mission information but do not provide:

Comparative agency analysis
Reliability scoring
Long-term success trends
Strategic mission portfolio insights
ISRO benchmarking against global agencies

The objective is to transform raw mission data into actionable insights using SQL analytics and interactive dashboards.

Objectives
Analyze mission success rates across agencies.
Study launch trends over time.
Compare ISRO with global competitors.
Create a custom Mission Reliability Index.
Visualize mission portfolio evolution.
Build interactive Power BI dashboards.
Demonstrate advanced SQL skills.
Dataset

Primary Dataset:
Global Space Missions Dataset (1957–2035)

Expected Records:
10,000+ missions

Expected Attributes:

Mission Name
Agency
Launch Date
Launch Vehicle
Orbit Type
Mission Type
Success Status
Payload Mass
Cost (if available)
Country
Technology Stack
Data Processing
Python
Pandas
NumPy
Database
PostgreSQL
Querying
SQL
Visualization
Power BI
Documentation
GitHub
Markdown
Database Schema

Tables:

Agency

agency_id
agency_name
country

Mission

mission_id
mission_name
agency_id
launch_date
mission_type
orbit_type
success_status
payload_mass

LaunchVehicle

vehicle_id
vehicle_name
capacity

MissionVehicle

mission_id
vehicle_id
Advanced SQL Concepts Used
Window Functions
RANK()
DENSE_RANK()
ROW_NUMBER()
LAG()
LEAD()
AVG() OVER()
CTEs

WITH statements for multi-step analytics.

Aggregations
SUM()
AVG()
COUNT()
GROUP BY
HAVING
Joins
INNER JOIN
LEFT JOIN
SELF JOIN
Key Business Questions
Q1

Which agencies have the highest mission success rates?

Insight:
Operational excellence comparison.

Q2

How have success rates changed over time?

Insight:
Technology maturity trends.

Q3

Which agencies improved most over the last decade?

Insight:
Growth and innovation measurement.

Q4

Which launch vehicles are most reliable?

Insight:
Engineering reliability.

Q5

How has mission focus evolved?

Insight:
Shift from Earth Observation to Deep Space Exploration.

Q6

How does ISRO compare to NASA, ESA and SpaceX?

Insight:
Global benchmarking.

Q7

Which agencies have the most balanced mission portfolios?

Insight:
Strategic diversification.

Custom Metric
Mission Reliability Index

Purpose:
Create a proprietary metric to compare agencies.

Formula:

Reliability Index =
0.60 × Success Rate
+
0.20 × Mission Diversity Score
+
0.20 × Launch Frequency Score

Output:
Agency ranking based on overall operational performance.

Dashboard Structure
Page 1

Executive Overview

KPIs:

Total Missions
Success Rate
Total Agencies
Active Launch Vehicles

Charts:

Missions per Year
Global Mission Distribution
Page 2

Agency Performance

Charts:

Success Rate Ranking
Reliability Index Ranking
Top Performing Agencies
Page 3

Mission Trends

Charts:

Yearly Mission Growth
Success Trend Analysis
Decade Comparison
Page 4

Mission Portfolio Analysis

Charts:

Mission Type Distribution
Orbit Distribution
Agency Specialization
Page 5

ISRO Strategic Deep Dive

Charts:

ISRO vs NASA
ISRO vs ESA
ISRO vs SpaceX

Metrics:

Success Rate
Launch Frequency
Mission Diversity
Deliverables
Cleaned Dataset
PostgreSQL Database
SQL Query Collection
Power BI Dashboard
Project Documentation
GitHub Repository
Resume Outcome

Space Mission Intelligence Platform | SQL, PostgreSQL, Power BI, Python

Developed a data analytics platform analyzing global space missions across ISRO, NASA, ESA, SpaceX and Roscosmos. Designed advanced SQL workflows using window functions and CTEs, created a custom Mission Reliability Index, and built interactive Power BI dashboards to evaluate mission success, agency performance, and strategic space exploration trends.
