from utils import RequestService
from bs4 import BeautifulSoup
import logging
from celery import Task

class DistributedPython(Task):

    identifier = "distributed-python"

    def __init__(self):
        self.url = "https://www.distributedpython.com"
        self.posts = []
        self.tags = ['python']

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select("#post-list li")
        
        for eachData in data:
            try :
                data = {
                         "label" : eachData.a.next_sibling.next_sibling.h2.text,
                         "link" : "{}{}".format(self.url,eachData.a.attrs['href']),
                         "identifier" : self.identifier,
                         "tags" : self.tags
                 }
                self.posts.append(data)
            except Exception as e:
                logging.error(str(e))

        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context


