import jwt

TOKEN = None, JWT = None

def auth():
    def decorator(function):
        def wrapper(args, **kwargs):
            token = args['__ow_headers'].get('authorization', False)
            if not token:
                return {'statusCode': 401, "body": {"error": "missing Authorization"}}
            token_spl = token.split(' ')
            if token_spl[0] != 'Bearer':
                return {"statusCode": 401, "body": {"error": "Authorization failed"}}
            TOKEN = token_spl[1]
            secret = args.get('JWT_SECRET')
            try:
                JWT = jwt.decode(token, key=secret, algorithms='HS256')
            except:
                return {"statusCode": 401, "body": {"error": "Invalid token"}}
            return function(args, **kwargs)
        return wrapper
    return decorator