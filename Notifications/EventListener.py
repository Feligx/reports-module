from abc import abstractmethod, ABC


class EventListener(ABC):
    def __init__(self, event):
        pass


    def update(self):
        pass