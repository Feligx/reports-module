import json
from logging import basicConfig, INFO
from datetime import datetime

import uvicorn
from fastapi import FastAPI, APIRouter

from Notifications.Content import Content
from Notifications.EventHandler import EventHandler
from Reports.database_clients import SQLClient, NoSQLClient

basicConfig(level=INFO)


class Application:
    relational_client: SQLClient = SQLClient()
    no_relational_client: NoSQLClient = NoSQLClient()

    def __init__(self):
        self.microservice: FastAPI = FastAPI()
        self.router: APIRouter = APIRouter()
        self.router.add_api_route("/get_report/{id:int}", self.get_report, methods=["GET"])
        self.router.add_api_route("/insert_report", self.insert_report, methods=["POST"])
        self.router.add_api_route("/update_report/{id:int}", self.update_report, methods=["PUT"])
        self.router.add_api_route("/appeal_report/{id:int}", self.appeal_report, methods=["PUT"])
        self.router.add_api_route("/get_form_metadata", self.get_form_metadata, methods=["GET"])
        self.router.add_api_route("/get_content_status/{id:str}", self.get_content_status, methods=["GET"])
        self.router.add_api_route("/set_content_status/{id:str}", self.set_content_status, methods=["POST"])
        self.router.add_api_route("/get_content_url/{id:str}", self.get_content_url, methods=["GET"])
        self.microservice.include_router(self.router)

    def get_report(self, id):
        print(f"Getting report {id} from DB")
        return self.relational_client.get_report(id)

    def insert_report(self, report_data: dict):
        content = Content()
        content.json_to_content(report_data)
        print(content.content_to_json())

        # eventHandler recibe decifrado en JSON
        print("Sending notif to EventHandler")
        eventHandler = EventHandler(content.content_to_json())
        eventHandler.update_WS()

        print("Saving report into DB")
        return self.relational_client.insert_report(
            report_data
        )

    def update_report(self, id, report_data: dict):
        print("Updating report into DB")
        return self.relational_client.update_report(
            id,
            report_data
        )

    def appeal_report(self, id):
        print("Appealing report into DB")
        return self.relational_client.update_report(
            id,
            {
                "status": "APPEALED"
            }
        )

    def get_form_metadata(self):
        print("Getting form metadata")
        return self.no_relational_client.get_form_metadata()

    def get_content_status(self, id):
        with open("content.json", "r") as f:
            json_data = json.load(f)
            print("Getting content status")
            return json_data[id].get("status")

    def set_content_status(self, id, status: dict):
        with open("content.json", "r") as f:
            json_data = json.load(f)
            json_data[id].update(status)
            with open("content.json", "w") as f_edit:
                print("Setting content status")
                f_edit.write(json.dumps(json_data))
                print("Content status set")

    def get_content_url(self, id):
        with open("content.json", "r") as f:
            json_data = json.load(f)
            print("Getting content url")
            return json_data[id].get("url")


app: FastAPI = Application().microservice
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
