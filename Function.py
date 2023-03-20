import os 
import json 
import requests 
text = input("input text:")
from google_speech import Speech
inp1 = input("input your language: ")
lang = inp1
sox_effects = ('speed',"1.04")
inp = input("Speak: ")
speech = Speech(inp,lang)
speech.play(sox_effects)
if text == "hello":
         print("Greeting!")
else:
         print("Hi")

def Function1(inp):

          #print("Print_say world")
          #inp = input("Speak: ")
          speech = Speech(inp,lang)
          speech.play(sox_effects)
def Function2(text_data):

          print("say siuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!")
          Function1(text_data) 
def Func_arguement(test_text,data_payload):
    
           print(test_text)
           print(data_payload)

#Function1()
#Function2("hello my name is sky ")
#Func_arguement("Test_1234","yes!")
#def Function1():
#          print("Print_say world")
#def Funtion2():
#         print("say siuuuuuuuuuuuuuuuuuu!")
