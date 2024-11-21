from wine_quality.exception import CustomException
from wine_quality.logger import logging
from wine_quality.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine_quality.pipline.stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started  <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX============")
except CustomException as e:
    logging.error(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except CustomException as e:
    logging.error(e)
    raise e