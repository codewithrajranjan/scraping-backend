from utils import RequestService
from bs4 import BeautifulSoup
import logging
from celery import Task

class FreeCodeCampPythonLatest(Task):

    identifier = "freecodecamp-python-latest"

    def __init__(self):
        self.url = "https://medium.com/tag/python/latest/"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".postArticle.postArticle--short")
        
        for eachData in data:
            try :
                    data = {
                             "label" : eachData.find('div',class_='section-content').h3.string or "no label",
                             "link" : eachData.find('div',class_='postArticle-content').parent.attrs['href'],
                             "identifier" : self.identifier,
                             "tags" : ["python"]
                     }
                    self.posts.append(data)

            except Exception as e:
                logging.error("Error while parsing data",str(e))
                continue


        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
