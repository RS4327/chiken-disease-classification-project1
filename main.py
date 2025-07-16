import sys
import os
#import numpy as np
os.chdir("../")
sys.path.append(os.path.join(os.getcwd(), "src"))

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_prepare_callbacks import PrepareCallBackTrainingPipeline
from cnnClassifier.pipeline.stage_04_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_05_evaluation import EvaluationPipeline


sys.path.append(os.path.abspath(".."))  # or "." depending on your structure
STAGE_NAME='Data Ingestion Stage'


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} complated <<<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

#logger.info("welcome to my custome log")
STAGE_NAME ="Prepare Base Model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} complated <<<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare CallBacks"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=PrepareCallBackTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} complated <<<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Training"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} complated <<<<<<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Evaluation stage"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
            