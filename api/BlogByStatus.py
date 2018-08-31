from flask_restful import Resource
from database import DatabaseManager
import requests
from core import Post
from bson import ObjectId
from utils import ResponseHandler
import logging
import traceback





class BlogByStatus(Resource):




    def post(self,blogId,blogStatus):
        try:

            whereClause = {
                    '_id': ObjectId(blogId)
            }

            data = DatabaseManager.find(Post,whereClause)

            if len(data) == 0 or len(data) > 1:
                formattedResponse = ResponseHandler.formatResponse('POST_NOT_FOUND')
                return formattedResponse,formattedResponse['statusCode']

            postInstance = data[0]

            postInstance.status = blogStatus
            
            result = DatabaseManager.update(postInstance)

            formattedResponse = ResponseHandler.formatResponse('POST_UPDATE_SUCCESS')            
            return formattedResponse,formattedResponse['statusCode']


        except Exception as e:

            logging.error(traceback.format_exc())
            formattedResponse = ResponseHandler.formatResponse('POST_UPDATE_FAILED)',exception=e)
            return formattedResponse,formattedResponse['statusCode']

        



    def options(self):
        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
               {'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Authorization, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
             'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'}




















