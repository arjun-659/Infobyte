import speech_recognition as sr
import pyttsx3 as pt
import datetime
import webbrowser
import pywhatkit as pwk

#speech recognizer
recognizer = sr.Recognizer()

#text-to-speech
speech = pt.init()
def speak(text):
    speech.say(text)
    speech.runAndWait()

#recognize speech
def listen():
    with sr.Microphone() as source:
        print("Speak...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry Mani, I could not understand. Can you please repeat?")
            query = None

    return query

# Function to greet the user based on the time of the day
def greet():
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 12:
        speak("Good morning Mani!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon Mani!")
    else:
        speak("Good evening Mani!")

def search(query):
    speak(f"Searching for {query} on the web...")
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

# Main function
def main():
    greet()
    speak("I am your voice assistant. How can I help you ?")

    while True:
        query = listen()

        if query:
            #hello
            if "hello" in query.lower():
                print("Hello! How can I help you Mani?")
                speak("Hello! How can I help you Mani?")

            #time
            elif "time" in query.lower():
                current_time = datetime.datetime.now().strftime("%H:%M")
                print(f"The time is {current_time}")
                speak(f"The time is {current_time}")

            #date
            elif "date" in query.lower():
                date_today = datetime.datetime.now().strftime('%B %d, %Y')
                print(f"The date is {date_today}")
                speak(f"The date is {date_today}")

            #chrome
            elif "chrome" in query.lower():
                print("Opening Chrome...")
                speak("Opening Chrome")
                webbrowser.open("chrome.com")

            #wikipedia
            elif "wikipedia" in query.lower():
                print("Opening wikipedia...")
                speak("Opening wikipedia")
                webbrowser.open("wikipedia.com")

            #spotify
            elif "music" in query.lower():
                print("Opening spotify...")
                speak("Opening spotify")
                webbrowser.open("spotify.com")

            #linkedin
            elif "linkedin" in query.lower():
                print("Opening linkedin...")
                speak("Opening linkedin")
                webbrowser.open("linkedin.com")

            #youtube
            elif "youtube" in query.lower():
                print("Opening Youtube...")
                speak("Opening Youtube")
                webbrowser.open("youtube.com")
                #pwk.playonyt("Play (opens_what_we_need) ")

            #thankyou
            elif "thank you" in query.lower():
                print("you're welcome Mani")
                speak("you're welcome Mani")

            #exit or quit or bye
            elif "exit" in query.lower() or "quit" in query.lower() or "bye" in query.lower():
                print("Goodbye Mani!")
                speak("Goodbye Mani!")
                break

            else:
                speak("Sorry, I don't understand. Can you please repeat?")

if __name__ == "__main__":
    main()