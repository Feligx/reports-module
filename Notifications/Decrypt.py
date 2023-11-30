from Command import Command
from cryptography.fernet import Fernet

class Decrypt(Command):
    def __init__(self):
        event = None
        

    def de(self, f: Fernet):
        print("Decrypting...")
        return f.decrypt(self.event).decode()

    def execute(self, event, f: Fernet):
        self.event = event
        return self.de(f)