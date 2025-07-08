import os
import sys
#os.chdir("../")
os.chdir(r"C:\Users\rajum\DATA SCIENCE\DeepLearning\ImageClassification\chiken-disease-classification-project")
#sys.path.append(os.path.join(os.getcwd(), "src"))
from box.exceptions import BoxValueError
import  yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import Box
from pathlib  import Path
from typing import  Any
import base64


class ConfigBox(Box):
    def __getattr__(self, item):
        if item not in self:
            raise AttributeError(f"Key '{item}' not found in ConfigBox.")
        return super().__getattr__(item)


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox (dot-access dict).

    Args:
        path_to_yaml (Path): Path to YAML file

    Raises:
        ValueError: if file is empty or content is invalid

    Returns:
        ConfigBox: Parsed YAML config
    """
    try:
        print("Current Working Directory yaml:",path_to_yaml)
        print("Current Directory:", os.getcwd())
        print("Files:", os.listdir())
        print("Config Folder Contents:", os.listdir("config") if os.path.exists("config") else "Config folder missing")

        with open(Path(str(path_to_yaml).replace('\\', '/'))) as yaml_file:
            content = yaml.safe_load(yaml_file)
            print("DEBUG YAML path_to_yaml:", path_to_yaml)
            print("DEBUG YAML content:", content, "TYPE:", type(content))

        if content is None:
            raise ValueError(f"YAML file is empty: {path_to_yaml}")
        if not isinstance(content, dict):
            raise ValueError(f"YAML content must be a dictionary, got {type(content)}")

        logger.info(f"YAML file : {path_to_yaml} loaded successfully")
        return ConfigBox(content)

    except BoxValueError:
        raise ValueError("read_yaml1: YAML file content is invalid for Box")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories :list,verbose=True):
    '''Create list of directories

    args : Path_to_directories(list): list of path of directories
    ignore_log(bool,optional):ignore if multiple dirs is tobe created.Defaults to false
    '''
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")

@ensure_annotations
def save_json(path:Path,data: dict):
    ''' 
    save json data

    args: 
        path(path): Path to json file
        data(dict): data to be saved in the json file
    '''
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"file saved at :{path}")


@ensure_annotations
def load_json(path :Path) -> ConfigBox:
    '''
    Load json files data
    
    args: Path(path): path to json file
    
    return : ConfigBox:data as class attributes insted of dict

    '''
    with open(path) as f:
        content =json.load()
    
    logger.info(f"json file loadded successfully from :{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    '''
    save binary file
    
    args:
        data(any) : data to be saved as binary
        path(path) : path to binary file
    '''
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at :{path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    ''' 
        Load binary data

        args :
            path(path): Path to binary file

        Returns : 
            Any: Object stored in the file
    '''
    data=joblib.load(path)
    logger.info(f"Binary file loaded from :{path}")
    return data
@ensure_annotations
def get_size(path:Path) ->str:
    '''
        Get the size in KB
        args:
            path(path): path of the file
        Return: 
            str: Size in kb 

    '''
    size_in_kb=round(os.path.getsize(path/1024))
    return f"~{size_in_kb} KB"

def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()
    
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode.read()
    




              
              