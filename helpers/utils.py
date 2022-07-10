import re
import os
import numpy as np
import tensorflow_hub as hub
import sys

sys.path.insert(0, '../')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

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
        similarity_matrix = np.inner(embeddings_matrix, embeddings_matrix)

        return similarity_matrix[0][1:]

    def remove_word_from_sentence(self, sentence, pointer):
        temp = sentence[pointer:].copy()
        temp.remove(sentence[pointer])
        return sentence[:pointer] + temp

if __name__ == '__main__':
    pass