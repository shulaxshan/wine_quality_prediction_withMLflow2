from wine_quality.components.data_transformation import DataTransformation
from wine_quality.exception import CustomException
from wine_quality.logger import logging

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation()



if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except CustomException as e:
        logging.error(e)
    


