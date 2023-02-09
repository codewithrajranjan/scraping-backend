from flask_restful import Resource
from database import DatabaseManager
from core import Post
from flask import request
from webargs import fields
from webargs.flaskparser import parser
from utils import DateManager
from scrapingFunctions import SCRAPING_FUNCTIONS
from urllib import parse

filterForIdentifier = []

for eachScrapingFunction in SCRAPING_FUNCTIONS:
    filterForIdentifier.append({'identifier': eachScrapingFunction.identifier})


class Blogs(Resource):

    def get(self):
        parsed_query_string = dict(parse.parse_qsl(request.query_string.decode('ASCII')))
        argsRecieved = {
            'status': parsed_query_string.get("status") or "new",
            'tag': parsed_query_string.get("tag") or None,
            'identifier': parsed_query_string.get("identifier") or None,
            'searchtext': parsed_query_string.get("searchtext") or None
        }

        status = argsRecieved['status']

        whereClause = {}

        if status == "new":
            whereClause["$and"] = [{"$or": [{'status': 'new'}, {'status': 'visited'}]}, {"$or": filterForIdentifier}]
        else:
            whereClause['status'] = argsRecieved['status']

        if argsRecieved['tag'] != None:
            whereClause['tags'] = argsRecieved['tag']

        if argsRecieved['identifier'] != None:
            whereClause['identifier'] = argsRecieved['identifier']

        if argsRecieved['searchtext'] != None:
            whereClause['$or'] = [
                {'label': {"$regex": argsRecieved['searchtext'], "$options": "$i"}},
                {'tags': {"$regex": argsRecieved['searchtext'], "$options": "$i"}}

            ]
        print("======= {}".format(whereClause))
        result = DatabaseManager.find(Post, whereClause, responseFormat="json")

        for eachBlog in result:
            eachBlog['createdAt'] = DateManager.getHumanRedableDateDiff(DateManager.getTodaysDate(),
                                                                        eachBlog['createdAt'])

        return result, 200
