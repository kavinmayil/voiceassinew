import pyttsx3
import pyWhatkit as kit
import datetime
import speech_recognition as sr
import pyaudio
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=5,phrase_time_limit=10)
        
        try:
            print("Recoginizing")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}")
            
        except Exception as e:
            speak("say that againplease")
            return "none"
        return query
    
def wish():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am shri,please tell me how can i help you")
    
if__name__=="__main__":
    wish()
    while True:
        query=takecommand().lower()
        
    if"open notepad" in query:
        path="C:\\Windows\\System32\\notepad.exe"
        os.startfile(path)
    elif"open cmd"in query:
        path="C:\\Windows\\System32\\cmd.exe"
        os.starfile(path)
    elif"play vedio on youtube" in query:
        speak("which vedio i will play for you")
        vedioquery=takecommand()
        kit.playonyt(vedioquery)
    elif"open google chrome"in query:
        speak("what can i search for you")
        searchquery=takecommand()
        kit.playonyt(searchquery)
