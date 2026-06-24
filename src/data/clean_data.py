from __future__ import annotations

import logging
import sys
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
PROJECT_ROOT        = Path(__file__).resolve().parents[2]
RAW_DATA_PATH       = PROJECT_ROOT / "data" / "raw" / "Space_Corrected.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "space_missions_cleaned.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# Ordered list of columns in the final output
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
    # Raw audit columns
    "datum_raw",
    "detail_raw",
    "rocket_status_raw",
    "cost_usd_millions_raw",
]

# US state/territory names → canonical country label
_COUNTRY_OVERRIDES: dict[str, str] = {
    "Florida":                        "United States",
    "California":                     "United States",
    "Texas":                          "United States",
    "Virginia":                       "United States",
    "New Mexico":                     "United States",
    "Alaska":                         "United States",
    "Marshall Islands":               "United States",
    "Pacific Missile Range Facility": "United States",
    "Yellow Sea":                     "China",
    "Barents Sea":                    "Russia",
    "Pacific Ocean":                  "International Waters",
    "Gran Canaria":                   "Spain",
    "Shahrud Missile Test Site":      "Iran",
    "French Guiana":                  "France",
    "French Guiana, France":          "France",
}

_ROCKET_STATUS_MAP = {"StatusActive": "Active", "StatusRetired": "Retired"}


# ---------------------------------------------------------------------------
# Step 1 – Load
# ---------------------------------------------------------------------------
def load_raw(path: Path) -> pd.DataFrame:
    log.info("Loading raw dataset from: %s", path)
    df = pd.read_csv(path, encoding="utf-8", encoding_errors="replace")
    log.info("Raw shape: %d rows x %d columns", *df.shape)
    return df


# ---------------------------------------------------------------------------
# Step 2 – Drop redundant index columns
# ---------------------------------------------------------------------------
def drop_redundant_columns(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in df.columns if c.startswith("Unnamed")]
    log.info("Dropping redundant columns: %s", cols)
    return df.drop(columns=cols)


# ---------------------------------------------------------------------------
# Step 3 – Rename to snake_case
# ---------------------------------------------------------------------------
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
        "Company Name":   "company",
        "Location":       "location",
        "Datum":          "datum_raw",
        "Detail":         "detail_raw",
        "Status Rocket":  "rocket_status_raw",
        " Rocket":        "cost_usd_millions_raw",
        "Status Mission": "mission_status",
    }
    log.info("Renaming columns to snake_case.")
    return df.rename(columns=rename_map)


# ---------------------------------------------------------------------------
# Step 4 – Deduplicate
# ---------------------------------------------------------------------------
def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.drop_duplicates(keep="first").reset_index(drop=True)
    log.info("Duplicates removed: %d  (before=%d, after=%d)", before - len(df), before, len(df))
    return df


# ---------------------------------------------------------------------------
# Step 5 – Parse launch datetime
# ---------------------------------------------------------------------------
def parse_launch_datetime(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Parsing launch datetime.")
    df["launch_datetime"] = pd.to_datetime(
        df["datum_raw"].str.strip().str.replace(r"\s*UTC$", "", regex=True),
        format="mixed",
        dayfirst=False,
        utc=True,
        errors="coerce",
    )
    nat_count = df["launch_datetime"].isna().sum()
    if nat_count:
        log.warning("launch_datetime: %d rows could not be parsed (NaT).", nat_count)
    else:
        log.info("launch_datetime: all rows parsed successfully.")
    return df


# ---------------------------------------------------------------------------
# Step 6 – Temporal features
# ---------------------------------------------------------------------------
def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Deriving launch_year, launch_month, launch_decade.")
    dt = df["launch_datetime"].dt
    df["launch_year"]   = dt.year.astype("Int64")
    df["launch_month"]  = dt.month.astype("Int64")
    df["launch_decade"] = df["launch_year"].apply(
        lambda y: f"{(y // 10) * 10}s" if pd.notna(y) else None
    )
    return df


# ---------------------------------------------------------------------------
# Step 7 – Clean cost column
# ---------------------------------------------------------------------------
def clean_cost_column(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Cleaning cost_usd_millions.")
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
    log.info("cost_usd_millions: %d present, %d NULL (%.1f%% missing).",
             filled, missing, 100 * missing / len(df))
    return df


# ---------------------------------------------------------------------------
# Step 8 – Standardise rocket_status
# ---------------------------------------------------------------------------
def standardise_rocket_status(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Standardising rocket_status.")
    df["rocket_status"] = df["rocket_status_raw"].map(_ROCKET_STATUS_MAP)
    unmapped = df["rocket_status"].isna().sum()
    if unmapped:
        log.warning("rocket_status: %d values could not be mapped.", unmapped)
    return df


# ---------------------------------------------------------------------------
# Step 9 – Split detail into rocket_model / payload_name
# ---------------------------------------------------------------------------
def parse_detail_column(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Splitting detail_raw into rocket_model and payload_name.")
    split = df["detail_raw"].str.split(r"\|", n=1, expand=True)
    df["rocket_model"] = split[0].str.strip()
    df["payload_name"] = split[1].str.strip() if 1 in split.columns else None
    no_pipe = df["payload_name"].isna().sum()
    if no_pipe:
        log.warning("payload_name: %d rows had no '|' delimiter.", no_pipe)
    return df


# ---------------------------------------------------------------------------
# Step 10 – Extract launch_country
# ---------------------------------------------------------------------------
def extract_launch_country(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Extracting launch_country from location.")
    raw_country = df["location"].str.split(",").str[-1].str.strip()
    df["launch_country"] = raw_country.replace(_COUNTRY_OVERRIDES)
    log.info("launch_country: %d unique values.", df["launch_country"].nunique())
    return df


# ---------------------------------------------------------------------------
# Step 11 – is_success flag
# ---------------------------------------------------------------------------
def add_success_flag(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Deriving is_success flag.")
    df["is_success"] = (df["mission_status"] == "Success").astype(int)
    log.info("is_success: %.1f%% success rate.", df["is_success"].mean() * 100)
    return df


# ---------------------------------------------------------------------------
# Step 12 – Column selection and export
# ---------------------------------------------------------------------------
def select_final_columns(df: pd.DataFrame) -> pd.DataFrame:
    available = [c for c in FINAL_COLUMNS if c in df.columns]
    skipped   = [c for c in FINAL_COLUMNS if c not in df.columns]
    if skipped:
        log.warning("Columns not found, skipping: %s", skipped)
    return df[available].reset_index(drop=True)


def export_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")
    log.info("Exported: %s  (%d rows x %d cols)", path, *df.shape)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
def run_validation(df: pd.DataFrame) -> bool:
    log.info("-" * 55)
    log.info("Running validation checks...")
    all_passed = True

    def _check(condition: bool, msg: str) -> None:
        nonlocal all_passed
        status = "PASS" if condition else "FAIL"
        (log.info if condition else log.error)("  [%s]  %s", status, msg)
        if not condition:
            all_passed = False

    valid_years    = df["launch_year"].dropna()
    cost_non_null  = df["cost_usd_millions"].dropna()
    missing_pct    = df["cost_usd_millions"].isna().mean() * 100
    dup_count      = df.duplicated(subset=["company", "launch_datetime", "detail_raw"]).sum()

    _check(len(df) == 4323,
           f"Row count == 4323 (actual: {len(df)})")
    _check(dup_count == 0,
           f"No duplicates on (company, launch_datetime, detail_raw) (found: {dup_count})")
    _check(df["launch_datetime"].isna().sum() == 0,
           f"launch_datetime: no NaT values (found: {df['launch_datetime'].isna().sum()})")
    _check(valid_years.between(1957, 2021).all(),
           f"launch_year in [1957, 2021] (min={valid_years.min()}, max={valid_years.max()})")
    _check((cost_non_null >= 0).all(),
           f"No negative cost values (min={cost_non_null.min() if len(cost_non_null) else 'N/A'})")
    _check(missing_pct < 80,
           f"cost_usd_millions missing rate < 80% (actual: {missing_pct:.1f}%)")
    _check(set(df["rocket_status"].dropna().unique()).issubset({"Active", "Retired"}),
           f"rocket_status values: {set(df['rocket_status'].dropna().unique())}")
    _check(set(df["mission_status"].dropna().unique()).issubset(
               {"Success", "Failure", "Partial Failure", "Prelaunch Failure"}),
           f"mission_status values valid")
    _check(df["is_success"].isin([0, 1]).all(),
           f"is_success contains only 0 or 1")
    _check(df["rocket_model"].isna().sum() == 0,
           f"rocket_model: no nulls (found: {df['rocket_model'].isna().sum()})")
    _check(df["launch_country"].isna().sum() == 0,
           f"launch_country: no nulls (found: {df['launch_country'].isna().sum()})")
    _check(not [c for c in FINAL_COLUMNS if c not in df.columns],
           f"All expected columns present")

    log.info("-" * 55)
    log.info("Validation %s.", "PASSED" if all_passed else "FAILED — review errors above")
    return all_passed


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------
def run_pipeline() -> pd.DataFrame:
    log.info("=" * 55)
    log.info("OrbitIQ — Data Cleaning Pipeline START")
    log.info("=" * 55)

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
    run_validation(df)
    export_csv(df, PROCESSED_DATA_PATH)

    log.info("=" * 55)
    log.info("Pipeline COMPLETE — output: %s", PROCESSED_DATA_PATH)
    log.info("=" * 55)
    return df


if __name__ == "__main__":
    run_pipeline()
