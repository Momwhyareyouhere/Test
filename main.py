import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said: ", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def assistant():
    speak("Hello! I am your Python assistant. How can I help you today?")
    
    while True:
        speak("What can I do for you?")
        command = listen()

        if command:
            if "exit" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    assistant()
