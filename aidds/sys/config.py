import os
from datetime import timedelta
from dotmap import DotMap

_sys = {
    "name": "aidds",
    # Search for directory one up(parent) in current path
    "app_root": os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../')
    ),
}
_sys.update({
    "error": {
        "is_display": True,
        "pattern": r'\n[A-Z].*?\n',
        "endswith": '***',
        "head": f" ||| [{_sys['name']}-error] ",
    },
})
sys = DotMap(_sys)

_app = {
    "static_folder": os.path.join(sys.app_root, 'client', 'static'),
    "template_folder": os.path.join(sys.app_root, 'client', 'templates'),
    "debug": True,
    "connect_args": {"options": "-c timezone=utc"},
    "secret_key": "aIddSzA#x8yqp!xwowHpwct",
    "session_cookie_name": "AIDDS_SESSION",
    "session_lifetime": timedelta(31),    # 31 days
    "jinja": {
        "trim_blocks": True,
    },
}
app = DotMap(_app)

# Data type
_type = {
    # Provide DataSet
    'pds': ['cons', 'pole', 'line', 'sl'],
    # Training DataSet
    'tds': ['train_x', 'test_x', 'train_y', 'test_y']
}
type = DotMap(_type)

# Columns
_cols = {
    # Column to be used for joining
    'join'                      : 'acc_no',
    # Column to be used as the target for model training
    'target'                    : 'cons_cost'
}
_cols.update({
    'cons': [
        _cols['join'],
        _cols['target'],  
        'pred_id',
        'pred_seq',
        'office_cd',
        'cntr_pwr',
        'sply_tpcd',
    ]
})
cols = DotMap(_cols)

_file = {
    'type': {
        'data'                  : 'data',
        'pickle'                : 'pickle',
        # Using: joblib
        'model'                 : 'model',
    },
    'ext': {
        'data'                  : '.csv',
        'pickle'                : '.pkl',
        'model'                 : '.model',
    },
    'base_path': os.path.join(sys.app_root, 'data'),
}
_csv = _file["ext"]["data"]
_pkl = _file['ext']['pickle']
_model = _file['ext']['model']
_file.update({
    # CSV data
    'data': {
        'pp': 'data04_scaling'+_csv,
        'cleaning': {
            pkey: f'data01_{pkey}_cleaning'+_csv \
                for pkey in type.pds
        },
    },
    # Memory Data
    'pickle': {
        'office_codes': 'mem01_office_codes'+_pkl,
        'pole_one_hot_cols': 'mem02_pole_one_hot_cols'+_pkl,
        'line_one_hot_cols': 'mem03_line_one_hot_cols'+_pkl,
        'sl_one_hot_cols': 'mem04_sl_one_hot_cols'+_pkl,
        'last_pp_cols': 'mem05_last_pp_cols'+_pkl,
        'modeling_cols': 'mem06_modeling_cols'+_pkl,
        'scaler': 'mem07_scaler'+_pkl,
    },
    # Model Data: 
    # This model data is stored using joblib instead of pickle
    'model': f'mem09_model_best'+_model,
})
file = DotMap(_file)