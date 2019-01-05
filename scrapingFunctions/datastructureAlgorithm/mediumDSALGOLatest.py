from utils import RequestService
from bs4 import BeautifulSoup
import re
import logging
from celery import Task

class MediumDSALGOLatest(Task):

    identifier = "medium-data-structure-algorithm"

    def __init__(self):
        self.url = "https://medium.com/tag/data-structures/latest"
        self.posts = []

    def scrape(self):

        try :
                response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(response.content,'html.parser')
                data = soup.select(".postArticle.postArticle--short")
                
                for eachData in data:

                        try : 

                            data = {
                                     "label" : eachData.find('div',class_='section-content').h3.string,
                                     "link" : eachData.find('div',class_='postArticle-content').parent.attrs['href'],
                                     "identifier" : self.identifier,
                                     "tags" : ["nodejs"]
                             }
                            self.posts.append(data)

                        except Exception as e :
                            logging.error("Error occured in processing  {}".format(self.identifier))
                            continue

                return self.posts

        except Exception as e:
                logging.error(e)

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context



