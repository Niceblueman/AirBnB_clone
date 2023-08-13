#!/usr/bin/python3
import unittest
import json
import pep8
import datetime

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def document_constract_test(self):
        document = State.__init__.__doc__
        self.assertGreater(len(document), 1)
        
    def doc_m_test(self):
        document = State.__doc__
        self.assertGreater(len(document), 1)

    def pep8_test(self):
        styles = pep8.StyleGuide(quiet=True).check_files(['models/state.py'])
        self.assertEqual(styles.total_errors, 0,"error or warning found.")

    def c_test(self):
        with self.subTest(msg='Att'):
            self.assertIsInstance(State.name, str)
            
        with self.subTest(msg='Inh'):
            self.assertTrue(issubclass(State, BaseModel))

    def pep8_state_test(self):
        styles = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_state.py'])
        self.assertEqual(styles.total_errors, 0,"error or warning found.")




if __name__ == '__main__':
    unittest.main()
