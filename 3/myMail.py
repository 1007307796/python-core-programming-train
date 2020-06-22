from poplib import POP3
from smtplib import SMTP
from time import sleep
from secret import *

SMTPSVR = 'smtp.163.com'
POP3SVR = 'pop.163.com'

Fwho = MAILBOX_163
Twho = MAILBOX_163
body = '''
From:{}
To:{}
Subject:test msg

Hello World!
'''.format(Fwho,Twho)

sendSvr = SMTP(SMTPSVR)
sendSvr.login(MAILBOX_163,PASSWD)
errs = sendSvr.sendmail(Fwho,Twho,body)
sendSvr.quit()
assert len(errs) == 0,errs
sleep(10)
recvSvr = POP3(POP3SVR)
recvSvr.user(MAILBOX_163)
recvSvr.pass_(PASSWD)
rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index(b'')
recvBody = msg[sep+1:]
print('Message:\n',recvBody)