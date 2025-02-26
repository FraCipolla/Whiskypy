import jwt
import os

class ow_auth:
    def __init__(self, func):
        self._fn = func
        self.token = "token"
        self.decoded = "decoded"

    def __call__(self, args, **kwargs):
        token = args['__ow_headers'].get('authorization', False)
        if not token:
            return {'statusCode': 401, "body": {"error": "missing Authorization"}}
        token_spl = token.split(' ')
        if token_spl[0] != 'Bearer':
            return {"statusCode": 401, "body": {"error": "Authorization failed"}}
        secret = args['JWT_SECRET']
        self.token = token_spl[1]
        try:
            self.decoded = jwt.decode(self.token, key=secret, algorithms='HS256')
        except Exception as e:
            return {"statusCode": 401, "body": {"error": e}}
        return self._fn(args, **kwargs)

def auth_decorator(function):
    def wrapper(args, **kwargs):
        token = args['__ow_headers'].get('authorization', False)
        if not token:
            return {'statusCode': 401, "body": {"error": "missing Authorization"}}
        token_spl = token.split(' ')
        if token_spl[0] != 'Bearer':
            return {"statusCode": 401, "body": {"error": "Authorization failed"}}
        secret = args['JWT_SECRET']
        try:
            jwt.decode(token_spl[1], key=secret, algorithms='HS256')
        except Exception as e:
            return {
                "headers": {'Set-Cookie': f"{os.environ['__OW_NAMESPACE']}-sess-cookie=; HttpOnly; Secure; expires=Thu, 01 Jan 1970 00:00:01 GMT"},
                "statusCode": 401,
                "body": {"error": "token expired"}
                }
        return function(args, **kwargs)
    return wrapper