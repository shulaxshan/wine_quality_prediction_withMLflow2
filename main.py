from wine_quality.exception import CustomException
from wine_quality.logger import logging
from wine_quality.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started  <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX============")
except Exception as e:
    logging.exception(e)
    raise e