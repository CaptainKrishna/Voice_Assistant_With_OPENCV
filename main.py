import sys
import pyttsx3
import speech_recognition as sr
import os
import mysql.connector
import wikipedia
import pyjokes
import pyautogui
import webbrowser
import smtplib
import string as s
import requests
import wolframalpha
import win32com.client as wincl
import cv2
import numpy as np
import face_recognition
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pynotifier import Notification
from requests.api import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from random import*
from playsound import playsound
from PIL import Image
import datetime
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.config import config
from httplib2 import RelativeURIError
from Jarvis import JarvisAssistant

# voice assistant Voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#speaking Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#starting wish me Function
def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"""Good Morning    
                {name} !""")
    elif hour >= 12 and hour < 18:
        speak(f"""Good Afternoon    
                {name} !""")
    else:
        speak(f"""Good Evening 
                {name} !""")
        speak("I am  Jay , your personal Assistant \t what can i help you")

#push notification Function
def noti(notifi):
     Notification(title='Task completed', description=notifi,duration=5, urgency='normal').send()

#voice input command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Sorry sir please can you say that again..")
        return 'None'
    return query

# email sending
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jayvoiceassistant@gmail.com', 'JayVoiceAssistant123')
    server.sendmail('jayvoiceassistant@gmail.com', to, content)
    server.close()

# searching data on google
def speakquery(answe):
    con = mysql.connector.connect(host="localhost", user="root", passwd="Krishna@123", database="voice")
    mycursor = con.cursor()
    sql = "select * from `voicequery` where `query` like '" + answe + "';"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[2])
        speak(x[2])

# simple Google search
def googlesearch(query):
    speak(f'searching {query} on google')
    webbrowser.open("https://www.google.com/search?q="+query+"&rlz=1C1CHZN_enIN949IN949&oq="+query +
                    "&aqs=chrome..69i57j0i131i433j0i433j0i131i433l3j0i433j0i131i433j0i433j0.2513j0j15&sourceid=chrome&ie=UTF-8")

# encoding the faces
def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# save the user Data
def attendance1(name):
    with open('data.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            speak(f"Welcome {name}")
            f.writelines(f'\n{name},{tStr},{dStr}')

def openc():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(
            faces, facesCurrentFrame)
        encodeListKnown=""
        personNames=[]
        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex] != True:
                break
            if matches[matchIndex]:
                name = personNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                attendance1(name)
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) == 13:
            pyautogui.press("enter")
            break
    cap.release()
    cv2.destroyAllWindows()


class MainThread(QThread):
    
    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        speak("Images are incoding stage , please wait")
        path = 'images'
        images = []
        personNames = []
        myList = os.listdir(path)
        print(myList)
        for cu_img in myList:
            current_Img = cv2.imread(f'{path}/{cu_img}')
            images.append(current_Img)
            personNames.append(os.path.splitext(cu_img)[0])
            print(personNames)

            encodeListKnown = faceEncodings(images)
        speak('All Encoading are Completed!!!')

        wishMe("Krishna")

        while True:
            query = takeCommand().lower()
            speakquery(query)
           
            if 'where is' in query:       
                query = query . replace('where is', '')
                speak(f'serching {query} on maps ')
                webbrowser.open("https://www.google.co.in/maps/place/" + query+'')
                noti(f"Serching {query}")
        
            #Google search query   
            elif'search' in query:
                query = query . replace('search', '')
                googlesearch(query)
                noti("task completed")
        
            #Taking screen shot
            elif 'take a screen'in query:
                im1 = pyautogui.screenshot("hello.jpg")
                speak("Image are Save in folder")
                noti("Image are capture")
        
            #show image
            elif'show image' in query:            
                im = Image.open(r"hello.jpg") 
                speak("Image are opening")
                im.show()
        
            # serch on wikipedia
            elif 'wikipedia' in query or 'tell me about' in query:
                try:
                    query = query . replace("wikipedia", "")
                    query = query . replace("tell me about", "")
                    speak('Searching Wikipedia...')
                    noti(f'{query} Searching')
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("No result found")
        
            # show time
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                noti(strTime)
                speak(f"Sir, the time is {strTime}")

            # showing IP address
            elif "ip" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            #play music
            elif 'play music' in query or 'music' in query:
                noti("Playing music")
                music_dir = 'D:\\Jay voice assisatant\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
                
            # switch the window
            elif "switch the window" in query or "switch window" in query:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")        

            # serching on youtube
            elif 'play' in query:
                query = query . replace("play", "")
                speak("serching on youtube")
                webbrowser.open("https://www.youtube.com/results?search_query="+query)

            # python jokes
            elif'jokes' in query or 'jokes' in query:
                a = pyjokes.get_joke()
                print(a)
                speak(a)

            # sending Mail to contact
            elif 'send email to' in query:
            # query=query.replace('send email to ','')
            # name=query
            # receiver=email_list[name]
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    jay = 'This E-mail has been genrated by JayVoice Assistant'
                    receiver = 'krishvishwa888@gmail.com'
                    contactJay = (f'{jay}\n \t{content}\n')
                    sendEmail(receiver, contactJay)
                    noti("Email has been send")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir . I am not able to send this email")

            # wether API
            elif 'weather' in query:
                query = query . replace("weather", "")
                city = query
                url = "https://www.google.com/search?q="+"weather"+city
                html = requests.get(url).content
                soup = BeautifulSoup(html, 'html.parser')
                temp = soup.find(
                    'div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                data = str.split('\n')
                time = data[0]
                sky = data[1]
                final_response = f"""sir currently {city} wether is {sky} with the temperature of {temp} """
                print(final_response)
                speak(final_response)
                noti(f"{city} Current Temprature is {temp}")

            # exit the programm
            elif 'exit' in query:
                noti("Thanks for giving me your time")
                speak("Thanks for giving me your time")
                exit()

            # walfram alfa library
            elif 'what is' in query or "who is" in query:
                client = wolframalpha.Client("VYGWWR-X682V98YHT")
                res = client.query(query)
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")

            # write a notes
            elif 'write a note' in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('voice.txt', 'w')
                file.write(note)

            # showing the notes
            elif "show note" in query:
                speak("Showing Notes")
                file = open("voice.txt", "r")
                print(file.read())
                speak(file)
        
            # opening website using Mysql Database
            elif 'open ' in query:
                query = query . replace('open ', '')
                con = mysql.connector.connect(host="localhost", user="root", passwd="Krishna@123", database="voice")
                mycursor = con.cursor()
                sql2 = "select * from `voiceweb` where `search` like '"+query+"';"
                mycursor.execute(sql2)
                myresult2 = mycursor.fetchall()
                for x in myresult2:
                    print(x[2])
                    webbrowser.open_new(x[2])

            # security Mode for motion detaction
            elif'security mode' in query:
                cam = cv2.VideoCapture(1)
                while cam.isOpened():
                    ret, frame1 = cam.read()
                    ret, frame2 = cam.read()
                    diff = cv2.absdiff(frame1, frame2)
                    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                    blur = cv2.GaussianBlur(gray, (5, 5), 0)
                    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                    dilated = cv2.dilate(thresh, None, iterations=3)
                    contours, _ = cv2.findContours(
                    dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                    for c in contours:
                        if cv2.contourArea(c) < 5000:
                           continue
                        x, y, w, h = cv2.boundingRect(c)
                        cv2.rectangle(frame1, (x, y), (x+w, y+h), (200, 255, 0), 2)
                        speak("Security alert Some one is founnd on camera")
                        try:
                            receiver = 'krishvishwa888@gmail.com'
                            contactJay = 'This email has been generated automatically \n Security alert Some one is founnd on camera'
                            sendEmail(receiver, contactJay)
                        except Exception as e:
                            print("Email Has some problem")
                    # playsound('D:\\final year\\voiceassistant\\alert.wav')
                    if cv2.waitKey(10) == ord('q'):
                        break
                    cv2.imshow('Jay Security Eye', frame1)
        
            # Normal Mode for motion detaction   
            elif 'normal check' in query or 'who is there' in query or 'check' in query:
                openc()
            
startExecution = MainThread()

# Gui code is here
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
