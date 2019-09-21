import unittest

class TestSomething(unittest.TestCase):
    def test_first(self):
        self.assertEqual(10, 5+5)