from unittest import TestCase, mock

from fastapi.testclient import TestClient

from main import app
from mock.entity_loader import load_message


class TestGetMessageDetails(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app=app)
        self.url_to_call = lambda x: f'/api/v1/paths/messages/{x}'

        self.message_id = "65b17831cfa4dd89737beb2c"

    @mock.patch("pymongo.collection.Collection.find_one")
    def test_get_messages_empty_result(self, mock_find_one):
        mock_find_one.return_value = load_message(
            filename="test_get_message_by_id.json"
        )

        path = self.url_to_call(self.message_id)
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)
