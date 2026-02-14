from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.7,
)

response = llm.invoke("What is the capital of India?")
print(response.content)
