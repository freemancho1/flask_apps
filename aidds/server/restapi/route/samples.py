from flask import jsonify, request, json, abort
from flask.views import MethodView
from werkzeug.exceptions import HTTPException

from aidds import http_codes as hc
from aidds.utils import app_exception
from aidds.utils import route_error_handle
from aidds.server.restapi.service import service_manager

sm = service_manager().get_instance()


class Samples(MethodView):
    
    def get(self):
        try:
            recommend_count: int = request.args.get('req_cnt', default=3, type=int)
            req_list_str: str = request.args.get('req_list', default='[]')
            req_list = list(map(str, req_list_str.strip('[]').split(',')))
            sample = sm.samples().get(
                recommend_count = recommend_count, 
                req_list = req_list
            )
            # Test HTTPException
            # abort(401)
            return sample, hc.OK
        except HTTPException as he:
            return route_error_handle(f'hc_msg.e{he.code}', None, he.code, he)
        except app_exception as ae:
            return route_error_handle('hc_msg.e500', None, hc.ISE, ae)
        except Exception as e:
            return route_error_handle('hc_msg.e500', None, hc.ISE, e) 
        
    def post(self):
        try:
            # Exception handling is ambiguous
            # input_json = request.json
            input_data = request.get_data()
            input_json = json.loads(input_data)
        except ValueError as ve:
            return route_error_handle('bad_json', str(ve), hc.BR, ve)
        
        return input_json, hc.OK
        
        