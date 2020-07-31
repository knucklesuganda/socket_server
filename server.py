from twisted.internet import reactor, protocol
from twisted.internet.protocol import ServerFactory as ServFactory
from twisted.internet.endpoints import TCP4ServerEndpoint


class Server(protocol.Protocol):
    def __init__(self, clients: set):
        print("Init serv")
        self.clients = clients

    def connectionMade(self):
        self.clients.add(self)

    def send_message(self, data: str, where=None):
        if where:
            where.transport.write(data.encode("utf-8"))
        else:
            self.transport.write(data.encode("utf-8"))

    def dataReceived(self, data):
        print(data)
        data = data.decode("utf-8")

        for client in self.clients:
            self.send_message(data, client)


class ServerFactory(ServFactory):
    def __init__(self):
        print("Init factory")
        self.clients = set()

    def buildProtocol(self, addr):
        return Server(self.clients)


if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 12345)
    endpoint.listen(ServerFactory())
    reactor.run()
