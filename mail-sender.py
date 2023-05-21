import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime, time

def sendmail(startTime, endTime, packageName, statusReport):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    userName = 'amoghsyshpe@gmail.com'
    passWord = 'sgipqysszhtkitos'
    server.starttls()
    server.login(userName, passWord)
    receiverMail = 'amoghpgowda@gmail.com'
    # create message object instance
    msg = MIMEMultipart()
    
    # setup the parameters of the message
    msg['From'] = userName
    msg['To'] = receiverMail
    msg['Subject'] = 'Status report for ' + packageName
    
    startStr = startTime.strftime('%Y-%m-%d %H:%M:%S')
    endStr = endTime.strftime('%Y-%m-%d %H:%M:%S')

    # add in the message body
    body = 'Package name: ' + packageName + '\nStart time: ' + startStr + '\nEnd time: ' + endStr + '\nStatus report: ' + statusReport
    msg.attach(MIMEText(body, 'plain'))

    server.sendmail(userName, receiverMail, msg.as_string())
    server.quit()
