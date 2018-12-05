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
                'tag': fields.Str(missing=None,location='querystring'),

        }

        

        argsRecieved = parser.parse(inputArgs,request)


        # checking if status value is new then showing visited also
        status = argsRecieved['status']

        whereClause = {}

        if status == "new":
            whereClause["$or"] = [{'status': 'new'},{'status':'visited'}]
        else : 
            whereClause['status'] = argsRecieved['status']

        if argsRecieved['tag'] != None :
            whereClause['identifier'] = argsRecieved['tag']

        result = DatabaseManager.find(Post,whereClause,responseFormat="json")

        return result,200



    def options(self):
        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
                {'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': 'Authorization, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
                        'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'}




















