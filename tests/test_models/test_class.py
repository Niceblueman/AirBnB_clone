#!/usr/bin/python3
import inspect
import unittest
import pep8
class TestClassDocumentation():
    def __init__(self, tests, _class):
        self.tests = tests
        self.name = _class
        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def document(self):
        with self.tests.subTest(msg='Test method'):
            for f in self.functions:
                with self.tests.subTest(msg='Document  {}'.format(f[0])):
                    document = f[1].__doc__
                    self.tests.assertGreaterEqual(len(document), 1)

        with self.tests.subTest(msg='Test class'):
            document = self.name.__doc__
            self.tests.assertGreaterEqual(len(document), 1)

    def pep8(self, files):
        styles = pep8.StyleGuide(quiet=True).check_files(files)
        self.tests.assertEqual(styles.total_errors, 0,'error or warning found."')

if __name__ == '__main__':
    unittest.main()