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
import pandas

from mysql.connector import connect

import csv
import smtpd
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class DashBoardTester:

    __chrome_options = webdriver.ChromeOptions()
    __chrome_options.add_argument('--no-sandbox')
    __chrome_options.add_argument('--disable-gpu')
    __chrome_options.add_argument('--headless')
    __chrome_options.add_argument('--disable-dev-shm-usage')
    __browser = webdriver.Chrome(executable_path=config('CHROMEDRIVER'),chrome_options=__chrome_options)

    mydb = connect(
        host = config("host"),
        user = config("username"),
        password = config("password"),
        database = 'testing_webs'
    )
    cursor = mydb.cursor()

    def __init__(self):
        raise Exception("Instantiation doesnt support yet for this class")

    @classmethod
    def get_info(cls):
        sql = f"SELECT * FROM dashboards"
        cls.cursor.execute(sql)
        datas = cls.cursor.fetchall()
        print(datas)
        return datas

    @classmethod    
    def test_requests(cls):
        with open("success_login_webs.csv",'w') as file:
            fieldnames = ['instance','url','username','password']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()

        with open("failed_login_webs.csv",'w') as file:
            fieldnames = ['instance','url','username','password']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()

        datas = cls.get_info()
        failed_logins = []
        for data in datas:
            
            instance ,url , mail , password , destination_url  = data[1],data[2],data[3],data[4],data[5]
            try:
                cls.__browser.get(url)

                WebDriverWait(cls.__browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="email"],#phone_number,#user_login')))
                # time.sleep(4)
                
                user_name = cls.__browser.find_element_by_css_selector("input[name='email'],#phone_number,#user_login")

                user_name.clear()
            
                user_name.send_keys(mail)

                password_box = cls.__browser.find_element_by_css_selector("input[name='password'],#user_pass,#password")
                password_box.clear()
                password_box.send_keys(password)

                password_box.send_keys(Keys.ENTER)
                time.sleep(4)
                current_url = cls.__browser.current_url
                print(current_url,'--------',destination_url)
                # response = requests.get(current_url).status_code
                if current_url != destination_url:
                    print("Login Unsuccessful")
                    # msg = f"Failed to login this page {url}"
                    with open('failed_login_webs.csv','a') as file:
                        fieldnames = ['instance','url','username','password']
                        writer = csv.DictWriter(file,fieldnames=fieldnames)

                        writer.writerow({'instance': instance,'url': url,'username': mail,'password': password})
                    failed_logins.append(instance)

                    
                else:
                    print("Login Successful")
                    with open('success_login_webs.csv','a') as file:
                        fieldnames = ['instance','url','username','password']
                        writer = csv.DictWriter(file,fieldnames=fieldnames)

                        writer.writerow({'instance': instance,'url': url,'username': mail,'password': password})
                
                time.sleep(2)
            except Exception as e:
                print("Login Unsuccessful")
                    # msg = f"Failed to login this page {url}"
                with open('failed_login_webs.csv','a') as file:
                    fieldnames = ['instance','url','username','password']
                    writer = csv.DictWriter(file,fieldnames=fieldnames)

                    writer.writerow({'instance': instance,'url': url,'username': mail,'password': password})
                failed_logins.append(instance)
                time.sleep(2)

        unsuccess_pages = pandas.read_csv('failed_login_webs.csv')
        success_pages = pandas.read_csv('success_login_webs.csv')
        if unsuccess_pages.empty:
            failed_count = 0
            table_part2 = f"<html>\
                          <head></head>\
                          <body>\
                              <header style='width: auto; height: auto; margin: auto;padding: 30px; text-align: left;'>\
                                  <h2 style='color:#000000'>Website Login Check</h2>\
                                  <hr>\
                              </header>\
                              <div style='width:800px;height:auto;margin: auto;padding: 30px; text-align: center;'>\
                                <h2 style='color:#000000;margin: 0;'>There is no failed login pages</h2>\
                              </div>\
                            "
        else:
            failed_count = len(unsuccess_pages)
            table_part1 = f"<html>\
                            <head></head>\
                            <body>\
                                <header style='width: auto; height: auto; margin: auto;padding: 30px; text-align: left;'>\
                                  <h2 style='color:#000000'>Website Login Check</h2>\
                                  <hr>\
                                </header>\
                                <div style='width:1000px;height:auto;margin: auto;padding: 30px; text-align: center;'>\
                                <h2 style='color:#aa222a;margin: 0;'>Fail Login Pages</h2>\
                                <div style='width:100%;margin:auto;text-align: center;'>\
                                <div style='padding:5px;'>\
                                    <table style='font-family: arial, sans-serif;border-collapse: collapse;width: 100%;'>\
                                    <tr>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Website Name</th>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Url</th>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>User Name</th>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Password</th>\
                                    </tr>"
            for index,row in unsuccess_pages.iterrows():
                # print(row['instance'],row['url'])
                concat_str = f"<tr>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['instance']}</td>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['url']}</td>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['username']}</td>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['password']}</td>\
                                </tr>"
                table_part1 += concat_str

            table_end = f"</table>\
                            </div>\
                            </div>\
                            </div>"
            table_part2 = table_part1 + table_end

        table_part3 = f"<div style='width:1000px;height:auto;margin: auto;padding: 30px; text-align: center;'>\
                            <h2 style='color:#000000;margin: 0;'> Login Success Pages</h2>\
                            <div style='width:100%;margin:auto;text-align: center;'>\
                            <div style='padding:5px;'>\
                                <table style='font-family: arial, sans-serif;border-collapse: collapse;width: 100%;'>\
                                <tr>\
                                    <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Website Name</th>\
                                    <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Url</th>\
                                    <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>User Name</th>\
                                    <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Password</th>\
                                </tr>"
        for index,row in success_pages.iterrows():
            concat_str = f"<tr>\
                                <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['instance']}</td>\
                                <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['url']}</td>\
                                <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['username']}</td>\
                                <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['password']}</td>\
                            </tr>"
            table_part3 += concat_str
            
        end_html = f"</table>\
                        </div>\
                        </div>\
                        </div>\
                        </body>\
                        </html>"
            
        complete_html = table_part2 + table_part3 + end_html

        ''' Uncomment below 2 lines if u want to check html format before sending email '''
        # with open('index_login.html','w') as file:
        #     file.write(complete_html)
        
        # print(complete_html)          
        
        cls.__browser.close()
        return complete_html , failed_count , failed_logins
    
    @staticmethod
    def send_email(text_message):
        email_address = config('my_mail')
        email_pass = config('my_pass')
        print(email_address,email_pass)
        contacts = config('CONTACTS')
        # msg = EmailMessage()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Websites Login status check'
        msg['From'] = email_address
        msg['To'] = contacts
        # msg.set_content(text_message)
        part1 = MIMEText(text_message,'html')
        msg.attach(part1)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smt:
            smt.login(email_address,email_pass)
            smt.send_message(msg)


    
if __name__ == "__main__":
    hmtl , count = DashBoardTester.test_requests()
    # DashBoardTester.send_email("Mail Success")
    # dashboard = DashBoardTester()
    
    






