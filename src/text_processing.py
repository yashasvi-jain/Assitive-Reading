from nltk import sent_tokenize

class TextProcessing:

  def sentence_tokenizer(self, text):
    tokenzied_paragraph = sent_tokenize(text, language='english')
    return tokenzied_paragraph