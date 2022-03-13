import csv, smtplib, ssl
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# import smtp_server, port, login, password
import production_config


#### global variables
message_text_path = "message/text.txt"
message_html_path = "message/html.txt"


#### test configuration with smtpd package
''' sudo python -m smtpd -c DebuggingServer -n localhost:1025 ''' # run local Python test server
smtp_server = "localhost"
port = 1025
login = ""
password = ""

#### for production config pass True
def activate_production_settings(activate):
    if activate:
        global smtp_server
        global port
        global login
        global password
        smtp_server = production_config.smtp_server
        port = production_config.port
        login = production_config.login
        password = production_config.password


#### create the message from files
def create_message(sender_email, subject, text_file_path, html_file_path, plain_text):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = "{receiver_email_address}" # format data when sending message

    # import the plain-text and HTML versions of your message
    text_file = open(text_file_path,'r')
    text = text_file.read()
    text_file.close()
    html_file = open(html_file_path,'r')
    html = html_file.read()
    html_file.close()

    # convert to plain/html MIMEText objects
    part_text = MIMEText(text, "plain")
    part_html = MIMEText(html, "html")
    # attach/add plain-text/HTML parts to the MIMEMultipart message
    message.attach(part_text)

    if not plain_text:
        message.attach(part_html)

    return message


#### send the emails
def send_email(csv_data, sender_email, message, sleep_min, sleep_max, production):
    if production:
        activate_production_settings(True)
    
    with smtplib.SMTP(smtp_server, port) as server:

        # settings and server.variables for production use
        if production:
            context = ssl.create_default_context() # Create SSL context
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(login, password)
    
        with open(csv_data) as file:
            reader = csv.reader(file)
            next(reader)  # Skip the csv header
            for name, shortname, email in reader: # csv column-names
                print(f"Send mail to: {name} \n {shortname} \n {email} \n")
                
                receiver_email = email
                server.sendmail(
                    sender_email, 
                    receiver_email, 
                    message.as_string().format(name=shortname, receiver_email_address=email)
                    )
                
                # spam detection bypass: time buffer between loop iterations
                if isinstance(sleep_min, int) and isinstance(sleep_max, int):
                    # sleep between min/max seconds between emails (integers)
                    sleep_time = int(random.uniform(sleep_min, sleep_max))
                    time.sleep(sleep_time) # sleep_time in seconds
                    print("Wait seconds: " + str(sleep_time) )


#### csv data files
csv_data_path = "csv_data/test_data.csv"


message = create_message(
    sender_email="username@domain.com",
    subject="This email is about a subject",
    text_file_path=message_text_path, 
    html_file_path=message_html_path,
    plain_text = False # only send the plain-text version
    )



send_email(
    csv_data=csv_data_path, # double check the correct data file
    sender_email="username@domain.com",
    message=message,
    sleep_min=10, # minimal seconds between emails
    sleep_max=20, # maximum seconds between emails
    production=True
    )
