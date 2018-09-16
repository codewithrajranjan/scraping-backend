from utils import RequestService
from bs4 import BeautifulSoup
import re
from celery.utils.log import get_task_logger
from celery import Task

logger = get_task_logger(__name__)

class Test:
        database = "scraping"

        collectionName = "posts"



class GeeksForGeeks(Task):

    identifier = "geeks-for-geeks"

    def __init__(self):
        self.url = "https://www.geeksforgeeks.org/"
        self.posts = []

    def scrape(self):
        print("==============")
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        print(response.content)
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".repo-list li")
        for eachData in data:
            print("raj")
            try :
                #label = "{}{} - {}".format(eachData.h3.a.span.string,eachData.h3.a.text,eachData.p.string)
                label = "{} - {}".format(eachData.h3.a.text,eachData.p.string)
                newLabel = label.replace('\n',"")
                newLabel = re.sub(' +',' ',newLabel)
                data = {
                         "label" : newLabel,
                         "link" : "https://github.com{}".format(eachData.h3.a.attrs['href']),
                         "identifier" : self.identifier
                 }
                self.posts.append(data)
            except Exception as e:
                logger.error(str(e))

        return self.posts

    def run(self):
        self.scrape()



#GeeksForGeeks = celeryApp.register_task(GeeksForGeeks())
