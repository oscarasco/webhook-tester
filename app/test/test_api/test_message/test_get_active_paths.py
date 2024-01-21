from unittest import TestCase, mock

from fastapi.testclient import TestClient

from main import app
from mock.entity_loader import load_active_paths


class TestGetActivePaths(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app=app)
        self.url_to_call = '/api/v1/paths'

    @mock.patch("pymongo.collection.Collection.aggregate")
    def test_get_paths_one_path(self, mock_aggregate):
        mock_aggregate.return_value = load_active_paths(
            filename="test_active_path_one_path.json"
        )

        path = self.url_to_call
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)

    @mock.patch("pymongo.collection.Collection.aggregate")
    def test_get_paths_one_path_empty_result(self, mock_aggregate):
        mock_aggregate.return_value = load_active_paths(
            filename="test_active_path_empty_pipe_result.json"
        )

        path = self.url_to_call
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)

    @mock.patch("pymongo.collection.Collection.aggregate")
    def test_get_paths_multiple_paths(self, mock_aggregate):
        mock_aggregate.return_value = load_active_paths(
            filename="test_active_path_multiple_paths.json"
        )

        path = self.url_to_call
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)
