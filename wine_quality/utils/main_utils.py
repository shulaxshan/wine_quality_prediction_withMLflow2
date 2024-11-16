import os
import sys
import numpy as np
import dill
import yaml
import pickle
from pandas import DataFrame
from pathlib import Path
import json
from wine_quality.exception import CustomException
from wine_quality.logger import logging



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

