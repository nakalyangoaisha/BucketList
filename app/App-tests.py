import unittest

from models import User
from App import App


class Test_User(unittest.TestCase):
    def setUp(self):
        self.user = User('username', 'password')

    def test_init_method(self):
        self.assertDictEqual({}, self.user.users)

    def test_validate_on_signup_function(self):
        initialdictlen = len(self.user.users)
        self.assertTrue(self.user.validate_on_signup('a', 'n'))
        self.assertFalse(self.user.validate_on_signup('a', 'p'))
        finaldictlen = len(self.user.users)
        self.assertEqual(finaldictlen - initialdictlen, 1)

    # def test_validate_on_signin_returns_false_if_user_not_registered(self):


if __name__ == '__main__':
    unittest.main()
