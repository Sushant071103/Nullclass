import json

# Load existing knowledge base (intents.json)
def load_intents():
    try:
        with open('intents.json', 'r') as file:
            intents_data = json.load(file)
    except FileNotFoundError:
        intents_data = {"intents": []}  # If the file doesn't exist, start with an empty knowledge base
    return intents_data

# Function to add new Q&A pairs (new intents) to the knowledge base
def add_to_knowledge_base(new_intent):
    intents_data = load_intents()  # Load the existing knowledge base
    intents_data["intents"].append(new_intent)  # Append the new intent

    # Save the updated knowledge base back to the file
    with open('intents.json', 'w') as file:
        json.dump(intents_data, file, indent=4)
    print("New intent added successfully!")

# Example of a new Q&A pair to be added to the knowledge base
new_intent = {
    "tag": "headache",
    "patterns": ["How can I relieve a headache?", "What are the symptoms of a headache?"],
    "responses": ["You can relieve a headache by drinking water, resting, and using over-the-counter medication."]
}

# Add the new intent to the knowledge base
add_to_knowledge_base(new_intent)
