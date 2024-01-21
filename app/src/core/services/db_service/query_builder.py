from typing import Optional, List, Dict

from bson import ObjectId

PATHS_PIPELINE = [
    {"$group": {
        "_id": "$path", "total_message": {"$sum": 1},
        "last_message_at": {"$max": "$server_received_message_at"}
    }}
]


class MongoQueryBuilder:

    def __init__(
            self,
            document_id: Optional[str] = None,
            search_in_paths: Optional[List] = None,
            status_code: Optional[int] = None,
            server_timeout: Optional[int] = None
    ):
        self.document_id = document_id
        self.search_in_paths = search_in_paths
        self.status_code = status_code
        self.server_timeout = server_timeout

    def __call__(self) -> Dict:
        query = {}

        if self.document_id is not None:
            query['_id'] = ObjectId(self.document_id)
        if self.search_in_paths not in (None, []):
            query["path"] = {"$in": [str(i) for i in self.search_in_paths]}
        if self.status_code is not None:
            query["response_status_code"] = self.status_code
        if self.server_timeout is not None:
            query['server_timeout'] = self.server_timeout

        return query
