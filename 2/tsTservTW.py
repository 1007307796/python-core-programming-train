from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:',clnt)
    def dataReceived(self, data):
        data = '[{}] {}'.format(ctime(),data.decode())
        data = data.encode('utf-8')
        self.transport.write(data)
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()