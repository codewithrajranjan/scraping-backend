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
            {"tagName": "nodejs", "tags": ["medium", "nodejs"]},
            {"tagName": "python", "tags": ["medium", "python"]},
            {"tagName": "docker compose", "tags": ["medium", "docker compose", "docker"]},
            {"tagName": "kubernetes", "tags": ["kubernetes"]}

        ]

    def scrape(self):

        # for each tag we need to call medium website
        for eachTagData in self.tagData:
            tagToSearch = eachTagData['tagName']
            postTags = eachTagData['tags']

            # making the url to search
            url = self.url.format(tagToSearch)

            response = RequestService.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.content, 'html.parser')
            data = soup.select(".postArticle.postArticle--short")

            for eachData in data:
                try:
                    data = {
                        "label": eachData.find('div', class_='section-content').h3.string,
                        "link": eachData.find('div', class_='postArticle-content').parent.attrs['href'],
                        "identifier": self.identifier,
                        "tags": postTags
                    }
                    self.posts.append(data)
                except Exception as e:
                    logging.error("Error while parsing data", str(e))
                    logging.error("Error while parsing data")
                    continue

        return self.posts

    def run(self, context):
        scrapedPost = self.scrape()
        context['posts'].extend(scrapedPost)
        return context
