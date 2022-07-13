import re
import os
import numpy as np
import tensorflow_hub as hub
import sys

sys.path.insert(0, '../')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Utils:
    def __init__(self):
        self._embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    # Returns the frequency of a word in a list
    def word_frequency(self, word: str, text: list) -> int:
        return text.count(word)

    # Returns the frequency of a word in a string
    def word_frequency(self, word: str, text: str) -> int:
        return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), text))

    def sentence_similarity(self, sentence1, sentence2):
        """
        Creates node-embeddings of the size 2 X 512 using the google-universal-sentence-encoder.
        The similarity matirx is evaluated by calculating the inner product of the node-embeddings by itself.
        Parameters: {str, str} - first sentence, second sentence it is being compared to.
        """
        messages = [sentence1, sentence2]
        embeddings_matrix = self._embed(messages)
        similarity_matrix = np.inner(embeddings_matrix, embeddings_matrix)

        return similarity_matrix[0][1:]

    def remove_word_from_sentence(self, sentence, pointer):
        temp = sentence[pointer:].copy()
        temp.remove(sentence[pointer])
        return sentence[:pointer] + temp

if __name__ == '__main__':
    pass