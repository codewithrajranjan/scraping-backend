from flask_restful import Resource
from database import DatabaseManager
from core import ScrapingEngine
from core import Post



class ScrapingResourceByIdentifier(Resource):

    def post(self,identifier):

        ScrapingEngine()\
                    .scrape(identifier=identifier)
        


        return 200


    def get(self):

        whereClause = {}
        result = DatabaseManager.find(Post,whereClause,responseFormat="json")
        
        return result,200

    def options(self):
        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
                {       'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': 'Authorization, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
                        'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'}















