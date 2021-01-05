from DashBoardTester import DashBoardTester
from HomePageTester import HomePageTester

from decouple import config
import datetime
import json

import smtpd
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(html1 , html2 , failed_count):
    
    if failed_count > 0:
        subjects = f"{failed_count} fail in checking website status and login."
    else:
        subjects = f"No fail in checking website status and login."

    email_address = config('my_mail')
    email_pass = config('my_pass')
    print(email_address,email_pass)
    contacts = config('CONTACTS')
    # msg = EmailMessage()
    msg = MIMEMultipart()
    msg['Subject'] = subjects
    msg['From'] = email_address
    msg['To'] = contacts
    # msg.set_content(text_message)
    part1 = MIMEText(html1,'html')
    part2 = MIMEText(html2,'html')
    msg.attach(part1)
    msg.attach(part2)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smt:
        smt.login(email_address,email_pass)
        smt.send_message(msg)

from decouple import config

if __name__ == "__main__": 
    
    htm1 , failed_status_count , failed_homepages = HomePageTester.test_requests()
    html2 , failed_login_count , failed_dashboards = DashBoardTester.test_requests()
    current_time = int(datetime.datetime.now().strftime("%H"))
    # current_time = 18
    print(f"current_time ------------> {current_time}")
    if current_time >= 18:
        print("The current hour reach or past the 18 hr.")

        with open("websites_results.txt","r") as file:
            web_result = json.load(file)
        with open("dashboard_results.txt",'r') as file:
            dash_result = json.load(file)

        if web_result == failed_homepages and dash_result == failed_dashboards:
            print('The result are same as morning')
        else:
            print('There are some difference in results')
            total_failed_count = failed_status_count + failed_login_count
            send_email(htm1,html2 , total_failed_count)
    else:
        print("The current hour doesnt reach to 18 hr yet !!")
        total_failed_count = failed_status_count + failed_login_count
        send_email(htm1,html2 , total_failed_count)
    with open("websites_results.txt",'w') as file:
        json.dump(failed_homepages,file)

    with open('dashboard_results.txt','w') as file:
        json.dump(failed_dashboards,file)

    
