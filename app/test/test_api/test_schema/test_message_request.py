from unittest import TestCase

from api.schema import MessageRequest


class TestMessageRequest(TestCase):

    def setUp(self) -> None:

        self.to_validate = {
            "customerCreatedRequestAt": "2024-01-27T17:54:51.673Z",
            "additionalProp1": 1234
        }

    def test_validate_message_with_payload(self):

        message_request = MessageRequest.model_validate(self.to_validate)
        self.assertIsInstance(message_request, MessageRequest)
