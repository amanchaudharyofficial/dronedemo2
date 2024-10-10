from threading import Thread
import time
from logger import DailyMessageLogger
import reciever 
from sender import send_message, sendMsg, sendInit
from json_handler import read_json
from subprocess import call
import IndianEnglishModel
import main
import os
import sys
import json
import vosk
import pyaudio
import speech_recognition as sr



DEST = "192.168.110.102"
# DEST = "192.168.111.72"
# HOST ="192.168.110.131" 
HOST ="192.168.110.131"  # Listen on all interfaces
PORT = 5007

# def audioFunction(stream,recognizer):             
  # data = stream.read(4000)
  # if len(data)== 0:
  #  return
  # if recognizer.AcceptWaveform(data):
  #   result = json.loads(recognizer.Result())
  #   text = result["text"]
  #   print("Recognized:", text)                

def main_thread():
  """
  Main function demonstrating communication and logging.
  """
#   while True:
  # while True:
  #   print("main called")
  # while True:
  #   print("Aman calling",main.flag)
  logger = DailyMessageLogger()
  logger.log_function_entry("main")
  logger.log_function_exit("main")


def send_thread():
  counter=1
  DEST = "192.168.111.95"
  #DEST = "192.168.110.102"
  # DEST = "10.10.40.5"  # Change to target IP if needed
  PORT = 5010
  # sendMsg(DEST,PORT,)
def audio_thread():

  recognizer = sr.Recognizer()
    # Initialize PyAudio
  # p = pyaudio.PyAudio()
  #stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000, start=True)
 

    # Start listening
  # print("Listening... Press Ctrl+C to stop.")
    
    # try:
  print("top",main.flag)
  while True:
    # if main.flag==1 and main.streamFlag==1:
    # if main.flag==-1:
      with sr.Microphone() as source:
        try:
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Recording...please speak")
            # recorded_audio = recognizer.listen(source, timeout=0.4)
            recorded_audio = recognizer.listen(source, 3,10)
            print("Done recording")
            main.streamFlag=0
        except sr.WaitTimeoutError as e:
         pass

      try:
        print("Recognizing the text")
        text = recognizer.recognize_google(recorded_audio, language="en-GB")
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("Decoded Text : {}".format(text))
        print("flaaag", main.flag)
        if text=="shaktiman" or text=="Shaktiman":
          if main.flag==-1:
            main.flag=0
            text=""
            print("success")
          # elif main.flag==0:
          #   main.flag=1
          #   text=""
          #   print("STUCK")
        
        # if text=="shaktiman" and main.flag==0:
        #   main.flag=1
          # main.counter_text=1
        if main.flag==0:
          if(len(main.TEXT)<256)and (text!=""):
            main.TEXT=main.TEXT+text
            # main.counter_text=0
            main.flag=-1
            print("Stopped listening...............................")
            print("CHECKKKKK")
            print("TEXTTTT ", main.TEXT)
            sendMsg(DEST,5007,main.TEXT)
            main.TEXT=""
            

        # if main.flag==1:
        #   main.counter_text=0
        #   main.flag=-1
        #   print("Stopped listening...............................")
        #   print("CHECKKKKK")
        #   print("TEXTTTT ", main.TEXT)
        #   sendMsg(DEST,5007,main.TEXT)
        #   main.TEXT=""




      except Exception as ex:
         pass
      
      
     
                              
      time.sleep(0.20) 
      
      




  
  # while True:  
  #   message = f"Message from sender at main {counter}"
  #   send_message(message,HOST,PORT)
  #   counter=counter+1
  #   time.sleep(3)  # Adjust sending frequency

def receive_thread():
  while True:
    reciever.receive_message()
    time.sleep(0.30)
    
    


# Start sender and receiver threads call(["python","IndianEnglishModel.py"])


  








