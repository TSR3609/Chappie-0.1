import pyttsx3
#import qrcode as qr
import datetime
import wikipedia 
import webbrowser
import os
import time as tsr
from playsound import playsound
#import pywhatkit
#import pyautogui as sender
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
sec = 5
feeling_sad = ['i am feeling sad','i am sad','my mood is off','i am feeling depressed','depressed']
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")    

    else:
        speak("Good Evening Sir !")  

if __name__ == "__main__":
    #print("hi")
    playsound('E:\\Chappie\\intro.mp3')
    speak("INITIALIZING SYSTEMS.....")
    time()
    def func():
           speak("How May I Be, of your service, sir")
           query  = input("How May I Be of your service sir: ").lower()
           if "open youtube" in query:
               webbrowser.open("youtube.com")
               tsr.sleep(1)
               print("")
               func()
           elif "open google" in query:
               google_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
               os.startfile(google_path)
               tsr.sleep(1)
               print("")
               func()
          
           elif "open roblox" in query:
               webbrowser.open("roblox.com")
               tsr.sleep(1)
               print("")
               func()
              
           elif "open discord" in query:
               webbrowser.open("discord.com/app")
               tsr.sleep(1)
               print("")
               func()
           
           elif "open classroom" in query:
               webbrowser.open("https://classroom.google.com/u/1/c/NDg0Mjk4NTQ1OTcx")
               tsr.sleep(1)
               print("   ")
               func()
           elif "open calculator" in query:
               os.startfile('calc.exe')
               tsr.sleep(1)
               print("   ")
               func()
           elif "open instagram" in query:
               webbrowser.open("instagram.com")
               tsr.sleep(1)
               print("   ")
               func()
           elif "open cmd" in query:
               print("Opening cmd....")
               speak("Opening cmd....")
               os.startfile("cmd.exe")
               tsr.sleep(1)
               print("   ")
               func()
           elif "open my channel" in query:
               webbrowser.open("https://www.youtube.com/@technoanimaters9346/featured")
               print("Opening  Your channel...")
               speak("Opening  Your channel....")
               tsr.sleep(0.5)
               tsr.sleep(1)
               print("   ")
               func()
           elif "cart" in query:
               webbrowser.open("amazon.in/cart/")
               print("Opening Amazon Cart...")
               speak("Opening Amazon Cart....")
               tsr.sleep(0.5)
               tsr.sleep(1)
               print("   ")
               func()
           if "open amazon" in query:
               webbrowser.open("amazon.com")
               tsr.sleep(1)
               print("")
               func()
           if "open poki" in query:
               webbrowser.open("poki.com")
               tsr.sleep(1)
               print("")
               func()
           elif "open gmail" in query:
               webbrowser.open("https://mail.google.com/mail/u/0/#inbox/")
               print("Opening Gmail...")
               #speak("Opening Gmail....")
               tsr.sleep(0.4)
               tsr.sleep(1)
               print("")
               func()
               #searching 
                  
           elif "google" in query:
               search = input("Search Google :")
               print("Searching Google.....")
               speak("Searching Google.....")
               tsr.sleep(0.5)
               webbrowser.open("https://www.google.com/search?q="+search)
               tsr.sleep(1)
               print("    ")
               func()
        
           elif "youtube" in query:
               y_search = input("Search Youtube :").lower()
               print("Searching Youtube...")
               speak("Searching Youtube....")
               tsr.sleep(0.5)
               pywhatkit.playonyt(y_search)
               tsr.sleep(1)
               print("   ")
               func()
           elif "poki" in query:
               p_search = input("Search game:  ")
               print("Searching Poki...")
               speak("Searching Poki....")
               tsr.sleep(0.5)
               webbrowser.open("https://poki.com/en/g/"+p_search)
               tsr.sleep(1)
               print("   ")
               func() 
           elif "amazon" in query:
               amazon_search = input("Search amazon:  ")
               print("Searching Amazon...")
               speak("Searching Amazon....")
               tsr.sleep(0.5)
               webbrowser.open("https://www.amazon.in/s?k="+amazon_search)
               tsr.sleep(1)
               print("   ")
               func() 
           elif "open website" in query:
               link = input("Enter the link of the website you want to get redirected to: ")
               print("Opening website....")
               speak("Opening website....")
               webbrowser.open(link)
               tsr.sleep(1)
               print(" ")
               func()
           elif "images" in query:
               img_search = input("Enter the name of the image you want to search: ")
               print("Searching Images...")
               speak("Searching Images....")
               img_link = "=img"
               webbrowser.open("https://www.google.com/search?q="+img_search)
               tsr.sleep(1)
               print(" ")
               func()
           #baisc commands
           elif "what is my name" in query:
               speak("Your name is Shriniketan Sir!")
               tsr.sleep(1)
               print("")
               func()
           elif "what is your name" in query:
               speak("My name is Chappie, Sir!")
               tsr.sleep(1)
               print("")
               func()
               
           elif "time" in query:
               strTime = datetime.datetime.now().strftime("%H:%M:%S")    
               print(strTime)
               speak(f"Sir, the time is {strTime}")
               tsr.sleep(1)
               print("")
               func()
            
           elif "shutdown" in query:
               speak(f"Your device will shutdown in {sec} seconds sir!")
               os.system(f'shutdown /s /t {sec}')     
           elif "i am very happy" or "i am feeling happy" in query:
               speak("Nice Sir! Always be happy, and keep your surroundings happy.")
               print("Nice Sir! Always be happy, and keep your surroundings happy.")
               print(" ")
               tsr.sleep(1)
               func()
           elif "bye" in query:
               speak("Bye Sir! Have a good day!")
               print("Collapsing All windows....")
               tsr.sleep(0.5)
               os.system("taskkill /f /im code.exe")
           elif "quit" in query:
               speak("Bye sir! have a good day")
               print("Collapsing All windows....")
               tsr.sleep(0.5)
               os.system("taskkill /f /im code.exe")
           elif "i am sad" or "my mood is off" or "i feel depressed" or  "i am depressed" in query:
               speak("Don't worry sir! everything will be, alright. Be relaxed ,and don't ,take much stress.")
               print("Don't worry sir! everything will be alright. Be relaxed and don't take much stress.")
               print(" ")
               tsr.sleep(1)
               func()      
           elif "open code" in query:
               os.startfile("C:\\Users\Turpu Kartikeya Rao\AppData\Local\Programs\Microsoft VS Code\Code.exe")
               print(" ")
               tsr.sleep(1)
               func()
           elif "thank you" or "thanks" in query:
               speak("Always at your service sir")
               print("Always at yout service sir :)")
               print("")
               tsr.sleep(1)
               func()
           else:
               print("Wrong Command! Try Again")
               speak("Wrong Command! Try Again")
               func()
func()