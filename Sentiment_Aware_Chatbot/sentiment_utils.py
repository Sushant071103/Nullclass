# sentiment_utils.py

from textblob import TextBlob

# List of strong negative words
NEGATIVE_KEYWORDS = [
    "fail", "failed", "sad", "angry", "upset", "argument", "loss", "bad",
    "depressed", "hate", "worse", "pain", "severe", "unbearable", "deteriorating",
    "side effect", "complication", "infection", "injury"
]

# List of strong positive words
POSITIVE_KEYWORDS = [
    "success", "successful", "recovery", "recovering", "better", "improved",
    "healed", "healing", "good news", "relieved", "joy", "happy", "grateful"
]

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text.
    Returns 'positive', 'negative', or 'neutral'.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    lowered_text = text.lower()

    # Check strong negative words
    if any(word in lowered_text for word in NEGATIVE_KEYWORDS):
        return 'negative'

    # Check strong positive words
    if any(word in lowered_text for word in POSITIVE_KEYWORDS):
        return 'positive'

    # Then fallback to polarity
    if polarity > 0.5:
        return 'positive'
    elif polarity < -0.5:
        return 'negative'
    else:
        return 'neutral'
