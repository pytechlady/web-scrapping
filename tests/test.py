from unittest import TestCase
from request import RequestUrl
from plot import PlotGraph


class TestScraper(TestCase):
    def setUp(self):
        self.request_url = RequestUrl()
        self.plot_graph = PlotGraph()

    def test_check_url(self):
        result = self.request_url.url
        answer = ["on", "and", "yes", "or"]
        self.assertIsNotNone(self.request_url.url, result)
        self.assertEqual(self.request_url.url, result)
        self.assertNotEqual(self.request_url.filter_common_word(), answer)
