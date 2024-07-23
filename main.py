import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsAPI = "d0ee84894d484e16988eae068a2f2a05"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]  # Split only once
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song} in the music library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPI}")
        if r.status_code == 200:
            headlines = r.json().get("articles", [])
            if headlines:
                speak("Here are the top headlines.")
                for i, article in enumerate(headlines[:5], start=1):  # Limit to top 5 headlines
                    speak(f"Headline {i}: {article['title']}")
            else:
                speak("Sorry, I couldn't find any news articles.")
        else:
            speak(f"Failed to fetch headlines. Status code: {r.status_code}")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
