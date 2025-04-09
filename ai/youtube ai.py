import pyttsx3
import speech_recognition as sr


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',160)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.microphone() as source:
            print('listening....')
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            command= command.lower()
            print(command)
            return command
    except:
        return " __"
    
def run_jarvis():
        command= take_command()
        if 'hello' in command :
            talk('hi boss how are you')
        elif 'exit' in command:
            talk('goodBye!')
            exit()
        else:
            talk(" i dont understand")


talk('hello billi kya dhekh rhi ho?')

while True:
    run_jarvis()
