from utils import RequestService
from bs4 import BeautifulSoup
import re
import logging
from celery import Task

class BlogTest(Task):

    identifier = "hackerearth-notes"

    def __init__(self):
        self.url = "https://www.hackerearth.com/practice/notes/newest/"
        self.posts = []

    def scrape(self):

        try :
                response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(response.content,'html.parser')
                print(soup)
                data = soup.select(".notes-container")
                print(data) 
                for eachData in data:

                        try : 

                            data = {
                                     "label" : eachData,
                                     #"link" : "{}{}".format("https://www.careercup.com",eachData.find('span',class_='entry').a.attrs['href']),
                                    "identifier" : self.identifier,
                             }
                            self.posts.append(data)

                        except Exception as e :
                            logging.error("{} === Error occured in processing  {}".format(self.identifier,e))
                            continue
                print(self.posts);
                return self.posts

        except Exception as e:
                logging.error(e)

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context



if __name__ == '__main__' :



    obj = BlogTest()
    result = obj.scrape()
    print(result)
