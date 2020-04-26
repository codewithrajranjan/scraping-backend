from flask_restful import Resource
from scrapingFunctions import SCRAPING_FUNCTIONS
from core.post import PostUtils





class Identifier(Resource):

    def get(self):

        identifierList = [] 

        for eachScrpingFunction in SCRAPING_FUNCTIONS : 
            identifierList.append({
                                'key': eachScrpingFunction.identifier,
                                'value' : eachScrpingFunction.identifier
                            })


        # getting the stats of posts based on status
        result = PostUtils.getStatsBasedOnStatus()
        
        # now normalizing the data
        for eachData in identifierList:
            eachData["new"] = 0
            eachData["visited"] = 0
            eachData["total"] = 0
            for eachRecord in result:
                # here the identifier data is container in the _id of aggregated result 
                # and in the value of identifierList
                if eachRecord['_id'] == eachData['value'] : 
                    eachData['new'] = eachRecord['new']
                    eachData['visited'] = eachRecord['visited']
                    eachData['total'] = eachRecord['total']

        
        # once normalization has been done we need to sort the list based on the value of new post count
        print(identifierList)
        identifierList.sort(key=lambda x: x["new"], reverse=True)

        response = {

                "code" : "identifierFound",
                "data" : identifierList,
                "message" : "Blog Identifier found successfully"
        }

        return response,200
