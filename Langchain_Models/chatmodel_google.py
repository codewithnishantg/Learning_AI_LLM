from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview',google_api_key="AIzaSyAgpPR_k5lyTkr-yyFFiTKFuY27L7OOG30")

result = model.invoke('What is the capital of India')

print(result.content)