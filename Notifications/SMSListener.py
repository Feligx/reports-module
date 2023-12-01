from EventListener import EventListener
from time import sleep

class SMSListener(EventListener):
    def __init__(self):
        pass

    def enviar_sms(self, mensaje):
        print("Enviando SMS: ", mensaje)
        sleep(1)
        print("SMS enviado")

    def update(self):
        pass
