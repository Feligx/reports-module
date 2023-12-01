from EventListener import EventListener
from email.mime.text import MIMEText
from time import sleep



class SMTPListener(EventListener):#message lo obtenemos del EventListener
    def __init__(self):
        pass

    def update(self):
        pass

    def enviar_correo(self, mensaje):
        print("Enviando correo: ", mensaje)
        sleep(1)
        print("Correo enviado")