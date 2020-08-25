from twisted.internet import reactor, protocol
from twisted.internet.protocol import ReconnectingClientFactory as ClFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from sys import stderr
import json


class Client(protocol.Protocol):
    def __init__(self):
        print("Created")
        reactor.callInThread(self.message_input)

    @staticmethod
    def __encode_json(**kwargs):
        return json.dumps(kwargs)

    def send_message(self, **kwargs):
        self.transport.write(self.__encode_json(**kwargs).encode("utf-8"))

    def message_input(self):
        while True:
            self.send_message(value=input("value:"), type=input("type:"))

    def dataReceived(self, data):
        try:
            data = json.loads(data.decode("utf-8"))
        except UnicodeDecodeError or json.JSONDecodeError:
            print("Something went wrong :(", file=stderr)
            return

        if data['type'] == 'error':
            print(data.get('value', "Unknown error"), file=stderr)
        else:
            print(data.get('value', "No value in the message"))


class ClientFactory(ClFactory):
    def clientConnectionLost(self, connector, unused_reason):
        self.retry(connector)

    def clientConnectionFailed(self, connector, reason):
        print(reason)
        self.retry(connector)

    def buildProtocol(self, addr):
        return Client()


if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 12345)
    endpoint.connect(ClientFactory())
    reactor.run()
