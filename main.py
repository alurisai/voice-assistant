import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from YT_audio import music  # Updated import
import randfacts
from jokes import joke
import datetime
import requests

# Initializing the text-to-speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  # Separate the arguments
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()


def wishme():
    """Return appropriate greeting based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 8 < hour < 12:
        return "morning"
    elif 12 <= hour < 16:
        return "afternoon"
    else:
        return "evening"


def listen(recognizer):
    """Listens for commands and returns them as text."""
    with sr.Microphone() as source:
        recognizer.energy_threshold = 10000
        recognizer.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")
            return None


def fetch_news():
    """Fetches the latest news headlines."""
    try:
        api_key = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-24&sortBy=publishedAt&apiKey=7163fdcb0d794b6d93da7fee862d2618"  # Replace with your actual news API key
        url = f'http://newsapi.org/v2/top-headlines?country=us&apiKey=7163fdcb0d794b6d93da7fee862d2618'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        headlines = [article['title'] for article in articles[:5]]
        return headlines
    except Exception as e:
        print(f"Failed to fetch news: {e}")
        speak("Sorry, I am unable to fetch news at the moment.")
        return []


def main():
    today_date = datetime.datetime.now()
    r = sr.Recognizer()

    speak(f"Hello sir, good {wishme()} I am Friday.")
    speak(
        f"Today is {today_date.strftime('%d')} of {today_date.strftime('%B')} and it's currently {today_date.strftime('%I:%M %p')}.")

    speak("What can I do for you?")

    while True:
        text = listen(r)
        if text:
            if "stop" in text.lower():
                speak("Stopping the program. see you later!")
                break

            if "how" in text.lower() and "about" in text.lower() and "you" in text.lower():
                speak("I am also having a good day sir.")

            elif "information" in text.lower():
                speak("You need information on which topic?")
                infor = listen(r)
                if infor:
                    speak(f"Searching {infor} in Wikipedia")
                    print(f"Searching {infor} in Wikipedia")
                    assist = infow()
                    assist.get_info(infor)

            elif "play" in text.lower() and "video" in text.lower():
                speak("You want me to play which video?")
                vid = listen(r)
                if vid:
                    print(f"Playing {vid} on YouTube")
                    speak(f"Playing {vid} on YouTube")
                    yt_assist = music()  # Ensure the updated class is being used
                    yt_assist.play(vid)

            elif "news" in text.lower():
                speak("Sure sir, now I will read news for you.")
                news_items = fetch_news()
                for news_item in news_items:
                    print(news_item)
                    speak(news_item)

            elif "fact" in text.lower() or "facts" in text.lower():
                speak("Sure sir,")
                x = randfacts.getFact()
                print(x)
                speak("Did you know that, " + x)

            elif "joke" in text.lower() or "jokes" in text.lower():
                speak("Sure sir, get ready for some chuckles")
                arr = joke()
                print(arr[0])
                speak(arr[0])
                if len(arr) > 1:
                    print(arr[1])
                    speak(arr[1])

            speak("What can I do for you?")


if __name__ == "__main__":
    main()



