from cryptography.fernet import Fernet

from Notifications.Command import Command


class Invoker:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        

    def invoke(self, command: Command, event):
        return command.execute(event, self.f)
        