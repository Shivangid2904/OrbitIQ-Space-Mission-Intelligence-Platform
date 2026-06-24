# OrbitIQ – Space Mission Intelligence Platform

## Project Type

Data Analytics | Business Intelligence | SQL | PostgreSQL | Power BI

---
# Goal

Build a Space Mission Intelligence Platform that analyzes over 4,300 global space launches conducted by major organizations including ISRO, SpaceX, Roscosmos, CASC, JAXA, Arianespace, Blue Origin, and others.

The platform leverages SQL, PostgreSQL, Power BI, and Python to identify mission trends, compare organizational performance, evaluate launch reliability, and generate strategic insights into the evolution of the global space industry.

A dedicated ISRO analytics section benchmarks India's space program against leading international space organizations.

---

# Problem Statement

Space agencies and commercial launch providers have conducted thousands of launches since the beginning of the Space Age in 1957.

While launch data is publicly available, it often lacks:

* Comparative organization analysis
* Reliability benchmarking
* Historical performance evaluation
* Launch site intelligence
* Strategic operational insights
* ISRO benchmarking against global competitors

The objective is to transform raw launch data into actionable intelligence using SQL analytics and interactive business dashboards.

---

# Objectives

* Analyze mission success rates across organizations
* Study launch trends over time
* Compare ISRO with global competitors
* Create a custom Mission Reliability Index
* Evaluate launch site performance
* Track the evolution of global launch activity
* Build interactive Power BI dashboards
* Demonstrate advanced SQL analytics skills

---

# Dataset

## Primary Dataset

Space Missions Dataset (1957–Present)

## Source

NextSpaceFlight Launch Database

## Records

4,324+ Space Missions

## Key Attributes

* Company Name
* Launch Location
* Launch Date & Time
* Rocket / Mission Details
* Rocket Status
* Mission Cost (Available for Selected Missions)
* Mission Status

---

# Technology Stack

## Data Processing

* Python
* Pandas
* NumPy

## Database

* PostgreSQL

## Querying

* SQL

## Visualization

* Power BI

## Documentation

* GitHub
* Markdown

---

# Database Schema

## Fact Table

### Space_Missions

| Column               | Description                         |
| -------------------- | ----------------------------------- |
| mission_id           | Unique Mission Identifier           |
| company_name         | Organization Conducting Launch      |
| location             | Launch Site                         |
| launch_datetime      | Launch Date & Time                  |
| rocket_detail        | Rocket / Payload Information        |
| rocket_status        | Active / Retired                    |
| mission_cost_million | Mission Cost (USD Million)          |
| mission_status       | Success / Failure / Partial Failure |

---

# Advanced SQL Concepts Used

## Window Functions

* RANK()
* DENSE_RANK()
* ROW_NUMBER()
* LAG()
* LEAD()
* AVG() OVER()

## CTEs

WITH statements for multi-step analytics.

## Aggregations

* SUM()
* AVG()
* COUNT()
* GROUP BY
* HAVING

## Joins

* INNER JOIN
* LEFT JOIN
* SELF JOIN

---

# Key Business Questions

## Q1

Which organizations have the highest mission success rates?

**Insight:** Operational excellence comparison.

---

## Q2

How have mission success rates changed over time?

**Insight:** Technology maturity trends.

---

## Q3

Which organizations improved the most over the last decade?

**Insight:** Innovation and reliability growth.

---

## Q4

Which launch sites are the most reliable?

**Insight:** Launch infrastructure performance.

---

## Q5

How has global launch activity evolved since 1957?

**Insight:** Growth of the modern space industry.

---

## Q6

How does ISRO compare to SpaceX, Roscosmos, CASC, and Arianespace?

**Insight:** Global benchmarking.

---

## Q7

Which organizations demonstrate the strongest long-term operational consistency?

**Insight:** Strategic performance evaluation.

---

# Custom Metric

## Mission Reliability Index (MRI)

### Formula

MRI =
0.70 × Success Rate +
0.20 × Launch Volume Score +
0.10 × Operational Longevity Score

### Purpose

Create a proprietary performance metric that combines reliability, scale, and experience to rank global launch organizations.

---

# Dashboard Structure

## Page 1 – Executive Overview

### KPIs

* Total Missions
* Overall Success Rate
* Total Organizations
* Active Rockets

### Charts

* Missions per Year
* Global Launch Distribution
* Success vs Failure Overview

---

## Page 2 – Organization Performance

### Charts

* Success Rate Ranking
* Mission Reliability Index Ranking
* Top Launch Organizations

---

## Page 3 – Historical Trends

### Charts

* Launches per Year
* Success Rate Trend
* Decade Comparison

---

## Page 4 – Launch Site Intelligence

### Charts

* Top Launch Sites
* Launch Site Reliability
* Geographic Distribution of Launches

---

## Page 5 – ISRO Strategic Deep Dive

### Comparisons

* ISRO vs SpaceX
* ISRO vs Roscosmos
* ISRO vs CASC
* ISRO vs Arianespace

### Metrics

* Success Rate
* Mission Count
* Operational Longevity
* Reliability Index

---

# Deliverables

* Cleaned Dataset
* PostgreSQL Database
* SQL Query Collection
* Power BI Dashboard
* Data Dictionary
* Project Documentation
* GitHub Repository

---

# Resume Outcome

### OrbitIQ – Space Mission Intelligence Platform | SQL, PostgreSQL, Power BI, Python

Developed a data analytics platform analyzing 4,324+ global space missions conducted by leading organizations including ISRO, SpaceX, Roscosmos, CASC, and Arianespace. Designed advanced SQL workflows using window functions and CTEs, created a custom Mission Reliability Index, and built interactive Power BI dashboards to evaluate mission success trends, launch site reliability, and organizational performance across the global space ecosystem.
