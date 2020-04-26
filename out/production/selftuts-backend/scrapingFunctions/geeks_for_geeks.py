from utils import RequestService
from bs4 import BeautifulSoup
import logging
from celery import Task

class GeeksForGeeksHomePage(Task):

    identifier = "geeks-for-geeks-home"

    def __init__(self):
        self.url = "https://www.geeksforgeeks.org/"
        self.posts = []
        self.tags = ['geeks for geeks','data structure','algorithm']

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select("article header h2")
        
        for eachData in data:
            try :
                data = {
                         "label" : eachData.a.string,
                         "link" : eachData.a.attrs['href'],
                         "identifier" : self.identifier
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



if __name__ == '__main__' :



    obj = GeeksForGeeksHomePage()
    obj.scrape()
