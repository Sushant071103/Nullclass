# app.py

from flask import Flask, render_template, request, jsonify
from sentiment_utils import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']

    # Analyze sentiment
    sentiment = analyze_sentiment(user_message)

    # Prepare base sentiment message
    sentiment_message = f"Sentiment detected: {sentiment.capitalize()}. "

    # Generate appropriate response based on sentiment
    if sentiment == 'positive':
        bot_message = sentiment_message + "That's wonderful to hear! 😊 How else can I assist you?"
    elif sentiment == 'negative':
        bot_message = sentiment_message + "I'm sorry to hear that. 🙏 I'm here to help — tell me more!"
    else:  # neutral
        bot_message = sentiment_message + "Got it. Let's continue. What else would you like to discuss?"

    return jsonify({'bot_message': bot_message})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, use_reloader=False)
