import re
import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

import sys
sys.path.insert(0, '../')

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

class Utils:
    def __init__(self):
        pass

    # Return the frequency of a word in a string or a list
    def word_frequency(self, word: str, text) -> int:
        if isinstance(text, str):
            return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), text))
        return text.count(word)

    def sentence_similarity(self, sentence1, sentence2):
        messages = [sentence1, sentence2]

        embeddings_matrix = embed(messages)
        #np.inner(embeddings_matrix, embeddings_matrix)
        print(np.inner(embeddings_matrix, embeddings_matrix))

if __name__ == '__main__':
    u = Utils()
    u.sentence_similarity('Sid is gay', 'Sid was gay')