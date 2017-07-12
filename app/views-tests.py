import unittest
from app import app


class Test_views(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_homepage(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200, msg='Home page did not load')

    def test_signup_page(self):
        result = self.app.get('/signup')
        self.assertEqual(result.status_code, 200, msg='Sign up page did not load')

    def test_signin_page(self):
        result = self.app.get('/signin')
        self.assertEqual(result.status_code, 200, msg='Sign in page did not load')
