import pyttsx3
import speech_recognition as sr
import speedtest
import pyautogui
import pyjokes
import winshell
import webbrowser
import random
import requests
from bs4 import BeautifulSoup
import datetime
import os
import tkinter as tk


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "none"
    return query.lower()

# Function to change password
def change_password():
    new_pw = input("Enter the new password: ")
    with open('password.txt', 'w') as pw_file:
        pw_file.write(new_pw)
    speak("Done, Boss. Your new password is " + new_pw)

# Function to check internet speed
def check_internet_speed():
    wifi = speedtest.Speedtest()
    upload_speed = wifi.upload() / 1048576
    download_speed = wifi.download() / 1048576
    speak(f"WiFi upload speed is {upload_speed} megabits per second.")
    speak(f"WiFi download speed is {download_speed} megabits per second.")

# Function to take a screenshot
def take_screenshot():
    try:
        im = pyautogui.screenshot()
        im.save("ss.jpg")
        speak("Your screenshot is saved.")
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I couldn't capture the screenshot.")

# Function to take a photo
def take_photo():
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    speak("Smile!")
    pyautogui.press("enter")
    speak("yes it was nice")

def translate(query):
    from Translator import translategl
    query=query.replace("zia","")
    query=query.replace("translate","")
    translategl(query)

def open_news_channel():
    news_url = "https://www.thehindu.com/"  
    webbrowser.open(news_url)

def weather():
    search="query"
    url= f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temp=data.find("div",class_="BNeawe").text
    speak(f"current{search} is {temp}")

from drawing import drawing
def launch_drawing_app():
    root = tk.Tk()
    app = drawing(root)
    root.mainloop()

def handle_command(query):
    if "wake up" in query:
        speak("Hello! How can I assist you?")
        while True:
            query = take_command()

            if "goodbye" in query:
                speak("Goodbye! Have a great day.")
                break
            elif "change password" in query:
                speak("What's the new password, Boss?")
                change_password()
            elif "internet speed" in query:
                check_internet_speed()
            elif "screenshot" in query:
                take_screenshot()
            elif "take a photo" in query:
                take_photo()
            elif "translate" in query:
                translate(query)
            elif "hello" in query or "hi" in query:
                speak("Hello Boss, how are you?")
            elif "good" in query or "fine" in query:
                speak("great boss")
            elif "how are you" in query or "what about you" in query:
                speak("I am perfect Boss, thank you for counting on me")

            elif "Love you" in query or "i love you" in query:
                speak("Love you too, Boss")
            elif "change your name" in query:
                speak("what would youl ike to call me, Mamdam")
                assname=take_command()
                speak("thanks boss for nameing me")
            elif "what's your name" in query or "what is your name" in query or "how should i address you" in query or "how do we call you" in query:
                speak("you can call me")
                speak(assname)
                print("you can call me",assname)
            elif "who made you" in query or "who created you" in query:
                speak("I was created by Ojaswini.")
            elif "tell a joke" in query: 
                 
                joke = random.choice(pyjokes.get_jokes())
                speak(joke)  
 
            elif "why they created you" in query:
                speak("Thanks to Ojaswini. I exist to assist users like you and to be friendly")
            elif "What is love" in query:
                speak("Love is a profound emotion characterized by affection, connection, empathy, and care towards others.")
            elif "empty my recycle bin" in query:
                winshell.recycle_bin.empty(confirm=False,show_progress=False,sound=True)
                speak("It is accomplished")
            elif "Where is" in query:
                query=query.replace("where is","")
                location=query
                speak("you asked for")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/"+location+"")
            elif "be my girlfriend" in query:
                speak("sorry, I am not capable of forming personal relationships, including romantic ones.")
            elif "be my boyfriend" in query:
                speak("sorry, I am not capable of forming personal relationships, including romantic ones.")
            elif "i am tired" in query:
                speak("If you are tired i cam play come of your favorite melody songs, Boss")
                a=(1,2,3)
                b=random.choice(a)
                if b==1:
                    webbrowser.open("https://youtu.be/uoxY6fX2sqo?si=aHucI0S9G9ZeN3VO")      
            elif "aren't you tired" in query:
                speak("I don't experience fatigue or tiredness in the way humans do. I'm here to assist you whenever you need help or have questions") 
            elif "volume up" in query:
                from keyboard import volumeup
                speak("raising the volume, Boss")
                volumeup()
            elif "volume down" in query:
                from keyboard import volumedown
                speak("turning volume dowm, Boss")
                volumedown()
            elif "mute" in query:
                from keyboard import mute
                speak("yes boss, it's done")
                mute()

            elif "google" in query:
                from searchnow import searchGoogle
                searchGoogle(query)
            
            elif "youtube" in query:
                from searchnow import searchYoutube
                searchYoutube(query)

            elif "who is " in query or "what is the" in query:
                from searchnow import searchWikipedia
                searchWikipedia(query)
            
            elif "news" in query:
                open_news_channel()
            elif "temperature" in query:
                    weather()

            elif " what is the time" in query:
                strTime=datetime.datetime.now().strftime("%H:%M")
                speak(f"Boss, the time is {strTime}")

            elif "remember" in query:  
                rememberMessage=query.replace("remember","")
                rememberMessage=query.replace("zia","")
                speak("you told me to "+rememberMessage)
                remember=open("Remember.txt","w")
                remember.write(rememberMessage)
                remember.close() 

            elif "what is  the secret" in query:
                speak("Yes, Boss.")
                speak("Do you want me to tell?")
                if "yes" in query:
                    try:
                        with open("Remember.txt", 'r') as remember_file:
                            remembered_info = remember_file.read()
                            speak("You told me " + remembered_info)
                    except FileNotFoundError:
                        speak("Sorry, I couldn't find any remembered information.")
                elif "no" in query:
                    speak("That's okay, Boss.")
            elif "paint" in query:
                speak("yes, Boss")
                launch_drawing_app()


            elif "shutdown the system" in query:
                speak("Are you sure Boss, you want me to shutdown")
                shutdown=input("Do you wish to shutdown the computer? (yes/no)")
                if shutdown=="yes":
                    os.system("shutdown /s /t 1")
                elif shutdown=="no":
                    break
            else:
                speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    for i in range(3):
        password = input("Enter the password to open Zia: ")
        with open('password.txt', 'r') as pw_file:
            correct_pw = pw_file.read().strip()
        if password == correct_pw:
            break
        elif i == 2:
            exit()
        else:
            print('Please try again.')
    #from INTRO import play_gif
    #play_gif
    while True:
        query = take_command()
        handle_command(query)

