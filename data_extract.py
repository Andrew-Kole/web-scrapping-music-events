import requests
import selectorlib



def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """This function extracts data we need from .html page"""
    extractor = selectorlib.Extractor.from_yaml_file("files/extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


if __name__ == "__main__":
    scraped = scrape("http://programmer100.pythonanywhere.com/tours/")
    extracted = extract(scraped)
    print(extracted)