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

class ow_controller:
    def __init__(self, func):
        self._fn = func

    def __call__(self, args, **kwargs):
        print(locals())
    
def controller(mapping = {'get': {}, 'post': {}, 'delete': {}, 'put': {}, 'default': {'statusCode': 404}}):
    def decorator(function):
        def wrapper(args, **kwargs):
            body = str(inspect.getsourcelines(function))
            lines = body.split('\n')
            # print(lines)
            i = 0
            method = args['__ow_method']
            path = args['__ow_path']
            function(args, **kwargs)
            try:
                # while lines:
                #     if lines[i].startswith('def main'):
                #         break
                #     i += 1
                # while lines:
                #     if lines[i].startswith('@' + method):
                #         inner_path = lines[i].split('(')[1]
                #         if inner_path[:-1] == path:
                #             next_line = lines[i + 1]
                fn = mapping[method][path]
                if type(fn) is Response:
                    return {"headers": fn.headers, "statusCode": fn.status_code, "body": fn.json()}
                return fn(args)
            except Exception as e:
                if 'default' in mapping:
                    return mapping['default']
            return {'statusCode': 404}
        print(locals())
        return wrapper
    return decorator

def get(path=''):
    def decorator(function):
        def wrapper(args, **kwargs):
            return function(args)
        return wrapper
    return decorator

def post(path=''):
    def decorator(function):
        def wrapper(args, **kwargs):
            return function(args)
        return wrapper
    return decorator

def delete(path=''):
    def decorator(function):
        def wrapper(args, **kwargs):
            return function(args)
        return wrapper
    return decorator

def put(path=''):
    def decorator(function):
        def wrapper(args, **kwargs):
            return function(args)
        return wrapper
    return decorator