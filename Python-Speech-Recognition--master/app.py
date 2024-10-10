import speech_recognition as sr
import pyaudio
recognizer = sr.Recognizer()

with sr.Microphone() as source:
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
    print("Recording for 4 seconds")
    recorded_audio = recognizer.listen(source, timeout=None)
    print("Done recording")

try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-GB"
        )

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
    


except Exception as ex:

    print("ex")


sr.Microphone.list_microphone_names()