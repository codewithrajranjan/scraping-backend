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
            {"tagName": "nodejs", "tags": ["medium", "nodejs"]}

        ]

    def scrape(self):
        # for each tag we need to call medium website
        for eachTagData in self.tagData:
            tag_to_search = eachTagData['tagName']
            post_tags = eachTagData['tags']

            # making the url to search
            url = self.url.format(tag_to_search)
            response = RequestService.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.content, 'html.parser')
            data = soup.select("[aria-label='Post Preview Title']")

            for eachData in data:
                try:
                    data = {
                        "label": eachData.find('h2').string,
                        "link": "https://medium.com{}".format(eachData.attrs["href"]),
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
