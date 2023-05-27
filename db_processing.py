import sqlite3

connection = sqlite3.connect("data.db")
def db_data_generate(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    return row


def store_db(row):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read_db(row):
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows
