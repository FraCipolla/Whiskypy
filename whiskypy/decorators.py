def param(argument):
    def decorator(function):
        def wrapper(args, **kwargs):
            if argument not in args:
                return {"statusCode": 500, "body": {"error": f"Internal server error: {argument} missing"}}
            return function(args, **kwargs)
        return wrapper
    return decorator

def require(argument):
    def decorator(function):
        def wrapper(args, **kwargs):
            if argument not in args:
                return {"statusCode": 404, "body": {"error": argument + "not found"}}
            return function(args, **kwargs)
        return wrapper
    return decorator

def controller(method = 'get', path = '', fn = None):
    def decorator(function):
        def wrapper(args, **kwargs):
            if args['__ow_method'] == method and args['__ow_path'] == path:
                return fn(args, **kwargs)
            return function(args, **kwargs)
        return wrapper
    return decorator