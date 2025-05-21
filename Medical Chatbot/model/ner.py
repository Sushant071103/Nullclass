# model/ner.py

import re

# Simple medical keywords for basic NER (expand as needed)
SYMPTOMS = ["fever", "cough", "headache", "nausea", "fatigue", "pain", "dizziness"]
DISEASES = ["diabetes", "cancer", "heart disease", "asthma", "arthritis", "stroke"]
TREATMENTS = ["chemotherapy", "radiation", "insulin", "surgery", "therapy", "medication"]

def extract_entities(user_query):
    """
    Extracts basic medical entities (symptoms, diseases, treatments) from the user query.

    Args:
        user_query (str): User's input query.

    Returns:
        dict: Extracted entities categorized by type.
    """
    user_query = user_query.lower()

    detected_symptoms = [word for word in SYMPTOMS if re.search(rf'\b{word}\b', user_query)]
    detected_diseases = [word for word in DISEASES if re.search(rf'\b{word}\b', user_query)]
    detected_treatments = [word for word in TREATMENTS if re.search(rf'\b{word}\b', user_query)]

    return {
        "symptoms": detected_symptoms,
        "diseases": detected_diseases,
        "treatments": detected_treatments
    }
