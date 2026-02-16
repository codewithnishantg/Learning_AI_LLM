from langchain_ollama import ChatOllama
from pydantic import BaseModel


class PrimeMinister(BaseModel):
    name: str
    country: str
    position: str


llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

structured_llm = llm.with_structured_output(PrimeMinister)

result = structured_llm.invoke(
    "Who is the Prime Minister of India?"
)

print(result)
