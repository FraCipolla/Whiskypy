import os
import requests
from requests.auth import HTTPBasicAuth

class _Invoke:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def get(self, action=None, headers={}, params={}, namespace=None):
        try:
            if not action:
                raise ValueError('action name missing')
            return requests.get(
                f"{self.apihost}/api/v1/web/{self.namespace if not namespace else namespace}/{action}",
                headers=headers,
                params=params
                )
        except requests.exceptions.RequestException as e:
            print(e)
            raise SystemExit(e)
        
    def post(self, action=None, headers = {"Content-Type": "application/json"}, params={}, body = {}, namespace=None):
        try:
            if not action:
                raise ValueError('action name missing')
            return requests.get(
                f"{self.apihost}/api/v1/web/{self.namespace if not namespace else namespace}/{action}",
                headers=headers,
                json=body,
                params=params
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def delete(self, action=None, headers = {}, params={}, namespace=None):
        try:
            if not action:
                raise ValueError('action name missing')
            return requests.delete(
                f"{self.apihost}/api/v1/web/{self.namespace if not namespace else namespace}/{action}",
                headers=headers,
                params=params
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def put(self, action=None, headers = {"Content-Type": "application/json"}, params={}, body = {}, namespace=None):
        try:
            return requests.put(
                f"{self.apihost}/api/v1/web/{self.namespace if not namespace else namespace}/{action}",
                headers=headers,
                json=body,
                params=params
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Action:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def list(self, limit = 30, skip = 0):
        try:
            return requests.get(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    params={"limit": limit, "skip": skip}
                    )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def get(self, action=None):
        try:
            if action:
                return requests.get(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    )
            raise ValueError("action name missing")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def create(self, action=None, body={}):
        try:
            if not action:
                raise ValueError("action name missing")
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                json=body,
                params={"overwrite": False}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def update(self, action=None, body={}):
        try:
            if not action:
                raise ValueError("action name missing")
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                json=body,
                params={"overwrite": True}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def delete(self, action=None):
        try:
            if not action:
                raise ValueError("action name missing")
            return requests.delete(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def invoke(self, action=None, blocking=False, result=False, timeout=60000, payload={}):
        try:
            if not action:
                raise ValueError("action name missing")
            return requests.post(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"blocking": blocking, 'result': result, 'timeout': timeout},
                json=payload
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Package:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace
    
    def list(self, public=False, limit=30, skip=0):
        try:
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"public": public, "limit": limit, "skip": skip}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def get(self, package=None, public=False, limit=30, skip=0):
        try:
            if package:
                return requests.get(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages/{package}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    params={"public": public, "limit": limit, "skip": skip}
                    )
            raise ValueError('package name missing')
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def delete(self, package, force=False):
        try:
            r = requests.delete(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages/{package}?force=true",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"force": force}
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def create(self, package, overwrite=False, body={}):
        try:
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages/{package}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                json=body,
                params={"overwrite": overwrite}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def update(self, package, overwrite=True, body={}):
        try:
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages/{package}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                json=body,
                params={"overwrite": overwrite}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Activation:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def list(self, name = None, limit = 30, skip = 0, since = 0, upto = 0, docs=False):
        try:
            if name:
                return requests.get(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    params={'name': name, "limit": limit, "skip": skip, "since": since, "upto": upto, 'docs': docs}
                    )    
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"limit": limit, "skip": skip, "since": since, "upto": upto, 'docs': docs}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def get(self, id=None):
        try:
            if id:
                return requests.get(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations/{id}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    )
            raise ValueError("activation id is missing")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def logs(self, id):
        try:
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations/{id}/logs",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def result(self, id):
        try:
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations/{id}/result",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Rule:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def list(self, limit = 30, skip = 0):
        try:
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/rules",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"limit": limit, "skip": skip}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def get(self, name=None):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/rules/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def create(self, name=None, body={}):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/rules/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"overwrite": False},
                json=body
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def update(self, name=None, body={}):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/rules/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"overwrite": True},
                json=body
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def delete(self, name=None):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.delete(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/rules/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def enable(self, name=None):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.post(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/rules/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                json={"status": "active"}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def disable(self, name=None):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.post(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/rules/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                json={"status": "inactive"}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Trigger:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def list(self, limit = 30, skip = 0):
        try:
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/triggers",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"limit": limit, "skip": skip}
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def get(self, name=None):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/triggers/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def create(self, name=None, body={}):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/triggers/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"overwrite": False},
                json=body
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def update(self, name=None, body={}):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/triggers/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"overwrite": True},
                json=body
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def delete(self, name=None):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.delete(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/triggers/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def fire(self, name=None, payload={}):
        try:
            if not name:
                raise ValueError("rule name missing")
            return requests.post(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/triggers/{name}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                json=payload
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Namespace:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def list(self):
        try:
            return requests.get(
                f"{self.apihost}/api/v1/namespaces",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Limit:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def list(self, namespace=None):
        try:
            if namespace:
                return requests.get(
                f"{self.apihost}/api/v1/namespaces/{namespace}/limits",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
            return requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/limits",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class Openwhisk:

    __version__ = "0.3"

    def __init__(self, apihost = None):
        if not apihost:
            raise ValueError("apihost missing")
        self.apihost = apihost
        self.apikey = os.environ['__OW_API_KEY']
        self.namespace = os.environ['__OW_NAMESPACE']
        self.action_name = os.environ['__OW_ACTION_NAME']
        self.action_version = os.environ['__OW_ACTION_VERSION']
        self.activation_id = os.environ['__OW_ACTIVATION_ID']
        self.deadline = os.environ['__OW_DEADLINE']
        self.invoke = _Invoke(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.actions = _Action(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.packages = _Package(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.activations = _Activation(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.rules = _Rule(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.triggers = _Trigger(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.namespaces = _Namespace(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.limits = _Limit(apihost=apihost, apikey=self.apikey, namespace=self.namespace)

    def test(__self__):
        print("test method")
