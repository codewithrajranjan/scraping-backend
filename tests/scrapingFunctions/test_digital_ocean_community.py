from unittest import TestCase
from scrapingFunctions.digital_ocean_community import DigitalOceanCommunity


class TestDigitalOceanCommunity(TestCase):
    def test_scrape(self):
        task = DigitalOceanCommunity()
        actual_response = task.scrape()
        self.assertTrue(len(actual_response) > 0)
        first_post = actual_response[0]
        self.assertTrue("label" in first_post)
        self.assertTrue("link" in first_post)
        self.assertTrue("identifier" in first_post)
