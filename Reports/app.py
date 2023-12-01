import json

import uvicorn
from fastapi import FastAPI, APIRouter

from Reports.database_clients import SQLClient, NoSQLClient


class Application:
    relational_client: SQLClient = SQLClient()
    no_relational_client: NoSQLClient = NoSQLClient()

    def __init__(self):
        self.microservice: FastAPI = FastAPI()
        self.router: APIRouter = APIRouter()
        self.router.add_api_route("/get_report", self.get_report, methods=["GET"])
        self.router.add_api_route("/insert_report", self.insert_report, methods=["POST"])
        self.router.add_api_route("/get_form_metadata", self.get_form_metadata, methods=["GET"])
        self.router.add_api_route("/get_content_status/{id}", self.get_content_status, methods=["GET"])
        self.router.add_api_route("/set_content_status/{id}", self.set_content_status, methods=["POST"])
        self.router.add_api_route("/get_content_url/{id}", self.get_content_url, methods=["GET"])
        self.microservice.include_router(self.router)

    def get_report(self):
        return self.relational_client.get_report("123456789")

    def insert_report(self):
        return self.relational_client.insert_report(
            {
                "id": "123456789",
                "name": "test",
                "age": 20,
                "city": "New York"
            }
        )

    def get_form_metadata(self):
        val = self.no_relational_client.get_form_metadata()
        return val

    def get_content_status(self, id):
        with open("content_status.json", "r") as f:
            json_data = json.load(f)
            return json_data[id]

    def set_content_status(self, id, status):
        with open("content_status.json", "r") as f:
            json_data = json.load(f)
            json_data[id] = status
            with open("content_status.json", "w") as f_edit:
                f_edit.write(json.dumps(json_data))

    def get_content_url(self, id):
        with open("content_url.json", "r") as f:
            json_data = json.load(f)
            return json_data[id]


app: FastAPI = Application().microservice
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
