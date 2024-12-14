from wine_quality.components.model_trainer import ModelTrainer
from wine_quality.exception import CustomException
from wine_quality.logger import logging

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        model_training = ModelTrainer()
        model_training.initiate_model_trainer()



if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except CustomException as e:
        logging.error(e)
    