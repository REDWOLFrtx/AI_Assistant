import pyttsx3
def text_to_speech(text):
    eng=pyttsx3.init()
    rate=eng.getProperty('rate')
    eng.setProperty('rate', rate-30)
    eng.say(text)
    eng.runAndWait()
    