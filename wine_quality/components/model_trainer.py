import os
from wine_quality.exception import CustomException
from wine_quality.logger import logging
import pandas as pd
import sys
from dataclasses import dataclass
from sklearn.linear_model import ElasticNet
import joblib
from wine_quality.utils.main_utils import read_yaml_file,save_bin
from wine_quality.constants import SCHEMA_FILE_PATH,PARAM_FILE_PATH,MODEL_PATH,MODEL_TEST_DATA_PATH,MODEL_TRAIN_DATA_PATH


@dataclass
class ModelTrainerConfig:
    model_obj_file_path = os.path.join(MODEL_PATH)


class ModelTrainer:
    def __init__(self):
        try:
            self.model_trainer_config = ModelTrainerConfig()
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
            self._param_config = read_yaml_file(file_path=PARAM_FILE_PATH)

        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_model_trainer(self):
        train_data = pd.read_csv(MODEL_TRAIN_DATA_PATH)
        test_data = pd.read_csv(MODEL_TEST_DATA_PATH)
        logging.info("Sucessfully loaded train and test data for model trainer")

        train_x = train_data.drop([self._schema_config['TARGET_COLUMN']['name']], axis=1)
        test_x = test_data.drop([self._schema_config['TARGET_COLUMN']['name']], axis=1)
        train_y = train_data[[self._schema_config['TARGET_COLUMN']['name']]]
        test_y = test_data[[self._schema_config['TARGET_COLUMN']['name']]]
        logging.info("Sucessfully splitted the data set as train_x,test_x,train_y and test_y")

        lr = ElasticNet(alpha=self._param_config['ElasticNet']['alpha'], l1_ratio=self._param_config['ElasticNet']['l1_ratio'], random_state=42)
        lr.fit(train_x, train_y)

        
        save_bin(lr,self.model_trainer_config.model_obj_file_path)
        logging.info("Model Trainer completed successfully and saved the trained model")

        return self.model_trainer_config.model_obj_file_path