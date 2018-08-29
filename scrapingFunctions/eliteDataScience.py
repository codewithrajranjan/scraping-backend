from utils import RequestService
from bs4 import BeautifulSoup

class EliteDataScience():

    def __init__(self):
        self.url = "https://elitedatascience.com/",
        self.identifier = "eliteDataScience"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".op-list-headline")
        for eachData in data:
             data = {
                     "label" : eachData.a.string,
                     "link" : eachData.attrs['href'],
                     "identifier" : self.identifier
             }
             self.posts.append(data)

        return self.posts

