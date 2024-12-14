import os
import urllib.parse
from pathlib import Path


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


"""
Data transformations
"""
DATA_TRANSFORM_DIR = "artifacts/data_ingestion/final_data.csv"


"""
Model Trainer
"""
PARAM_FILE_PATH = Path("parameter.yaml")
MODEL_TRAINER_DIR = "artifacts/model_trainer"
MODEL_TRAIN_DATA_PATH = "artifacts/data_transformation/train_data.csv"
MODEL_TEST_DATA_PATH = "artifacts/data_transformation/test_data.csv"
MODEL_PATH = "artifacts/model_trainer/model.joblib"