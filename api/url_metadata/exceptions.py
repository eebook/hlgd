from ..common.exceptions import APIException


class MetadataException(APIException):
    errors_map = {
        'url_not_support': {
            'message': 'This url is not supported',
            'type': 'not_found'
        }
    }
