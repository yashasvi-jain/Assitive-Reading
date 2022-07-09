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
    #self._DM = DatabaseManager()
    self._Utils = Utils()

  def catch(self):

    # tp = transcribed audio pointer & vp = valid words pointer
    tp, vp = 0, 0
    wrong = []
    added = []
    missed = []
    correct = []

    while True:
      if tp == len(self._transcribed_audio) and vp < len(self._valid_words):
        for word in self._valid_words[vp:]:
          missed.append(word)
        break
      elif vp == len(self._valid_words) and tp < len(self._transcribed_audio):
        for word in self._transcribed_audio[tp:]:
          added.append(word)
        break
      elif vp == len(self._valid_words) and tp == len(self._transcribed_audio):
        break

      correct_word = self._valid_words[vp]
      if self._Utils.word_frequency(correct_word, self._transcribed_audio[tp:]) == 0:
        if self._Utils.word_frequency(self._transcribed_audio[tp], self._valid_words[vp:]) == 0:
          wrong.append(correct_word)
          tp += 1
          pass
          # The word was read incorrectly
        else:
          missed.append(correct_word)
          # The word has been missed
          pass
        vp += 1

        pass
      else:
        if self._transcribed_audio[tp] == self._valid_words[vp]:
          # Read correctly
          correct.append(correct_word)
          tp += 1
          vp += 1
        else:
          if self._Utils.word_frequency(self._transcribed_audio[tp], self._valid_words[vp+1:]) > 0:
            # The word was added later
            added.append(correct_word)
            temp = self._transcribed_audio[tp:].copy()
            temp.remove(correct_word)
            self._transcribed_audio = self._transcribed_audio[:tp] + temp
            vp += 1
            pass
          else:
            added.append(self._transcribed_audio[tp])
            temp = self._transcribed_audio[tp:].copy()
            temp.remove(self._transcribed_audio[tp])
            self._transcribed_audio = self._transcribed_audio[:tp] + temp
    # print('correct: ', correct)
    # print('added: ', added)
    # print('missed: ', missed)
    # print('wrong: ', wrong)

if __name__ == '__main__':
  # yash sid > 1 : read fist wrong and added rest: leviegh distance ~ -> true - pop all
  # or added all - pop all
  #if = 1: replacement - pop 1
  # test =  ['hello',  'student'  at drexel ]
  # valid = ['hello', am 'student' at drexel studying at drexel]

  # some one hello student
  # test =  i  some * student one hello student am drexel
  # valid = i yash am student * am drexel
  # yash am  - missed
  # one hello student - added

  # ls1 = ['hello', 'student', at drexel]
  # ls2 = ['hello', 'i', 'am', 'student' at penn]
  # test = ['hello', 'i', 'am', 'student']
  # valid = ['hello', 'i', 'am', 'student']

  # test = ['hello', 'was', 'am', 'student', 'drexel']
  # valid = ['hello', 'i', 'am', 'student']

  # test = ['hello', 'was', 'am', 'class','student']
  # valid = ['hello', 'i', 'am', 'student', 'drexel']

  # test = 'i good a student'.split()
  # valid = 'i am a was good student'.split()

  # CM = CatchMistake(test, valid)
  # CM.catch()
  pass