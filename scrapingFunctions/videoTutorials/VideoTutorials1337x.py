from utils import RequestService
from bs4 import BeautifulSoup
from celery import Task

class VideoTutorial1337x(Task):

    identifier = "video-tutorial-1337x"

    def __init__(self):
        self.baseUrl = "https://www.1377x.to"
        self.url = "https://www.1377x.to/user/{}/"
        self.users = ['CourseClub','Fclab','SunRiseZone','fcs0310','freecoursewb']
        self.posts = []

    def scrape(self):
        for eachUser in self.users:
            
            # creating url for each user
            url = self.url.format(eachUser)
            response = RequestService.get(url,headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.content,'html.parser')
            data = soup.select("td.name")
            for eachData in data:
                element = eachData.find_all('a')[1]
                data = {
                     "label" : element.string,
                     "link" : "{}{}".format(self.baseUrl,element.attrs['href']),
                     "identifier" : self.identifier
                }
                self.posts.append(data)
        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
