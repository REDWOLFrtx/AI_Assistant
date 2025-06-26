import speech_recognition as sr

def speech_to_text():
    re=sr.Recognizer()
    with sr.Microphone() as source:
        audio = re.listen(source)
    try:
        voice_data = ""
        voice_data = re.recognize_google(audio, language='en-US')
        return voice_data
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")