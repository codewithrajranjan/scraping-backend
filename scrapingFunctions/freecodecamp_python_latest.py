from utils import RequestService
from bs4 import BeautifulSoup

class FreeCodeCampPythonLatest():

    identifier = "freecodecamp-python-latest"

    def __init__(self):
        self.url = "https://medium.com/tag/python/latest/"
        self.posts = []

    def scrape(self):
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select(".postArticle.postArticle--short")
        
        for eachData in data:
            data = {
                     "label" : eachData.find('div',class_='section-content').h3.string,
                     "link" : eachData.find('div',class_='postArticle-content').parent.attrs['href'],
                     "identifier" : self.identifier
             }
            self.posts.append(data)

        return self.posts


