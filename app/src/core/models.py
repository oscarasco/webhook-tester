import datetime
import uuid
from typing import Optional, Dict

from pydantic import BaseModel, Field


class Message(BaseModel):

    path: str
    body: Optional[Dict] = Field(default_factory=dict)

    customer_created_request_at: Optional[datetime.datetime] = None
    received_at: datetime.datetime
    created_at: Optional[datetime.datetime] = Field(
        default=datetime.datetime.utcnow())
