import os
import sys
from wine_quality.exception import CustomException
from wine_quality.logger import logging
import pandas as pd
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    final_data_path: str=os.path.join('artifacts/data_ingestion',"final_data.csv")
    # category_data_path: str=os.path.join('artifacts/data_ingestion',"category_data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:

            wine_df = pd.read_csv('notebook/data/winequality-red.csv',encoding = 'latin1')
            wine_df = wine_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            print('wine_df data shape',wine_df.shape)
            final_data_set = wine_df.copy()
            logging.info('Read all dataset and prepared final data as dataframe to preform data tranformation')

            os.makedirs(os.path.dirname(self.ingestion_config.final_data_path),exist_ok=True)

            final_data_set.to_csv(self.ingestion_config.final_data_path,index=False,header=True,encoding='latin1')
            logging.info("Data ingestion completed")
            
            return (self.ingestion_config.final_data_path)
            #return final_data_set
        
        except CustomException as e:
            logging.error(e)


# if __name__ == "__main__":
#     data_ingestion=DataIngestion()
#     final_data_path = data_ingestion.initiate_data_ingestion()

#     data_transform = DataTransformation()
#     selected_df_daily,selected_df_weekly,selected_df_monthly, max_date = data_transform.data_preprocessor(final_data_path)

#     model_trainer =ModelTraining()
#     model_trainer.initiate_model_forecast(selected_df_weekly,max_date)

