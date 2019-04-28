from utils import RequestService
from bs4 import BeautifulSoup
import logging
from celery import Task


class CareerCup(Task):

    identifier = "careerCup"

    def __init__(self):
        self.url = "https://www.careercup.com/page"
        self.posts = []

    def scrape(self):

        try :
                response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(response.content,'html.parser')
                data = soup.select("#question_preview li.question")
                
                for eachData in data:

                        try : 

                            data = {
                                     "label" : "{}".format(eachData.find('span',class_='entry').a.p),
                                     "link" : "{}{}".format("https://www.careercup.com",eachData.find('span',class_='entry').a.attrs['href']),
                                    "identifier" : self.identifier
                             }
                            self.posts.append(data)

                        except Exception as e :
                            logging.error("{} === Error occured in processing  {}".format(self.identifier,e))
                            continue
                #print(self.posts)
                return self.posts

        except Exception as e:
                logging.error(e)


    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context



