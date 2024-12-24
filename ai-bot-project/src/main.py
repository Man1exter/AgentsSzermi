# FILE: /ai-bot-project/ai-bot-project/src/main.py
from bot import Bot
from audio import record_audio, play_audio

def main():
    bot = Bot()
    bot.start_conversation()

    while True:
        user_input = record_audio()
        response = bot.respond_to_input(user_input)
        play_audio(response)

if __name__ == "__main__":
    main()