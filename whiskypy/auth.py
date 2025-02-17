import jwt

JWT = None
DECODED_JWT = None

def auth_decorator():
    def decorator(function):
        def wrapper(args, **kwargs):
            token = args['__ow_headers'].get('authorization', False)
            if not token:
                return {'statusCode': 401, "body": {"error": "missing Authorization"}}
            token_spl = token.split(' ')
            if token_spl[0] != 'Bearer':
                return {"statusCode": 401, "body": {"error": "Authorization failed"}}
            JWT = token_spl[1]
            secret = args['JWT_SECRET']
            try:
                DECODED_JWT = jwt.decode(JWT, key=secret, algorithms='HS256')
            except Exception as e:
                return {"statusCode": 401, "body": {"error": e}}
            return function(args, **kwargs)
        return wrapper
    return decorator