from RealTime.SocketClient import SocketClient
from RealTime.SocketService import SocketService


class SocketAdapter(SocketClient):
    def __init__(self):
        adaptee: SocketService = None
        super().__init__()

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def update(self):
        pass

    def notify(self):
        pass