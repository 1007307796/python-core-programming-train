#!/usr/bin/env python
# coding=gbk
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    #accept返回一个元组:（新的socket对象，客户端地址）
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data = data.decode('utf-8')
        data = '[{}] {}'.format(ctime(),data)
        data = data.encode('utf-8')
        tcpCliSock.send(data)
    tcpCliSock.close()
tcpSerSock.close()