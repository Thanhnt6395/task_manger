from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class ResponseRender(JSONRenderer):
    
    charset = 'utf-8'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if 'ErrorDetail' in str(data):
            response_dict = {
                'status': 'failure',
                'data': None,
                'message': data,
            }
        else:
            response_dict = {
                'status': 'success',
                'data': data,
                'message': 'Action success',
            }
        return json.dumps(response_dict)