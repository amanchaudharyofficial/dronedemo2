
# Start sender and receiver threads call(["python","IndianEnglishModel.py"])
from threading import Thread
import subMain
import IndianEnglishModel

import os
import sys
import json
import vosk
import pyaudio
import time
flag=-1 
streamFlag = -1
counter_text=0
TEXT=""


# def audioFunction():             
# while(flag==1):
#   data = stream.read(4000)
#   if len(data) == 0:00000
#     break
#   if recognizer.AcceptWaveform(data):
#     result = json.loads(recognizer.Result())
#     text = result["text"]
#     print("Recognized:", text)
                 
# print("Stopped listening...............................")
# stream.stop_stream()
# stream.close()
# p.terminate()
                          

def audio_thread_working():
  
  IndianEnglishModel.speech_to_text()
if __name__ == "__main__":
  # main()n
  
  # message = f"hii test time {time.time()}"
  print("inside main")
   
  
  #receive_thread()++++++
  # call(["python","IndianEnglishModel.py"])
  
  receiver_thread = Thread(target=subMain.receive_thread)
  # sender_thread = Thread(target=subMain.send_thread)
  main_thread = Thread(target=subMain.main_thread)
  audio_threadT = Thread(target=subMain.audio_thread)
  audio_threadT.start()
  receiver_thread.start()
  
  # sender_thread.start()
  main_thread.start()
  
  # main_thread.join()
  # receiver_thread.join() 
  # audio_thread.join()
  # sender_thread.join()
  








