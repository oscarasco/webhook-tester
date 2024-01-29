from unittest import TestCase

from core.services.db_service.query_builder import MongoQueryBuilder


class TestQueryBuilder(TestCase):

    def test_status_code(self):

        builder = MongoQueryBuilder(status_code=200)
        query = builder()

        expected = {"response_status_code": 200}
        self.assertEqual(expected, query)

    def test_server_timeout(self):

        builder = MongoQueryBuilder(server_timeout=10)
        query = builder()

        expected = {"server_timeout": 10}
        self.assertEqual(expected, query)
