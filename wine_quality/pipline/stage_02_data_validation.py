from wine_quality.components.data_validation import DataValidation
from wine_quality.exception import CustomException
from wine_quality.logger import logging

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        data_validation = DataValidation()
        data_validation.validate_all_columns()



if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except CustomException as e:
        logging.error(e)
    


