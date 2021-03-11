import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
