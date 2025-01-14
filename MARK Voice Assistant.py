import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio as p
import wikipedia 
import webbrowser
import os 
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("I am Mark. How may i help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearinng...")
        r.pause_thresshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
    # print(e)
        print("Say that again please.... ")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Here you go to youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to google\n")
            webbrowser.open("google.com")
        
        elif 'play video' in query:
            speak("here you go with videos music")
            music_dir = "E:\\songs videos"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)

        elif 'how are you' in query:
            speak("I am fine, what about you?")

        elif 'fine' in query:
            speak("i am also good")

        elif 'joke' in query:
            joke= pyjokes.get_joke(language='en', category='all')
            speak(pyjokes.get_joke())
            print(joke)

        elif 'exit' in query:
            speak("Thanks for giving your precious time")
            exit()

        elif 'who made you' in query:
            speak("i have been created by Mark team")

        elif 'who are you' in query:
            speak("i am your minor project")

        

        

            

        
        

    

        


        

       


        


        
        
         
           
           


