from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if you have access
        messages=[
            {"role": "system", "content": "You are a helpful college assistant bot."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response['choices'][0]['message']['content'].strip()
    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
