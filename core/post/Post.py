import logging
from utils import raiseException

class Post():

    database = "scraping"

    collectionName = "posts"

    def __init__(self,**kwargs):

        self.id = kwargs.get('id')
        self.label = kwargs.get('label') or raiseException("Label not found in kwargs")
        self.identifier = kwargs.get('identifier') or raiseException("Identifier not found ")
        self.link = kwargs.get('link') or raiseException("link not found in kwargs")



    def getModelData(self):

        return {

                "label" : self.label,
                "identifier" : self.identifier,
                "link" : self.link
        }
