from unittest import TestCase, mock

from fastapi.testclient import TestClient

from main import app
from mock.entity_loader import load_messages


class TestGetMessages(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app=app)
        self.url_to_call = '/api/v1/paths/messages'

    @mock.patch("pymongo.collection.Collection.find")
    @mock.patch("pymongo.cursor.Cursor.sort")
    def test_get_messages_empty_result(self, mock_find, mock_sort):
        mock_find.return_value = load_messages(
            filename="test_messages_empty_find_result.json"
        )

        path = self.url_to_call
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)

    @mock.patch("pymongo.collection.Collection.find")
    @mock.patch("pymongo.cursor.Cursor.sort")
    def test_get_messages_multiple_messages(self, mock_find, mock_sort):
        mock_find.return_value = load_messages(
            filename="test_messages_find_multiple_messages.json"
        )

        path = self.url_to_call
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)


class TestGetMessageFilteredPaths(TestCase):

    def setUp(self) -> None:

        self.client = TestClient(app=app)
        self.url_to_call = \
            'http://localhost:8000/api/v1/paths/messages?maxItems=100&' \
            'pathsToInclude=3fa85f64-5717-4562-b3fc-2c963f66afa6,' \
            '%203fa85f64-5717-4562-b3fc-2c963f66afa7'

    @mock.patch("pymongo.collection.Collection.find")
    @mock.patch("pymongo.cursor.Cursor.sort")
    def test_get_messages_with_filtered_paths(self, mock_find, mock_sort):

        response = self.client.get(url=self.url_to_call)
        self.assertEqual(200, response.status_code)
