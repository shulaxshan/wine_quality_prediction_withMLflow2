import os
import sys
import numpy as np
import dill
import yaml
import pickle
import joblib
from pandas import DataFrame
from pathlib import Path
import json
from wine_quality.exception import CustomException
from wine_quality.logger import logging
from typing import Any



def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e, sys) from e
    

def create_directories(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"Directory '{path}' created successfully.")


def save_json(path: Path, data: dict):

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")


def load_json(path: Path):
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded succesfully from: {path}")
    return content



def save_bin(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            joblib.dump(obj, file_obj)
        logging.info(f"binary file saved at: {file_path}")
    except Exception as e:
        raise CustomException(e,sys)



def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data

