from utils import RequestService
from bs4 import BeautifulSoup
import re
from celery.utils.log import get_task_logger
from celery import Task
logger = get_task_logger(__name__)


class GitHubTrendingToday(Task):

    identifier = "github"

    def __init__(self):
        self.url = "https://github.com/trending/"
        self.posts = []
        self.tags = ['github']

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".repo-list li")
        
        for eachData in data:
            try :
                label = "{} - {}".format(eachData.h3.a.text,eachData.p.string)
                newLabel = label.replace('\n',"")
                newLabel = re.sub(' +',' ',newLabel)
                data = {
                         "label" : newLabel,
                         "link" : "https://github.com{}".format(eachData.h3.a.attrs['href']),
                         "identifier" : self.identifier,
                         "tags" : self.tags
                 }
                self.posts.append(data)
            except Exception as e:
                logger.error(str(e))

        return self.posts
    

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context



