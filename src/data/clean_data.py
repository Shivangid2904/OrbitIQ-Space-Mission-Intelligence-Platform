from __future__ import annotations

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Space_Corrected.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "space_missions_cleaned.csv"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


# ===========================================================================
# Step 1 – Load raw data
# ===========================================================================
def load_raw(path: Path) -> pd.DataFrame:
    
    log.info("Loading raw dataset from: %s", path)
    df = pd.read_csv(path, encoding="utf-8", encoding_errors="replace")
    log.info("Raw shape: %d rows × %d columns", *df.shape)
    return df


# ===========================================================================
# Step 2 – Drop redundant index columns
# ===========================================================================
def drop_redundant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the two auto-generated integer index columns written by Pandas
    when the file was previously saved without index=False.
    """
    cols_to_drop = [c for c in df.columns if c.startswith("Unnamed")]
    log.info("Dropping redundant index columns: %s", cols_to_drop)
    return df.drop(columns=cols_to_drop)


# ===========================================================================
# Step 3 – Rename columns to snake_case
# ===========================================================================
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
        "Company Name":   "company",
        "Location":       "location",
        "Datum":          "datum_raw",     # preserved until datetime parsing is complete
        "Detail":         "detail_raw",    # preserved until split into model / payload
        "Status Rocket":  "rocket_status_raw",
        " Rocket":        "cost_usd_millions_raw",
        "Status Mission": "mission_status",
    }
    log.info("Renaming columns to snake_case.")
    return df.rename(columns=rename_map)


# ===========================================================================
# Step 4 – Remove duplicate records
# ===========================================================================
def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows that are identical across every business column (ignoring the
    row-number index).  The subset excludes any lingering index-like columns.
    """
    before = len(df)
    df = df.drop_duplicates(subset=df.columns.tolist(), keep="first")
    after = len(df)
    log.info("Duplicate rows removed: %d  (rows before=%d, after=%d)", before - after, before, after)
    return df.reset_index(drop=True)


# ===========================================================================
# Step 5 – Parse launch datetime
# ===========================================================================
def parse_launch_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert 'datum_raw' into a proper UTC-aware datetime column.
    """
    log.info("Parsing launch datetime from 'datum_raw'.")

    def _parse(raw: str) -> pd.Timestamp | pd.NaT:
        if not isinstance(raw, str):
            return pd.NaT
        cleaned = raw.strip().removesuffix(" UTC").strip()
        # Try full datetime first (most common)
        for fmt in ("%a %b %d, %Y %H:%M", "%a %b %d, %Y"):
            try:
                return pd.Timestamp(cleaned, tz="UTC")
            except Exception:
                pass
        return pd.NaT

    df["launch_datetime"] = pd.to_datetime(
        df["datum_raw"]
        .str.strip()
        .str.replace(r"\s*UTC$", "", regex=True),
        format="mixed",
        dayfirst=False,
        utc=True,
        errors="coerce",
    )

    nat_count = df["launch_datetime"].isna().sum()
    if nat_count > 0:
        log.warning("launch_datetime: %d rows could not be parsed (set to NaT).", nat_count)
    else:
        log.info("launch_datetime: all rows parsed successfully.")

    return df


# ===========================================================================
# Step 6 – Derive temporal features
# ===========================================================================
def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    
    log.info("Deriving temporal feature columns.")
    dt = df["launch_datetime"].dt
    df["launch_year"]   = dt.year.astype("Int64")      # nullable integer for NaT rows
    df["launch_month"]  = dt.month.astype("Int64")
    df["launch_decade"] = df["launch_year"].apply(
        lambda y: f"{(y // 10) * 10}s" if pd.notna(y) else None
    )
    return df


# ===========================================================================
# Step 7 – Clean rocket cost column
# ===========================================================================
def clean_cost_column(df: pd.DataFrame) -> pd.DataFrame:
    
    log.info("Cleaning rocket cost column.")
    df["cost_usd_millions"] = (
        df["cost_usd_millions_raw"]
        .astype(str)
        .str.strip()
        .str.replace(",", "", regex=False)
        .replace({"nan": None, "": None, "None": None})
        .astype(float)
    )
    filled  = df["cost_usd_millions"].notna().sum()
    missing = df["cost_usd_millions"].isna().sum()
    log.info("cost_usd_millions: %d values present, %d NULL (%.1f%% missing).",
             filled, missing, 100 * missing / len(df))
    return df


# ===========================================================================
# Step 8 – Standardise rocket status
# ===========================================================================
def standardise_rocket_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Map 'rocket_status_raw' values from 'StatusActive' / 'StatusRetired'
    to clean, human-readable labels 'Active' / 'Retired'.
    """
    status_map = {
        "StatusActive":  "Active",
        "StatusRetired": "Retired",
    }
    log.info("Standardising rocket_status values.")
    df["rocket_status"] = df["rocket_status_raw"].map(status_map).fillna(df["rocket_status_raw"])
    unmapped = df["rocket_status"].isin(["StatusActive", "StatusRetired"]).sum()
    if unmapped > 0:
        log.warning("rocket_status: %d values were not mapped — inspect raw values.", unmapped)
    return df


# ===========================================================================
# Step 9 – Parse Detail → rocket_model + payload_name
# ===========================================================================
def parse_detail_column(df: pd.DataFrame) -> pd.DataFrame:
    
    log.info("Parsing 'detail_raw' into rocket_model and payload_name.")
    split = df["detail_raw"].str.split(r"\|", n=1, expand=True)
    df["rocket_model"]  = split[0].str.strip()
    df["payload_name"]  = split[1].str.strip() if 1 in split.columns else None
    no_pipe = df["payload_name"].isna().sum()
    if no_pipe > 0:
        log.warning("payload_name: %d rows had no '|' separator.", no_pipe)
    return df


# ===========================================================================
# Step 10 – Extract launch country from location
# ===========================================================================
def extract_launch_country(df: pd.DataFrame) -> pd.DataFrame:
    
    log.info("Extracting launch_country from location.")

    # Take the last comma-delimited segment
    raw_country = df["location"].str.split(",").str[-1].str.strip()

    # Mapping of raw last-segment values → canonical country names
    country_overrides: dict[str, str] = {
        # US states → United States
        "Florida":              "United States",
        "California":           "United States",
        "Texas":                "United States",
        "Virginia":             "United States",
        "New Mexico":           "United States",
        "Alaska":               "United States",
        "Marshall Islands":     "United States",
        "Pacific Missile Range Facility": "United States",
        # Maritime / non-sovereign regions
        "Yellow Sea":           "China",          # Tai Rui barge – China-operated
        "Barents Sea":          "Russia",         # Russian submarine launches
        "Pacific Ocean":        "International Waters",  # Sea Launch platform
        "Gran Canaria":         "Spain",
        "Shahrud Missile Test Site": "Iran",
        # Overseas territories
        "French Guiana":        "France",
        "French Guiana, France": "France",
    }

    df["launch_country"] = raw_country.replace(country_overrides)
    log.info("launch_country: %d unique countries identified.",
             df["launch_country"].nunique())
    return df


# ===========================================================================
# Step 11 – Derive is_success flag
# ===========================================================================
def add_success_flag(df: pd.DataFrame) -> pd.DataFrame:
    
    log.info("Deriving is_success binary flag.")
    df["is_success"] = (df["mission_status"] == "Success").astype(int)
    success_pct = df["is_success"].mean() * 100
    log.info("is_success: %.1f%% of launches are successes.", success_pct)
    return df


# ===========================================================================
# Step 12 – Select, order, and export final columns
# ===========================================================================
FINAL_COLUMNS = [
    "company",
    "location",
    "launch_country",
    "launch_datetime",
    "launch_year",
    "launch_month",
    "launch_decade",
    "rocket_model",
    "payload_name",
    "rocket_status",
    "cost_usd_millions",
    "mission_status",
    "is_success",
    # Keep raw columns for auditability / cross-reference
    "datum_raw",
    "detail_raw",
    "rocket_status_raw",
    "cost_usd_millions_raw",
]


def select_final_columns(df: pd.DataFrame) -> pd.DataFrame:
    
    available = [c for c in FINAL_COLUMNS if c in df.columns]
    missing   = [c for c in FINAL_COLUMNS if c not in df.columns]
    if missing:
        log.warning("Expected columns not found and will be skipped: %s", missing)
    return df[available].reset_index(drop=True)


def export_csv(df: pd.DataFrame, path: Path) -> None:

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")
    log.info("Cleaned dataset written to: %s  (%d rows × %d columns)", path, *df.shape)


# ===========================================================================
# Validation checks
# ===========================================================================
def run_validation(df: pd.DataFrame) -> bool:
    log.info("=" * 60)
    log.info("Running post-cleaning validation checks …")
    all_passed = True

    def _check(condition: bool, message: str) -> None:
        nonlocal all_passed
        if condition:
            log.info("  [PASS]  %s", message)
        else:
            log.error("  [FAIL]  %s", message)
            all_passed = False

    # 1. Row count – should be exactly 4323 after removing 1 duplicate from 4324
    _check(len(df) == 4323,
           f"Row count == 4323  (actual: {len(df)})")

    # 2. No duplicate rows on business columns
    biz_cols = ["company", "launch_datetime", "detail_raw"]
    dup_count = df.duplicated(subset=biz_cols).sum()
    _check(dup_count == 0,
           f"Zero duplicate rows on (company, launch_datetime, detail_raw)  (found: {dup_count})")

    # 3. launch_datetime — no unexpected NaT values beyond the known date-only rows
    nat_count = df["launch_datetime"].isna().sum()
    _check(nat_count == 0,
           f"launch_datetime has zero NaT values  (found: {nat_count})")

    # 4. launch_year range — all years must be between 1957 and 2021
    valid_years = df["launch_year"].dropna()
    _check(
        valid_years.between(1957, 2021).all(),
        f"All launch_year values in range [1957, 2021]  "
        f"(min={valid_years.min()}, max={valid_years.max()})"
    )

    # 5. cost_usd_millions — no negative values
    cost_non_null = df["cost_usd_millions"].dropna()
    _check(
        (cost_non_null >= 0).all(),
        f"No negative cost_usd_millions values  (min={cost_non_null.min() if len(cost_non_null) else 'N/A'})"
    )

    # 6. cost_usd_millions — missing rate must be < 80%
    missing_pct = df["cost_usd_millions"].isna().mean() * 100
    _check(missing_pct < 80,
           f"cost_usd_millions missing rate < 80%  (actual: {missing_pct:.1f}%)")

    # 7. rocket_status — only valid clean labels
    valid_statuses = {"Active", "Retired"}
    actual_statuses = set(df["rocket_status"].dropna().unique())
    _check(actual_statuses.issubset(valid_statuses),
           f"rocket_status contains only 'Active' / 'Retired'  (found: {actual_statuses})")

    # 8. mission_status — only known outcome categories
    valid_missions = {"Success", "Failure", "Partial Failure", "Prelaunch Failure"}
    actual_missions = set(df["mission_status"].dropna().unique())
    _check(actual_missions.issubset(valid_missions),
           f"mission_status values are within expected set  (found: {actual_missions})")

    # 9. is_success — only 0 or 1
    invalid_flags = ~df["is_success"].isin([0, 1])
    _check(not invalid_flags.any(),
           f"is_success contains only 0 or 1  (invalid count: {invalid_flags.sum()})")

    # 10. rocket_model — no nulls (every row must have a launch vehicle)
    model_nulls = df["rocket_model"].isna().sum()
    _check(model_nulls == 0,
           f"rocket_model has zero null values  (found: {model_nulls})")

    # 11. launch_country — no null values
    country_nulls = df["launch_country"].isna().sum()
    _check(country_nulls == 0,
           f"launch_country has zero null values  (found: {country_nulls})")

    # 12. Schema — all expected final columns are present
    missing_cols = [c for c in FINAL_COLUMNS if c not in df.columns]
    _check(not missing_cols,
           f"All expected columns present  (missing: {missing_cols})")

    log.info("=" * 60)
    if all_passed:
        log.info("All validation checks PASSED.")
    else:
        log.error("One or more validation checks FAILED. Review errors above.")
    return all_passed


# ===========================================================================
# Pipeline orchestrator
# ===========================================================================
def run_pipeline() -> pd.DataFrame:
    log.info("=" * 60)
    log.info("OrbitIQ — Data Cleaning Pipeline START")
    log.info("=" * 60)

    df = load_raw(RAW_DATA_PATH)
    df = drop_redundant_columns(df)
    df = rename_columns(df)
    df = drop_duplicates(df)
    df = parse_launch_datetime(df)
    df = add_temporal_features(df)
    df = clean_cost_column(df)
    df = standardise_rocket_status(df)
    df = parse_detail_column(df)
    df = extract_launch_country(df)
    df = add_success_flag(df)
    df = select_final_columns(df)

    validation_passed = run_validation(df)
    export_csv(df, PROCESSED_DATA_PATH)

    log.info("=" * 60)
    log.info("OrbitIQ — Data Cleaning Pipeline COMPLETE")
    log.info("Output : %s", PROCESSED_DATA_PATH)
    log.info("Shape  : %d rows × %d columns", *df.shape)
    log.info("=" * 60)

    if not validation_passed:
        log.error("Pipeline completed with validation warnings. "
                  "Review the log above before proceeding to database ingestion.")

    return df


if __name__ == "__main__":
    run_pipeline()
