import pandas as pd
import random
import os

# Create folder if not exists
os.makedirs("data/medquad", exist_ok=True)

# Sample templates
symptoms = ["fever", "cough", "headache", "fatigue", "dizziness", "nausea", "chest pain", "shortness of breath", "vomiting", "rash"]
diseases = ["diabetes", "cancer", "heart disease", "asthma", "arthritis", "stroke", "flu", "COVID-19", "hypertension", "pneumonia"]
treatments = ["chemotherapy", "insulin therapy", "surgery", "radiation therapy", "physical therapy", "antibiotics", "vaccination", "lifestyle changes", "medication", "oxygen therapy"]

questions = []
answers = []

# Generate around 500 entries
for _ in range(500):
    type_of_q = random.choice(["symptom", "cause", "treatment", "diagnosis", "definition"])
    disease = random.choice(diseases)
    symptom = random.choice(symptoms)
    treatment = random.choice(treatments)

    if type_of_q == "symptom":
        q = f"What are the symptoms of {disease}?"
        a = f"Common symptoms of {disease} include {symptom}, fatigue, and difficulty breathing."
    elif type_of_q == "cause":
        q = f"What causes {disease}?"
        a = f"{disease} may be caused by genetic factors, lifestyle habits, infections, or other health conditions."
    elif type_of_q == "treatment":
        q = f"How is {disease} treated?"
        a = f"Treatment for {disease} typically includes {treatment}, lifestyle changes, and regular medical monitoring."
    elif type_of_q == "diagnosis":
        q = f"How is {disease} diagnosed?"
        a = f"{disease} is diagnosed through medical history evaluation, physical exams, imaging studies, and laboratory tests."
    else:
        q = f"What is {disease}?"
        a = f"{disease} is a medical condition that affects the body, often requiring long-term management and treatment."

    questions.append(q)
    answers.append(a)

# Create DataFrame
df = pd.DataFrame({
    "question": questions,
    "answer": answers
})

# Save CSV
output_path = "data/medquad/medquad_clean.csv"
df.to_csv(output_path, index=False, encoding='utf-8')

print(f"✅ Dataset created and saved to {output_path} with {len(df)} entries!")
