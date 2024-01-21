import uuid
from typing import Optional, List, Annotated, Dict

from pydantic import BeforeValidator
from pymongo import MongoClient, DESCENDING

from core import models
from core.services.db_service.query_builder import (
    MongoQueryBuilder,
    PATHS_PIPELINE
)
from core.services.db_service.query_builder import MongoQueryBuilder

PyObjectId = Annotated[str, BeforeValidator(str)]


#TODO: aggiungere mappers su tutte le trasformazioni da models -> schema


class DbService:

    DB_NAME = 'webhook'
    COLLECTION_NAME = 'messages'

    def __init__(self):
        # TODO: aggiungere settings
        self.client = MongoClient('mongodb://localhost:27017')

    @property
    def db(self):
        return self.client[self.DB_NAME]

    @property
    def messages_collection(self):
        return self.db[self.COLLECTION_NAME]

    def persist_message(self, message: models.Message) -> None:
        document_to_insert = message.model_dump(exclude={"message_id"})
        self.messages_collection.insert_one(
            document=document_to_insert
        )

    def fetch_messages(
            self, items_to_fetch: int,
            paths: Optional[List[uuid.UUID]] = None,
            status_code: Optional[int] = None,
            server_timeout: Optional[int] = None
    ) -> List[models.Message]:

        query_builder = MongoQueryBuilder(
            search_in_paths=paths,
            status_code=status_code,
            server_timeout=server_timeout
        )

        sort_criteria = [("server_received_message_at", DESCENDING)]
        messages = self.messages_collection.find(query_builder()).sort(
            sort_criteria).limit(items_to_fetch)

        return [models.Message.model_validate(message) for message in messages]

    def fetch_paths(self) -> List[models.Path]:
        out = []
        to_iter = tuple(self.messages_collection.aggregate(PATHS_PIPELINE))
        for current_path in to_iter:
            to_append = models.Path(
                path=current_path["_id"],
                total_message=current_path["total_message"],
                last_message_at=current_path["last_message_at"]
            )
            out.append(to_append)
        return out

    def fetch_message_by_id(self, _id: str) -> models.Message:

        query_builder = MongoQueryBuilder(document_id=_id)
        fetched_document = self.messages_collection.find_one(query_builder())
        if fetched_document is None:
            # TODO: definire errori
            raise Exception("Message does not exist")
        return models.Message.model_validate(fetched_document)


db_service = DbService()

