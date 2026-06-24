# OrbitIQ – Space Mission Intelligence Platform

## Project Type

Data Analytics | Business Intelligence | SQL | PostgreSQL | Power BI

# Project Overview

OrbitIQ is a Space Mission Intelligence Platform designed to analyze historical space launches conducted by major organizations including ISRO, NASA, SpaceX, Roscosmos, CASC, Arianespace, JAXA, Blue Origin, and others.

The platform leverages SQL, PostgreSQL, Power BI, and Python to transform raw launch data into actionable insights. Through advanced analytics and interactive dashboards, OrbitIQ evaluates mission reliability, launch trends, organizational performance, and the evolution of the global space industry.

A dedicated ISRO Analytics module benchmarks India's space program against leading international organizations.

---

# Problem Statement

Since the beginning of the Space Age in 1957, thousands of space missions have been launched worldwide. While launch data is publicly available, it often lacks meaningful analytical insights regarding:

* Organizational performance
* Reliability benchmarking
* Historical launch trends
* Launch site intelligence
* Long-term operational consistency
* Strategic comparisons between global space organizations

OrbitIQ addresses these challenges by transforming raw launch records into a comprehensive business intelligence platform that supports data-driven analysis of the global space ecosystem.

---

# Objectives

* Analyze mission success rates across organizations
* Study launch trends over time
* Compare ISRO with global competitors
* Develop a custom Mission Reliability Index (MRI)
* Evaluate launch site reliability
* Measure long-term operational consistency
* Build interactive Power BI dashboards
* Demonstrate advanced SQL analytics techniques

---

# Dataset

## Primary Dataset

Space Missions Dataset (1957–Present)

## Source

NextSpaceFlight Launch Database

## Dataset Statistics

* 4,324+ Space Missions
* 56 Organizations
* 137 Launch Sites
* Coverage from 1957 to Present

## Available Attributes

| Column         | Description                        |
| -------------- | ---------------------------------- |
| Company Name   | Organization conducting the launch |
| Location       | Launch site                        |
| Datum          | Launch date and time               |
| Detail         | Rocket and mission information     |
| Status Rocket  | Rocket operational status          |
| Rocket         | Mission cost (where available)     |
| Status Mission | Mission outcome                    |

---

# Technology Stack

## Data Processing

* Python
* Pandas
* NumPy

## Database

* PostgreSQL

## Querying & Analytics

* SQL

## Visualization

* Power BI

## Documentation

* GitHub
* Markdown

---

# Database Schema

## Table: space_missions

| Column               | Data Type          |
| -------------------- | ------------------ |
| mission_id           | SERIAL PRIMARY KEY |
| company_name         | VARCHAR(100)       |
| location             | TEXT               |
| launch_datetime      | TIMESTAMP          |
| rocket_detail        | TEXT               |
| rocket_status        | VARCHAR(30)        |
| mission_cost_million | NUMERIC            |
| mission_status       | VARCHAR(30)        |

---

# Advanced SQL Concepts Used

## Window Functions

* RANK()
* DENSE_RANK()
* ROW_NUMBER()
* LAG()
* LEAD()
* AVG() OVER()

## Common Table Expressions (CTEs)

* Multi-step analytical workflows
* Intermediate aggregations
* Ranking calculations

## Aggregations

* COUNT()
* SUM()
* AVG()
* GROUP BY
* HAVING

## Joins

* INNER JOIN
* LEFT JOIN
* SELF JOIN

---

# Key Business Questions

## Q1. Which organizations have the highest mission success rates?

**Insight:** Compare operational excellence across organizations.

---

## Q2. How have launch success rates changed over time?

**Insight:** Measure technological maturity and operational improvement.

---

## Q3. Which organizations improved the most over the last decade?

**Insight:** Evaluate growth and innovation trends.

---

## Q4. Which launch sites are the most reliable?

**Insight:** Assess launch infrastructure performance.

---

## Q5. How has global launch activity evolved since 1957?

**Insight:** Understand the growth of the global space industry.

---

## Q6. How does ISRO compare with NASA, SpaceX, Roscosmos, CASC, and Arianespace?

**Insight:** Benchmark India's space program against leading competitors.

---

## Q7. Which organizations have the most stable success rates year-over-year?

**Insight:** Identify organizations demonstrating long-term operational consistency.

---

# Custom Metric

## Mission Reliability Index (MRI)

### Purpose

The Mission Reliability Index (MRI) is a proprietary metric developed to evaluate organizations based on reliability, operational scale, and longevity.

### Formula

MRI =

0.70 × Success Rate

* 0.20 × Launch Volume Score

* 0.10 × Operational Longevity Score

### Output

Organizations are ranked based on overall operational performance and consistency.

---

# Dashboard Structure

## Page 1 – Executive Overview

### KPIs

* Total Missions
* Overall Success Rate
* Total Organizations
* Active Rockets

### Visualizations

* Launches per Year
* Global Launch Distribution
* Success vs Failure Overview

---

## Page 2 – Organization Performance

### Visualizations

* Success Rate Ranking
* Mission Reliability Index Ranking
* Top Launch Organizations
* Organization Comparison Dashboard

---

## Page 3 – Historical Trends

### Visualizations

* Launches per Year
* Success Rate Trend Analysis
* Year-over-Year Growth
* Decade Comparison

---

## Page 4 – Launch Site Intelligence

### Visualizations

* Top Launch Sites
* Launch Site Reliability Ranking
* Geographic Distribution of Launches
* Launch Site Performance Analysis

---

## Page 5 – ISRO Strategic Deep Dive

### Comparative Analysis

* ISRO vs NASA
* ISRO vs SpaceX
* ISRO vs Roscosmos
* ISRO vs CASC
* ISRO vs Arianespace

### Metrics

* Mission Count
* Success Rate
* Operational Longevity
* Mission Reliability Index

### Visualizations

* Organization Comparison Charts
* ISRO Historical Performance Trend
* Reliability Comparison Dashboard

---

# Key Insights Expected

* Identify the most reliable launch organizations.
* Benchmark ISRO against leading global competitors.
* Analyze long-term growth of global launch activity.
* Evaluate launch site performance and reliability.
* Measure operational consistency across organizations.
* Rank organizations using the Mission Reliability Index.
* Understand the evolution of the global space industry since 1957.

---

# Project Structure

```text
OrbitIQ-Space-Mission-Intelligence-Platform
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── exploratory_analysis.ipynb
│
├── sql/
│   ├── 01_success_rate_analysis.sql
│   ├── 02_trend_analysis.sql
│   ├── 03_launch_site_reliability.sql
│   ├── 04_decade_analysis.sql
│   ├── 05_mission_reliability_index.sql
│   ├── 06_isro_benchmark.sql
│   └── 07_consistency_analysis.sql
│
├── powerbi/
│   └── OrbitIQ.pbix
│
├── screenshots/
│
├── README.md
└── requirements.txt
```

---

# Deliverables

* Cleaned Dataset
* PostgreSQL Database
* SQL Query Collection
* Power BI Dashboard
* Project Documentation
* GitHub Repository

---

# Implementation Timeline

## Week 1 – Data Preparation

* Data exploration and validation
* Data cleaning and preprocessing
* PostgreSQL database setup
* Data loading and schema creation

## Week 2 – SQL Analytics

* Development of analytical SQL queries
* Window function implementation
* CTE-based analysis workflows
* Validation and optimization

## Week 3 – Dashboard Development

* Power BI data modeling
* Dashboard design and implementation
* KPI creation
* Interactive visualization development

## Week 4 – Documentation and Deployment

* Dashboard refinement
* Documentation preparation
* GitHub repository organization
* Final project review

---

# Resume Outcome

**OrbitIQ – Space Mission Intelligence Platform | SQL, PostgreSQL, Power BI, Python**

Developed a data analytics platform analyzing 4,324+ global space missions conducted by leading organizations including ISRO, NASA, SpaceX, Roscosmos, and CASC. Designed advanced SQL workflows using window functions and CTEs, created a custom Mission Reliability Index, and built interactive Power BI dashboards to evaluate launch success trends, launch site reliability, and organizational performance across the global space ecosystem.
