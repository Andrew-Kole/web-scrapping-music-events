import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"
#app's behaviour will be as browser's
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """This function extracts data we need from .html page"""
    selectorlib.Extractor.from_yaml_file("extract.yaml")


if __name__ == "__main__":
    print(scrape(URL))