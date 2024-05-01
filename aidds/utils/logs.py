from datetime import datetime
from flask import jsonify

from aidds import config as cfg
from aidds import messages as msg
from aidds.utils import get_caller, get_error
from aidds.utils import app_exception


def service_logs(code:str=None, value:any=None) -> None:
    """ Logs display function for the service section. """
    if not cfg.sys.error.is_display:
        return
    display = f'[{datetime.now()}]'
    display += f' {eval(f"msg.log.{code}")}' if code else ''
    display += '' if value is None else f' {value}'
    print(display)
    
    
def route_error_logs(error:any=None) -> None:
    """ Logs display function for the route errors. """
    if not cfg.sys.error.is_display:
        return
    head_message = cfg.sys.error.head
    display = f'\n[{datetime.now()}]'
    display += f'{head_message}[{get_caller()}]\n{get_error(str(error))}\n'
    print(display) 
    
    
def route_error_handle(
    code=None, 
    value=None, 
    status_code=None,
    error_obj=None
):
    if isinstance(error_obj, app_exception):
        error_obj.print()
    else:
        route_error_logs(error_obj)
    error_message = eval(f'msg.exception.{code}')
    error_message += '' if value is None else f': {value}'
    return jsonify({'error': error_message}), status_code