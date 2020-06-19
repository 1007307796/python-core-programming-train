# coding=gbk
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024

def GetAddr():
    Host = input("请输入主机地址：")
    Port = input("请输入端口号：")
    if not Host:
        Host = HOST
    if not Port:
        Port = PORT
    return Host,int(Port)

Host,Port = GetAddr()
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'),ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
udpCliSock.close()