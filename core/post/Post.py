import logging
from utils import raiseException

class Post():

    database = "scraping"

    collectionName = "posts"

    def __init__(self,**kwargs):

        self._id = kwargs.get('_id')
        self.label = kwargs.get('label')
        self.identifier = kwargs.get('identifier') or raiseException("Identifier not found ")
        self.link = kwargs.get('link') or raiseException("link not found in kwargs")
        self.status = kwargs.get('status')
        self.createdAt = kwargs.get('createdAt')



    def getModelData(self):

        return {


                "label" : self.label,
                "identifier" : self.identifier,
                "link" : self.link,
                "status" : self.status,
                "createdAt" : self.createdAt
        }
