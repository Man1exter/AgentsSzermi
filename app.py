from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    bot_reply = response['choices'][0]['message']['content']
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
