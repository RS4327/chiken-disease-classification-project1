from cnnClassifier.config.configuration import ConfigurarationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier import logger

STAGE_NAME = "Prepare CallBacks"

class PrepareCallBackTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            config = ConfigurarationManager()
            prepare_callbacks_config = config.get_prepare_callback_config()
            prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
            callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
            
        except Exception as e:
            raise e
    

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=PrepareCallBackTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} complated <<<<<<<<<< \n\nx=========x")
    except Exception as e:
        logger.exception(e)
