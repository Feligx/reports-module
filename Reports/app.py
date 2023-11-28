import uvicorn
from fastapi import FastAPI, APIRouter


class Application:

    def __init__(self):
        self.microservice: FastAPI = FastAPI()
        self.router: APIRouter = APIRouter()
        self.router.add_api_route("/notify", self.notify, methods=["POST"])
        self.router.add_api_route("/insert_report", self.insert_report, methods=["POST"])
        self.router.add_api_route("/get_form_metadata", self.get_form_metadata, methods=["GET"])
        self.microservice.include_router(self.router)

    def notify(self):
        return {"message": "Hello, World! uwu"}

    def insert_report(self):
        return {"message": "Hello, World! uwu"}

    def get_form_metadata(self):
        return {"message": "Hello, World! uwu"}


app: FastAPI = Application().microservice
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
