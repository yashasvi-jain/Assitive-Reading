import sys
sys.path.insert(0, '../src')

import unittest
from catch_mistake import CatchMistake

class TestCatchMistake(unittest.TestCase):

    def test_read_correctly(self):
        test = ['i', 'am', 'a', 'student']
        valid = ['i', 'am', 'a', 'student']
        CM = CatchMistake(test, valid)
        self.assertTrue(CM.catch())

    def test_list_of_same_lenght_but_one_word_read_incorrectlty(self):
        test = ['i', 'am', 'a', 'teacher']
        valid = ['i', 'am', 'a', 'student']
        CM = CatchMistake(test, valid)
        self.assertFalse(CM.catch())


if __name__ == '__main__':
    unittest.main()