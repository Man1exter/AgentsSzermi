# AI Bot Project

This project is an AI bot designed to communicate through headphones. It utilizes audio input and output to facilitate interaction with users.

## Project Structure

```
ai-bot-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── bot              # Contains the Bot class for processing input and generating responses
│   ├── audio            # Handles audio input and output
│   └── utils            # Utility functions for various tasks
├── requirements.txt     # Lists project dependencies
├── tts.py               # Text-to-speech functionality
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-bot-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

To run the AI bot, execute the following command:
```
python src/main.py
```

Follow the prompts to interact with the bot through your headphones.

## Text-to-Speech

To use the text-to-speech functionality, you can call the `text_to_speech` function from the `tts.py` module:
```python
from tts import text_to_speech

text_to_speech("Hello, this is a test.")
```