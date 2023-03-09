from email.message import EmailMessage
import ssl
import smtplib
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

email_sender = os.getenv('SENDER_EMAIL')
email_receiver = os.getenv('RECEIVER_EMAIL')
email_password = os.getenv("EMAIL_PASSWORD") 
port = os.getenv('PORT')
email_server = os.getenv('EMAIL_SERVER')

print("RECEIVER_EMAIL" + str(email_receiver))
print("SENDER_EMAIL" + str(email_sender))
print("EMAIL_PASSWORD" + str(email_password))
print("PORT" + str(port))
print("EMAIL_SERVER" + srt(email_server))


# email_sender = "envolonakis@gmail.com"
# email_password = "nffygmqgllrtwfew"
# email_receiver = "envolonakis@gmail.com"

# subject = "Test Subject"
# body = "Test Body"

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context()

# email_server = 'smtp.gmail.com'
# port = 465
# with smtplib.SMTP_SSL(email_server, port, context = context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())

