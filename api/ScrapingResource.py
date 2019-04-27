from flask_restful import Resource, reqparse
import logging
from utils import ResponseHandler
from database import DatabaseManager
from utils import RequestService
from bs4 import BeautifulSoup
from core import ScrapingEngine
from database import DatabaseManager
from core import Post



class ScrapingResource(Resource):

    def post(self):

        allNewPosts = ScrapingEngine()\
                    .scrape()

        return {'message': 'Activated scraping job'},200


    
#    def options(self):
#        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
#               {'Access-Control-Allow-Origin': '*',
#            'Access-Control-Allow-Headers': 'Authorization, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
#             'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'}
#
