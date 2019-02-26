# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:28:54 2019

@author: harshvardhan
"""

from gtts import gTTS 
import speech_recognition as sr
import os 


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        mytext = r.recognize_google(audio)
        
    except:
        print("Sorry could not recognize what you said")  
# The text that you want to convert to audio 

  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("welcome.mp3") 