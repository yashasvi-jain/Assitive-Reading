import sys
sys.path.insert(0, '../src')

import unittest
from text_processing import TextProcessing

class TestTextProcessing(unittest.TestCase):

    def test_sentence_tokenizer_for_empty_string(self):
        result = TextProcessing.sentence_tokenizer(self, '')
        self.assertEqual(result, [])
        print('Success')

if __name__ == '__main__':
    unittest.main()