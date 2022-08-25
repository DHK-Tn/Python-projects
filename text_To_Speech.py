#impoting moduke
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(Audio):
	engine.say(Audio)
	engine.runAndWait()

Your_Text = input("Enter Your Text pls : \n >> ")
speak(Your_Text)