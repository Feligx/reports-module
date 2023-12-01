
from cryptography.fernet import Fernet

from Notifications.Command import Command


class Encrypt(Command):
    def __init__(self):
        event = None
        

    def en(self, f: Fernet):
        print("Encrypting...")
        return f.encrypt(self.event.encode())

    def execute(self, event, f: Fernet):
        self.event = event
        return self.en(f)
        