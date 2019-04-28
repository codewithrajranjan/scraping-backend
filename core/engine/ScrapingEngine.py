import logging
from scrapingFunctions import registerTask
from worker import celeryApp
registeredTaskDict = registerTask(celeryApp)
from celery import chain
from core.task import filterUniquePost
from core.task import sendEmail

class ScrapingEngine:

    def __init__(self):
        logging.debug("Starting scraping")
        self.allPosts = []

    
    
    def scrape(self,identifier=None):

        scrapingFunctionChain = []
        # adding initial context
        context = {
            "posts" : []
        }
        for eachTask in registeredTaskDict:
            if identifier != None  : 
                if eachTask == identifier:
                    scrapingFunctionChain.append(registeredTaskDict[eachTask].s()) 
            else :
                scrapingFunctionChain.append(registeredTaskDict[eachTask].s()) 
        
        if len(scrapingFunctionChain) == 0 :
            raise Exception("No registerTask found with identifier = {}".format(identifier))
        
        
        scrapingFunctionChain.append(filterUniquePost.s())
        #scrapingFunctionChain.append(sendEmail.s())


        chainInstance = chain(*scrapingFunctionChain)

        

        chainInstance(context)
        # once the chain of task has been completed then we need to add the filter new post task

