from abc import ABC, abstractmethod

class SocketClient(ABC):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @abstractmethod
    def on_connect(self):
        pass

    @abstractmethod
    def on_disconnect(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def notify(self):
        pass
