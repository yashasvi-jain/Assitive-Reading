import speech_recognition as sr

class SpeechRecognition:
  def __init__(self):
    self._r = sr.Recognizer()
    self._m = sr.Microphone(device_index=1)

  def transcribe(self):
    # for index, name in enumerate(self._m.list_microphone_names()):
    #   print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    while True:
      with self._m as source:
        self._r.adjust_for_ambient_noise(source)
      print(" ")
      print("Say the given statement!")
      with self._m as source:
        audio = self._r.listen(source)
        print()
      try:
        recognized_audio = self._r.recognize_google(audio)
        print()
        return str(recognized_audio)

      except sr.UnknownValueError:
        print("Oops! Didn't catch that")
      except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service: ", e)
      except:
        print('error transcribe')