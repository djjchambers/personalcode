import pytest
from class_exercise_bonanza import *

class TestNumToRom(unittest.TestCase):

    def test_num_to_roman_convert(self, num):
        num_to_roman_convert('9')
        self.assertEqual('9', 'IX')

if __name__ == '__main__':
    unittest.main()