import sys
sys.path.insert(0, '../')

from db.database_manager import DatabaseManager
from helpers.utils import Utils

class CatchMistake:
  def __init__(self, transcribed_audio: list, valid_words: list):
    self._transcribed_audio = transcribed_audio
    self._valid_words = valid_words
    self._flag = 0
    self._words_were_missed = len(self._transcribed_audio) < len(self._valid_words)
    self._words_were_added = len(self._transcribed_audio) > len(self._valid_words)
    self._DM = DatabaseManager()
    self._Utils = Utils()

  def catch(self):

    if self._words_were_missed:
      words_missed = []
      words_missed_index = []
      for valid_word in self._valid_words:
        if valid_word not in self._transcribed_audio:
          words_missed.append(valid_word)
          words_missed_index.append(self._valid_words.index(valid_word))
      # ADD DB STROE COMMAND

    elif self._words_were_added:
      words_added = self._transcribed_audio.copy()
      for word in self._transcribed_audio:
        if word in self._valid_words:
          words_added.remove(word)
      # ADD DB STROE COMMAND

    else:
      for i in range(len(self._transcribed_audio)):
        if self._transcribed_audio[i] != self._valid_words[i]:
          self._flag = i
          correct_word = self._valid_words[i]
          wrong_word = self._transcribed_audio[i]
          total_count = self._Utils.word_frequency(correct_word, self._valid_words)

          # Insert/Update row in WrongWords Table
          self._DM.addToWrongWords(correct_word, wrong_word, total_count)

if __name__ == '__main__':
  # ls1 = ['hello', 'i', 'am', 'student']
  # ls2 = ['hello', 'i', 'am', 'teacher']

  # CM = CatchMistake(ls1, ls2)
  # CM.catch()
  pass