import json

from SocketService import SocketService
import logging
# use websockets instead of socketio
from websockets import serve
import asyncio

logging.basicConfig(level=logging.INFO)


class WebSocket(SocketService):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.payload = None

    async def notify(self, websocket):
        async for message in websocket:
            logging.info("WebSocket: Updating payload")
            self.payload = json.loads(message)
            await websocket.send(json.dumps(self.payload))

    async def start_server(self):
        logging.info("WebSocket: Starting server")
        async with serve(self.notify, self.host, self.port):
            await asyncio.Future()


if __name__ == '__main__':
    ws_server = WebSocket("localhost", 8765)

    # Start the WebSocket server
    asyncio.run(ws_server.start_server())