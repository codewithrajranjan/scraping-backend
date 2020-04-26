from database import DatabaseManager
from .Post import Post

class PostUtils:
    def __init__(self):
        pass

    @classmethod
    def getStatsBasedOnStatus(cls):

        aggregateClause = [ { "$group" : { 
                                            "_id" : "$identifier",
                                            "total" :  { "$sum" : 1},
                                            "new" : {
                                                     "$sum" : {
                                                                "$cond" : [{"$eq" : ["$status","new"]},1,0]
                                                            }
                                                   },
                                            "visited" : {
                                                         "$sum" : {
                                                                    "$cond" : [{"$ne" : ["$status","new"]},1,0]
                                                                }
                                                          }
                                            }

                                       },
                             { "$sort": {"new": -1}}
                          ]
        result = DatabaseManager.aggregate(Post,aggregateClause)
        return result
