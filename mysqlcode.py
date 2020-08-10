import mysql.connector
import pandas as pd
from datetime import datetime,date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='',database='penta6_db')
mycursor = mydb.cursor()
l=['Id', 'Name', 'Email', 'Goods', 'Carrier type', 'Destination Country', 'Origin Country', 'ISD Code', 'Phone Number', 'Message', 'Destination Address', 'Destination Pincode', 'Origin Address', 'Origin Pincode', 'Quantity','Time Stamp']
mycursor.execute('select * from freight_quotes order by timestamp desc')
result = mycursor.fetchall()
# print(l2)
d=[]
index=[]
for i in result:
    if (datetime.now()-i[-1]).total_seconds()>86400:
        break
    d.append(i[1:])
    index.append(i[0])
df = pd.DataFrame(data=d,columns=l[1:],index=index)
df.to_csv('data2.csv')
sender_address='cs@pentasixbright.com'
reciever_address='cs@pentasixbright.com'
sender_password='Shadow0427@'
message=MIMEMultipart()
message['From']=sender_address
message['To']=reciever_address
message['Subject']="Daily Quote Report - {date}".format(date=date.today())
if d:
    mail_content = """
    Hi Admin,

    Daily Quote Report for '{date}' has been attached.

    Regards,
    Team Shimmer""".format(date=date.today())
    attachfilename='data2.csv'
    # payload = MIMEApplication(open(attachfilename,'rb').read())
    attachfile = open(attachfilename,'rb')
    payload = MIMENonMultipart('text', 'csv', charset='utf-8')
    payload.set_payload(attachfile.read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment',filename="data.csv")
    message.attach(payload)
else:
    mail_content="""
    Hi Admin,

    No qoutes for '{date}'.

    Regards,
    Team Shimmer""".format(date=date.today())
print("Connecting")
message.attach(MIMEText(mail_content,'plain'))
session = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
# session.starttls()
session.ehlo()
session.login(sender_address, sender_password) 
text = message.as_string()
session.sendmail(sender_address, reciever_address, text)
session.quit()
print('mail send')