from twisted.internet import reactor, protocol
from twisted.internet.protocol import ServerFactory as ServFactory, connectionDone
from twisted.internet.endpoints import TCP4ServerEndpoint


class Server(protocol.Protocol):
    def __init__(self, clients: dict, my_id):
        self.my_id = my_id
        self.clients = clients
        self.another_client = None

    def connectionMade(self):
        self.clients[self.my_id] = self

    def send_message(self, data: str, where=None):
        if where:
            where.transport.write(data.encode("utf-8"))
        else:
            self.transport.write(data.encode("utf-8"))

    def dataReceived(self, data):
        data = data.decode("utf-8")

        if not self.another_client:
            try:
                another_client = int(data)
                if another_client in self.clients.keys():
                    self.another_client = another_client
                else:
                    raise KeyError

            except ValueError:
                self.send_message("Write another id as int")
            except KeyError:
                self.send_message("Can't find that client")

            else:
                self.send_message(f"Talk to {self.another_client}")

        else:
            try:
                self.send_message(data, self.clients[self.another_client])
            except KeyError:
                self.send_message("something wrong happened, try another client")
                self.another_client = None

    def connectionLost(self, reason=connectionDone):
        self.disconnect()

    def disconnect(self):
        del self.clients[self.my_id]


class ServerFactory(ServFactory):
    def __init__(self):
        self.clients = {}
        self.last_id = 0

    def buildProtocol(self, addr):
        self.last_id += 1
        return Server(self.clients, self.last_id)


if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 12345)
    endpoint.listen(ServerFactory())
    reactor.run()
