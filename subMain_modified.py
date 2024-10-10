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
  HOST = "localhost"  # Change to target IP if needed
  PORT = 5051
  sendMsg(HOST,PORT)
def audio_thread():
  model_path = "vosk-model-en-in-0.5"  # Update this with the path to your downloaded Vosk model
  if not os.path.exists(model_path):
   print("model path is wrong")
   return
  vosk_model =vosk.Model(model_path)
  recognizer = vosk.KaldiRecognizer(vosk_model, 16000)

    # Initialize PyAudio
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
  # stream.start_stream()
    # Start listening
  print("Listening... Press Ctrl+C to stop.")
    
    # try:
  print("top",main.flag)
  while True:
    if main.flag==1:
      data = stream.read(4000)
      if len(data)== 0:
       return
      if recognizer.AcceptWaveform(data):
       result = json.loads(recognizer.Result())
       text = result["text"]
       print("Recognized:", text)                

      # audioFunction(stream,recognizer)
    if main.flag==0:
      print("Stopped listening...............................")
      stream.stop_stream()
      stream.close()
      p.terminate()
      main.flag=-1




  
  # while True:  
  #   message = f"Message from sender at main {counter}"
  #   send_message(message,HOST,PORT)
  #   counter=counter+1
  #   time.sleep(3)  # Adjust sending frequency

def receive_thread():
  while True:
    reciever.receive_message()
    
    


# Start sender and receiver threads call(["python","IndianEnglishModel.py"])


  







