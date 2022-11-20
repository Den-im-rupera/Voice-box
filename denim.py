import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as web
import os
import requests
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
web.register('chrome', None, web.BackgroundBrowser(chrome_path))

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening sir !")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"you said: {query} \n")
    except Exception as e:
        print(e)
        speak("say it again sir !")
        return "None"
    return query


def kelvin_to_celsious(kVal):
    return int((kVal - 273.15))


def epoch_to_time(timestamp):
    result = datetime.datetime.fromtimestamp(timestamp)
    print(result)
    return result


if __name__ == "__main__":
    speak("Buddy, I am Denim, listening to your commands")

    while True:
        query = takeCommand().lower()
        # logic for execution based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
            except Exception as e:
                speak("No results")

        elif "open youtube" in query:
            # web.get(chrome_path).open("youtube.com")
            web.get('chrome').open_new_tab("youtube.com")

        elif "open google" in query:
            web.get('chrome').open_new_tab("google.com")
            # web.open("google.com")

        elif "open gmail" in query:
            # web.open("gmail.com")
            web.get('chrome').open_new_tab("gmail.com")

        elif "open vs code" in query:
            vscode = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscode)

        elif "open pgadmin" in query:
            pgadmin = "C:\\Program Files\\PostgreSQL\\14\\pgAdmin 4\\bin\\pgAdmin4.exe"
            os.startfile(pgadmin)

        elif "open chat" in query:
            # google_chat = "C:\\Users\\harsh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Google Chat.lnk"
            # google_chat = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe"
            # os.startfile(google_chat)
            pass

        elif "open docker" in query:
            docker = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
            os.startfile(docker)

        elif "dil jhoom jhoom" in query:
            dil_jhoom_jhoom = "https://www.youtube.com/watch?v=tfchHFd3CvU"
            web.get('chrome').open_new_tab(dil_jhoom_jhoom)

        elif "weather in ahmedabad" in query:
            try:
                openweather = f"http://api.openweathermap.org/data/2.5/weather?appid=09dea27793930ca6dc1161d3ab99e995&q=Ahmedabad"
                data = requests.get(openweather).json()
                temp = kelvin_to_celsious(data['main']['temp'])
                hum = data['main']['humidity']
                weather = data['weather'][0]['main']
                sunrise = epoch_to_time(data['sys']['sunrise'])
                sunset = epoch_to_time(data['sys']['sunset'])
                message = f"It feels like {weather}, sunrise was at {sunrise.hour} {sunrise.minute} AM, sunset was at {sunset.hour} {sunset.minute} PM, Temperature is {temp} degree celsious, and Humidity is {hum} percent, Have a good day"
                speak(message)
            except Exception as e:
                print(e)
                speak("No weather data available, My apology")
            # print(data)
            # pass

        elif "calculate love" in query:
            try:
                speak("Tell me Boy Name")
                boy_name = takeCommand().lower()
                speak("Tell me girl name")
                girl_name = takeCommand().lower()

                love_calc = f"https://love-calculator.p.rapidapi.com/getPercentage?sname={boy_name}&fname={girl_name}"

                headers = {
                    "X-RapidAPI-Key": "66120017f2msh160cb07eb40f4e6p10e744jsn2eb96ec0536e",
                    "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
                }

                data = requests.request("GET", love_calc, headers=headers).json()

                percent = data['percentage']
                luv_msg = data['result']

                message = f"{boy_name}, and {girl_name} You both love each other {percent} percent, {luv_msg}"
                speak(message)

            except Exception as e:
                print(e)
                speak("My apology")

        elif "mia khalifa" in query:
            speak("lund, gandu, lund, gandu, gandu, lund, lund, gandu")
            # speak("su maal che, aek number")

        elif "dani daniels" in query:
            speak("Bass kar paagal, rullaayega kya ?")

        elif "quit" in query:
            exit()
