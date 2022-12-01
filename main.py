from inspect import FrameInfo
from Jarvis import JarvisAssistant
import re
import os
import wikipedia
import random
import pprint
import cv2
import smtplib
import datetime
import requests
import sys
import urllib.parse
import webbrowser  
import pyjokes
import time
import pyautogui
import pywhatkit
import wolframalpha
import pywhatkit as py
import numpy as np
import speech_recognition as sr
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from pyzbar.pyzbar import decode
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from urllib.parse import quote_from_bytes
from PyQt5.QtWidgets import *
from tkinter import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.config import config

obj = JarvisAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'myself': 'ankushrachewar909@gmail.com',
    'my official email': 'ankushrachewar909@gmail.com',
    'my second email': 'kushrachewar1234@gail.com',
    'my official mail': 'kushrachewar1234@gmail.com',
    'my second mail': 'rachewarankush1145@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
# =======================================================================================================================================================

def speak(text):
    obj.tts(text)

app_id = config.wolframalpha_id

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")
# if __name__ == "__main__":

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        wishMe()

        while True:
            command = obj.mic_input()
            if 'wikipedia' in command:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in command:
                webbrowser.open("youtube.com")

            elif 'open google' in command:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in command:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in command:
                music_dir = "J:\Music\songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in command:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in command:
                codePath = "C:\\Users\\Ankush Rachewar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'you can sleep' in command:
                speak("thanks for using me sir,have a good day")
                self.ui.command.connect(self.close)
                # exit(app.exec_())
                  
                # sys.exit()

            elif 'open notepad' in command:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'tell me a joke' in command:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'play music on youtube' in command:
                py.playonyt("shape of you")

            elif 'message' in command:
                py.sendwhatmsg("+918412915454", "Hello", 22, 28)
                print("Successfully Sent!")

            elif 'open qr code' in command:
                def decoder(image):
                    gray_img = cv2.cvtColor(image,0)
                    barcode = decode(gray_img)

                    for obj in barcode:
                        points = obj.polygon
                        (x,y,w,h) = obj.rect
                        pts = np.array(points, np.int32)
                        pts = pts.reshape((-1, 1, 2))
                        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                        barcodeData = obj.data.decode("utf-8")
                        barcodeType = obj.type
                        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
                        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
                        print("Barcode: "+barcodeData +" | Type: "+barcodeType)
                cap = cv2.VideoCapture(0)
                while 2:
                    ret, frame = cap.read()
                    decoder(frame)
                    cv2.imshow('Image', frame)
                    code = cv2.waitKey(10)
                    if code == ord('q'):
                        break
                    # exit(app.exec_())

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask) 
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.setGeometry(QtCore.QRect(1000, 580, 101, 51))
        self.ui.pushButton_2.setGeometry(QtCore.QRect(1200, 580, 101, 51)) 

    # def __del__(self):
        # sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())