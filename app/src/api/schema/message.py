import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MessageRequest(BaseModel):

    customer_created_request_at: Optional[datetime.datetime] = Field(
        alias="customerCreatedRequestAt")

    model_config = ConfigDict(
        extra="allow"
    )


class MessageResponse(BaseModel):
    model_config = ConfigDict(
        extra="allow"
    )
