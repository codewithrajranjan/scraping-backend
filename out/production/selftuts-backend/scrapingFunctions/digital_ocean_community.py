from utils import RequestService
from bs4 import BeautifulSoup
import re
import logging
from celery import Task

class DigitalOceanCommunity(Task):

    identifier = "digital-ocean"

    def __init__(self):
        self.url = "https://www.digitalocean.com/community/tutorials/"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select("li.tutorial")
        
        for eachData in data:
            try :
                data = {
                         "label" : eachData.h3.a.string,
                         "link" : "https://www.digitalocean.com{}".format(eachData.h3.a.attrs['href']),
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
