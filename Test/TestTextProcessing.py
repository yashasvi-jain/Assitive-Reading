import sys
sys.path.insert(0, '../src')

import unittest
from text_processing import TextProcessing

class TestTextProcessing(unittest.TestCase):

    def setUp(self):
        self._TextProcessing = TextProcessing()

    def test_sentence_tokenizer_for_empty_string(self):
        result = self._TextProcessing.sentence_tokenizer('')
        self.assertEqual(result, [])

    def test_word_tokenizer_for_a_sentence(self):
        sentence = 'Hello World!'
        result = self._TextProcessing.word_tokenizer(sentence)
        self.assertEqual(result, ['hello', 'world'])

    def test_word_tokenizer_for_a_sentence_with_numbers(self):
        sentence1 = 'Hello World 42!'
        result = self._TextProcessing.word_tokenizer(sentence1)
        self.assertEqual(result, ['hello', 'world', 'forty', 'two'])

        sentence2 = '10001'
        result = self._TextProcessing.word_tokenizer(sentence2)
        self.assertEqual(result, ['ten', 'thousand', 'and', 'one'])

        sentence3 = 'I got 99 problems and money ain\'t one'
        result = self._TextProcessing.word_tokenizer(sentence3)
        self.assertEqual(result, ['i', 'got', 'ninety', 'nine', 'problems', 'and', 'money', 'ain\'t', 'one'])

if __name__ == '__main__':
    unittest.main()