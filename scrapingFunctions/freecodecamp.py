from utils import RequestService
from bs4 import BeautifulSoup
from celery import Task

class FreeCodeCamp(Task):

    identifier = "freecodecamp"

    def __init__(self):
        self.url = "https://medium.freecodecamp.org/"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".postArticle > div > a")
        for eachData in data:
             data = {
                     "label" : eachData.h3.string,
                     "link" : eachData.attrs['href'],
                     "identifier" : self.identifier
             }
             self.posts.append(data)

        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
