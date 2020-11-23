from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options

import requests
from decouple import config
import time
import datetime

import smtpd
import smtplib
from email.message import EmailMessage

class DashBoardTester:

    browser = webdriver.Chrome(config('CHROMEDRIVER'))

    @staticmethod
    def get_info():
        try:
            urls = config('login_urls').split(',')
            emails = config('USER_NAMES').split(',')
            passwords = config('PASSWORDS').split(',')
        except:
            urls = config('login_urls')
            emails = config('USER_NAMES')
            passwords = config('PASSWORDS')
        return urls,emails,passwords

    @classmethod    
    def test_requests(cls):
        urls , mails , passwords = cls.get_info()
        for url,mail,password in zip(urls,mails,passwords):
            destination_url = url.replace('/login','')
            print(destination_url)
            time.sleep(10)
            cls.browser.get(url)

            WebDriverWait(cls.browser, 10 ).until(EC.presence_of_element_located((By.NAME,'email')))
            user_name = cls.browser.find_element_by_name("email")
            user_name.send_keys(mail)

            password_box = cls.browser.find_element_by_name("password")
            password_box.send_keys(password)

            password_box.send_keys(Keys.ENTER)
            time.sleep(5)
            current_url = cls.browser.current_url
            print(current_url)
            # response = requests.get(current_url).status_code
            if current_url != destination_url:
                print("Request Unsuccessful")
                msg = f"Failed to login this page {url}"
                cls.send_email(msg)
            else:
                print("Request Successful")
        cls.browser.close()
    
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
    DashBoardTester.test_requests()
    # DashBoardTester.send_email("Mail Success")
    






