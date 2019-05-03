from utils import RequestService
from bs4 import BeautifulSoup
from celery import Task

class DockerBlog(Task):

    identifier = "docker-blog"

    def __init__(self):
        self.url = "https://blog.docker.com/"
        self.posts = []
        self.tags = ["docker"]

    def scrape(self):
        # creating url for each user
        response = RequestService.get(self.url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.select("h2.entry-title")
        for eachData in data:
            element = eachData.find_all('a')[0]
            data = {
                "label" : element.string,
                "link" : "{}".format(element.attrs['href']),
                "identifier" : self.identifier,
                "tags" : self.tags
            }
            self.posts.append(data)
        return self.posts

    def run(self,context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
