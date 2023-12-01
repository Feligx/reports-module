import socketio
import json

from Notifications.Content import Content
from Notifications.Encrypt import Encrypt
from Notifications.Invoker import Invoker

# Create a Socket.IO client instance
sio = socketio.Client()

# Connect to the Socket.IO server
#multicoment python

sio.connect('http://127.0.0.1:5000')

# Event handler for successful connection
@sio.event
def connect():
    print("Connected to server")

# Event handler for disconnection
@sio.event
def disconnect():
    print("Disconnected from server")

# Method to send data to "/receive_report"
def send_report(data):
    sio.emit('receive_report', data, namespace='/')
    print(f"Report sent: {data}")

class EventHandler:
    def __init__(self,contentjson): 
        self.contentjson = contentjson
        self.mensaje = contentjson["description"]
        self.user_id = contentjson["user_id"] 


    def update_WS(self):

        invoker = Invoker()
        encrypt = Encrypt()
        content = Content()

        content.json_to_content(self.contentjson)

        a = content.content_to_string()
        print(a)
        
        en = invoker.invoke(encrypt, a)
        print(en)

        diccionario = {"user_id":self.user_id,"content_en":en}
        print("Contento cifrado: ",diccionario,"user_id: ",self.user_id)

        connect()
        
        diccionario["content_en"] = diccionario["content_en"].decode('utf-8')
        send_report(json.dumps(diccionario))
        disconnect()
        return None


    def subscribe(self, listener):
        pass

    def unsubscribe(self, listener):
        pass