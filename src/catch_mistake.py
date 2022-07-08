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
    self._words_were_added = len(self._transcribed_audio) > len(self._valid_words):
    self._DM = DatabaseManager()
    self._Utils = Utils()
    pass

  # def checkIfWordsWereMissed(self):
  #   i = len(self._transcribed_audio) - 1
  #   j = len(self._valid_words) - 1
  #   for

  def catch(self):
    added_words_range = set() # (start index, end index)

    if self._words_were_missed:
      pass

    elif self._words_were_added:
      for i range()

    else:
      for i in range(len(self._transcribed_audio)):
        if self._transcribed_audio[i] != self._valid_words[i]:
          this._flag = i
          correct_word = self._valid_words[i]
          wrong_word = elf._transcribed_audio[i]
          total_count = self._Utils.word_frequency(correct_word, self._valid_words)
          self._DM.addToWrongWords(correct_word, wrong_word, total_count)
