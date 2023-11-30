from abc import ABC, abstractmethod
from cryptography.fernet import Fernet

class Command(ABC):
    

    @abstractmethod
    def execute(self, event, f: Fernet):
        pass