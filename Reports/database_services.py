from os.path import join
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from pathlib import Path
import logging
from sqlalchemy import inspect
from sqlalchemy.orm import RelationshipProperty

from pymongo import MongoClient
from . import models

BASE_DIR = Path.cwd().resolve()

OfflineBase = declarative_base()
DB_PATH = join(BASE_DIR, "offline.db")
offline_engine = create_engine('sqlite:///' + DB_PATH)
offline_session = scoped_session(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=offline_engine))


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
        models.OfflineBase.metadata.create_all(bind=offline_engine)

    def insert(self, data):
        with offline_session as s:
            s.add(data)
            s.commit()

    def update(self, id, data):
        with offline_session as s:
            s.query(models.Report).filter(models.Report.id == id).update(data)
            s.commit()

    def get(self, id):
        with offline_session as s:
            return s.query(models.Report).first()


class MongoService(Service):
    client: MongoClient

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['test-database']
        super().__init__()

    def insert(self, data):
        self.db['test-form'].insert_one(data)

    def update(self, id, data):
        self.db['test-form'].update_one(
            {"_id": data["_id"]}, {"$set": data}
        )

    def get(self, id=""):
        return self.db['test-form'].find_one()
