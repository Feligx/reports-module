import uuid
from datetime import datetime

from pydantic import BaseModel, Field

class Report(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    class Config:
        orm_mode = True