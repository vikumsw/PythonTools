#!/usr/bin/python

import smtplib

sender = 'vikumsw@gmail.com'
receivers = ['vikumsw@gmail.com']

message = """From: From Person <vikumsw@gmail.com>
To: To Person <vikumsw@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")