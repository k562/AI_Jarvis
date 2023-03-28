import pyttsx3 # pip install pyttsx3 
import datetime
import speech_recognition as sr #pip install SpeecRegonition
import language 
import pyaudio
import wikipedia # pip install wikipedia 
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("ohhh hello sir,Welcome back")
 
    time()
    
    date()
    hour = datetime.datetime.now().hour 
    if hour >= 6 and hour<12:
        speak ("Good morning sir ")
    elif hour  >=12 and hour<18:
        speak("Good after noon sir")
    elif hour  >=18 and  hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")           
    speak("jarvis at your service .Please tell me how can i help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print ("Recongizing...")
        query = r.recognize_google(audio,language='en-in'  )
        print(query)

    except Exception as e:
        print(e)
        speak ("Say  that again please ...")


        return "None"
    return query   

def sendEmail(to, content):
    server  = smtplib.SMTP('smtp.gmail.com',587) 
    server.echo()
    server.starttls()
    server.login('kaushikkaransinghkks@gmail.com','9852564774')
    server.sendmail('kaushikkaransinghkks@gmail.com',to,content)
    server.close()
    
if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query= query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print (result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendEmail(to,content)

                speak("Email has been sent successfully . sir")
            except Exception as e :
                print(e)
                speak("Unable to send the email , got some technical network issue or technical issue you can say")

        elif 'search in chrome' in  query:
            speak("what should i search sir?")
            chromepath = 'C:/Program Files (x86)/Google/chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif 'logout' in query:
            speak("okay sir sytem is going to be shudown")
            os.system("shutdown -1")

        elif 'shutdown' in query:
            speak("okay sir the system is going to be shudown")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("okay sir the system is going to be restart")
            os.system("shutdown /r /t 1")    

        elif 'offline' in query:
            speak("Good bye sir , have a good day  asshole ")
            quit()
                
