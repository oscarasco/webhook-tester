import datetime
import uuid
from typing import Optional, List, Dict

from pydantic import BaseModel, ConfigDict, Field, RootModel

from api.schema.base import BaseApiSchema


class MessageRequest(BaseApiSchema):

    customer_created_request_at: Optional[datetime.datetime] = Field(
        default=None, alias="customerCreatedRequestAt")

    model_config = ConfigDict(
        extra="allow"
    )


class MessagePayloadResponse(BaseModel):
    model_config = ConfigDict(
        extra="allow"
    )


class Message(BaseApiSchema):

    message_id: str
    path: uuid.UUID
    service_sent_message_at: datetime.datetime
    server_received_message_at: datetime.datetime
    response_status_code: int
    server_timeout: int


class MessageDetails(Message):
    extra: Optional[Dict] = Field(default_factory=dict)


class Messages(RootModel):
    root: List[Message] = Field(default_factory=list)

    model_config = ConfigDict(
        from_attributes=True
    )