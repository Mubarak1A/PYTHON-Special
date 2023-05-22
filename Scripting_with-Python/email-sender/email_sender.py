#!/usr/bin/python3
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

emails = [] #list suppose contain list of emails to send mail to

#looping through emails to send mail
for email in emails:
    html = Template(Path("email_with_python\index.html").read_text()) # accessing the mail content file
    email = EmailMessage() #making a mail object from EmailMessage class
    email['from'] = 'Mubarak' #the sender
    email['to'] = mail #receiver email
    email['subject'] = 'You have win Huge!' # email subject

    email.set_content(html.substitute(name = 'TinTin'), 'html') #substituting the html file for the content

# the smtplib guide...(Simple Mail Transfer Protocol lib)
    with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('Sender-email Here', 'Sender Password here')
        smtp.send_message(email)
        
        print(f'Mail Sent to {mail} successfully!')

#note sender password will be generated on email app password after authenticating 2-step verification...