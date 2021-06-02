import unittest
from unittest.mock import Mock, patch

from src.web_scraping import get_page_header_text, get


class TestWebScraping(unittest.TestCase):

    # mocked data - for zero h1 elments
    def get_zero_h1_elements_request(self, url):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.text = "<div>test header</div>"

        return response_mock

    # mocked data - for one h1 element
    def get_one_h1_element_request(self, url):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.text = "<h1>test header</h1>"

        return response_mock

    # mocked data -for two or more h1 elements
    def get_two_h1_elements_request(self, url):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.text = """ <h1>test header 1 </h1>
                                <h1>test header 2 </h1>"""

        return response_mock

    def setUp(self):
        print('setup')
        self.url = "http://localhost/"

    @patch("src.web_scraping.get")
    def test_get_zero_page_header(self, mock_get):
        result = "There are no h1 elements"

        with self.assertRaises(Exception) as exc:
            mock_get.side_effect = self.get_zero_h1_elements_request
            page_header = get_page_header_text(self.url)

        self.assertEqual(str(exc.exception), result)
        mock_get.assert_called_once_with(self.url)

    @patch("src.web_scraping.get")
    def test_get_two_page_headers(self, mock_get):
        result = "There is more than one h1 element."

        with self.assertRaises(Exception) as exc:
            mock_get.side_effect = self.get_two_h1_elements_request
            page_header = get_page_header_text(self.url)

        self.assertEqual(str(exc.exception), result)
        mock_get.assert_called_once_with(self.url)

    def tearDown(self):
        print('teardown')

    @patch("src.web_scraping.get")
    def test_get_one_page_header(self, mock_get):
        result = "test header"

        mock_get.side_effect = self.get_one_h1_element_request
        page_header = get_page_header_text(self.url)
        self.assertEqual(page_header, result)
        mock_get.assert_called_once_with(self.url)

    def tearDown(self):
        print('teardown')


if __name__ == "__main__":
    unittest.main()
