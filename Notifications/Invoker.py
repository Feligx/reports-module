from Command import Command
from cryptography.fernet import Fernet


class Invoker:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        

    def invoke(self, command: Command, event):
        return command.execute(event, self.f)
        