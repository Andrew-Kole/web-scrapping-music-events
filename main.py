import data_extract
import processing_text_file
import sending_mail as sm
import db_processing
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
# app's behaviour will be as browser's
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
connection = sqlite3.connect("data.db")


def process_function(url):
    """the entrance point to programm"""
    scraped = data_extract.scrape(url)
    extracted = data_extract.extract(scraped)
    print(extracted)
    if extracted != "No upcoming tours":
        content = processing_text_file.read()
        row = db_processing.read_db(db_processing.db_data_generate(extracted), connection)
        print(row)
        if extracted not in content and not row:
            processing_text_file.store(extracted)
            db_processing.store_db(db_processing.db_data_generate(extracted), connection)
            message = "Hello, a new event was found" + ("\n" * 3) + extracted
            sm.send_email(message)
            print("mail_sent")


if __name__ == "__main__":
    while True:
        process_function(URL)
        time.sleep(2)
