import os
import requests
from requests.auth import HTTPBasicAuth
# https://walkiria.cloud/api/v1/namespaces/appfront/actions/base/openAPI-async
# https://walkiria.cloud/api/v1/web/appfront/base/openAPI

class _Action:
    def __init__(self, apihost, apikey):
        self.apihost = apihost
        self.apikey = apikey.split(':')

    def get(self, action: str, headers = {}, body = {}, web = True, blocking = False):
        try:
            if not web:
                split_action = action.split('/')
                r = requests.get(
                    f"{self.apihost}/api/v1/namespace/{split_action[0]}/actions/{split_action[1]}/{split_action[2]}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    headers=headers,
                    body=body
                    )
            else:
                r = requests.get(
                    f"{self.apihost}/api/v1/web/{action}?blocking={blocking}",
                    headers=headers,
                    body=body
                    )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def post(self, action: str, headers = {}, body = {}, web = True, blocking = False):
        try:
            if not web:
                split_action = action.split('/')
                r = requests.post(
                    f"{self.apihost}/api/v1/namespace/{split_action[0]}/actions/{split_action[1]}/{split_action[2]}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1])
                    )
            else:
                r = requests.get(
                    f"{self.apihost}/api/v1/web/{action}?blocking={blocking}",
                    headers=headers,
                    body=body
                    )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    def delete(self, action: str, headers = {}, body = {}, web = True, blocking = False):
        try:
            if not web:
                split_action = action.split('/')
                r = requests.delete(
                    f"{self.apihost}/api/v1/namespace/{split_action[0]}/actions/{split_action[1]}/{split_action[2]}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    headers=headers,
                    body=body
                    )
            else:
                r = requests.delete(
                    f"{self.apihost}/api/v1/web/{action}?blocking={blocking}",
                    headers=headers,
                    body=body
                    )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    def put(self, action: str, headers = {}, body = {}, web = True, blocking = False):
        try:
            if not web:
                split_action = action.split('/')
                r = requests.put(
                    f"{self.apihost}/api/v1/namespace/{split_action[0]}/actions/{split_action[1]}/{split_action[2]}?blocking={blocking}",
                    auth=HTTPBasicAuth(self.apikey[0], self.apikey[1]),
                    headers=headers,
                    body=body
                    )
            else:
                r = requests.put(
                    f"{self.apihost}/api/v1/web/{action}?blocking={blocking}",
                    headers=headers,
                    body=body
                    )
            return r
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
            
class openwhisk:

    def __init__(self, apihost = None):
        if not apihost:
            raise ValueError("apihost missing")
        self.apihost = apihost
        self.apikey = os.environ['__OW_API_KEY']
        self.namespace = os.environ['__OW_NAMESPACE']
        self.action_name = os.environ['__OW_ACTION_NAME']
        self.action_version = os.environ['__OW_ACTION_VERSION']
        self.action = _Action(apihost=apihost, apikey=self.apikey)
        # self.activation_id = os.environ['__OW_ACTIVATION_ID']
        # self.deadline = os.environ['__OW_DEADLINE']
