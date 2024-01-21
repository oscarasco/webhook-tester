import datetime
import uuid

from fastapi import  Request

from api import schema
from core import models


def map_message_model_from_request_schema(
        path: uuid,
        received_at: datetime.datetime,
        response_status_code: int,
        response_timeout: int,
        message: schema.MessageRequest,
        request: Request
) -> models.Message:

    body = message.model_extra
    headers = request.headers

    _a = message.customer_created_request_at
    customer_created_request_at = _a if _a else None

    return models.Message(
        path=str(path),
        response_status_code=response_status_code,
        server_timeout=response_timeout,
        extra={"body": body, "headers": headers},
        service_sent_message_at=customer_created_request_at,
        server_received_message_at=received_at
    )


def map_message_from_model_to_schema(
        message: models.Message) -> schema.Message:

    _message: schema.Message = schema.Message(
        message_id=message.message_id,
        path=message.path,
        service_sent_message_at=message.service_sent_message_at,
        server_received_message_at=message.server_received_message_at,
        response_status_code=message.response_status_code,
        server_timeout=message.server_timeout
    )
    return _message
