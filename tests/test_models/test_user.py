#!/usr/bin/python3
import unittest
import json
import pep8
import datetime

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def doc_m_test(self):
        document = User.__doc__
        self.assertGreater(len(document), 1)

    def pep8_test(self):
        styles = pep8.StyleGuide(quiet=True).check_files(['models/user.py'])
        self.assertEqual(styles.total_errors, 0,"error or warning found.")

    def pep8_user_test(self):
        styles = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_user.py'])
        self.assertEqual(styles.total_errors, 0,"error or warning found.")

    def test_doc_constructor(self):
        document = User.__init__.__doc__
        self.assertGreater(len(document), 1)

    def c_test(self):
        with self.subTest(msg='Att'):
            self.assertIsInstance(User.last_name, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.email, str)


        with self.subTest(msg='Inh'):
            self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
