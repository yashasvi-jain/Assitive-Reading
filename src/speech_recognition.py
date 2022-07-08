import speech_recognition as sr

class SpeechRecognition():
  def __init__():
    self._r = sr.Recognizer() 
    slef._m = sr.Microphone()

  def transcribe():
    with self._m as source: 
      self._r.adjust_for_ambient_noise(source)
    with self._m as source:
      audio = self._r.listen(source)
    try:
      recognized_audio = self._r.recognize_google(audio)
      return recognized_audio

    except sr.UnknownValueError:
      print("Oops! Didn't catch that")
    except sr.RequestError as e:
      print("Uh oh! Couldn't request results from Google Speech Recognition service: {0}".format(e))
        