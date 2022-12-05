import unittest

class TestNothing(unittest.TestCase):

    def test_savings_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')