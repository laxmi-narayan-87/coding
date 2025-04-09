import numpy as np
import openai
import random
from scipy.io.wavfile import write
import sounddevice as sd
import pyttsx3
import os

# Set your OpenAI API key here
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("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")
openai.api_key = api_key


# Global variable to store audio data
audio = []

# Adjectives to generate random names for voices
adjectives = ["beautiful", "sad", "mystical", "serene", "whispering", "gentle", "melancholic"]
nouns = ["sea", "love", "dreams", "song", "rain", "sunrise", "silence", "echo"]
#initializing pytts for text to speech output
engine = pyttsx3.init()
engine.setProperty('rate', 130)

 
def generate_random_name():
    # to generate random unique names for the audio voice recordings
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

def new_record_audio():
    # to record audio as wav file
    print("Recording... Press 's' to stop.")
    fs = 44100
    seconds = 6
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    audio_name = generate_random_name()
    write(f'./{audio_name}.wav', fs, myrecording)  # Save as WAV file 
    print("Recording stopped.")
    return f'./{audio_name}.wav'
    
def generate_response(transcript):
        chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
)
    
    # Create a list of messages with the user's input
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": transcript}
    ]
    # Make the API call for gpt AI
        chat_completion = openai.ChatCompletion.create(
        engine="text-davinci-002",
        prompt=transcript,
        max_tokens=150
        )
        response = completion.choices[0].text.strip()
        return response



def speech_to_text(response):
    # to generate the final output voice from text
    engine.say(response)
    engine.runAndWait()




def main():
    while True:
        print("Press 's' to stop recording and transcribe the audio.")
        # Start recording live voice input
        recorded_audio_path = new_record_audio()
        print("Recording stopped. Transcribing audio...")
        # Save the recorded audio as a WAV file
        print("Recorded audio saved to:", recorded_audio_path)
        print("----end---")
        # Transcribe the audio
        transcript = generate_response(recorded_audio_path)
        # Create a list of messages with the user's input
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": transcript}
        ]
        print("Transcript:")
        print(transcript)
        # Make the API call for gpt AI
        response = generate_response(transcript)
        
        # Print the assistant's response
        print("Assistant:", response)
        
        # Convert output to voice
        speech_to_text(response)

        # Ask whether to continue or stop
        user_choice = input("Continue? (y/n): ")
        if user_choice.lower() != "y":
            print("Glad to help bye!")
            break  # Exit the loop if the user doesn't want to continue

if __name__ == "__main__":
    main()

#Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key. Run the script, and it will start recording your voice input. Press the 's' key when you're #done speaking to stop the recording and transcribe the audio using OpenAI's Whisper API. The transcribed text will be displayed in the console.
