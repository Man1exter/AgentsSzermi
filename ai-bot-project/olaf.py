import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import openai

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key'

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def respond(text):
    if text:
        ai_response = get_ai_response(text)
        print(f"AI response: {ai_response}")
        tts = gTTS(text=ai_response, lang='en')
        filename = "response.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

if __name__ == "__main__":
    while True:
        user_input = listen()
        respond(user_input)