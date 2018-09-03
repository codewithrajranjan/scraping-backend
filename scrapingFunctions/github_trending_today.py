from utils import RequestService
from bs4 import BeautifulSoup
import re
import logging

class GitHubTrendingToday():

    identifier = "github"

    def __init__(self):
        self.url = "https://github.com/trending/"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".repo-list li")
        
        for eachData in data:
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
                logging.error(str(e))

        return self.posts


