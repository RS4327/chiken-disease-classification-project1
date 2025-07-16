from cnnClassifier.config.configuration import ConfigurarationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME ="Prepare Base Model"

class PrepareBaseModelTrainingPipeline():
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurarationManager()
        prepare_base_model_config=config.get_prepare_base_model_cofig()
        prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
    



if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} complated <<<<<<<<<< \n\nx=========x")
    except Exception as e:
        logger.exception(e)
