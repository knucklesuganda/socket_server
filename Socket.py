import socket
import asyncio


class Socket:
    def __init__(self):
        self.socket = socket.socket(

            socket.AF_INET,
            socket.SOCK_STREAM,

        )

        self.main_loop = asyncio.new_event_loop()

    async def send_data(self, data=None):
        raise NotImplementedError()

    async def listen_socket(self, listened_socket=None):
        raise NotImplementedError()

    async def main(self):
        raise NotImplementedError()

    def start(self):
        self.main_loop.run_until_complete(self.main())

    def set_up(self):
        raise NotImplementedError()

