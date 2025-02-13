import os
import requests

class Invoke:
    def __init__(self, apihost):
        self.apihost = apihost

    def get(self, action: str, web = True, blocking = False):
        try:
            r = requests.get(f"{self.apihost}/{action}?blocking={blocking}")
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        
    def post(self, action: str, web = True, blocking = False):
        try:
            r = requests.get(f"{self.apihost}/{action}?blocking={blocking}")
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
    def delete(self, action: str, web = True, blocking = False):
        try:
            r = requests.delete(f"{self.apihost}/{action}?blocking={blocking}")
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        
    def put(self, action: str, web = True, blocking = False):
        try:
            r = requests.put(f"{self.apihost}/{action}?blocking={blocking}")
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
            
class openwhisk:

    def __init__(self, apihost = None):
        self.invoke = Invoke(apihost=apihost)
        self.apihost = apihost
        self.apikey = os.environ['__OW_API_KEY']
        self.namespace = os.environ['__OW_NAMESPACE']
        self.action_name = os.environ['__OW_ACTION_NAME']
        self.action_version = os.environ['__OW_ACTION_VERSION']
        self.activation_id = os.environ['__OW_ACTIVATION_ID']
        self.deadline = os.environ['__OW_DEADLINE']
