from abc import abstractmethod, ABC


class RealTimeSubscriber(ABC):
    def __init__(self, event):
        pass

    @abstractmethod
    def update(self):
        pass
