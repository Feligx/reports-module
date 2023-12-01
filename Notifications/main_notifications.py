from Invoker import Invoker
from Encrypt import Encrypt
from Decrypt import Decrypt
from Content import Content
from datetime import datetime
from EventHandler import EventHandler

def main():
    invoker = Invoker()
    encrypt = Encrypt()
    decrypt = Decrypt()

    content = Content()
    content.user_id = "1234"
    content.content_id = "456"
    content.info = {"hello": "world"}
    content.created_at = datetime.now()
    content.status = "Pending"

    #eventHandler recibe decifrado en JSON
    eventHandler = EventHandler(content.content_to_json())
    eventHandler.update_WS()

if __name__ == "__main__":
    main()