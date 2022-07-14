from src.text_processing import TextProcessing
from src.speech_recognition import SpeechRecognition
from src.catch_mistake import CatchMistake
from sockets.socket_manager import SocketManager

# Create instances of classes
textProcessor = TextProcessing()
speechRecognizer = SpeechRecognition()

def main(paragraph: str):
  # Tokenize paragraph into sentences
  sentences = textProcessor.sentence_tokenizer(paragraph)

  # Begin the driver function for the given paragraph
  driver(sentences)

def driver(sentences):

  for sentence in sentences:
    recognized_audio = speechRecognizer.transcribe()
    tokenized_sentence = textProcessor.word_tokenizer(sentence)
    mistakeCatcher = CatchMistake(recognized_audio, tokenized_sentence)
    result = mistakeCatcher.catch()

    if not result :
      pass

if __name__ == "__main__":
  SocketManager()
  pass