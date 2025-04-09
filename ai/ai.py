from openai import OpenAI
client = OpenAI()

audio_file = open(C:\Users\lalkr\AppData\Local\Temp\728c7cd9-aae7-472f-83b0-7de4178cf00a_harvard.wav.zip.00a\harvard.wav, "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
{
  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that."
}
