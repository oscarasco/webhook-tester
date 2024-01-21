import uuid
from unittest import TestCase, mock

from fastapi.testclient import TestClient

from main import app


class TestPostMessage(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app=app)
        self.url_builder = lambda x: f'/api/v1/{x}'

    @mock.patch("pymongo.collection.Collection.insert_one")
    def test_post_message_default_parameters(self, mock_insert_one):

        path = self.url_builder(str(uuid.uuid4()))
        response = self.client.post(path, json={})
        self.assertEqual(204, response.status_code)

    @mock.patch("pymongo.collection.Collection.insert_one")
    def test_post_message_default_status_code_200(self, mock_insert_one):

        params = "/?responseStatusCode=200"
        path = self.url_builder(str(uuid.uuid4())+params)
        response = self.client.post(path, json={})
        self.assertEqual(200, response.status_code)

    @mock.patch("pymongo.collection.Collection.insert_one")
    def test_post_message_default_status_code_400(self, mock_insert_one):

        params = "/?responseStatusCode=400"
        path = self.url_builder(str(uuid.uuid4())+params)
        response = self.client.post(path, json={})
        self.assertEqual(400, response.status_code)

    @mock.patch("pymongo.collection.Collection.insert_one")
    def test_post_message_default_status_code_500(self, mock_insert_one):

        params = "/?responseStatusCode=500"
        path = self.url_builder(str(uuid.uuid4())+params)
        response = self.client.post(path, json={})
        self.assertEqual(500, response.status_code)
