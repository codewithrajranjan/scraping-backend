from flask_restful import Resource
from database import DatabaseManager
from core import Post
from flask import request
from webargs import fields, validate
from webargs.flaskparser import parser





class Blogs(Resource):

    def get(self):
        inputArgs = {
                'status': fields.Str(missing='new',location='querystring'),
        }

        argsRecieved = parser.parse(inputArgs,request)

        result = DatabaseManager.find(Post,argsRecieved,responseFormat="json")

        return result,200



    def options(self):
        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
                {'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': 'Authorization, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
                        'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'}




















