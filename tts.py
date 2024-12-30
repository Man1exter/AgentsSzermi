# This module provides text-to-speech functionality using the pyttsx3 library.

import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    # Convert text to speech
    engine.say(text)
    # Wait for the speech to complete
    engine.runAndWait()
