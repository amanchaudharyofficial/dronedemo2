#! /usr/bin/env python3
import os
import sys
import json
import vosk
import pyaudio
import main
import time 
#from reciever import flag
def speech_to_text():
    # Initialize Vosk recognizer
    print("Inside code",main.flag)
    model_path = "vosk-model-en-in-0.5"  # Update this with the path to your downloaded Vosk model
    if not os.path.exists(model_path):
        print("model path is wrong")
        return

    # Create a Vosk recognizer using the model
    vosk_model =vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(vosk_model, 16000)

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    # Start listening
    print("Listening... Press Ctrl+C to stop.")
    
    # try:
    print("top",main.flag)  
    while main.flag==1:
        data = stream.read(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result["text"]
            print("Recognized:", text)
            print("flag",main.flag)
            time.sleep(5)
        print(main.flag) 
    print(main.flag)   
    #   elif(main.flag==0):
        #  break
         
    print("Stopped listening...............................")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
                    
    # except KeyboardInterrupt:
    #     pass

    # Stop listening and clean up
    

if __name__ == "__main__":
    speech_to_text()
