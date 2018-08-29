
from .responseList import responseList
class ResponseHandler:

    @classmethod
    def formatResponse(cls,responseKey,*args,**kwargs):
        """
            This function recieves a response key and find the suitable error value from the dictionary 
            to be sent as a response

            Parameter
            ---------
            **kwargs can contain named arguments like
                message
                parameterName
        """
        #Extracting response data from the list
        responseData = responseList.get(responseKey).copy()


        #if parameteName key is there in kwargs then transforming the message
        if 'parameterName' in kwargs:
            parameterName = kwargs['parameterName']
            responseData['message'] = responseData['message'].format(parameterName)

        # overriding message value
        if 'message' in kwargs:
            responseData['message'] = kwargs['message']

        # overriding statusCode
        if 'statusCode' in kwargs:
            responseData['statusCode'] = kwargs['statusCode']

        #overriding the data
        if 'data' in kwargs:
            responseData['data'] = kwargs['data']

        if 'exception' in kwargs:
            responseData['data'] = str(kwargs['exception'])


        if 'transactionId' in kwargs:
            transactionId = kwargs['transactionId']
            responseData['transactionId']   = transactionId
            if 'jobDefinition' in responseData:
                responseData['jobDefinition'] = responseData['jobDefinition'].format(transactionId)

        
        return responseData





