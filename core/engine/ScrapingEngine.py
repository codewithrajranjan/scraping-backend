import logging
from scrapingFunctions import SCRAPING_FUNCTIONS
from database import DatabaseManager
from core import Post

class ScrapingEngine:

    def __init__(self):
        logging.debug("Starting scraping")
        self.allPosts = []

    
    
    def scrape(self,identifier=None):
        
        for eachScrapingClass in SCRAPING_FUNCTIONS:

            if identifier != None and eachScrapingClass.identifier != identifier:
                continue;

            scrapingInstance = eachScrapingClass() 

            posts = scrapingInstance.scrape()

            # we need to find that the post that are coming by scraping already exists in the database of not
            newPost = self.filterNewPost(posts)
            
            if len(newPost) != 0:
                self.allPosts.extend(newPost)

        return self


    def insertNewPostsInDatabase(self):

        postIdentifiers = ""

        for eachPost in self.allPosts:
            postIdentifiers += eachPost['identifier'] + " - "
            eachPost['status'] = "new"
            print(eachPost)
            DatabaseManager.create(Post(**eachPost))

        return self


    def sendEmail(self):
        print("EmailSent")
        return self



    def filterNewPost(self,postFromScrapingArray):

        labelArray = []
        labelBasedDict = {}

        for eachPost in postFromScrapingArray: 
            labelArray.append(eachPost['label'])
            #labelBasedDict[eachPost['label']] = eachPost

            
        whereClause = {
                    "label" : { "$in" : labelArray }
        }
        alreadyExistingPostInDatabase =  DatabaseManager.find(Post,whereClause,responseFormat="json")

        # if the length of all new post and searched post from database is same then 
        # no new post has been updated by the 
        if len(alreadyExistingPostInDatabase) == len(postFromScrapingArray):
            # returning empty array as no new post has been found
            return [] 

        remaingingPost = []
        # if the length don't match then we need only return new posts
        for eachNewPost in postFromScrapingArray:
            label = eachNewPost['label']
            flag = True
            for eachPostInDatabase in alreadyExistingPostInDatabase:
                if label == eachPostInDatabase['label']:
                    flag = False

            if flag == True :
                remaingingPost.append(eachNewPost)

        # getting post if it is remaining in labelBasedDict

        return remaingingPost









