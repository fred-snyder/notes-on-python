import smtplib, ssl

# import smtp_server, port, login, password
import production_config

# Create SSL context
context = ssl.create_default_context()

# test the smtp server
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(login, password)
except Exception as e:
    # Print error messages
    print(e)
finally:
    server.quit() 
