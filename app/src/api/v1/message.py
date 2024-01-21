import datetime
import uuid as uuid
from typing import Optional

from fastapi import APIRouter, Response, Body

from api.schema.message import MessageRequest, MessageResponse
from core.mappers import map_message_model_from_request_schema
from core.services.db import db_service

router = APIRouter()


@router.post("/{_id}")
async def post_message(
        _id: uuid.UUID,
        message: MessageRequest = Body(default_factory=dict),
        response_status_code: Optional[int] = 204,
        response_timeout_s: Optional[int] = 0,
        return_request_payload: Optional[bool] = False,
        response: Response = Response()
) -> Optional[MessageResponse]:

    response.status_code = response_status_code
    received_at = datetime.datetime.utcnow()

    message_to_persist = map_message_model_from_request_schema(
        path=_id, message=message, received_at=received_at
    )
    db_service.persist_message(message=message_to_persist)

    if return_request_payload:
        response = MessageResponse(**message.model_dump())
        return response
    return None
