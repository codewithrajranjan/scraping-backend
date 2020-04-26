import requests
import logging
requests.post
class RequestService:
    """ Module to contact third party system using http protocol
    """
    def __int__():
        pass
     

    @classmethod
    def get(cls,url,queryParams={},headers={}):
        auth = headers.get('auth',None) 
        logging.debug("Calling url : {}".format(url))
        response = requests.get(url, params=queryParams, headers=headers, auth=auth)
        return response

