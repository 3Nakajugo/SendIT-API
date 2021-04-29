import json
import unittest
from app import app
from app.auth import auth_model, auth_view, auth_controller


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.user = {
            "email": "edna@gmail.com",
            "password": "ednanakajugo"
        }

    def tearDown(self):
        auth_model.users.clear()

    def test_create_user_success(self):
        res = self.client.post(
            '/api/v1/users', content_type='application/json',
            data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)

    def test_create_user_with_invalid_email_fails(self):
        payload = {
            "email": "ednagmail.com",
            "password": "ednanakajugo"
        }
        res = self.client.post(
            '/api/v1/users', content_type='application/json',
            data=json.dumps(payload))
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res_data["message"], "Invalid email")

    def test_create_user_with_no_email_fails(self):
        payload = {
            "email": "",
            "password": "ednanakajugo"
        }
        res = self.client.post(
            '/api/v1/users', content_type='application/json',
            data=json.dumps(payload))
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res_data["message"], "email is required")

    def test_create_user_with_invalid_password_fails(self):
        payload = {
            "email": "edna@gmail.com",
            "password": "naka"
        }
        res = self.client.post(
            '/api/v1/users', content_type='application/json',
            data=json.dumps(payload))
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res_data["message"],
                         "password should be longer than 8 characters")

    def test_create_user_with_no_password_fails(self):
        payload = {
            "email": "edna@gmail.com",
            "password": ""
        }
        res = self.client.post(
            '/api/v1/users', content_type='application/json',
            data=json.dumps(payload))
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res_data["message"], "password is required")

    def test_login_user_success(self):
        res = self.client.post(
            '/api/v1/users', content_type='application/json',
            data=json.dumps(self.user))
        login_res = self.client.post(
            '/api/v1/users/login', content_type='application/json',
            data=json.dumps(self.user))

        res_data = json.loads(login_res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(login_res.status_code, 200)
        self.assertEqual(res_data["message"], "Login successful")

    def test_login_user_with_wrong_credentials_fails(self):
        login_res = self.client.post(
            '/api/v1/users/login', content_type='application/json',
            data=json.dumps(self.user))
        self.assertEqual(login_res.status_code, 404)
