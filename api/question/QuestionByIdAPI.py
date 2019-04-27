from flask_restful import Resource
from core import Question
from flask import request
from webargs import fields
from webargs.flaskparser import parser
from utils.helperFunctions import logRestRequest
import logging
import traceback


class QuestionByIdAPI(Resource):

    def put(self,questionId):
        try: 

            logRestRequest(request)

            inputArgs = {
                    'question': fields.Str(required=True,location='json'),
                    'topic': fields.Str(required=True,location='json'),
                    'description': fields.Str(location='json'),
                    }
            try:

                argsRecieved = parser.parse(inputArgs,request)

            except Exception as e:

                logging.error("Failed to parse input args : {}")
                logging.error(e)
                return {'message': 'not valid input parameters'},400


            #first finding the question 
            result = Question.find({'id':questionId})
            questionInstance = result[0]
            questionInstance.setDescritption(argsRecieved['description'])
            questionInstance.setTopics(argsRecieved['topic'])
            questionInstance.setQuestion(argsRecieved['question'])

            questionInstance.update()

            return {'message':'Question successfully updated'},200

        except Exception as e:

            logging.error(e)
            traceback.print_exc()
            return {'message': "Failed to create question "},500

    def delete(self,questionId):
        try: 

            logRestRequest(request)


            #first finding the question 
            Question.deleteById(questionId)

            return {'message':'Question deleted successfully'},200

        except Exception as e:

            logging.error(e)
            traceback.print_exc()
            return {'message': "Failed to create question "},500




