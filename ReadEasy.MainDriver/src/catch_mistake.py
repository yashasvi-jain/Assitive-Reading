import sys
import requests
sys.path.insert(0, '../')

from db.database_manager import DatabaseManager
from helpers.utils import Utils
from helpers.format_mistakes_data import FormatMistakesData

class CatchMistake:
  def __init__(self, transcribed_audio: list, valid_words: list):
    self._transcribed_audio = transcribed_audio
    self._valid_words = valid_words
    self._flag = 0
    self._words_were_missed = len(self._transcribed_audio) < len(self._valid_words)
    self._words_were_added = len(self._transcribed_audio) > len(self._valid_words)
    #self._DM = DatabaseManager('../db/AssistiveReading.db')
    self._Utils = Utils()

  def catch(self):
    audio = self._transcribed_audio
    valid = self._valid_words
    word_frequency = self._Utils.word_frequency
    sentece_similarity = self._Utils.sentence_similarity
    word_remover = self._Utils.remove_word_from_sentence
    temp_data =  FormatMistakesData()

    # tp = transcribed audio pointer & vp = valid words pointer
    tp, vp = 0, 0
    wrong = []
    added = []
    missed = []
    correct = []
    placement  = []

    while True:
      if tp == len(audio) and vp < len(valid):
        for word in valid[vp:]:
          missed.append(word)
        break
      elif vp == len(valid) and tp < len(audio):
        for word in audio[tp:]:
          added.append(word)
        break
      elif vp == len(valid) and tp == len(audio):
        break

      correct_word = valid[vp]
      if correct_word not in audio[tp:]:
        word_in_audio = audio[tp]

        if word_in_audio not in valid:
          # Could be an insertion or a replacement

          # SIMILARITY CHECK
          better_replacement = False
          temp = self._valid_words.copy()
          temp[vp] = word_in_audio
          temp = ' '.join(temp)
          similarity = sentece_similarity(temp, ' '.join(self._valid_words))

          for word in audio[tp+1:]:
            temp = valid.copy()
            temp[vp] = word
            temp = ' '.join(temp)
            sim = sentece_similarity(temp, ' '.join(self._valid_words))
            if sim > similarity:
              better_replacement = True
              break

          if better_replacement:
            # The word has been added
            # REMOVE added.append(word_in_audio)
            temp_data.catch_insertions(word_in_audio)
            audio = word_remover(audio, tp)

          else:
            # The word has been replaced
            # REMOVE wrong.append(word_in_audio)
            wrong_word_occourence = word_frequency(word_in_audio, valid)
            temp_data.catch_replacements(word_in_audio, vp)
            # REMOVE tempDB.add_to_replacements(correct_word, word_in_audio, wrong_word_occourence)
            tp += 1
            vp += 1
        else:
          # The word has been missed
          # REMOVE missed.append(correct_word)
          temp_data.catch_omission(correct_word, vp)
          vp += 1
      else:
        if audio[tp] == valid[vp]:
          # Read correctly
          # REMOVE correct.append(correct_word)
          tp += 1
          vp += 1
        else:
          if word_frequency(audio[tp], valid[vp+1:]) > 0:
            # Placement error
            # REMOVE placement.append(correct_word)
            temp_data.catch_misplacement(correct_word)
            temp = audio[tp:].copy()
            temp.remove(correct_word)
            audio = audio[:tp] + temp
            vp += 1
            pass
          else:
            # The word has been added
            # REMOVE added.append(audio[tp])
            temp_data.catch_insertions(audio[tp])
            audio = word_remover(audio, tp)

    json_temp_data = temp_data.toJSONString()
    #res = requests.post('http://localhost:4000/send?data={}'.format(json_temp_data))
    # if (wrong or added or missed or placement): return False
    # return True

if __name__ == '__main__':
  pass