from SocketService import SocketService


class WebSocket(SocketService):
    def __init__(self):
        super().__init__()
        self.payload = None

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def update(self):
        pass

    def notify(self):
        pass
