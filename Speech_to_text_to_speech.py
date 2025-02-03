import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen_and_respond():
    # Use the microphone as the source of audio input
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        # Recognize the speech and convert it to text
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        
        # Customize responses based on the command
        if "hello" in command.lower():
            response = "Hi, how can I assist you today?"
            print('Hi, how can I assist you today?')
        elif "how are you" in command.lower():
            response = "I'm just a program, but I'm doing great, thanks for asking!"
        elif "time" in command.lower():
            import time
            response = f"The current time is {time.strftime('%H:%M:%S')}"
        elif "bye" in command.lower():
            response = "Goodbye! Have a great day!"
        else:
            
            response = engine.say('I dont have answer for this so Im just repeating it')
            response= engine.say(command)
            response = 'This model is in still under development so I know only the answers of hello, How are you, what"s the time and bye. Thank you for talking with me see you soon'
        # Respond to the command
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        engine.say("Sorry, I could not understand the audio.")
        engine.runAndWait()
    
    except sr.RequestError:
        print("Sorry, the speech recognition service is unavailable.")
        engine.say("Sorry, the speech recognition service is unavailable.")
        engine.runAndWait()

# Run the function to listen and respond
listen_and_respond()
