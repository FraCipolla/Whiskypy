import os
import requests
from requests.auth import HTTPBasicAuth

class _Action:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def get(self, action: str, headers = {}, web = True, blocking = False):
        try:
            if not web:
                r = requests.get(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    headers=headers,
                    )
            else:
                r = requests.get(
                    f"{self.apihost}/api/v1/web/{self.namespace}/{action}?blocking={blocking}",
                    headers=headers,
                    )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def post(self, action: str, headers = {"Content-Type": "application/json"}, body = {}, web = True, blocking = False):
        try:
            if not web:
                return requests.post(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    headers=headers,
                    json=body
                    )
            else:
                return requests.get(
                    f"{self.apihost}/api/v1/web/{self.namespace}/{action}?blocking={blocking}",
                    headers=headers,
                    json=body
                    )
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def delete(self, action: str, headers = {}, web = True, blocking = False):
        try:
            if not web:
                r = requests.delete(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    headers=headers,
                    )
            else:
                r = requests.delete(
                    f"{self.apihost}/api/v1/web/{self.namespace}/{action}?blocking={blocking}",
                    headers=headers,
                    )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def put(self, action: str, headers = {"Content-Type": "application/json"}, body = {}, web = True, blocking = False):
        try:
            if not web:
                r = requests.put(
                    f"{self.apihost}/api/v1/namespaces/{self.namespace}/actions/{action}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    headers=headers,
                    json=body
                    )
            else:
                r = requests.put(
                    f"{self.apihost}/api/v1/web/{self.namespace}/{action}?blocking={blocking}",
                    headers=headers,
                    json=body
                    )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


class _Package:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def find(self, headers = {}, body = {}, blocking = False):
        try:
            r = requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                headers=headers,
                body=body
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def find_one(self, package, headers = {}, body = {}, blocking = False):
        try:
            r = requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages/{package}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                headers=headers,
                body=body
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def delete(self, package, headers = {}, body = {}, blocking = False):
        try:
            r = requests.delete(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages/{package}?force=true",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                headers=headers,
                body=body
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def add(self, package, headers = {"Content-Type": "application/json"}, body = {}, blocking = False):
        try:
            r = requests.put(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/packages/{package}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                headers=headers,
                body=body
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

class _Activation:
    def __init__(self, apihost, apikey, namespace):
        self.apihost = apihost
        self.apikey = apikey.split(':')
        self.namespace = namespace

    def find(self, limit = 30, skip = 0, since = 0, upto = 0):
        try:
            r = requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                params={"limit": limit, "skip": skip, "since": since, "upto": upto}
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def find_one(self, activation_id):
        try:
            r = requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations/{activation_id}",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def logs(self, activation_id):
        try:
            r = requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations/{activation_id}/logs",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def result(self, activation_id):
        try:
            r = requests.get(
                f"{self.apihost}/api/v1/namespaces/{self.namespace}/activations/{activation_id}/result",
                auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
class Openwhisk:

    __version__ = "0.2"

    def __init__(self, apihost = None):
        if not apihost:
            raise ValueError("apihost missing")
        self.apihost = apihost
        self.apikey = os.environ['__OW_API_KEY']
        self.namespace = os.environ['__OW_NAMESPACE']
        self.action_name = os.environ['__OW_ACTION_NAME']
        self.action_version = os.environ['__OW_ACTION_VERSION']
        self.actions = _Action(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.packages = _Package(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        self.activations = _Activation(apihost=apihost, apikey=self.apikey, namespace=self.namespace)
        # self.activation_id = os.environ['__OW_ACTIVATION_ID']
        # self.deadline = os.environ['__OW_DEADLINE']

    def test(self):
        print(self.apihost)
        print(self.apikey)
        print(self.namespace)
