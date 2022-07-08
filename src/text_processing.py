# import nltk
# nltk.download('punkt')

from nltk import sent_tokenize as st
#from nltk import word_tokenize as wt
from nltk.tokenize import WordPunctTokenizer
import string
from num2words import num2words

class TextProcessing:
  def __init__(self):
    self._punctuations = string.punctuation
    self._wpt = WordPunctTokenizer()

  # To break a paragarph into sentences
  def sentence_tokenizer(self, text):
    tokenzied_paragraph = st(text, language='english')
    return tokenzied_paragraph

  # To break sentences into words
  def word_tokenizer(self, sentence):
    tokenized_sentence = self._wpt.tokenize(sentence)

    for i in range( len(tokenized_sentence) ):
      word = tokenized_sentence[i]

      if word.isdigit():
        tokenized_sentence.remove(word)
        tokenized_number = self._wpt.tokenize(num2words(word))
        for n in range( len(tokenized_number) ):
          tokenized_sentence.insert( i+n, tokenized_number[n])
        if i+1 != len(tokenized_sentence):
          i = i + len(tokenized_number)

      if (word == '\''):
        tokenized_sentence[i-1] += '\'' + tokenized_sentence[i+1]
        tokenized_sentence.pop(i)
        tokenized_sentence.pop(i)

      if i+1 == len(tokenized_sentence): break

    x = 0
    while (x < len(tokenized_sentence)):
      if tokenized_sentence[x] in self._punctuations:
        tokenized_sentence.remove(tokenized_sentence[x])
      else:
        x += 1

    tokenized_sentence = list(map(lambda x: x.lower(), tokenized_sentence))

    return tokenized_sentence