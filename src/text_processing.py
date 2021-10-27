from nltk import sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
import string

class TextProcessing:
  def __init__(self):
    self._punctuations = string.punctuation

  def sentence_tokenizer(self, text):
    tokenzied_paragraph = sent_tokenize(text, language='english')
    return tokenzied_paragraph

  def word_tokenizer(self, sentence):
    sentence = sentence.lower()
    tokenized_sentence = TreebankWordTokenizer().tokenize(sentence)

    for punctuation in self._punctuations:
      if punctuation in tokenized_sentence:
        tokenized_sentence.remove(punctuation)

    return tokenized_sentence