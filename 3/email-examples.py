from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from secret import *

SENDER = 'MAILBOX_163'
RECIPS = 'MAILBOX_163'
SOME_IMG_FILE = 'dog.jpg'
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello world!\r\n','plain')
    email.attach(text)
    html = MIMEText('<html><body><h4>Hello World</h4></body></html>','html')
    email.attach(html)
    return email

def make_img_msg(fn):
    f = open(fn,'rb')
    data = f.read()
    f.close()
    pic = MIMEImage(data)
    pic.add_header('Content-Disposition','attachment',filename=fn)
    return pic

def sendMsg(fr,to,msg):
    s = SMTP('smtp.163.com',25)
    s.login(MAILBOX,PASSWD)
    s.sendmail(fr,to,msg)
    s.quit()

if __name__ == '__main__':
    print('Sending multipart alternative msg...')
    msg = make_mpa_msg()
    msg['From'] = SENDER
    msg['To'] = RECIPS
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER,RECIPS,msg.as_string())

    print('Sending image msg...')
    msg = make_img_msg(SOME_IMG_FILE)
    msg['From'] = SENDER
    msg['To'] = RECIPS
    msg['Subject'] = 'image file test'
    sendMsg(SENDER, RECIPS, msg.as_string())
