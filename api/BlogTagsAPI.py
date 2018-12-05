from flask_restful import Resource
from database import DatabaseManager
from core import Post
from flask import request
from webargs import fields, validate
from webargs.flaskparser import parser
from scrapingFunctions import SCRAPING_FUNCTIONS





class BlogTagsAPI(Resource):

    def get(self):

        tagsList = [] 

        for eachScrpingFunction in SCRAPING_FUNCTIONS : 
            tagsList.append({
                                'key': eachScrpingFunction.identifier,
                                'value' : eachScrpingFunction.identifier
                            })


        return tagsList,200



    def options(self):
        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
                    {   'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': 'Authorization, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
                        'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'}























