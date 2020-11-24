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

    __browser = webdriver.Chrome(config('CHROMEDRIVER'))

    def __init__(self):
        raise Exception("Instantiation doesnt support yet for this class")

    @staticmethod
    def __get_info():
        try:
            urls = config('login_urls').split(',')
            emails = config('USER_NAMES').split(',')
            passwords = config('PASSWORDS').split(',')
            d_urls = config('destination_urls').split(',')
        except:
            urls = config('login_urls')
            emails = config('USER_NAMES')
            passwords = config('PASSWORDS')
            d_urls = config('destination_urls')
        return urls,emails,passwords ,d_urls

    @classmethod    
    def test_requests(cls):
        urls , mails , passwords , destination_urls  = cls.__get_info()
        for url,mail,password ,destination_url in zip(urls,mails,passwords,destination_urls):
    
            cls.__browser.get(url)

            WebDriverWait(cls.__browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="email"],#phone_number')))
            # time.sleep(4)
            try:
                user_name = cls.__browser.find_element_by_name("email")
            except:
                user_name = cls.__browser.find_element_by_name('phone_number')
            user_name.clear()
            user_name.send_keys(mail)

            password_box = cls.__browser.find_element_by_name("password")
            password_box.clear()
            password_box.send_keys(password)

            password_box.send_keys(Keys.ENTER)
            time.sleep(4)
            current_url = cls.__browser.current_url
            print(current_url)
            # response = requests.get(current_url).status_code
            if current_url != destination_url:
                print("Login Unsuccessful")
                msg = f"Failed to login this page {url}"
                cls.send_email(msg)
            else:
                print("Login Successful")
            time.sleep(2)
        cls.__browser.close()
    
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
    # dashboard = DashBoardTester()
    
    






