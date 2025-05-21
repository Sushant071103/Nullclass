'''import streamlit as st
from langchain_community.llms import Ollama

# Initialize three different open-source LLMs
llm_llama3 = Ollama(model="llama3")
llm_mistral = Ollama(model="mistral")
llm_falcon = Ollama(model="falcon")

# Streamlit UI
st.title("📝 Article Generator Chatbot")
st.write("Generate high-quality articles using different open-source LLMs.")

# Model selection
tab1, tab2, tab3 = st.tabs(["LLaMA 3", "Mistral 7B", "Falcon 7B"])

# Function to generate article
def generate_article(llm, prompt):
    try:
        return llm(prompt)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return ""

with tab1:
    st.header("LLaMA 3")
    user_prompt1 = st.text_area("Enter your article topic:", "The Future of AI", key="ta_llama3")
    if st.button("Generate with LLaMA 3", key="btn_llama3"):
        with st.spinner("Generating with LLaMA 3..."):
            article = generate_article(llm_llama3, user_prompt1)
        st.write(article)

with tab2:
    st.header("Mistral 7B")
    user_prompt2 = st.text_area("Enter your article topic:", "The Future of AI", key="ta_mistral")
    if st.button("Generate with Mistral 7B", key="btn_mistral"):
        with st.spinner("Generating with Mistral 7B..."):
            article = generate_article(llm_mistral, user_prompt2)
        st.write(article)

with tab3:
    st.header("Falcon 7B")
    user_prompt3 = st.text_area("Enter your article topic:", "The Future of AI", key="ta_falcon")
    if st.button("Generate with Falcon 7B", key="btn_falcon"):
        with st.spinner("Generating with Falcon 7B..."):
            article = generate_article(llm_falcon, user_prompt3)
        st.write(article)

# Model Evaluation Report
st.subheader("📊 Model Performance Comparison")
st.write("### Evaluation Metrics:")
st.write("- **LLaMA 3:** High coherence, good factual accuracy, but may require fine-tuning.")
st.write("- **Mistral 7B:** Balanced response quality, generates concise and relevant content.")
st.write("- **Falcon 7B:** Strong in creativity and fluency but can sometimes hallucinate facts.")

st.write("### Final Recommendation:")
st.write("✅ **Mistral 7B** is the most suitable for article generation due to its balance between factual accuracy, coherence, and fluency.")
'''




















# ollama pull orca-mini, ollama pull stablelm2:1.6b, ollama pull tinyllama
import streamlit as st
from langchain_community.llms import Ollama

# Streamlit app config
st.set_page_config(page_title=" Article Generator Chatbot", page_icon="🧠")

# App Title
st.title("📝 Article Generator Chatbot")

# Model selection (ultra-light models only)
model_choice = st.selectbox(
    "Choose a low-memory LLM model:",
    ["tinyllama", "stablelm2:1.6b", "orca-mini"],
    key="model_select"
)

# Input fields (with unique keys)
article_topic = st.text_area("Enter your article topic:", "The Future of AI", key="topic_input")
additional_prompt = st.text_area("Optional: Add more context or style preferences:", "Include examples and make it engaging.", key="prompt_input")

# Generate button
if st.button("Generate Article"):
    with st.spinner("🧠 Thinking... Generating your article..."):
        try:
            # Load the selected model
            llm = Ollama(model=model_choice)

            # Full prompt construction
            prompt = f"Write a detailed article on the topic: '{article_topic}'. {additional_prompt}"

            # Generate response
            response = llm(prompt)

            # Output
            st.subheader("📝 Generated Article:")
            st.write(response)

        except Exception as e:
            st.error(f"An error occurred: {e}")
