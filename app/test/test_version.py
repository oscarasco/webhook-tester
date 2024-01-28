from unittest import TestCase

from version import webhook_tester_version


class TestVersion(TestCase):

    def test_version(self):
        version = webhook_tester_version.version
        self.assertEqual("10.11.12", version)
