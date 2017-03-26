#!/usr/bin/env python3
#Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh
# Requires PyAudio and PySpeech.

import RPi.GPIO as GPIO
import time
import os
import speech_recognition as sr
import datetime
from pyrebase import pyrebase

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(26, GPIO.IN)

ser = serial.Serial("/dev/ttyS0",115200,timeout=3) #FONA Serial
gpio.setup(callbutton,gpio.IN)#input

callstate = False

config = {
  "apiKey": "apiKey",
  "authDomain": "smartsafetyhardhat.firebaseapp.com",
  "databaseURL": "https://smartsafetyhardhat.firebaseio.com",
  "storageBucket": "smartsafetyhardhat.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#time variable
now = datetime.datetime.now()
time = now.strftime('%A %B %d, %Y %I:%M:%S %p')
#time = str(datetime.datetime.now())



# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    os.system("sudo shutdown -h now")

def getGPSCoordinates(channel):
    try:
        if ser.write("AT+CGNSPWR=?") == 'OK':
            gpsLocation = ser.write("AT+CGNSINF")
            
    except:
        #log error
def capturePicture(channel):
    #add naming code for image
    fswebcam -r 640x480 --save image4.jpg



def speech2text(channel):
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
        google_translate = r.recognize_google(audio)
        data = {"name": google_translate, "date": time }
        db.child("hazards").push(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def recHazLog(channel):


def startAnswerCall(channel):
    #ser = serial.Serial("/dev/ttyUSB0",115200,timeout=3) #FONA Serial
    if callstate == False:     #make call
        callstate = True
        #inputnum=str(input("Enter Phone Number"))
        ser.write("ATD"+str(inputnum)+";\r")
        endinput = str(input("Press e to end the call"))
        """while endinput != NULL :
          time.sleep(1)
          """
        ser.write("ATH\r")
        ser.close()
    else # answercall():

        print("Answering Call")
        ser.write("ATA\r")
        data=""
        data=ser.read(10)


    while True :
        input_value=gpio.input(callbutton)
        if input_value==False:#bcall button is pressed
            print"press"
            call()
            while innput_value==False:
                input_value=gpio.input(callbutton)

def endCall(channel):

# Add our function to execute when the button pressed event happens / function called on button down

# Now wait!
while 1:
    GPIO.add_event_detect(5, GPIO.RISING, callback = logHazard, bouncetime = 2000)         #board 29
    GPIO.add_event_detect(6, GPIO.RISING, callback = startEndCall, bouncetime = 2000)      #board 31
    GPIO.add_event_detect(13, GPIO.RISING, callback = capturePicture, bouncetime = 2000)   #board 33
    GPIO.add_event_detect(26, GPIO.RISING, callback = Shutdown, bouncetime = 2000)         #board 37
    #time.sleep(1)