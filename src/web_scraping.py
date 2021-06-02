from requests import get
import re


def get_page_header_text(url):
    web_response = get(url)

    matches = re.findall("<h1.*?>(.*)</h1>", web_response.text, re.IGNORECASE)

    if not matches or len(matches) == 0:
        raise Exception("There are no h1 elements")

    if len(matches) > 1:
        raise Exception("There is more than one h1 element.")

    return matches[0]
