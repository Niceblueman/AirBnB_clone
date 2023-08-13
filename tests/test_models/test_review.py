#!/usr/bin/python3
import unittest
import json
import pep8
import datetime

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def doc_m_test(self):
        document = Review.__doc__
        self.assertGreater(len(document), 1)

    def document_constract_test(self):
        document = Review.__init__.__doc__
        self.assertGreater(len(document), 1)

    def pep8_test(self):
        styles = pep8.StyleGuide(quiet=True).check_files(['models/review.py'])
        self.assertEqual(styles.total_errors, 0,"error or warning found.")
        
    def c_test(self):
        with self.subTest(msg='Att'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)
            
        with self.subTest(msg='Inh'):
            self.assertTrue(issubclass(Review, BaseModel))
    def pep8_reviem_test(self):
        styles = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_review.py'])
        self.assertEqual(styles.total_errors, 0,"error or warning found.")


if __name__ == '__main__':
    unittest.main()
