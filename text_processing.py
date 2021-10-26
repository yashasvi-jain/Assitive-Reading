from nltk.tokenize import sent_tokenize

class TextProcessing:

  def text_processing(self, text: str) -> str:
    tokenzied_paragraph = sent_tokenize(text, language='english')
    return tokenzied_paragraph