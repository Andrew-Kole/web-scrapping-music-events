import dataExtract as de
import processingTextFile as pt
import sendingMail as sm

URL = "http://programmer100.pythonanywhere.com/tours/"
#app's behaviour will be as browser's
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def process_function(url):
    """the entrance point to programm"""
    scraped = de.scrape(url)
    extracted = de.extract(scraped)
    content = pt.read()
    if extracted != "No upcoming tours":
        if extracted not in content:
            pt.store(extracted)
            sm.send_email()


if __name__ == "__main__":
    process_function(URL)