import unittest

from src.tests.test_temp_conversions import TestTempConversions
from src.tests.test_web_scraping import TestWebScraping


def suite():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        TestWebScraping)

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
