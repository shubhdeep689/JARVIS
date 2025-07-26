# 🎙️ Jarvis - AI Voice Assistant (Python + Groq)

Jarvis is a personal AI voice assistant built using Python. It can recognize voice commands and respond using text-to-speech. This project uses the **Groq API** for handling AI requests and provides a base for building more advanced voice-controlled applications.

---

## 🚀 Features

- 🎧 Voice recognition using `SpeechRecognition`
- 🧠 Smart replies using Groq API (LLMs like Mixtral, LLaMA, Gemma, etc.)
- 🔊 Text-to-speech using `pyttsx3`
- 🌐 Can open websites, answer questions, and interact like a smart assistant
- 🧪 Easily extendable with custom commands

---

## 🛠️ Tech Stack

- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [Groq API](https://console.groq.com)
- dotenv (`python-dotenv` for storing API key securely)

---

## 🔐 API Key Setup

1. Sign up on [https://console.groq.com](https://console.groq.com)
2. Generate your API key
3. Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
