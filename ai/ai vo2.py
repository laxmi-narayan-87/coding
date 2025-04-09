import time
import datetime
import numpy as np
import openai
import random
from scipy.io.wavfile import write
import sounddevice as sd
import pyttsx3
import os
from dotenv import load_dotenv

# Set your OpenAI API key here
load_dotenv()

# Ensure that the API key is set only if it's not already set
if not openai.api_key:
    openai.api_key = os.getenv("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")

# Global variable to store audio data
audio = []

# Adjectives to generate random names for voices
adjectives = ["beautiful", "sad", "mystical", "serene", "whispering", "gentle", "melancholic"]
nouns = ["sea", "love", "dreams", "song", "rain", "sunrise", "silence", "echo"]

# Initializing pyttsx for text-to-speech output
engine = pyttsx3.init()
engine.setProperty('rate', 10)

# Record the time of the last API call
last_api_call_time = datetime.datetime.now()

def can_make_api_call():
    global last_api_call_time
    elapsed_time = datetime.datetime.now() - last_api_call_time
    return elapsed_time.total_seconds() >= 60  # 60 seconds interval

def delay_between_requests():
    time.sleep(60)  # Adjust the delay duration based on OpenAI API rate limits

    
def generate_random_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

def new_record_audio():
    print("Recording... Press 's' to stop.")
    fs = 44100
    seconds = 6
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    audio_name = generate_random_name()
    write(f'./{audio_name}.wav', fs, myrecording)  # Save as WAV file
    print("Recording stopped.")
    return f'./{audio_name}.wav'


# Global variable to store the count of API calls
api_call_count = 0

def display_request_rate():
    global api_call_count
    print(f"Total API Calls: {api_call_count}")



def transcribe_audio(audio_path):
    global api_call_count
    print("Entered transcribe", "./" + audio_path)
    audio_file = open(audio_path, "rb")
    
    try:
        if can_make_api_call():
            delay_between_requests()
        api_call_count += 1  # Increment the API call count
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        print(transcript)
        return transcript['text']
    except openai.error.RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
        return "Rate limit exceeded. Please try again later."
    finally:
        display_request_rate()  # Display the request rate after each API call




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
        transcript = transcribe_audio(recorded_audio_path)
        # Create a list of messages with the user's input
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": transcript}
        ]
        print("Transcript:")
        print(transcript)
        # Make the API call for gpt AI
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response = completion.choices[0].message["content"]
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
