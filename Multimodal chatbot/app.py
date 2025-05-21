import streamlit as st
from utils.text_utils import generate_text
from utils.image_utils import analyze_image

st.set_page_config(page_title="Multi-Modal Chatbot", layout="wide")
st.title("🧠 Multi-Modal Chatbot (Text + Image)")

user_input = st.text_input("Type your message:")
image_file = st.file_uploader("Or upload an image", type=["jpg", "jpeg", "png"])

if st.button("Send"):
    with st.spinner("Thinking..."):
        if image_file:
            response = analyze_image(image_file)
            st.image(image_file, caption="Uploaded Image", use_column_width=True)
            st.markdown("**Gemini Vision Output:**")
            st.write(response)
        elif user_input:
            response = generate_text(user_input)
            st.markdown("**Gemini Text Response:**")
            st.write(response)
        else:
            st.warning("Please enter text or upload an image.")
