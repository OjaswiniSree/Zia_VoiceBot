import datetime
import pyttsx3

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning Boss")
    elif hour>12 and hour<=18:
        speak("Good afternoon Boss")
    else:
        speak("Good Evening Boss")
    speak("Please tell me, How can i help you?")
    