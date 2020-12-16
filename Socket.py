import socket
import asyncio
import struct


class Socket:
    def __init__(self):
        self.socket = socket.socket(

            socket.AF_INET,
            socket.SOCK_STREAM,

        )

        self.main_loop = asyncio.new_event_loop()

    async def send_data(self, data=None):
        raise NotImplementedError()

    async def _recv_message(self, listened_socket: socket.socket, message_len: int):
        message = bytearray()

        while len(message) < message_len:
            packet = await self.main_loop.sock_recv(listened_socket, message_len - len(message))
            if packet is None:
                return None

            message.extend(packet)

        return message

    async def _decode_data(self, data: bytes):
        return data.decode("utf-8")

    async def listen_socket(self, listened_socket):
        meta_data = await self._recv_message(listened_socket, 4)
        meta_data = struct.unpack("I>", meta_data)[0]
        print("need to get:", meta_data)

        data = await self._recv_message(listened_socket, meta_data)
        return self._decode_data(data)

    async def main(self):
        raise NotImplementedError()

    def start(self):
        self.main_loop.run_until_complete(self.main())

    def set_up(self):
        raise NotImplementedError()

