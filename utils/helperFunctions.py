import logging 

def raiseException(message):
    raise Exception(message)

def logRestRequest(request):
    logging.info("method : {}, resource={}, data={}, headers={}, args={}".format(request.method,request.url,request.data,request.headers,request.args))

