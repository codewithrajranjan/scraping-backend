from utils import RequestService
from bs4 import BeautifulSoup
import re
import logging
from celery import Task

class MongoDBBlog(Task):

    identifier = "mongodb-blog"

    def __init__(self):
        self.url = "https://www.mongodb.com/blog"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select("main .overflow-hidden > div")
        
        for eachData in data:
            try :
                data = {
                         "label" : eachData.a.h3.string,
                         "link" : "https://www.mongodb.com{}".format(eachData.a.attrs['href']),
                         "identifier" : self.identifier
                 }
                self.posts.append(data)
            except Exception as e:
                logging.error(str(e))

        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
