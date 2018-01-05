import unittest
from VowelSquare import *


class TestVowelSquare(unittest.TestCase):

    def test_array_input(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()