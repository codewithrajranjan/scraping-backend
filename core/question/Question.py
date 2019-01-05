from utils import raiseException
from database import DatabaseManager
import logging

class Question():

    database = "scraping"

    collectionName = "question"

    def __init__(self,**kwargs):

        self._id = kwargs.get('_id')
        self.question = kwargs.get('question') or raiseException('Question not found')
        self.topic = kwargs.get('topic') or raiseException('question topic not found')
        self.status = kwargs.get('status') or raiseException('status of question not found')
        self.description = kwargs('description') 
        self.createdAt = kwargs.get('createdAt')



    def getModelData(self):

        return {

                "question" : self.question,
                "topic" : self.topic,
                "status" : self.status,
                "description" : self.description,
                "createdAt" : self.createdAt
        }
    

    def create(self):
        logging.info("Creating question")
        # first we need to find if question already exists 
        result = DatabaseManager.find(self,{'question': self.question},responseFormat='json')
        if len(result)>0:
            raise Exception("QUESTION_ALREADY_EXISTS")

        result = DatabaseManager.create(self)
        return result


    @classmethod
    def find(cls,whereClause={}):
        logging.info("finding question")

        # if the where clause contains question based search then making that a regular expression
        if 'question' in whereClause:
            #whereClause['question'] = {'$regex': whereClause['question']}
            whereClause['$text'] = {
                                        '$search': whereClause['question'],
                                        '$caseSensitive': False
                                         
                                   }
            del whereClause['question']

        logging.info("criteria to find question : {}".format(whereClause))
    

        result = DatabaseManager.find(cls,whereClause,textMatching=True,responseFormat='json')
        return result






