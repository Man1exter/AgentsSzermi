import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
import openai

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key'

class OlafApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olaf AI Chatbot")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setStyleSheet("padding: 10px; font-size: 16px;")
        self.layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet("padding: 10px; font-size: 16px;")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.response_area = QTextEdit(self)
        self.response_area.setReadOnly(True)
        self.response_area.setStyleSheet("padding: 10px; font-size: 16px;")
        self.layout.addWidget(self.response_area)

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
        # Replace this with your own AI bot logic
        return "This is a response from your custom AI bot."

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OlafApp()
    window.show()
    sys.exit(app.exec())