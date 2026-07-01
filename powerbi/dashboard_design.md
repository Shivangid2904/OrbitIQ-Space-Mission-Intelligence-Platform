# OrbitIQ – Power BI Dashboard Architecture & UI/UX Design Specifications
**Premium Aerospace Intelligence & Data Engineering Showcase**

---

## 1. Overall Design Language & Theme Specification
The visual theme is modeled after modern aerospace operations software (such as SpaceX telemetry, NASA command rooms, and Palantir interfaces), using a high-density, low-glare dark design.

### Theme & Styling Parameters
*   **Palette:**
    *   **Deep Space Canvas (Background):** `#06090D` (solid, dark matte)
    *   **Telemetry Slate (Card Background):** `#0C1017` with 90% opacity (gives a subtle layered look)
    *   **Glow Accent (Cyan):** `#00F0FF` (indicates selected states, key interactive indicators, and volume metrics)
    *   **Launch Green (Success Indicator):** `#00E676` (indicates successful missions, active status)
    *   **Anomaly Red (Failure Indicator):** `#FF3838` (indicates failed missions, retired systems)
    *   **Muted Silver (Secondary Text/Labels):** `#8E9CA6`
    *   **Crisp White (Primary Text/Values):** `#FFFFFF`
*   **Fonts:**
    *   *Hero & KPI Values:* `Consolas` or `Bahnschrift` (highly readable monospaced character layout for numbers)
    *   *Headers & Section Labels:* `Segoe UI Semibold`
    *   *Labels & Captions:* `Segoe UI`
*   **Card Styles:**
    *   Border: Ultra-thin 1px solid `#182230`
    *   Radius: 4px (preserves flat, professional technical look)
    *   Drop Shadows: None (prevents visual clutter)

---

## 2. Navigation Flow & Bookmark Strategy
The dashboard uses a persistent sidebar structure with smooth page switching powered by Power BI Bookmarks.

### Collapsible Left Navigation Bar
*   **State A (Collapsed):** A thin 48px left panel containing only Fluent UI icons.
    *   *Icons:* Home, Rocket, Org, Clock, Map, Flow
*   **State B (Expanded):** A 160px panel showing both icons and text labels:
    *   `[ ] Mission Control`
    *   `[ ] Agency Intelligence`
    *   `[ ] Mission Timeline`
    *   `[ ] Launch Network`
    *   `[ ] Strategic Intelligence`
    *   `[ ] Data Pipeline`
*   **Bookmark Logic:** Two bookmarks per page (`PageName_NavCollapse` and `PageName_NavExpand`) control the visibility of the overlay panel using the **Selection Pane** visibility toggles.

---

## 3. Page Layouts & Wireframes

### Page 0 — Landing Page (Entry Portal)
*   **Visual Layout:** A centered, high-impact minimalistic layout.
*   **Components:**
    *   **Header:** `ORBITIQ` (40pt, Segoe UI Semibold, White, tracked out with 5px character spacing).
    *   **Sub-header:** `SPACE MISSION INTELLIGENCE PLATFORM` (14pt, Cyan, Uppercase).
    *   **Sub-title:** `Historical Space Launch Analytics // 1957–2021` (11pt, Muted Silver).
    *   **Interactive Button (Center Bottom):** Large rectangular button labeled `ENTER MISSION CONTROL`.
        *   *Styling:* `#0C1017` background, 1px `#00F0FF` border, hover state changes border to solid `#00E676` with a soft glow.
        *   *Action:* Bookmark navigation link to the **Mission Control** page.

---

### Page 1 — Mission Control (Global Operations)
*   **Layout Grid (16:9 - 1920x1080):**
    *   *Top Header (Height 60px):* Title, UTC clock, localized filter summary.
    *   *KPI Banner (Height 100px - 5 Cards):*
        1.  Total Launches (`4,324` | Metric count)
        2.  Success Rate (`89.7%` | Success indicator)
        3.  Active Agencies (`56` | Count)
        4.  Active Sites (`94` | Count)
        5.  Active Rockets (`210` | Count)
    *   *Left Grid (Width 30%):*
        *   **Treemap:** Launch count shares by Launch Country.
    *   *Center Main (Width 45%):*
        *   **Choropleth Map / Filled Map:** Launch country boundaries filled by launch count density (avoiding point coordinate mapping issues).
    *   *Right Grid (Width 25%):*
        *   **Donut Chart:** Mission status distribution (Success, Failure, Partial Failure).
        *   **Zebra BI Table:** Live-style running ticker of recent launch logs (Company, Rocket, Payload, Outcome).
*   **Interactions:** Selecting a country on the Treemap cross-filters the Map and status charts.

---

### Page 2 — Agency Intelligence
*   **Layout Grid:**
    *   *Left Sidebar:* Vertical slicer panel for Company Name (searchable dropdown) and Rocket Status.
    *   *Center Top (Width 70%):*
        *   **Scatter Plot:** Average Cost ($M) on Y-axis vs. Success Rate % on X-axis. Bubbles represent companies.
    *   *Center Bottom (Width 70%):*
        *   **Matrix Visual:** Company, Total Launches, Success Rate, Total Cost, Average Cost, and Reliability Rank (Calculated via DAX rank).
    *   *Right Column (Width 30%):*
        *   **Clustered Bar Chart:** Top 10 agencies by total launch volume.
*   **Drill-through:** Selecting a company in the Matrix enables a drill-through page showing details of specific rocket models and payloads used by that company.

---

### Page 3 — Mission Timeline
*   **Layout Grid:**
    *   *Top Panel:* Time range slider (`launch_year`).
    *   *Main Center (Height 60%):*
        *   **Line and Stacked Column Chart:** Columns indicate annual launches, Line shows YoY launch growth rate % (using secondary Y-axis).
    *   *Bottom Left (Width 50%):*
        *   **Ribbon Chart:** Top 5 agencies' launch volume rankings across decades (`1950s` to `2020s`).
    *   *Bottom Right (Width 50%):*
        *   **Matrix Heatmap:** Months (columns) vs. Decades (rows), cells colored by launch count density to analyze seasonal distribution.

---

### Page 4 — Launch Network
*   **Layout Grid:**
    *   *Left Column (Width 30%):* Slicer panel (Launch Country, Rocket Status). Underneath, a **Treemap** showing launch count share by site location.
    *   *Right Main (Width 70%):*
        *   **Bar Chart:** Location Name (Y-axis) vs. Launch Count (X-axis), color-saturated by Success Rate.
        *   **Matrix Ledger:** Details of launch sites, including the principal company operating at each site.

---

### Page 5 — Strategic Intelligence
*   **Layout Grid:**
    *   *Left Column (Width 30%):*
        *   **Matrix List:** Rocket Model, Total Launches, Success Rate %, and Cost.
    *   *Center Main (Width 40%):*
        *   **Clustered Column Chart:** Compares success rates of active rockets vs. retired rockets.
    *   *Right Column (Width 30%):*
        *   **Matrix Table:** Lists all payloads launched, classified by company and rocket model, showing target outcomes.

---

### Page 6 — Data Pipeline Page
*   **Layout Concept:** Structural infographic detailing the data engineering flow, proving repository quality.
*   **Layout Grid:**
    *   *Top Row (Metrics Cards):*
        *   Total Rows Imported: `4,324`
        *   Duplicate Rows Removed: `0` (Cleaned during Phase 2)
        *   Missing Cost Percentage: `77%` (Handled via pandas and represented as NULL)
        *   Validation Checks Passed: `5 / 5`
        *   Dataset Time Range: `1957 – 2020`
    *   *Center Flow (Visual Flow Diagram utilizing Card Visuals & Connector Lines):*
        ```text
        [Raw CSV] ➔ [Python Ingestion] ➔ [Feature Engineering] ➔ [PostgreSQL Star Schema] ➔ [Power BI]
        ```
    *   *Bottom Left (Technical Log Matrix):*
        *   Shows validation query outcomes (Row counts, Orphan check, Duplicate checks, Constraints).
    *   *Bottom Right (Data Model Schema diagram):*
        *   A static image detailing the relationships between the fact table and the dimension tables (`dim_company`, `dim_location`, `dim_rocket`, `dim_date`).

---

## 4. Required DAX Measures

These measures are optimized for analytical performance and avoid redundant calculations:

```dax
-- 1. Total Launches
Total Launches = COUNT(fact_launches[launch_id])

-- 2. Successful Launches
Successful Launches = CALCULATE([Total Launches], fact_launches[is_success] = 1)

-- 3. Success Rate
Success Rate % = DIVIDE([Successful Launches], [Total Launches], 0)

-- 4. Average Cost
Average Cost ($M) = AVERAGE(fact_launches[cost_usd_millions])

-- 5. Active Rockets Count
Active Rockets Count = CALCULATE(DISTINCTCOUNT(fact_launches[rocket_id]), dim_rocket[rocket_status] = "Active")

-- 6. YoY Launch Growth %
YoY Launch Growth % = 
VAR CurrentYearLaunches = [Total Launches]
VAR PrevYearLaunches = 
    CALCULATE(
        [Total Launches],
        DATEADD(dim_date[launch_datetime], -1, YEAR)
    )
RETURN
    DIVIDE(CurrentYearLaunches - PrevYearLaunches, PrevYearLaunches, 0)

-- 7. 3-Year Rolling Launches Average
3Yr Rolling Avg Launches = 
AVERAGEX(
    DATESINPERIOD(
        dim_date[launch_datetime],
        LASTDATE(dim_date[launch_datetime]),
        -3,
        YEAR
    ),
    [Total Launches]
)
```

---

## 5. UI/UX & Tooltip Strategy
*   **Custom Tooltip Page (`Tooltip_Details`):** Hovering over any element on the Scatter Plot or Matrix displays a custom tooltip page showing:
    *   Selected Company/Site.
    *   A mini line chart showing launches over the years.
    *   Current success rate in a highlighted KPI card.
*   **Cross-Highlighting:** Enabled globally. Selecting an item in a bar chart highlights corresponding data in other visuals while keeping the underlying dataset context visible.
