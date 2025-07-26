import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musicLibrary
import requests
import requests
import os
from dotenv import load_dotenv

load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "1587fc07b60c4edf8aca0213691017c1"



def speak(text):
    import pyttsx3
    print("Speaking:", text)
    engine = pyttsx3.init('sapi5')  # reinitialize each time
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def ask_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # Fast & smart. You can use "llama3-70b-8192" too
        "messages": [
            {"role": "system", "content": "You are Jarvis, a smart helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error talking to Groq: {e}"

def processCommand(c):
        
        if "open google" in c.lower():
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in c.lower():
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open facebook" in c.lower():
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
            
        elif c.lower().startswith ("play"):
            song = c.lower().split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
        elif "news" in c.lower():
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apikey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles[:5]:
                    speak(article['title'])

        else:
            # Send unknown command to Groq
            speak("Let me think about that.")
            answer = ask_groq(c)
            print("Groq:", answer)
            speak(answer)


if __name__ == "__main__":
    speak("initializing jarvis.")

    while True:
        r = sr.Recognizer()
        

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2,phrase_time_limit=4)
                word = r.recognize_google(audio)
                if(word.lower() == "jarvis"):
                    
                    speak("yes sir.")

                    #listen for command 
                    with sr.Microphone() as source:
                        print("Active...")
                        audio = r.listen(source  )  
                        command = r.recognize_google(audio)

                        
                        processCommand(command)


        except sr.UnknownValueError:
            print("Sphinx could not understand the audio")
        except Exception as e:
            print("Error; {0}".format(e))