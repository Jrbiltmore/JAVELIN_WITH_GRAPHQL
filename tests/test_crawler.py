import unittest
from crawler.web_crawler import WebCrawler

class TestWebCrawler(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://example.com'
        self.crawler = WebCrawler(self.base_url, max_depth=2, max_pages=5)

    def test_initialization(self):
        self.assertEqual(self.crawler.base_url, self.base_url)
        self.assertEqual(self.crawler.max_depth, 2)
        self.assertEqual(self.crawler.max_pages, 5)

    def test_crawl_page(self):
        # This is a placeholder test to check if the method runs without error
        self.crawler.crawl_page(self.base_url, 0)
        self.assertTrue(self.crawler.visited)

    def test_extract_links(self):
        # This is a placeholder test to check if the method runs without error
        soup = None  # Replace with BeautifulSoup object if needed for real test
        self.crawler.extract_links(soup, self.base_url, 0)
        self.assertIsInstance(self.crawler.to_visit, list)

    def test_is_valid_url(self):
        valid_url = 'http://example.com/test'
        invalid_url = 'ftp://example.com/test'
        self.assertTrue(self.crawler.is_valid_url(valid_url))
        self.assertFalse(self.crawler.is_valid_url(invalid_url))

if __name__ == '__main__':
    unittest.main()
