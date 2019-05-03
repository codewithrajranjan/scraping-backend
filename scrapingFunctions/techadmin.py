from utils import RequestService
from bs4 import BeautifulSoup
from celery import Task

class TechAdmin(Task):

    identifier = "techadmin"

    def __init__(self):
        self.url = "https://tecadmin.net/"
        self.posts = []
        self.tags = ['linux']

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".title.home-post-title.entry-title")
        for eachData in data:
             data = {
                     "label" : eachData.a.string,
                     "link" : eachData.a.attrs['href'],
                     "identifier" : self.identifier,
                     "tags" : self.tags
             }
             self.posts.append(data)

        return self.posts





    def run(self,context):
        print(context)
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
