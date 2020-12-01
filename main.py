from DashBoardTester import DashBoardTester
from HomePageTester import HomePageTester

from decouple import config

import smtpd
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(html1 , html2):
    email_address = config('my_mail')
    email_pass = config('my_pass')
    print(email_address,email_pass)
    contacts = config('CONTACTS')
    # msg = EmailMessage()
    msg = MIMEMultipart()
    msg['Subject'] = 'Websites Status Check'
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
    
    htm1 = HomePageTester.test_requests()
    html2 = DashBoardTester.test_requests()
    send_email(htm1,html2)

    
