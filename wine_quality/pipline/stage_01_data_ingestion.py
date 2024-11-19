from wine_quality.components.data_ingestion import DataIngestion
from wine_quality.exception import CustomException
from wine_quality.logger import logging



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        data_ingestion= DataIngestion()
        final_data_path = data_ingestion.initiate_data_ingestion()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>>> stage {STAGE_NAME} started  <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX============")
    except Exception as e:
        logging.exception(e)
        raise e
    
