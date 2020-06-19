#!/usr/bin/env python
# coding=gbk
from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:',self.client_address)
        data = '[{}] {}'.format(ctime( ),self.rfile.readline().decode())
        data = data.encode('utf-8')
        self.wfile.write(data)

tcpServ = TCP(ADDR,MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()