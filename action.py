import speech_text
import text_speech
from datetime import datetime
import webbrowser
import requests
import json

def action(data):


    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "google/gemma-3n-e4b-it:free",
        "messages": [
        {
            "role": "user",
            "content":  data+"Just give me a simple answer which i can convert to speech. Do not include any special characters and greetings in your response and limit your response to 20 words."
        }
        ],
    })
    )
    if "time now" in data:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        text_speech.text_to_speech(f"The current time is {current_time}.")
        return f"The current time is {current_time}."
    elif "open youtube" in data:
        text_speech.text_to_speech("Opening YouTube for you.")
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube for you."
    elif "open google" in data:
        text_speech.text_to_speech("Opening Google for you.")
        webbrowser.open("https://www.google.com")
        return "Opening Google for you."
    elif "play music" in data:
        text_speech.text_to_speech("Playing music for you.")
        webbrowser.open("https://www.youtube.com/results?search_query=music")
        return "Playing music for you."
    elif response.status_code == 200:
        response_data = response.json()
        data = response_data['choices'][0]['message']['content']
        data = data.strip() 
        text_speech.text_to_speech(data)
        return data
    else:
        text_speech.text_to_speech("Sorry, I didn't understand that.")
        return "Sorry, I didn't understand that."


# def action():
#     data = speech_text.speech_to_text()
#     data = data.lower()  # Normalize input to lowercase for easier matching
#     if "what is your name" in data:
#         text_speech.text_to_speech("MY name is AI assistant.")
#         return "MY name is AI assistant."
#     elif "hello" in data:
#         text_speech.text_to_speech("Hello, how can I assist you today?")
#         return "Hello, how can I assist you today?"
#     elif "how are you" in data:
#         text_speech.text_to_speech("I am just a program, but thank you for asking!")
#         return "I am just a program, but thank you for asking!"
#     elif "what can you do" in data:
#         text_speech.text_to_speech("I can assist you with various tasks, answer questions, and provide information.")
#         return "I can assist you with various tasks, answer questions, and provide information."
#     elif "tell me a joke" in data:
#         text_speech.text_to_speech("Why did the computer go to the doctor? Because it had a virus!")
#         return "Why did the computer go to the doctor? Because it had a virus!"
#     elif "time now" in data:
#         now = datetime.now()
#         current_time = now.strftime("%H:%M")
#         text_speech.text_to_speech(f"The current time is {current_time}.")
#         return f"The current time is {current_time}."
#     elif "open youtube" in data:
#         text_speech.text_to_speech("Opening YouTube for you.")
#         webbrowser.open("https://www.youtube.com")
#         return "Opening YouTube for you."
#     elif "open google" in data:
#         text_speech.text_to_speech("Opening Google for you.")
#         webbrowser.open("https://www.google.com")
#         return "Opening Google for you."
#     elif "play music" in data:
#         text_speech.text_to_speech("Playing music for you.")
#         webbrowser.open("https://www.youtube.com/results?search_query=music")
#         return "Playing music for you."
#     else:
#         text_speech.text_to_speech("Sorry, I didn't understand that.")
#         return "Sorry, I didn't understand that."
