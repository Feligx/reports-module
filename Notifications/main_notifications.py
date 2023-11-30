from Invoker import Invoker
from Encrypt import Encrypt
from Decrypt import Decrypt
from Content import Content
from datetime import datetime


def main():
    content = Content()
    content.user_id = "123"
    content.content_id = "456"
    content.info = {"hello": "world"}
    content.created_at = datetime.now()
    content.status = "10"

    a = content.content_to_string()
    print(a)
    invoker = Invoker()
    encrypt = Encrypt()
    decrypt = Decrypt()

    

    en = invoker.invoke(encrypt, a)
    print(en)

    de = invoker.invoke(decrypt, en)
    print(de)

if __name__ == "__main__":
    main()