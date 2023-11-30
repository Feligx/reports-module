import uuid
from datetime import datetime

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime

from Reports.database_services import OfflineBase


class ReportForm(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    class Config:
        orm_mode = True


class Report(OfflineBase):
    __absract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    description = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
