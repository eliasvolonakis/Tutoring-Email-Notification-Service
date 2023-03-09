from email.message import EmailMessage
import ssl
import smtplib
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Set Up All Environment Variables
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

def sendmail(student_name, session_time, student_email, zoom_link)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = student_email
    em['Subject'] = "Session Reminder {session_time}".format(session_time=session_time)

    body = """
    Good morning {studen_name}!

    I'll see you this evening from {session_time} for our tutoring session. 
    Please use the zoom link below:
    {zoom_link}}

    Thanks, 
    Elias
    """

    em.set_content(body)
    context = ssl.create_default_context()

    email_server = 'smtp.gmail.com'
    port = 465
    with smtplib.SMTP_SSL(email_server, port, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

