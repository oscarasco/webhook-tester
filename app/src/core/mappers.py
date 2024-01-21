import datetime
import uuid

from api import schema
from core import models


def map_message_model_from_request_schema(
        path: uuid,
        received_at: datetime.datetime,
        message: schema.MessageRequest) -> models.Message:

    body = message.model_dump(exclude={"customer_created_request_at"})

    _a = message.customer_created_request_at
    customer_created_request_at = _a if _a else None

    return models.Message(
        path=str(path),
        body=body,
        customer_created_request_at=customer_created_request_at,
        received_at=received_at
    )
