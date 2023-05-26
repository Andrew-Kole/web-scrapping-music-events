import dataExtract as de

URL = "http://programmer100.pythonanywhere.com/tours/"
#app's behaviour will be as browser's
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


if __name__ == "__main__":
    scraped = de.scrape(URL)
    extracted = de.extract(scraped)
    print(extracted)