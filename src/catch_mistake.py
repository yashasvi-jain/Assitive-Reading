import sys
import Levenshtein as lev
import scipy.special as sp
sys.path.insert(0, '../')

#from db.database_manager import DatabaseManager
from db.in_memory_database import InMemoryDatabase
from helpers.utils import Utils

class CatchMistake:
  def __init__(self, transcribed_audio: list, valid_words: list):
    self._transcribed_audio = transcribed_audio
    self._valid_words = valid_words
    self._flag = 0
    self._words_were_missed = len(self._transcribed_audio) < len(self._valid_words)
    self._words_were_added = len(self._transcribed_audio) > len(self._valid_words)
    #self._DM = DatabaseManager()
    self._IDM = InMemoryDatabase()
    self._Utils = Utils()

  def catch(self):

    self._IDM.createTables()
    # tp = transcribed audio pointer & vp = valid words pointer
    tp, vp = 0, 0
    wrong = []
    added = []
    missed = []
    missed_index = []
    correct = []
    placement  = []

    # while True:
    #   if tp == len(self._transcribed_audio) and vp < len(self._valid_words):
    #     for word in self._valid_words[vp:]:
    #       missed.append(word)
    #     break
    #   elif vp == len(self._valid_words) and tp < len(self._transcribed_audio):
    #     for word in self._transcribed_audio[tp:]:
    #       added.append(word)
    #     break
    #   elif vp == len(self._valid_words) and tp == len(self._transcribed_audio):
    #     break

    #   correct_word = self._valid_words[vp]
    #   if self._Utils.word_frequency(correct_word, self._transcribed_audio[tp:]) == 0:
    #     if self._Utils.word_frequency(self._transcribed_audio[tp], self._valid_words[vp:]) == 0:
    #       wrong_word = self._transcribed_audio[tp]
    #       correct_word_count = self._Utils.word_frequency(correct_word, self._valid_words)
    #       dist = []
    #       for word in self._transcribed_audio[tp:]:
    #         if word not in self._valid_words[vp:]:
    #           dist.append(lev.distance(correct_word, word))
    #       print(sp.softmax(dist))
    #       wrong.append(correct_word)
    #       self._IDM.addToWrongWords(correct_word, wrong_word, correct_word_count)

    #       tp += 1
    #       pass
    #       # The word was read incorrectly
    #     else:
    #       missed.append(correct_word)
    #       # The word has been missed
    #       pass
    #     vp += 1

    #     pass
    #   else:
    #     if self._transcribed_audio[tp] == self._valid_words[vp]:
    #       # Read correctly
    #       correct.append(correct_word)
    #       tp += 1
    #       vp += 1
    #     else:
    #       if self._Utils.word_frequency(self._transcribed_audio[tp], self._valid_words[vp+1:]) > 0:
    #         # The word was added later
    #         # added.append(correct_word)
    #         placement.append(correct_word)
    #         temp = self._transcribed_audio[tp:].copy()
    #         temp.remove(correct_word)
    #         self._transcribed_audio = self._transcribed_audio[:tp] + temp
    #         vp += 1
    #         pass
    #       else:
    #         added.append(self._transcribed_audio[tp])
    #         temp = self._transcribed_audio[tp:].copy()
    #         temp.remove(self._transcribed_audio[tp])
    #         self._transcribed_audio = self._transcribed_audio[:tp] + temp

    for i in range(len(self._valid_words)):
      if self._valid_words[i] not in self._transcribed_audio:
        missed.append(self._valid_words[i])
        missed_index.append(i)

    for word in self._transcribed_audio:
      if word not in self._valid_words:
        added.append(word)

    print('correct:', correct)
    print('added:', added)
    print('missed:', missed)
    print('wrong:', wrong)
    print('placement', placement)

    self._IDM.closeConnection()

    if (wrong or added or missed or placement): return False
    return True

if __name__ == '__main__':
  # test = 'bhos i good good stud some some a were student'.split()
  # valid = 'i am a was good great student'.split()

  # test = 'i am a student at a school'.split()
  # valid = 'i am a teacher at a university'.split()

  test = 'the actor is charming accusative case marker the audience'.split()
  valid = 'the actor charmed accusative case marker the audience'.split()

  CatchMistake(test, valid).catch()
  pass