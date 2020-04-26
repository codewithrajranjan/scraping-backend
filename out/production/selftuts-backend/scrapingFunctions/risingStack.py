from utils import RequestService
from bs4 import BeautifulSoup
import logging
from celery import Task

class RisingStack(Task):

    identifier = "rising-stack"

    def __init__(self):
        self.url = "https://blog.risingstack.com"
        self.posts = []
        self.tags = ['nodejs']
        

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select("article.post")
        
        for eachData in data:
            try :
                data = {
                         "label" : eachData.header.h1.a.string,
                         "link" : "{}{}".format(self.url,eachData.header.h1.a.attrs['href']),
                         "identifier" : self.identifier,
                         "tags" : self.tags
                 }
                self.posts.append(data)
            except Exception as e:
                logging.error(str(e))

        print(self.posts)
        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context



