from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientFactory as ClFactory
from twisted.internet.endpoints import TCP4ClientEndpoint


class Client(protocol.Protocol):
    def __init__(self):
        print("Created")
        reactor.callInThread(self.message_input)

    def send_message(self, data: str):
        self.transport.write(data.encode("utf-8"))

    def message_input(self):
        while True:
            self.send_message(input())

    def dataReceived(self, data):
        data = data.decode("utf-8")
        print(data)


class ClientFactory(ClFactory):
    def buildProtocol(self, addr):
        return Client()


if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 12345)
    endpoint.connect(ClientFactory())
    reactor.run()
