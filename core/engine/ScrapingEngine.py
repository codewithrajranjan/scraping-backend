import logging
from scrapingFunctions import SCRAPING_FUNCTIONS
from database import DatabaseManager
from core import Post

class ScrapingEngine:

    def __init__(self):
        logging.debug("Starting scraping")


    def scrape(self):
        allPosts = []

        for eachScrapingClass in SCRAPING_FUNCTIONS:

            scrapingInstance = eachScrapingClass() 

            posts = scrapingInstance.scrape()

            # we need to find that the post that are coming by scraping already exists in the database of not
            newPost = self.filterNewPost(posts)
            
            if len(newPost) != 0:
                allPosts.extend(newPost)


        return allPosts

    def filterNewPost(self,postFromScrapingArray):

        labelArray = []
        labelBasedDict = {}

        for eachPost in postFromScrapingArray: 
            labelArray.append(eachPost['label'])
            labelBasedDict[eachPost['label']] = eachPost

            
        whereClause = {
                    "label" : { "$in" : labelArray }
        }
        alreadyExistingPostInDatabase =  DatabaseManager.find(Post,whereClause,responseFormat="json")

        # if the length of all new post and searched post from database is same then 
        # no new post has been updated by the 
        if len(alreadyExistingPostInDatabase) == len(postFromScrapingArray):
            # returning empty array as no new post has been found
            return [] 

        # if the length don't match then we need only return new posts
        for eachPostInDatabase in alreadyExistingPostInDatabase:
            label = eachPostInDatabase['label']
            # removing data from label based dictionary
            if label in labelBasedDict:
                del labelBasedDict[label]

        

        # getting post if it is remaining in labelBasedDict
        remaingingPost = []
        for eachKey in labelBasedDict:
            remaingingPost.append(labelBasedDict.get(eachKey))

        return remaingingPost









