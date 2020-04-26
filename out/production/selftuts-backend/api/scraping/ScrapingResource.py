from flask_restful import Resource
from core import ScrapingEngine



class ScrapingResource(Resource):

    def post(self):

        ScrapingEngine()\
                    .scrape()

        return {'message': 'Activated scraping job'},200

    def options(self):
        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
                {       'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': 'Authorization, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
                        'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'}












