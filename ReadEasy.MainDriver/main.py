from src.text_processing import TextProcessing
from src.speech_recognition import SpeechRecognition
from src.catch_mistake import CatchMistake
from helpers.utils import Utils

class Main():
  def __init__(self) -> None:
    self._textProcessor = TextProcessing()
    self._speechRecognizer = SpeechRecognition()
    self._utils = Utils()
    self._catcher = CatchMistake

  def main(self, sio, paragraph: str):
    # Tokenize paragraph into sentences
    sentences = self._textProcessor.sentence_tokenizer(paragraph)
    i = 0
    while i < len(sentences):
      sentence = sentences[i]
      print('Sentence:', sentence, end='\n')
      recognized_audio = self._speechRecognizer.transcribe()
      print('rec:', recognized_audio, end='\n')
      tokenized_audio = self._textProcessor.word_tokenizer(recognized_audio)
      tokenized_sentence = self._textProcessor.word_tokenizer(sentence)
      json_temp_data, read_correctly = self._catcher(tokenized_audio, tokenized_sentence).catch()
      sio.emit('transfer', json_temp_data, namespace='/main')
      if not read_correctly:
        continue
      print('Read Correctly')
      i += 1
    print('Para finished')

if __name__ == "__main__":
  from sockets.socket_manager import SocketManager
  socket = SocketManager()
  socket.init_main_socket()