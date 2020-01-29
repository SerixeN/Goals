from http import HTTPStatus

from flask_restful import abort


def error_handler(error_message):
    def base(func):
        def wrap(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=error_message)
        return wrap
    return base
