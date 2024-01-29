import datetime
import time
import uuid as uuid
from typing import Optional, List, Literal

from fastapi import APIRouter, Request, Response, Body, Path, Query

from api import schema
from core.mappers import map_message_model_from_request_schema, \
    map_message_from_model_to_schema
from core.services.db_service.db import db_service

router = APIRouter()


@router.post("/{id}")
async def post_message(
        request: Request,
        _id: uuid.UUID = Path(alias="id"),
        message: schema.MessageRequest = Body(default_factory=dict),
        response_status_code: Optional[int] = Query(
            default=204, alias="responseStatusCode"),
        response_timeout_s: Optional[int] = Query(
            default=0, alias='responseTimeoutS'),
        return_request_payload: Optional[bool] = Query(
            default=False, alias='returnRequestPayload'),
        response: Response = Response()
) -> Optional[schema.MessagePayloadResponse]:

    response.status_code = response_status_code
    received_at = datetime.datetime.utcnow()

    message_to_persist = map_message_model_from_request_schema(
        path=_id,
        message=message,
        received_at=received_at,
        response_status_code=response_status_code,
        response_timeout=response_timeout_s,
        request=request
    )
    db_service.persist_message(message=message_to_persist)

    if response_timeout_s > 0:
        time.sleep(response_timeout_s)

    if return_request_payload:
        response = schema.MessagePayloadResponse(**message.model_dump())
        return response
    return None


@router.get("/paths")
async def get_active_paths(
        order_by: Literal['totalMessage', 'lastMessage'] = Query(
            alias="orderBy", default='totalMessage'
        ),
        order: Literal['descending', 'ascending'] = Query(
            default='descending'
        )
) -> schema.Paths:

    path = db_service.fetch_paths()

    sorting_criteria = (lambda x: x.total_message, lambda x: x.last_message_at)
    # TODO: in refactor capire a quale service delegare
    sorted_response = schema.Paths(
        sorted(
            [schema.Path.model_validate(i) for i in path],
            reverse=order == 'descending',
            key=sorting_criteria[order_by == "lastMessage"]
        )
    )
    return sorted_response


@router.get("/paths/messages")
async def get_messages(
        paths_to_include: Optional[List[str]] = Query(
            alias="pathsToInclude", default_factory=list),

        max_items: int = Query(alias="maxItems", default=200),

        response_status_code: Optional[int] = Query(
            alias="responseStatusCode", default=None),

        server_timeout: Optional[int] = Query(
            alias="serverTimeout", default=None)
) -> schema.Messages:

    # FIXME: far fixare frontend
    paths = [i.replace(' ', '') for i in paths_to_include[0].split(',')] \
        if paths_to_include else None

    messages = db_service.fetch_messages(
        items_to_fetch=max_items,
        paths=paths,
        server_timeout=server_timeout,
        status_code=response_status_code
    )

    return schema.Messages.model_validate(
        [map_message_from_model_to_schema(i) for i in messages]
    )


@router.get("/paths/messages/{messageId}")
async def get_message_details_by_id(
        message_id: str = Path(alias='messageId')
) -> schema.MessageDetails:

    a = db_service.fetch_message_by_id(_id=message_id)

    return schema.MessageDetails.model_validate(a.model_dump())
