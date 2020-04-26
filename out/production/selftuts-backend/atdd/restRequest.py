import logging
import json

from robot.api import logger
import requests

class RestRequest:
    
    def __init__(self):
        pass
    
    def postJson(self,url,data=None):
        response = requests.post(url,json=json.loads(data))
        return response

    def putJson(self,url,data=None):
        if type(data) == 'dict' :
            data = json.loads(json.dumps(data))
        response = requests.put(url,json=data)
        return response


    def get(self,url):
        response = requests.get(url)
        return response


        


