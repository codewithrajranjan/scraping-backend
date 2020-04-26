from unittest import TestCase
from scrapingFunctions.geeks_for_geeks import GeeksForGeeksHomePage


class TestGeeksForGeeksHomePage(TestCase):
    def setUp(self):
        pass

    def test_scrape(self):
        task = GeeksForGeeksHomePage()
        actual_response = task.scrape();
        first_post = actual_response[0]
        self.assertGreater(len(actual_response), 1)
        self.assertTrue("label" in first_post)
        self.assertTrue("link" in first_post)
        self.assertTrue("identifier" in first_post)