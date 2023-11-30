from datetime import datetime
from Invoker import Invoker


class Content:
    def __init__(self):
        user_id: str = None
        content_id: str = None
        info: dict = None
        created_at: datetime = None
        status: str = None
    

    def content_to_json(self):
        return {
            "user_id": self.user_id,
            "content_id": self.content_id,
            "info": self.info,
            "created_at": self.created_at,
            "status": self.status
        }
    
    def json_to_content(self, json):
        self.user_id = json["user_id"]
        self.content_id = json["content_id"]
        self.info = json["info"]
        self.created_at = json["created_at"]
        self.status = json["status"]

    def content_to_string(self):
        return str(self.user_id) + "/" + str(self.content_id) + "/" + str(self.info) + "/" + str(self.created_at) + "/" + str(self.status)
    
    def string_to_content(self, string):
        self.user_id = string.split("/")[0]
        self.content_id = string.split("/")[1]
        self.info = string.split("/")[2]
        self.created_at = string.split("/")[3]
        self.status = string.split("/")[4]
