from utils import RequestService
from bs4 import BeautifulSoup
import logging
from celery import Task

class EliteDataScience(Task):

    def __init__(self):
        self.url = "https://elitedatascience.com/",
        self.identifier = "eliteDataScience"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".op-list-headline")
        for eachData in data:
            try:
                 data = {
                         "label" : eachData.a.string,
                         "link" : eachData.attrs['href'],
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
