import requests
from decouple import config

import smtpd
import smtplib
from email.message import EmailMessage

class HomePageTester:
    try:
        __urls = config('non_login_urls').split(',')
    except:
        __urls = config('non_login_urls')

    def __init__(self):
        raise Exception("Instantiation doesnt support yet for this class")
    
    @classmethod
    def test_requests(cls):
        for url in cls.__urls:
            response = requests.get(url).status_code
            if int(response) != 200:
                print("Request Unsuccessful")
                print("Status code : ", response)
                msg = f"Status code {response} occur while requesting this url : {url}"
                cls.send_email(msg)
            else:
                print("Request successful")

    @staticmethod
    def send_email(text_message):
        email_address = config('my_mail')
        email_pass = config('my_pass')
        print(email_address,email_pass)
        contacts = config('CONTACTS')
        msg = EmailMessage()
        msg['Subject'] = 'Request Unsuccessful'
        msg['From'] = email_address
        msg['To'] = contacts
        msg.set_content(text_message)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smt:
            smt.login(email_address,email_pass)
            smt.send_message(msg)

if __name__ == "__main__":
    HomePageTester.test_requests() 
    # HomePageTester.send_email("Mail Successful")

