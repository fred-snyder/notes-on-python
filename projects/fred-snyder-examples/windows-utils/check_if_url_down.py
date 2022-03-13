"""
A script that can check the status of an URL
"""

#!/usr/bin/env python
import smtplib
import time
import datetime
import requests #https://pypi.python.org/pypi/requests/2.7.0
from email.mime.text import MIMEText

const_subject = 'replace with message subject'
const_from = 'from email address'
const_to = 'to email address'

const_mail_server_ip = 'xxx.xxx.xxx.xxx'
const_mail_server_port = 587
const_mail_server_pass = 'xxxxxxxxxxxxxxxxxx'

def send_email(message):
    for recipient in [const_to]:
        msg = MIMEText(message)
        msg['Subject'] = const_subject
        msg['From'] = const_from

        server = smtplib.SMTP(const_mail_server_ip, const_mail_server_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(msg['From'], const_mail_server_pass)

        msg['To'] = recipient
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Message sent to {}".format(recipient))

    return

########### TEST IF URL IS UP OR DOWN
test_url = "https://some/url/filename.ext"

while True:
    r = requests.get(test_url)

    if r.status_code != 200:
        print( datetime.datetime.time( datetime.datetime.now() ) )
        print("Website is OFFLINE > The status code is: {}".format(r.status_code))
        send_email('The URL is not responding correctly')
        break
    elif r.status_code == 200:
        # print("Website is online > The status code is: {}".format(r.status_code))
        time.sleep(60)
