from typing import overload
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
                fn = mapping[method][path]
                function(args, **kwargs)
                return fn(args)
            except:
                if 'default' in mapping:
                    return mapping['default']
            return {'statusCode': 404}
        return wrapper
    return decorator