def text_processing(text):
    # Function to process text input
    return text.strip().lower()

def log_message(message):
    # Function to log messages
    with open('log.txt', 'a') as log_file:
        log_file.write(message + '\n')