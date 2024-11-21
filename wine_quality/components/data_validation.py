import os
from wine_quality.exception import CustomException
from wine_quality.logger import logging
import pandas as pd
from dataclasses import dataclass
from wine_quality.utils.main_utils import read_yaml_file
from wine_quality.constants import SCHEMA_FILE_PATH,DATA_VALIDATION_DIR_NAME,DATA_INGESTED_DIR
import sys


@dataclass
class DataValidationConfig:
    validation_status_file_path = os.path.join(DATA_VALIDATION_DIR_NAME, 'validation_status.txt')


# DataValidation Class
class DataValidation:
    def __init__(self):
        try:
            self.data_validation_config = DataValidationConfig()
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)

        except Exception as e:
            raise CustomException(e,sys)
        

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            # Read the dataset
            data = pd.read_csv(DATA_INGESTED_DIR)
            data_columns = list(data.columns)


            # Read schema columns
            schema = self._schema_config['COLUMNS_']
            schema_columns = list(schema)

            os.makedirs(os.path.dirname(self.data_validation_config.validation_status_file_path),exist_ok=True)
            
            for col in data_columns:
                if col not in schema_columns:
                    validation_status = False
                    with open(self.data_validation_config.validation_status_file_path,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.data_validation_config.validation_status_file_path, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status

        except CustomException as e:
            logging.error(e)
            raise


