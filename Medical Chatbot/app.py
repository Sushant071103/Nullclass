# app.py
'''
import streamlit as st
import pandas as pd
from utils.preprocessing import load_medquad_data
from model.retrieval import Retriever
from model.ner import extract_entities

# Streamlit Page Title
st.set_page_config(page_title="Medical Q&A Chatbot", layout="centered")
st.title("🩺 Medical Q&A Chatbot")
st.write("Ask any medical question related to diseases, symptoms, or treatments!")

# Load MedQuAD dataset
@st.cache_data
def load_data():
    return load_medquad_data("data/medquad/")

qa_df = load_data()

# Check if required columns are present
if "question" not in qa_df.columns or "answer" not in qa_df.columns:
    st.error("Error: Dataset does not contain required 'question' and 'answer' columns.")
    st.stop()

# (Optional) Debug: Show first few rows
# st.write("Sample of loaded data:")
# st.dataframe(qa_df.head())

# Initialize Retriever
retriever = Retriever(qa_df["question"].tolist())

# User Input
user_question = st.text_input("Enter your medical question:")

if user_question:
    # Step 1: Retrieve Best Answer
    answer = retriever.retrieve_best_answer(user_question, qa_df)

    # Step 2: Extract Medical Entities
    entities = extract_entities(user_question)

    # Step 3: Display Results
    st.subheader("📋 Retrieved Answer:")
    st.success(answer)

    st.subheader("🧬 Detected Medical Entities:")
    if any(entities.values()):
        st.json(entities)
    else:
        st.info("No specific medical entities detected.")

# Footer
st.markdown("---")
st.markdown("Created using the MedQuAD dataset. Educational purposes only.")
'''





















# app.py

import streamlit as st
import pandas as pd
from utils.preprocessing import load_medquad_data
from model.retrieval import Retriever
# Commented because NER is not needed anymore
# from model.ner import extract_entities

# Streamlit Page Title
st.set_page_config(page_title="Medical Q&A Chatbot", layout="centered")
st.title("🩺 Medical Q&A Chatbot")
st.write("Ask any medical question related to diseases, symptoms, or treatments!")

# Load MedQuAD dataset
@st.cache_data
def load_data():
    return load_medquad_data("data/medquad/")

qa_df = load_data()

# Check if required columns are present
if "question" not in qa_df.columns or "answer" not in qa_df.columns:
    st.error("Error: Dataset does not contain required 'question' and 'answer' columns.")
    st.stop()

# Initialize Retriever
retriever = Retriever(qa_df["question"].tolist())

# User Input
user_question = st.text_input("Enter your medical question:")

if user_question:
    # Step 1: Retrieve Best Answer
    answer = retriever.retrieve_best_answer(user_question, qa_df)

    # Step 2: Display Results
    st.subheader("📋 Retrieved Answer:")
    st.success(answer)

# Footer
st.markdown("---")
st.markdown("Created using the MedQuAD dataset. Educational purposes only.")

