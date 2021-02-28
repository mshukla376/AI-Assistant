import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from tkinter import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=5 and hour<20:
        speak("evening")
    else:
        speak("good night")
    speak("how may i help you sir")


def command():
    #it takes microphones input from the user and return string output
    k= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        k.pause_threshold= 1
        audio = k.listen(source)
    try:
        print("recognizing...")
        query = k.recognize_google(audio, language='en-In')
        print("User said :",query)
    except Exception as e:
        #print(e)
        print("Say that again")
        return "None"
    return query
    
    
def main():
    wish()
    query = command()
            


    if "wikipedia" in query.lower():
        speak("searching wikipedia...")
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(results)
                
    elif "open youtube" in query.lower():
        webbrowser.open("youtube.com")
    elif query == "say my name":
        speak("Mohit Shukla")
    elif "the time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(strTime)
    elif query.lower() == "how are you":
        speak("i am fine")
                
    elif "quit" in query.lower():
        exit()
    else:
        speak(query)

def openProgram():
    #call the `main` function defined in the other file
    main()
    

MGui = Tk()
MGui.geometry('450x450')

mbutton = Button(text = "Press To Speak", command = openProgram).pack()
MGui.mainloop()