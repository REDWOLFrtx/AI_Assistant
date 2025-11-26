#AI_Assistant

A simple Python-based voice assistant that converts speech to text, executes basic actions, and responds using text-to-speech.
This project is designed as a lightweight and easily extensible foundation for building custom AI or voice-controlled tools.

✨ Features

🎤 Speech-to-Text using microphone input

🔊 Text-to-Speech responses

🧠 Command processing via action.py

🧩 Modular architecture — easy to add new skills

🖼️ Includes an assistant icon (assistant.png)

📂 Project Structure
AI_Assistant/
│
├── main.py             # Main entry point
├── action.py           # Command handler and action executor
├── speech_text.py      # Speech-to-text processing
├── text_speech.py      # Text-to-speech output
│
├── assistant.png       # Assistant image/icon
└── README.md           # Project documentation

🚀 Getting Started
1. Clone this repository
git clone https://github.com/REDWOLFrtx/AI_Assistant.git
cd AI_Assistant

2. Install dependencies

Make sure Python 3.8+ is installed.

Install required libraries:

pip install speechrecognition pyttsx3 pyaudio


If pyaudio fails, install it from a prebuilt wheel (Windows users especially).

3. Run the assistant
python main.py

🛠 How It Works

Listens for voice input

Converts speech to text (speech_text.py)

Matches commands (action.py)

Responds via text-to-speech (text_speech.py)

Example commands (depending on your implementation):

“Open browser”

“What is the time?”

“Hello assistant”

🔧 Adding New Commands

Commands can be customized in:

action.py


Example:

if "hello" in command:
    speak("Hello! How can I assist you today?")

📦 Dependencies

This project may use:

SpeechRecognition

Pyttsx3

PyAudio

OS / Time modules

Check the source files for full import details.

🤝 Contributing

Pull requests and improvements are welcome.
Feel free to fork the repo and enhance the assistant with new features.

📄 License

This project is open-source and free to use.
