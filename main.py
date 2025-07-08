import sys
import os
#import numpy as np
os.chdir("../")
sys.path.append(os.path.join(os.getcwd(), "src"))

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_ingestion import DataIngestionTrainingPipeline


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

