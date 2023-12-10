from utils import RequestService
from bs4 import BeautifulSoup
import logging
from celery import Task


class MediumTagBased(Task):
    identifier = "medium-tag-based"

    def __init__(self):
        self.url = "https://medium.com/tag/{}/latest/"
        self.posts = []
        self.tags = ['nodejs']

        self.tagData = [
            # {"tagName": "nodejs", "tags": ["medium", "nodejs"]},
            # {"tagName": "kafka", "tags": ["medium", "kafka"]},
            # {"tagName": "docker", "tags": ["medium", "docker"]},
            # {"tagName": "kubernetes", "tags": ["medium", "kubernetes"]},
            # {"tagName": "python", "tags": ["medium", "python"]},
            {"tagName": "redis", "tags": ["medium", "redis"]},


        ]

    def scrape(self):
        # for each tag we need to call medium website
        for eachTagData in self.tagData:
            tag_to_search = eachTagData['tagName']
            post_tags = eachTagData['tags']

            # making the url to search
            url = self.url.format(tag_to_search)
            print(url)
            soup = RequestService.getFromSelenium(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = soup.find_all('article', attrs={"class": "ks"})
            for eachData in data:
                try:
                    result = eachData.find("a", attrs={"rel": "noopener follow"})
                    data = {
                        "label": result['aria-label'],
                        "link": "https://medium.com{}".format(result['href']),
                        "identifier": self.identifier,
                        "tags": post_tags
                    }
                    self.posts.append(data)
                except Exception as e:
                    logging.error("Error while parsing data", str(e))
                    logging.error("Error while parsing data")
                    continue
        return self.posts

    def run(self, context):
        scraped_post = self.scrape()
        context['posts'].extend(scraped_post)
        return context
