import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() # Initialize the speech recognizer
engine = pyttsx3.init() # Initialize the text-to-speech engine
voices = engine.getProperty('voices') # Get the voices available
engine.setProperty('voice', voices[1].id) # Set the voice to the second voice


def talk(text): # Define the function to talk   
    engine.say(text) # Say the text
    engine.runAndWait() # Run and wait for the text to be spoken    


def take_command(): # Define the function to take a command
    try:
        with sr.Microphone() as source:
            print('listening...') # Print the message to the console
            voice = listener.listen(source) # Listen to the voice
            command = listener.recognize_google(voice)
            command = command.lower() # Convert the command to lowercase
            if 'partner' in command:
                command = command.replace('partner', '') # Replace the word 'partner' with an empty string
                print(command) # Print the command to the console
    except:
        pass
    return command # Return the command

def run_partner():
    command = take_command() # Take the command

    print(command) # Print the command to the console
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song) # Talk the song

        pywhatkit.playonyt(song) # Play the song on YouTube "playonyt(play on youtube)"
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') # Get the current time (I: hour, M: minute, p: period)
        talk('Current time is ' + time) # Talk the current time

    elif 'search' in command:
        person = command.replace('search', '') # Replace the word 'search' with an empty string
        info = wikipedia.summary(person, 1) # Get the summary of the person
        print(info) # Print the summary to the console
        talk(info) # Talk the summary

    elif 'who is your creator' in command: # If the command is 'who is your creator'        (single quotes are used to avoid the apostrophe in the string)      
        talk('I was created by a Praveen to assist and communicate effectively. They did a great job, don’t you think?') # Talk the creator

    elif 'what can you do' in command: # If the command is 'what can you do'
        talk('I can perform a variety of tasks like searching for information, answering questions, and helping you stay productive. What would you like me to do first?') # Talk the tasks

    elif 'who are you' in command: # If the command is 'who are you'
        talk('I am your virtual assistant, designed to make your work easier and more efficient. How can I assist you today?') # Talk the assistant
        
    elif 'joke' in command: # If the command is 'joke'
        talk(pyjokes.get_joke()) # Talk the joke
    else: # If the command is not recognized
        talk('Please say the command again.') # Talk the command again


while True:
    run_partner()