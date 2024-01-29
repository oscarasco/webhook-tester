import datetime
import uuid
from unittest import TestCase

from api import schema
from core import models
from core.mappers import map_message_from_model_to_schema


class TestMapMessageFromModelToSchema(TestCase):

    def setUp(self) -> None:

        self.message_id = "65b68135a06977a7d35fa09a"
        self.path = str(uuid.uuid4())
        self.service_sent_message_at = datetime.datetime.utcnow()
        self.server_received_message_at = datetime.datetime.utcnow()
        self.response_status_code = 200
        self.server_timeout = 10

        self.to_map = models.Message(
            path=self.path,
            service_sent_message_at=self.service_sent_message_at,
            server_received_message_at=self.server_received_message_at,
            response_status_code=self.response_status_code,
            server_timeout=self.server_timeout
        )
        self.to_map.message_id = self.message_id

    def test_map_message_from_model_to_schema(self):

        mapped = map_message_from_model_to_schema(self.to_map)
        self.assertIsInstance(mapped, schema.Message)
