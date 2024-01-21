from pymongo import MongoClient

from core import models


class DbService:

    DB_NAME = 'webhook'
    COLLECTION_NAME = 'message'

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')

    def _init_db(self):
        db = self.client[self.DB_NAME]
        # TODO: vedo bene la init anche sulla collection che potrebbero diventare piu' di una
        collection = db[self.COLLECTION_NAME]
        return collection

    def _db_exist(self) -> bool:
        return self.DB_NAME in self.client.list_database_names()

    @property
    def db(self):
        return self.client[self.DB_NAME]

    @property
    def message_collection(self):
        return self.db[self.COLLECTION_NAME]

    def persist_message(self, message: models.Message) -> None:
        document_to_insert = message.model_dump()
        #TODO: scomporre accesso a collection
        self.message_collection.insert_one(
            document=document_to_insert
        )


db_service = DbService()
