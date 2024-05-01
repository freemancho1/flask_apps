import os
import pandas as pd
from pickle import load as pickle_load
from joblib import load as joblib_load

from aidds import config as cfg 
from aidds import messages as msg 
from aidds.utils import app_exception


def read_data(code:str=None, **kwargs) -> bytes:
    try:
        file_type, file_path = _get_file_path(code=code)
        match file_type:
            case cfg.file.type.pickle:
                with open(file_path, 'rb') as file:
                    return pickle_load(file)
            case cfg.file.type.model:
                return joblib_load(file_path)
            case _: # data
                return pd.read_csv(file_path, **kwargs)
    except Exception as e:
        raise app_exception(e)
    
def get_cleaning_data() -> dict[str, pd.DataFrame]:
    try:
        return {
            pkey: read_data(code=f'data.cleaning.{pkey}') \
                for pkey in cfg.type.pds
        }
    except Exception as e:
        raise app_exception(e)
    
def get_service_pickle() -> tuple[dict[str, bytes], bytes, bytes]:
    try:
        pkl = {
            pkey: read_data(code=f'pickle.{pkey}') \
                for pkey in list(cfg.file.pickle.keys())[:-1]
        }
        scaler = read_data(code='pickle.scaler')
        model = read_data(code='model')
        return pkl, scaler, model
    except Exception as e:
        raise app_exception(e)


def _get_file_path(code:str=None) -> tuple[str, str]:
    try:
        # Find file name and ext
        file_name = eval(f'cfg.file.{code}')
        _, file_ext = os.path.splitext(file_name)
        
        # Get file type
        assert file_ext.lower() in \
            [cfg.file.ext.data, cfg.file.ext.pickle, cfg.file.ext.model], \
            f'{msg.exception.unknown_file_ext} "{file_ext}"'
        
        match file_ext:
            case cfg.file.ext.data:
                file_type = cfg.file.type.data
            case cfg.file.ext.pickle:
                file_type = cfg.file.type.pickle
            case _:
                file_type = cfg.file.type.model
        
        # Get file path list
        file_paths = [cfg.file.base_path, file_type, file_name]
        #      file_type, file_path,                 file_ext
        return file_type, os.path.join(*file_paths)
    except Exception as e:
        raise app_exception(e)