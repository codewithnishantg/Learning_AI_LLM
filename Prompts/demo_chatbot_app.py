from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


# Initialize Ollama model
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.7,
)

while True:
    user_input = input("You: ")
    result = llm.invoke(user_input)
    print("AI: ",result.content)
