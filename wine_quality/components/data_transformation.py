import os
from wine_quality.exception import CustomException
from wine_quality.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from wine_quality.constants import DATA_TRANSFORM_DIR
from dataclasses import dataclass



@dataclass
class DataTransformationtionConfig:
    train_data_path: str=os.path.join('artifacts/data_transformation',"train_data.csv")
    test_data_path: str=os.path.join('artifacts/data_transformation',"test_data.csv")


class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationtionConfig()


    def initiate_data_transformation(self):
        logging.info("Entered the data transformation method")
        try:

            wine_df = pd.read_csv(DATA_TRANSFORM_DIR,encoding = 'latin1')
            wine_df = wine_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            print('wine_df data shape',wine_df.shape)
            final_data_set = wine_df.copy()
            logging.info('Read all dataset and prepared final data as dataframe to preform data tranformation')

            os.makedirs(os.path.dirname(self.transformation_config.train_data_path),exist_ok=True)

            # Split the data into training and test sets. (0.75, 0.25) split.
            train_data, test_data = train_test_split(final_data_set)
            logging.info(f'train data shape: %s' ,train_data.shape)
            logging.info(f'test data shape: %s' ,test_data.shape)

            train_data.to_csv(self.transformation_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.transformation_config.test_data_path,index=False,header=True)
            logging.info("Data transformation completed")
            
            return (self.transformation_config.train_data_path,self.transformation_config.test_data_path)
          
        
        except CustomException as e:
            logging.error(e)



