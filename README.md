# Ashley-s_Portfolio
Data Analytics Portfolio

import ssl
import smtplib
from email.mime.text import MIMEText
import schedule
import time
import pyodbc
def send_code_email():
...     email_sender = 'ashley05gooch@gmail.com'
...     email_password = 'hshjxnsjcfjbxnbr'
...     email_receiver = 'brandpromotionsonly@gmail.com'
...     subject = 'NHP Birthdays'
# Your Python code goes here
...     code = """
...     conn = pyodbc.connect(
... 	"Driver={ODBC Driver 17 for SQL Server};"
... 	"Server=AGIWK-ASHLEYG\\SQLEXPRESS;"
... 	"Database=AGIMain1;"
... 	"Trusted_Connection=yes"
... 	)
...
... cursor = conn.cursor()
... cursor.execute("SELECT IDNumber, Sex, Birthdate, CurrentLocation, Site FROM dbo.Primates WHERE CurrentLocation NOT IN ('Transfer', 'Shipped', 'Sold', 'Died') AND DATEPART(day, Birthdate) = DATEPART(day, DATEADD(day, 0, GETDATE())) AND DATEPART(month, Birthdate) = DATEPART(month, DATEADD(month, 0, GETDATE()))")
...
... for x in cursor:
...     print(x)
...	 """
...	msg = MIMEText(code)
...     msg['From'] = email_sender
...     msg['To'] = email_receiver
...     msg['Subject'] = subject
...     context = ssl.create_default_context()
...     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
...             smtp.login(email_sender, email_password)
...             smtp.sendmail(email_sender, email_receiver, msg.as_string())

# Schedule the email to be sent every day at 9:00 AM
>>> schedule.every().day.at("09:00").do(send_code_email)

# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)