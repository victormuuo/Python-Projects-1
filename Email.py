from email.message import EmailMessage
import ssl
import smtplib


email_sender='victormuuo2001@gmail.com'
email_password='nskfhqxdwqymeayg'

email_receiver='rakaw21302@jwsuns.com'

subject= 'Dont forget to subscribe to my Youtube Channel😋'
body="""
When you watch a video, please hit the subscribe button
"""

em=EmailMessage()
em['From']=email_sender
em['TO']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

