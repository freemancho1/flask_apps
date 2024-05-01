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