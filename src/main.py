from src.temp_conversions import fahrenheit_to_celsius, celsius_to_fahrenheit
from src.web_scraping import get_page_header_text

if __name__ == "__main__":

    print(fahrenheit_to_celsius(100))
    print(celsius_to_fahrenheit(37.78))

    print(get_page_header_text("https://microsoft.com"))
