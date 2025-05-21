import streamlit as st
import json
import random

# Load the intents from the intents.json file
def load_intents():
    with open('intents.json') as file:
        intents = json.load(file)
    return intents

# Simple function to predict a response based on user input
def get_response(user_input):
    intents = load_intents()
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

# Streamlit UI
st.title("Chatbot")

user_input = st.text_input("You: ", "")

if user_input:
    response = get_response(user_input)
    st.write("Bot: ", response)
