import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, Qt

from ast import operator
from asyncio import subprocess
from datetime import datetime
from email.message import EmailMessage
from email.mime import audio
from http import server
import ipaddress
from re import S
from socket import timeout
from time import time
from tokenize import Funny
from turtle import delay
from typing import KeysView
from unittest import result
from newsapi import NewsApiClient
from numpy import take
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import cv2
from requests import get
import pywhatkit 
import subprocess as sp
import Calculator
import requests
import openweather
import pyjokes
import sys
import pyautogui
import time
NEWS_API_KEY='12ea845f5ec1432cbbb6fc376ddacfc4'
OPENWEATHER_APP_ID='e51eef6f09d7cb8aa3a9794a7daa3992'

from jarvisGUI_new import Ui_jarvisGUI

engine=pyttsx3.init('sapi5')                    #making a Text to speech engine with the help of sapi5
voices=engine.getProperty('voices')             #getting details of current voice
engine.setProperty('voice',voices[0].id)        #changing index, changes voices. o for male and 1 for female 

#speak function
def speak(audio):
    ui.updateMovieDynamically("speaking")
    engine.say(audio)
    ui.terminalPrint(audio)
    print(audio)
    engine.runAndWait()

#wish Function with date time
def wishMe():
    ui.updateMovieDynamically("speaking")
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Sir. Please tell me how may I help you")

 #play any video from Youtube 
def play_on_youtube(video):
    pywhatkit.playonyt(video)

#search any think from google
def search_on_google(query):
    pywhatkit.search(query)

#send  whatsapp message 
def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)

#send email to anyone
def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = #WRITE YOUR EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login('EMAIL ADDRESS', 'PASSWORD')
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        ui.terminalPrint(e)
        print(e)
        return False

#open camera of computer
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

#Open calculator
def open_calculator():
    sp.run('start ms-calculator:', shell=True)

#News Function
def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
    
#Weather Function
def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

#Advice Function
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
   

class jarvisMain(QThread):
    def __init__(self):
        super(jarvisMain,self).__init__()

    def run(self):
            self.runJarvis()

    # It Takes Microphone input from the your and return string output
    def takeCommand(self):
        ui.updateMovieDynamically("listening")
        r=sr.Recognizer()                       #This class helps to recognise the audio from the user
        with sr.Microphone() as source:         # use the default microphone as the audio source
            ui.terminalPrint("Listening...")
            print("Listening...")
            r.pause_threshold=0.5                 #pause of 1 second  
            audio=r.listen(source, timeout=10,phrase_time_limit=5)   
        try:
            ui.updateMovieDynamically("processing")
            ui.terminalPrint("Recognizing...")
            print("Recognizing...")
            query= r.recognize_google(audio,language='en-in')
            ui.terminalPrint(f"Suryadeep Said: {query}\n")
            print(f"Suryadeep Said: {query}\n")
        except Exception as e:
            ui.terminalPrint(e)
            print(e)
            speak("Say that again please")
            #ui.terminalPrint("Say that again please...")
            return "None"
        return query


    def runJarvis(self):
        wishMe()
        while True:
            query=self.takeCommand().lower()

            #Logic for executing tasks based on Query
            if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        query= query.replace("wikipedia","")
                        result= wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        speak(result)

            elif 'open facebook' in query:
                        speak('Opening Facebook sir')
                        webbrowser.open("facebook.com")

            elif 'the time' in query:
                        strTime=datetime.now().strftime("%H:%M")
                        speak(f"Sir, the time is {strTime}")
                    
            elif 'open visual studio' in query:
                        speak('Opening Visual Studio Sir')
                        codePath="C:\\Users\\SURYADEEP DUTTA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codePath)
                        
            elif "send an email" in query:
                        speak("On what email address do I send sir? Please enter in the console: ")
                        receiver_address = input("Enter email address: ")
                        speak("What should be the subject sir?")
                        subject = self.takeCommand().capitalize()
                        speak("What is the message sir?")
                        message = self.takeCommand().capitalize()
                        if send_email(receiver_address, subject, message):
                            speak("I've sent the email sir.")
                        else:
                            speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
            
            elif 'play songs' in query:
                        music_dir='D:\\Major Project\\JARVISGUI\\JARVISGUI\\songs'
                        songs=os.listdir(music_dir)
                        rd=random.choice(songs)
                        os.startfile(os.path.join(music_dir,rd))

            elif 'notepad' in query:
                        speak('Opening Notepad sir')
                        path="C:\\Users\\SURYADEEP DUTTA\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
                        os.startfile(path)

            elif 'paint' in query:
                        speak('Opening Paint sir')
                        path="C:\\Users\\SURYADEEP DUTTA\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe"
                        os.startfile(path)
                    
            elif 'excel' in query:
                        speak('Opening Excel sir')
                        path="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                        os.startfile(path)

            elif 'word' in query:
                        speak('Opening Word sir')
                        path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                        os.startfile(path)

            elif 'powerpoint' in query:
                        speak('Opening Powerpoint sir')
                        path="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                        os.startfile(path)

            elif 'command prompt' in query:
                        speak('Opening Command Prompt sir')
                        path="C:\\Windows\\System32\\cmd.exe"
                        os.startfile(path)

            elif 'control panel' in query:
                        speak('Opening Control Panel sir')
                        path="C:\\Windows\\System32\\control.exe"
                        os.startfile(path)

            elif 'file explorer' in query:
                        speak('Opening File Explorer sir')
                        path="C:\\Windows\\explorer.exe"
                        os.startfile(path)

            elif "ip address" in query:
                        ip =get('https://api.ipify.org').text
                        speak(f"your IP adress is{ip}")

            elif "send message" in query:
                        speak('On what number should I send the message sir?')
                        number = self.takeCommand().lower()
                        speak("What is the message sir?")
                        message = self.takeCommand().lower()
                        send_whatsapp_message(number, message)
                        speak("Press Enter to Send the Message Sir")
                    
            elif 'open youtube' in query:
                        speak('What do you want to play on Youtube, sir?')
                        query = self.takeCommand().lower()
                        play_on_youtube(query)

            elif 'search on google' in query:
                        speak('What do you want to search on Google, sir?')
                        query = self.takeCommand().lower()
                        search_on_google(query)

            elif 'open camera' in query:
                        speak('Opening Camera sir')
                        open_camera()

            elif 'calculator' in query:
                        speak('Opening Calculator sir')
                        open_calculator()

            elif 'news' in query:
                        speak(f"I'm reading out the latest news headlines, sir")
                        speak(get_latest_news())

            elif 'weather' in query:
                        ip_address =get('https://api.ipify.org').text
                        #city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                        speak(f"Getting weather report for your city {'chandigarh'}")
                        #speak(f"Getting weather report for your city {city}")
                        weather, temperature, feels_like = get_weather_report('chandigarh')
                        #weather, temperature, feels_like = get_weather_report(city)
                        speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                        speak(f"Also, the weather report talks about {weather}")
                        speak("For your convenience, I am Printing it on the screen sir.")
                        ui.terminalPrint(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
                        print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
                    
            elif 'joke' in query:
                        speak(f"Hope you like this one sir")
                        joke = pyjokes.get_joke(language="en", category="neutral")
                        speak(joke)

            elif "advice" in query:
                        speak(f"Here's an advice for you, sir")
                        advice = get_random_advice()
                        speak(advice)

            elif "shutdown the system" in query:
                        os.system("shutdown /s /t 1")
                    
            elif "restart the system" in query:
                        os.system("shutdown /r /t 1")

            elif "sleep the system" in query:
                        os.system("shutdown /h ")
                        
            elif "you can sleep now" in query:
                        speak("Thanks for using me Sir, have a good day.")
                        sys.exit()   

            elif "switch the window" in query:
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.keyUp("alt")

            elif "where i am" in query:
                        speak("wait sir, Letme Check")
                        try:
                            ipAdd=requests.get('https://api.ipify.org').text
                            #ui.terminalPrint(ipAdd)
                            url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                            geo_requests= requests.get(url)
                            geo_data=geo_requests.json()
                            city=geo_data['city']
                            country=geo_data['country']
                            speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                        except Exception as e:
                            speak("Sorry Sir, Due to Network issue i am not able to find whare we are.")
                            pass
                    
            elif "screenshot" in query:
                        speak("Sir, pleaase tell the name for this screenshort file")
                        name=self.takeCommand().lower()
                        speak("please hold the screen for few seconds, I am taking Screenshort")
                        img=pyautogui.screenshot()
                        img.save(f"{name}.png")
                        speak("I am done sir, the screenshort is saved in our main folder")

startExecution=jarvisMain()   

class guiOfJarvis(QMainWindow):
    def __init__(self):
        super(guiOfJarvis,self).__init__()
        self.jarvisUI=Ui_jarvisGUI()
        self.jarvisUI.setupUi(self)
        self.runAllMovies()
        self.jarvisUI.enterBotton.clicked.connect(self.manualCodeFromTerminal)

    def runAllMovies(self):
        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\7LP8")
        self.jarvisUI.label.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\spheres-motion-for-ai-product-design-by-gleb-large.gif")
        self.jarvisUI.label_2.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\T8bahf.gif")
        self.jarvisUI.label_3.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\jarvis.gif")
        self.jarvisUI.logo.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\sound-wave-waves.gif")
        self.jarvisUI.lower_backgroung.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\a064a7f04f9ecbf99cc543f1ba976adb69949e71_hq.gif")
        self.jarvisUI.processing_label.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\ava_ai.gif")
        self.jarvisUI.speaking_label.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.movie = QtGui.QMovie("D:\\Major Project\\JARVISGUI\\JARVISGUI\\jarvis gif\\sirilike.gif")
        self.jarvisUI.listening_label.setMovie(self.jarvisUI.movie)
        self.jarvisUI.movie.start()

        self.jarvisUI.pushButton_2.clicked.connect(self.close)

        startExecution.start()

    def updateMovieDynamically(self, state):
            if state=="listening":
                    self.jarvisUI.listening_label.raise_()
                    self.jarvisUI.processing_label.hide()
                    self.jarvisUI.speaking_label.hide()
                    self.jarvisUI.listening_label.show()
            elif state=="speaking":
                    self.jarvisUI.speaking_label.raise_()
                    self.jarvisUI.processing_label.hide()
                    self.jarvisUI.listening_label.hide()
                    self.jarvisUI.speaking_label.show()
            elif state=="processing":
                    self.jarvisUI.processing_label.raise_()
                    self.jarvisUI.speaking_label.hide()
                    self.jarvisUI.listening_label.hide()
                    self.jarvisUI.processing_label.show()

    def terminalPrint(self,text):
            self.jarvisUI.terminalOutputBox.insertPlainText(str(text) +'\n')
            self.jarvisUI.terminalOutputBox.ensureCursorVisible()

    def manualCodeFromTerminal(self):
            cmd=self.jarvisUI.terminalInputBox.text()
            if cmd:
                    self.jarvisUI.terminalInputBox.clear()
                    self.jarvisUI.terminalOutputBox.insertPlainText(f" You Just Typed>>{cmd}") 
                    if cmd=='exit':
                            ui.close()
                    else:
                            pass
            else:
                    pass


if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=guiOfJarvis()
    ui.show()
    sys.exit(app.exec_())

