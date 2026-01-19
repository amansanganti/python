import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("Jarvis here !! ")
    



