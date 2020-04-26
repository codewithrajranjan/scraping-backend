from unittest import TestCase
from scrapingFunctions.medium.MediumTagBased import MediumTagBased


class TestMediumTagBased(TestCase):
    def test_scrape(self):
        task = MediumTagBased()
        actual_response = task.scrape()
        self.assertTrue(len(actual_response) > 0)
        first_post = actual_response[0]
        self.assertTrue("label" in first_post)
        self.assertTrue("identifier" in first_post)
        self.assertTrue("link" in first_post)
