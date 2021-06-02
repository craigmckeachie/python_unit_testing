import unittest

from src.temp_conversions import fahrenheit_to_celsius, celsius_to_fahrenheit


class TestTempConversions(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):

        fahrenheit_temp = 100
        celsius_temp = 37.78

        result = fahrenheit_to_celsius(fahrenheit_temp)
        self.assertEqual(result, celsius_temp)

    def test_celsius_to_fahrenheit(self):

        fahrenheit_temp = 100
        celsius_temp = 37.78

        result = celsius_to_fahrenheit(celsius_temp)
        self.assertEqual(result, fahrenheit_temp)


if __name__ == "__main__":
    unittest.main()
