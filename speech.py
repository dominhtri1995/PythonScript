# Requires PyAudio and PySpeech.
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import vlc

def speak(audioString):
	
	print(audioString)
	arr=audioString.split()
	tts = gTTS(text=audioString, lang='en')
	tts.save("audio.mp3")
	p = vlc.MediaPlayer("audio.mp3")
	p.play()
	time.sleep(len(arr)/2-0.1)
	
# initialization
if __name__ =="__main__":
	time.sleep(2)
	speak("Hi Frank what are you doing")
	time.sleep(3)
	speak("Hi Kevin")
	time.sleep(1)