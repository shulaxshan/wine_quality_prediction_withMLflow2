import os
import urllib.parse
from pathlib import Path

# CONFIG_FILE_PATH = Path("config/config.yaml")
# SCHEMA_FILE_PATH = Path("schema.yaml")
# PARAMS_FILE_PATH = Path("params.yaml")
# STATS_FILE_PATH: str = Path("artifacts/report.yaml")


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
CONFIG_FILE_PATH = Path("config/config.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")
# Root directory for artifacts
ARTIFACTS_ROOT = Path("artifacts")
DATA_VALIDATION_DIR_NAME: str = "artifacts/data_validation"
DATA_VALIDATION_DIR = ARTIFACTS_ROOT / "data_validation"
STATUS_FILE = DATA_VALIDATION_DIR / "status.txt"
DATA_INGESTED_DIR: str ="artifacts/data_ingestion/final_data.csv"
