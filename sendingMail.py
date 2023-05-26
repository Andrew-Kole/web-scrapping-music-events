import smtplib as sl
import ssl
import os
import typing
from dotenv import load_dotenv

load_dotenv()
MAIL_PASSWORD: typing.Final = os.getenv("MAIL_PASSWORD")
MAIL_USER: typing.Final = os.getenv("MAIL_USER")
MAIL_RECEIVER: typing.Final = os.getenv("MAIL_RECEIVER")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = MAIL_USER
    password = MAIL_PASSWORD
    receiver = MAIL_RECEIVER
    context = ssl.create_default_context()

    with sl.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    pass