from flask_restful import Resource
from core import Question
from flask import request
from webargs import fields
from webargs.flaskparser import parser
from utils.helperFunctions import logRestRequest
import logging
import traceback


class QuestionAPI(Resource):
    
    def post(self):
        try: 

            logRestRequest(request)

            inputArgs = {
                    'question': fields.Str(required=True,location='json'),
                    'topic': fields.Str(required=True,location='json'),
                    'description': fields.Str(missing=None,location='json'),
                    'status': fields.Str(missing='new',location='json')
            }

            try:

                argsRecieved = parser.parse(inputArgs,request)

            except Exception as e:

                logging.error("Failed to parse input args : {}")
                logging.error(e)
                return {'message': 'not valid input parameters'},400



            questionInstance = Question(**argsRecieved)

            questionInstance.create()

            return {'message':'Question successfully created'},200

        except Exception as e:

            logging.error(e)
            traceback.print_exc()
            return {'message': "Failed to create question "},500

    def get(self):
        try: 
            inputArgs = {
                    'topic': fields.Str(location='querystring'),
                    'question': fields.Str(location='querystring')
            }

            try:

                argsRecieved = parser.parse(inputArgs,request)

            except Exception as e:

                logging.error("Failed to parse input args : {}")
                logging.error(e)
                return {'message': 'not valid input parameters'},400

            result = Question.find(argsRecieved,responseFormat='json')


            return {'message':'Question successfully created','data': result},200

        except Exception as e:

            logging.error(e)
            traceback.print_exc()
            return {'message': "Failed to find question "},500



#    def options(self):
#        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
#               {
#                        'Access-Control-Allow-Origin': '*',
#                        'Access-Control-Allow-Headers': 'Authorization,Content-Type, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
#                        'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'
#                }
#


