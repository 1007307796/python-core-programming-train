#!/usr/bin/env python
# coding=gbk
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    data = data.decode('utf-8')
    data = '[{}] {}'.format(ctime(), data)
    data = data.encode('utf-8')
    udpSerSock.sendto(data,addr)
    print('...received from and return to:',addr)
udpSerSock.close()