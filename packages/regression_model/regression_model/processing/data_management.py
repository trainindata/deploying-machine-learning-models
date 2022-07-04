import pandas as pd
import joblib
from  sklearn.pipeline import Pipeline

from regression_model.config import config
from regression_model.config import logging_config
from regression_model import __version__ as _version

_logger = logging_config.get_logger("test")
def load_dataset(*, file_name: str) -> pd.DataFrame:
    """
    loads the data set from the file name 
    """
    print (f'{config.DATASET_DIR}/{file_name}')
    print(file_name)
    print('****')
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return _data

def save_pipeline(*, pipeline_to_persist) -> None:
    """
    persist the pipeline
    """

    save_file_name = f'{config.PIPELINE_SAVE_FILE}_{_version}.pkl'
    save_path = config.TRAINED_MODEL_DIR /save_file_name
    remove_old_pipelines(files_to_keep = save_file_name)
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f'saved pipeline: {save_file_name}')
    

def load_pipeline(*, file_name: str)-> Pipeline:
    """
    load a persisted pipeline
    """
    file_path = config.TRAINED_MODEL_DIR / file_name
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline

def remove_old_pipelines(*, files_to_keep):
    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in [files_to_keep, '__init__.py']:
            model_file.unlink()