from src.text_processing import TextProcessing
from src.speech_recognition import SpeechRecognition

def main(paragraph: str):
  # Create instances of classes
  textProcessor = TextProcessing()
  speechRecognizer = SpeechRecognition()

  # Tokenize paragraph into sentences
  sentences = textProcessor.sentence_tokenizer(paragraph)

  # Begin the driver function for the given paragraph
  driver(sentences)

def driver(sentences):
  for sentence in sentences:
    pass

if __name__ == "__main__":
  pass