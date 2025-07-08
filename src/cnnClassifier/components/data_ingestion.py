import os 
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
#from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):

        self.config=config
        

    def download_file(self):
        #print("Available keys in config 11:", self.config.keys())
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(url=self.config.source_URL,
                                               filename=self.config.local_data_file 
                                                )
            logger.info(f"{filename}  download! with following inof: \n{header}")
        else:
            logger.info(f"File already exists of the size : {get_size(Path(self.config.local_data_file))}")

        
    def extract_zip_file(self):
        '''
        zip_file_path:str
        extract the zip file into the data directory
        Function return None
        '''
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
