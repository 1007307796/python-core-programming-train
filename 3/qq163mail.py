from io import StringIO
from imaplib import  IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL
from smtplib import SMTP
import email

release = python_version()
if release > '2.6.2':
    from smtplib import SMTP_SSL
else:
    SMTP_SSL = None

from secret import *

who = '{}@163.com'.format(MAILBOX)
from_ = who
to = [who]

headers = [
    'From: {}'.format(from_),
    'To: {}'.format(', '.join(to)),
    'Subject: test SMTP send via 25/TLS',
]
body = [
    'Hello',
    'world!',
]
msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))

def getSubject(msg, default = '(no Subject line)'):
    for line in msg:
        if line.startswith('Subject:'):
            return line.rstrip()
        if not line:
            return default

#SMTP/TLS
print('*** Doing SMTP send via TLS...')
s = SMTP('smtp.163.com',25)
if release < '2.6':
    s.ehlo()
s.starttls()
if release < '2.5':
    s.ehlo()
s.login(MAILBOX,PASSWD)
s.sendmail(from_,to,msg)
s.quit()
print('TLS mail sent!')

# POP
print('***Doing POP recv...')
s = POP3_SSL('pop.163.com', 995)
s.user(MAILBOX)
s.pass_(PASSWD)
rv, msg_pop, sz = s.retr(s.stat()[0])
s.quit()
line = getSubject(msg_pop)
print('Received msg via POP: {}'.format(line.decode()))

headers[2] = headers[2].replace('25/TLS','465/SSL')
msg_SSL = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))
#SMTP/SSL
if SMTP_SSL:
    print('*** Doing SMTP send via SSL...')
    s = SMTP_SSL('smtp.163.com',465)
    s.login(MAILBOX,PASSWD)
    s.sendmail(from_,to,msg_SSL)
    s.quit()
    print('SSL mail sent!')

# IMAP
print('***Doing IMAP recv...')
s = IMAP4_SSL('imap.qq.com', 993)
s.login(MAILBOX_QQ, PASSWD_QQ)
rsp,Msgs = s.select('INBOX',True)
rsp,data = s.fetch(Msgs[0],'(RFC822)')
line = getSubject(StringIO(data[0][1].decode()))

s.close()
s.logout()
print('Received msg via IMAP: {}'.format(line))