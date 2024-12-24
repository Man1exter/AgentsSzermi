import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QFont
import openai

# Set your OpenAI API key here
openai.api_key = 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

class OlafApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olaf AI Chatbot")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.layout = QVBoxLayout()

        self.header = QLabel("Olaf AI Chatbot", self)
        self.header.setFont(QFont("Arial", 24))
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setStyleSheet("padding: 20px; color: #333;")
        self.layout.addWidget(self.header)

        self.response_area = QTextEdit(self)
        self.response_area.setReadOnly(True)
        self.response_area.setStyleSheet("""
            padding: 10px;
            font-size: 16px;
            border: 2px solid #ccc;
            border-radius: 5px;
            background-color: #ffffff;
            color: #333;
        """)
        self.layout.addWidget(self.response_area)

        self.input_layout = QHBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setStyleSheet("""
            padding: 10px;
            font-size: 16px;
            border: 2px solid #ccc;
            border-radius: 5px;
            background-color: #ffffff;
            color: #333;
        """)
        self.input_layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet("""
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
        """)
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)

        self.layout.addLayout(self.input_layout)
        self.setLayout(self.layout)

    @Slot()
    def send_message(self):
        user_input = self.input_field.text()
        if user_input:
            self.response_area.append(f"You: {user_input}")
            ai_response = self.get_ai_response(user_input)
            self.response_area.append(f"Olaf: {ai_response}")
            self.input_field.clear()

    def get_ai_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OlafApp()
    window.show()
    sys.exit(app.exec())