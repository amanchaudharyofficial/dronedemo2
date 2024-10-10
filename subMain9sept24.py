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



#from tqdm import tqdm
 
 




#DEST="192.168.111.46"      #IP Arohan
#HOST="192.168.171.18"

DEST="192.168.111.46"
HOST="192.168.110.131"      #IP Arohan
#DEST = "192.168.110.102"
#DEST = "192.168.111.72"
#HOST ="192.168.110.131"  # Listen on all interfaces
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
  #DEST = "192.168.111.95"
  #DEST = "192.168.110.102"
  #DEST = "192.168.111.46"  # IP Arohan
  DEST = "192.168.111.46"  # Change to target IP if needed
  PORT = 5007
  # sendMsg(DEST,PORT,)
def audio_thread():

  model_path_english = "vosk-model-en-in-0.5"  # Update this with the path to your downloaded Vosk model
  model_path_hindi = "vosk-model-hi-0.22"  # Hindi Model
  if not os.path.exists(model_path_hindi):
    print("model path is wrong hindi")
    return
  if not os.path.exists(model_path_english):
    print("model path is wrong english")
    return
  vosk_model_hindi =vosk.Model(model_path_hindi)
  vosk_model_english =vosk.Model(model_path_english)
  recognizer_english = vosk.KaldiRecognizer(vosk_model_english, 20000)
  recognizer_hindi = vosk.KaldiRecognizer(vosk_model_hindi, 20000)
  #recognizer = sr.Recognizer()
    # Initialize PyAudio
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000, start=True)
 

    # Start listening
  print("Listening... Press Ctrl+C to stop.")
    
    # try:
  print("top",main.flag)
  # while True:
      
    # if main.flag==1 and main.streamFlag==1:
    # if main.flag==-1:
      # with sr.Microphone() as source:
      #   try:
      #       print()
      #       print()
      #       print()
      #       print()
      #       print()
      #       print()
      #       print()
      #       print()
      #       print("Adjusting noise ")
      #       #recognizer.adjust_for_ambient_noise(source, duration=1)
      #       print("Recording...please speak")
      #       # recorded_audio = recognizer.listen(source, timeout=0.4)
      #       #recorded_audio = recognizer.listen(source, 3,10)
      #       print("Done recording")
      #       main.streamFlag=0
      #   except sr.WaitTimeoutError as e:
      #    pass
      # print("Listening... Press Ctrl+C to stop.")
  
  try:
    while True:
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # for i in tqdm(range(int(9e6))):
        #   pass
        
        data = stream.read(10000)
        if len(data) == 0:
            break
        if recognizer_english.AcceptWaveform(data) or recognizer_hindi.AcceptWaveform(data):
            result_english = json.loads(recognizer_english.Result())
            result_hindi = json.loads(recognizer_hindi.Result())
            text_english = result_english["text"]
            text_hindi=result_hindi["text"]
            print("TEXT_ENGLISH:: ", text_english)
            print("TEXT_HINDI:: ", text_hindi)
            if(text_english==""):
               print("Speak now")
            if ("charlie" in text_english) or ("charly" in text_english) or ("char" in text_english) or ("charley" in text_english)or ("shukla" in text_english) or ("starlink" in text_english):
            # if ("charlie" in text) or ("charly" in text) or ("char" in text) or ("charley" in text):
              if "lost" in text_english:
                  text_english="I have lost my key in CRL Ghaziabad"
                  sendMsg(DEST,5007,text_english)
              if "introduce" in text_english:
                  text_english="Introduce Yourself"
                  sendMsg(DEST,5007,text_english)
              if "yes this is my" in text_english or "this is my key" in text_english:
                text_english="Yes this is my key"
                sendMsg(DEST,5007,text_english)
              if "no" in text_english or"not" in text_english:
                text_english="No this my key"
              if "drop" in text_english or"bomb" in text_english:
                text_english="Drop Bomb"
                sendMsg(DEST,5007,text_english)
              if "proceed" in text_english:
                text_english="Yes you can proceed"
                sendMsg(DEST,5007,text_english)

              if "suspicious" in text_english or"neutralize" in text_english:
                text_english="Camp is present in suspicious area of CRL Neutralize it"
                sendMsg(DEST,5007,text_english)

              if "sensitive" in text_english or"yes this is sensitive area" in text_english:
                text_english="Yes this is sensitive area of CRL"
                sendMsg(DEST,5007,text_english)

              if "completed" in text_english:
                text_english="mission completed"
                sendMsg(DEST,5007,text_english)


              if "mission" in text_english or "start" in text_english :
                  if "start" in text_english:
                      text_english="Start Mission"
                      sendMsg(DEST,5007,text_english)
                  else:
                      text_english="Plan Mission"
                      sendMsg(DEST,5007,text_english)
            if(text_hindi==""):
               print("Speak now")
            if ("सत्यवान" in text_hindi) or ( "शक्तिमान" in text_hindi) or ("शक्ति" in text_hindi):
            # if ("charlie" in text) or ("charly" in text) or ("char" in text) or ("charley" in text):
              if "परिचय" in text_hindi:
                  text_hindi="अपना परिचय दें"
                  print("HINDI MESSAGE SENT अपना परिचय दें")
                  sendMsg(DEST,5007,text_hindi)

              # if "खो गई" in text_hindi and " मिशन प्लान" in text_hindi:
              #     text_hindi="मेरी चाबी सीआरल में खो गई है"
              #     sendMsg(DEST,5007,text_hindi)
              #     text_hindi="मिशन प्लान करें"
              #     sendMsg(DEST,5007,text_hindi)
              #     print("HINDI MESSAGE SENT मेरी चाबी सीआरल गाजियाबाद में खो गई है")
              if "गाजियाबाद" in text_hindi:
                  text_hindi="मेरी चाबी सीआरल गाजियाबाद में खो गई है"
                  sendMsg(DEST,5007,text_hindi)
                  print("HINDI MESSAGE SENT मेरी चाबी सीआरल गाजियाबाद में खो गई है")


              if "नष्ट" in text_hindi or "परिसर" in text_hindi:
                  text_hindi="सीआरएल परिसर में संदिग्ध कैंप है , उसे नष्ट कर दीजिये"
                  sendMsg(DEST,5007,text_hindi)
                  print("HINDI MESSAGE SENT सीआरएल परिसर में संदिग्ध कैंप है उसे नष्ट कर दीजिये")


                  
              if "मेरी चाबी है" in text_hindi:
                  text_hindi=" हाँ यह मेरी चाबी है "
                  sendMsg(DEST,5007,text_hindi)
                  print("HINDI MESSAGE SENT हाँ यह मेरी चाबी है")


              if "हाँ यह कैंप है " in text_hindi or "कैंप है" in text_hindi:
                  text_hindi="हाँ यह संदिग्ध कैंप है"
                  sendMsg(DEST,5007,text_hindi)
                  print("HINDI MESSAGE SENT हाँ यह कैंप है")

                
              

              if "सफल हुआ" in text_hindi:
                  text_hindi="मिशन सफल हुआ"
                  sendMsg(DEST,5007,text_hindi)
                  print("HINDI MESSAGE SENT मिशन सफल हुआ")
              if "मेरी चाबी नहीं है" in text_hindi:
                  text_hindi=" ये मेरी चाबी नहीं है "
                  sendMsg(DEST,5007,text_hindi)
                  print("HINDI MESSAGE SENT नहीं ये मेरी चाबी नहीं है")

              if "बम गिराओ" in text_hindi:
                  text_hindi=" बम गिराओ"
                  sendMsg(DEST,5007,text_hindi)
                  print("HINDI MESSAGE SENT बम गिराओ")

              if "मिशन" in text_hindi or "start" in text_hindi :
                  if "योजना" in text_hindi:
                      text_hindi="मिशन योजना बनाएं"
                      sendMsg(DEST,5007,text_hindi)
                      print("HINDI MESSAGE SENT मिशन योजना बनाएं")
                  if "शुरू" in text_hindi:
                      text_hindi="मिशन शुरू करें"
                      sendMsg(DEST,5007,text_hindi)
                      print("HINDI MESSAGE SENT  मिशन शुरू करें ")

              print() 
              print() 
              print() 
              print("Recognized hindi text:", text_hindi)  
              # with open('log_file.txt','a')as file:
              #    file.write(text_hindi+'\n')
              print() 
              print() 
              print()             
              text_hindi=""
              print("Recognized english text:", text_english)              
              text_english=""

                    
            
                    
  except KeyboardInterrupt:
        pass
  stream.stop_stream()
  stream.close()
  p.terminate()

  # try:
  #       print("Recognizing the text")
  #       #text = recognizer.recognize_google(recorded_audio, language="en-GB")
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("Decoded Text : {}".format(text))
  #       print("flaaag", main.flag)
  #       if text=="shaktiman" or text=="shaktimaan" or "Shaktiman":
  #         if main.flag==-1:
  #           main.flag=0
  #           text=""
  #           print("success")
  #         # elif main.flag==0:
  #         #   main.flag=1
  #         #   text=""
  #         #   print("STUCK")
        
  #       # if text=="shaktiman" and main.flag==0:
  #       #   main.flag=1
  #         # main.counter_text=1
  #       if main.flag==0:
  #         if(len(main.TEXT)<256)and (text!=""):
  #           main.TEXT=main.TEXT+text
  #           # main.counter_text=0
  #           main.flag=-1
  #           print("Stopped listening...............................")
  #           print("CHECKKKKK")
  #           print("TEXTTTT ", main.TEXT)
  #           sendMsg(DEST,5007,main.TEXT)
  #           main.TEXT=""
            

  #       # if main.flag==1:
  #       #   main.counter_text=0
  #       #   main.flag=-1
  #       #   print("Stopped listening...............................")
  #       #   print("CHECKKKKK")
  #       #   print("TEXTTTT ", main.TEXT)
  #       #   sendMsg(DEST,5007,main.TEXT)
  #       #   main.TEXT=""




  # except Exception as ex:
  #   pass
      
      
     
                              
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


  








