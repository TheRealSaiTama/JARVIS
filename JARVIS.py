import os
import subprocess
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import sounddevice as sd
import numpy as np
import wavio
import smtplib
import webbrowser as wb
import psutil
import pyjokes

engine = pyttsx3.init()
engine.setProperty('rate', 135)
engine.setProperty('volume', 2.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%A, %B %d, %Y, %I:%M %p")
    speak(Time)


def wishme():
    speak("Welcome back sir!")
    speak("The current time is")
    time()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning sir!")
    elif 12 <= hour <= 18:
        speak("Good afternoon sir!")
    elif 18 <= hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("Jarvis at your service sir. Please tell me how can I help you?")


def takeCommand():
    fs = 44100
    seconds = 5

    print("Listening...")
    audio = sd.rec(int(fs * seconds), samplerate=fs, channels=1)  # Mono recording for speech recognition
    sd.wait()

    # recognizer = sr.Recognizer()

    try:
        print("Recognizing...")
        wavio.write("output.wav", audio, fs, sampwidth=2)

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio_data = recognizer.record(source)  # Read the saved WAV file
            query_str = recognizer.recognize_google(audio_data, language='en-in')  # Perform online speech recognition

        print(f"User said: {query_str}\n")

    #       query_bytes = audio.tobytes()  # Convert the audio data to bytes
    #      query_str = recognizer.recognize_sphinx(query_bytes, language='en-in')  # Recognize the speech using Google API
    #     print(f"User said: {query_str}\n")

    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("Say that again")
        return "None"

    except Exception as e:
        print(e)
        speak("Say that again")
        return "None"
    return query_str


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('keshavsde@gmail.com', 'Keshav8527')
    server.sendmail('keshavsde@gmail.com', to, content)
    server.close()


def screenshot():
    subprocess.run(['scrot', 'screenshot.png'])

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()
        elif 'offline' in query:
            quit()
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple options. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any information on that topic.")
            except wikipedia.exceptions.WikipediaException as e:
                speak("Sorry, there was an error processing your request.")

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = 'mansecret490@gmail.com'
                sendemail(to, content)
                speak(content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'search in chrome' in query:
            speak("What should i search")
            firefoxpath = '/usr/bin/firefox'
            search = takeCommand().lower()
            wb.get(firefoxpath).open_new_tab(search + '.com')
        elif 'logout' in query:
            # os.system("shutdown -l")
            os.system("mate-session-save --logout-dialog")  # for my linux
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play songs' in query:
            songs_dir = '/home/keshav/Music'
            songs = os.listdir(songs_dir)
            # os.startfile(os.path.join(songs_dir, songs[0])) #for windows only
            selected_songs = os.path.join(songs_dir, songs[0])
            subprocess.run(["xdg-open", selected_songs])
        elif 'remember that' in query:
            speak("What should i remember")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()