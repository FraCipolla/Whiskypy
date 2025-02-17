from typing import overload

def param(argument):
    def decorator(function):
        def wrapper(args, **kwargs):
            if argument not in args:
                return {"statusCode": 500, "body": {"error": f"Internal server error: {argument} missing"}}
            return function(args, **kwargs)
        return wrapper
    return decorator

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
            fn = mapping[method][path]
            if fn:
                function(args, **kwargs)
                return fn(args)
            if 'default' in mapping:
                return mapping['default']
            return {'statusCode': 404}
        return wrapper
    return decorator

def parse(argument, store):
    def decorator(function):
        def wrapper(args, **kwargs):
            if argument not in args:
                return {"statusCode": 404, "body": {"error": argument + "not found"}}
            store = argument
            return function(args, **kwargs)
        return wrapper
    return decorator
