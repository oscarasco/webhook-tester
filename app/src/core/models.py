import datetime
from typing import Optional, Dict, Annotated

from pydantic import BaseModel, Field, BeforeValidator, ConfigDict

PyObjectId = Annotated[str, BeforeValidator(str)]


class Message(BaseModel):

    message_id: Optional[PyObjectId] = Field(alias="_id", default=None)
    path: str
    extra: Optional[Dict] = Field(default_factory=dict)
    response_status_code: int
    server_timeout: int

    service_sent_message_at: Optional[datetime.datetime] = None
    server_received_message_at: datetime.datetime
    created_at: Optional[datetime.datetime] = Field(
        default=datetime.datetime.utcnow())

    model_config = ConfigDict(
        from_attributes=True
    )


class Path(BaseModel):

    path: str
    total_message: int
    last_message_at: datetime.datetime
