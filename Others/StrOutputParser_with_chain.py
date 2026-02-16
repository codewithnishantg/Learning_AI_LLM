from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Initialize Ollama model
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.7,
)

# Create PromptTemplate
prompt = PromptTemplate(
    input_variables=["text"],
    template="What is :\n{text}"
)
prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Summary in 1 line:\n{text}"
)

# Create output parser
parser = StrOutputParser()

# Create chain using LCEL
chain = prompt | llm | parser | prompt2 | llm | parser

# Invoke chain
result = chain.invoke({"text": "upi?"})

print(result)
