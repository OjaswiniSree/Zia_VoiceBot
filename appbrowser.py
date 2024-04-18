import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp={"commandprompt":"cmd","paint":"paint","word":"windword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt","Camera":"camera","whatsapp":"whatsapp"}

def openappweb(query):
    speak("YES Boss")
    if ".com" or ".co.in" or ".org" in query:
        query = query.replace("open","")
        query = query.replace("zia","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing boss")
    if "one tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("closed, boss")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All are closed, Boss")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All are closed, Boss")
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")