import uuid
from datetime import datetime

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String

# from Reports.database_services import OfflineBase

from os.path import join
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from pathlib import Path


class ReportForm(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    class Config:
        orm_mode = True


BASE_DIR = Path.cwd().resolve()

OfflineBase = declarative_base()
DB_PATH = join(BASE_DIR, "offline.db")
offline_engine = create_engine('sqlite:///' + DB_PATH)
offline_session = scoped_session(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=offline_engine))

@contextmanager
def get_offline_db_session():
    try:
        yield offline_session
    finally:
        offline_session.remove()


class Report(OfflineBase):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    description = Column(String(200))
    created_at = Column(String, default=datetime.utcnow())
    updated_at = Column(String, default=datetime.utcnow())
    user_id = Column(Integer, nullable=True)
    content_id = Column(Integer, nullable=True)
    status = Column(String(30), nullable=True)


print("Creating database...")
OfflineBase.metadata.create_all(bind=offline_engine)
print("Created database!")