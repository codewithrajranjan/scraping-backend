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

    
    
    def scrape1(self,identifier=None):

       # if identifier !=None:

       #     # pushing task to rabbitmq
       #     registeredTaskDict[identifier].delay()
       #     return self
        
        scrapingFunctionChain = []
        # adding initial context
        context = {
            "posts" : []
        }
        for eachTask in registeredTaskDict:
            scrapingFunctionChain.append(registeredTaskDict[eachTask].s()) 

        
        #scrapingFunctionChain.append(filterUniquePost.s())
        #scrapingFunctionChain.append(sendEmail.s())


        chainInstance = chain(*scrapingFunctionChain)

        

        chainInstance(context)
        # once the chain of task has been completed then we need to add the filter new post task

    def scrape(self,identifier=None):

        context = {
            "posts" : []
        }
        for eachTask in registeredTaskDict:
            registeredTaskDict[eachTask].delay(context)

        
