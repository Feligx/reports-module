from pymongo import MongoClient
from . import models
from .models import get_offline_db_session


class Service:
    def __init__(self):
        ...

    def insert(self, data):
        ...

    def update(self, id, data):
        ...

    def get(self, id):
        ...


class SQLiteService(Service):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        with get_offline_db_session() as s:
            s.add(models.Report(**data))
            s.commit()

    def update(self, id, data):
        with get_offline_db_session() as s:
            s.query(models.Report).filter(models.Report.id == id).update(data)
            s.commit()
    def get(self, id):
        with get_offline_db_session() as s:
            result = s.query(models.Report).filter(models.Report.id == id).first()
            return result


class MongoService(Service):
    client: MongoClient

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['form-db']
        super().__init__()

    def insert(self, data):
        self.db['test-form'].insert_one(data)

    def update(self, id, data):
        self.db['test-form'].update_one(
            {"_id": data["_id"]}, {"$set": data}
        )

    def get(self, id=""):
        value = dict(self.db['test-form'].find_one())
        value.pop("_id", None)
        return value
