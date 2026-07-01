import os
import sys
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "orbitiq")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = PROJECT_ROOT / "data" / "processed" / "space_missions_cleaned.csv"

def get_engine():
    return create_engine(DATABASE_URL)

def ingest():
    if not CSV_PATH.exists():
        print(f"Error: Cleaned CSV not found at {CSV_PATH}")
        sys.exit(1)

    df = pd.read_csv(CSV_PATH)
    
    # Handle NaN in cost
    df["cost_usd_millions"] = df["cost_usd_millions"].where(pd.notnull(df["cost_usd_millions"]), None)
    
    # Generate date_key (YYYYMMDD)
    df["launch_datetime_parsed"] = pd.to_datetime(df["launch_datetime"], utc=True)
    df["date_key"] = df["launch_datetime_parsed"].dt.strftime("%Y%m%d").astype(int)

    engine = get_engine()

    with engine.begin() as conn:
        # 1. Populate dim_company
        companies = df[["company"]].drop_duplicates().rename(columns={"company": "company_name"})
        for _, row in companies.iterrows():
            conn.execute(
                text("INSERT INTO dim_company (company_name) VALUES (:company_name) ON CONFLICT (company_name) DO NOTHING"),
                {"company_name": row["company_name"]}
            )

        # 2. Populate dim_location
        locations = df[["location", "launch_country"]].drop_duplicates().rename(columns={"location": "location_name"})
        for _, row in locations.iterrows():
            conn.execute(
                text("INSERT INTO dim_location (location_name, launch_country) VALUES (:location_name, :launch_country) ON CONFLICT (location_name) DO NOTHING"),
                {"location_name": row["location_name"], "launch_country": row["launch_country"]}
            )

        # 3. Populate dim_rocket (Ensure one status per rocket model, preferring 'Active')
        rockets = df[["rocket_model", "rocket_status"]].copy()
        rockets["status_priority"] = rockets["rocket_status"].map({"Active": 1, "Retired": 2}).fillna(3)
        rockets = rockets.sort_values("status_priority").drop_duplicates(subset=["rocket_model"]).drop(columns=["status_priority"])
        for _, row in rockets.iterrows():
            conn.execute(
                text("INSERT INTO dim_rocket (rocket_model, rocket_status) VALUES (:rocket_model, :rocket_status) ON CONFLICT (rocket_model) DO UPDATE SET rocket_status = EXCLUDED.rocket_status"),
                {"rocket_model": row["rocket_model"], "rocket_status": row["rocket_status"]}
            )

        # 4. Populate dim_date
        dates = df[["date_key", "launch_datetime_parsed", "launch_year", "launch_month", "launch_decade"]].drop_duplicates(subset=["date_key"])
        for _, row in dates.iterrows():
            conn.execute(
                text("INSERT INTO dim_date (date_key, launch_datetime, launch_year, launch_month, launch_decade) VALUES (:date_key, :launch_datetime, :launch_year, :launch_month, :launch_decade) ON CONFLICT (date_key) DO NOTHING"),
                {
                    "date_key": int(row["date_key"]),
                    "launch_datetime": row["launch_datetime_parsed"],
                    "launch_year": int(row["launch_year"]),
                    "launch_month": int(row["launch_month"]),
                    "launch_decade": str(row["launch_decade"])
                }
            )

        # Get surrogate keys mappings
        company_map = {r[1]: r[0] for r in conn.execute(text("SELECT company_id, company_name FROM dim_company")).fetchall()}
        location_map = {r[1]: r[0] for r in conn.execute(text("SELECT location_id, location_name FROM dim_location")).fetchall()}
        rocket_map = {r[1]: r[0] for r in conn.execute(text("SELECT rocket_id, rocket_model FROM dim_rocket")).fetchall()}

        # 5. Populate fact_launches
        fact_rows = []
        for _, row in df.iterrows():
            fact_rows.append({
                "date_key": int(row["date_key"]),
                "company_id": company_map[row["company"]],
                "location_id": location_map[row["location"]],
                "rocket_id": rocket_map[row["rocket_model"]],
                "payload_name": row["payload_name"],
                "cost_usd_millions": row["cost_usd_millions"],
                "mission_status": row["mission_status"],
                "is_success": int(row["is_success"])
            })

        # Clear existing fact data if re-running ingestion
        conn.execute(text("TRUNCATE TABLE fact_launches CASCADE"))

        # Bulk insert facts
        conn.execute(
            text("""
                INSERT INTO fact_launches (date_key, company_id, location_id, rocket_id, payload_name, cost_usd_millions, mission_status, is_success)
                VALUES (:date_key, :company_id, :location_id, :rocket_id, :payload_name, :cost_usd_millions, :mission_status, :is_success)
            """),
            fact_rows
        )

    print("Data ingestion completed successfully.")

if __name__ == "__main__":
    ingest()
