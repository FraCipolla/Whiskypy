from typing import overload
from requests import Response
import inspect

@overload
def require(argument: str): ...
@overload
def require(argument: list[str]): ...

def require(argument: str | list[str]):
    def decorator(function):
        def wrapper(args, **kwargs):
            if isinstance(argument, list):
                for el in argument:
                    if el not in args:
                        return {"statusCode": 404, "body": {"error": el + "not found"}}        
            else:
                if argument not in args:
                    return {"statusCode": 404, "body": {"error": argument + "not found"}}
            return function(args, **kwargs)
        return wrapper
    return decorator

def controller(mapping = {'get': {}, 'post': {}, 'delete': {}, 'put': {}, 'default': {'statusCode': 404}}):
    def decorator(function):
        def wrapper(args, **kwargs):
            method = args['__ow_method']
            path = args['__ow_path']
            try:
                function(args, **kwargs)
                fn = mapping[method][path]
                if type(fn) is Response:
                    return {"headers": fn.headers, "statusCode": fn.status_code, "body": fn.json()}
                return fn(args)
            except Exception as e:
                if 'default' in mapping:
                    return mapping['default']
            return {'statusCode': 404}
        return wrapper
    return decorator

class ow_controller:
    def __init__(self):
        pass

    def get(self, path=''):
        def decorator(function):
            def wrapper(args, **kwargs):
                return function(args)
            return wrapper
        return decorator

    def post(self, path=''):
        def decorator(function):
            def wrapper(args, **kwargs):
                return function(args)
            return wrapper
        return decorator

    def delete(self, path=''):
        def decorator(function):
            def wrapper(args, **kwargs):
                return function(args)
            return wrapper
        return decorator

    def get(self, path=''):
        def decorator(function):
            def wrapper(args, **kwargs):
                return function(args)
            return wrapper
        return decorator