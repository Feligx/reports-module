from Command import Command
from cryptography.fernet import Fernet

class Encrypt(Command):
    def __init__(self):
        event = None
        

    def en(self, f: Fernet):
        print("Encrypting...")
        return f.encrypt(self.event.encode())

    def execute(self, event, f: Fernet):
        self.event = event
        return self.en(f)
        