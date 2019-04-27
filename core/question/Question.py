from utils import raiseException
from database import DatabaseManager
import logging

class Question():

    database = "scraping"

    collectionName = "question"

    def __init__(self,**kwargs):

        self.id = kwargs.get('id')
        self.question = kwargs.get('question') or raiseException('Question not found')
        self.topic = kwargs.get('topic') or raiseException('question topic not found')
        self.status = kwargs.get('status') or raiseException('status of question not found')
        self.tags = kwargs.get('tags') or []
        self.description = kwargs.get('description') 
        self.createdAt = kwargs.get('createdAt')
    
    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

    def setDescritption(self,description):
        self.description = description

    def setTopics(self,topic):
        self.topic = topic

    def setQuestion(self,question):
        self.question = question

    def getModelData(self):

        return {

                "question" : self.question,
                "topic" : self.topic,
                "status" : self.status,
                "tags" : self.tags,
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
    def find(cls,whereClause={},responseFormat=None):
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
    

        result = DatabaseManager.find(cls,whereClause,textMatching=True,responseFormat=responseFormat)
        return result

    @classmethod
    def deleteById(cls,questionId,responseFormat=None):

        result = DatabaseManager.find(cls,{'id':questionId},responseFormat='json')

        if len(result) == 0:
            raise Exception("Question doesn't exist")

        DatabaseManager.delete(cls,{'id':questionId})

        return result



    def update(self):

        logging.info("udpating question")

        # first we need to find if question already exists 
        result = DatabaseManager.find(self,{'id': self.id},responseFormat='json')

        if len(result) == 0:
            raise Exception("Unable to find question to update with id : {}".format(self.id))

        result = DatabaseManager.update(self)
        return result




