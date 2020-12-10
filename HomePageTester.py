import requests
from decouple import config
import datetime

from mysql.connector import connect
import smtpd
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import csv
import pandas
from tabulate import tabulate

class HomePageTester:
    
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
    def get_urls(cls):
        sql = "SELECT * FROM home_pages"
        cls.cursor.execute(sql)
        urls = cls.cursor.fetchall()
        return urls

    @classmethod
    def test_requests(cls):
        with open('test_webs.csv','w') as file:
            fieldnames = ['instance','url','return_status','response_time']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()

        urls = cls.get_urls()
        for url in urls:
            begin_time = datetime.datetime.now()
            response = requests.get(url[2]).status_code
            time_diff = datetime.datetime.now() - begin_time
            # response_time = time_diff.strftime("%M min %S sec")
            total_sec  = time_diff.total_seconds()
            response_time = '{} min {} sec'.format(round(total_sec % 3600 // 60 ), round(total_sec % 60))
            if int(response) != 200:
                
                print(f"Request Unsuccessful for {url[2]} , response_time : {response_time}")
                # print("Status code : ", response)
               
            else:
                print(f"Request successful for {url[2]} , response_time : {response_time}")
                
            with open('test_webs.csv','a') as file:

                fieldnames = ['instance','url','return_status','response_time']
                writer = csv.DictWriter(file,fieldnames=fieldnames)

                writer.writerow({'instance': url[1],'url': url[2],'return_status': response ,'response_time': response_time})
                

        df = pandas.read_csv("test_webs.csv")
        unsuccess_webs = df[df['return_status'] != 200]
        success_webs = df[df['return_status'] == 200]
        if unsuccess_webs.empty:
            failed_count = 0
            html_part2 = f"<html>\
                          <head></head>\
                          <body>\
                              <header style='width: auto; height: auto; margin: auto;padding: 30px; text-align: left;'>\
                                  <h2 style='color:#000000'>Website Status Check</h2>\
                                  <hr>\
                              </header>\
                              <div style='width:800px;height:auto;margin: auto;padding: 30px; text-align: center;'>\
                                <h2 style='color:#000000;margin: 0;'>There is no websites that can't access </h2>\
                              </div>\
                            "
        else:
            failed_count = len(unsuccess_webs)
            html_part1 = f"<html>\
                            <head></head>\
                            <body>\
                                <header style='width: auto; height: auto; margin: auto;padding: 30px; text-align: left;'>\
                                  <h2 style='color:#000000'>Website Status Check</h2>\
                                  <hr>\
                               </header>\
                                <div style='width:800px;height:auto;margin: auto;padding: 30px; text-align: center;'>\
                                <h2 style='color:#aa222a;margin: 0;'>We cannot access these websites</h2>\
                                <div style='width:100%;margin:auto;text-align: center;'>\
                                <div style='padding:5px;'>\
                                    <table style='font-family: arial, sans-serif;border-collapse: collapse;width: 100%;'>\
                                    <tr>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Website Name</th>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Url</th>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Return_Status</th>\
                                        <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Response Time</th>\
                                    </tr>"
            for index , row in unsuccess_webs.iterrows():
                concat_str = f"<tr>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['instance']}</td>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['url']}</td>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['return_status']}</td>\
                                    <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['response_time']}</td>\
                                </tr>"
                html_part1 += concat_str

            html_part1_end = f"</table>\
                            </div>\
                            </div>\
                            </div>"
            html_part2 = html_part1 + html_part1_end

        html_part3 = f"<div style='width:800px;height:auto;margin: auto;padding: 30px; text-align: center;'>\
                            <h2 style='color:#000000;margin: 0;'>These websites have no issues</h2>\
                            <div style='width:100%;margin:auto;text-align: center;'>\
                            <div style='padding:5px;'>\
                                <table style='font-family: arial, sans-serif;border-collapse: collapse;width: 100%;'>\
                                <tr>\
                                    <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Website Name</th>\
                                    <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Url</th>\
                                    <th style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>Response Time</th>\
                                </tr>"
        for index , row in success_webs.iterrows():
            concat_str = f"<tr>\
                                <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['instance']}</td>\
                                <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['url']}</td>\
                                <td style='border: 1px solid #dddddd;text-align: left;padding: 8px;color: #000000;'>{row['response_time']}</td>\
                            </tr>"
            html_part3 += concat_str

        end_html = f"</table>\
                        </div>\
                        </div>\
                        </div>\
                        </body>\
                        </html>"
        complete_html = html_part2 + html_part3 + end_html

        ''' Uncomment below 2 lines if u want to check html format before sending email '''
        # with open('index_status.html','w') as file:
        #     file.write(complete_html)
        
        return complete_html , failed_count
    

    @staticmethod
    def send_email(html):
        email_address = config('my_mail')
        email_pass = config('my_pass')
        print(email_address,email_pass)
        contacts = config('CONTACTS')
        # msg = EmailMessage()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Websites Status Check'
        msg['From'] = email_address
        msg['To'] = contacts
        # msg.set_content(text_message)
        # text1 = "We cannot access these websites"
        # text2 = "These websites have no issues"

        part1 = MIMEText(html,'html')
        # part3 = MIMEText(text2,'plain')
        # part4 = MIMEText(html2,'html')

        # msg.attach(part1)
        msg.attach(part1)
        # msg.attach(part3)
        # msg.attach(part4)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smt:
            smt.login(email_address,email_pass)
            smt.send_message(msg)

if __name__ == "__main__":
    html ,count = HomePageTester.test_requests() 
    # HomePageTester.send_email("Mail Successful")

