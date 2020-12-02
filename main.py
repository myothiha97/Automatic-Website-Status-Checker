from DashBoardTester import DashBoardTester
from HomePageTester import HomePageTester

from decouple import config

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
    
    htm1 , failed_status_count = HomePageTester.test_requests()
    html2 , failed_login_count = DashBoardTester.test_requests()
    total_failed_count = failed_status_count + failed_login_count
    send_email(htm1,html2 , total_failed_count)

    
