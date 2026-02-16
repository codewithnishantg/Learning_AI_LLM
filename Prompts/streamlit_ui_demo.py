from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Load env variables (if needed)
load_dotenv()

# Initialize Ollama model
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.7,
)

st.title("Ollama Chat App")

user_input = st.text_input("Ask something:")

if user_input:
    response = llm.invoke(user_input)
    st.write(response.content)
