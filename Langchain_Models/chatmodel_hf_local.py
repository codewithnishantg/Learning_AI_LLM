from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# Fix Windows path
os.environ['HF_HOME'] = r'D:\CodeWithNishant\huggingface_cache'

# Load local model (NO TOKEN HERE)
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100
    }
)

# Wrap in ChatHuggingFace
chat_model = ChatHuggingFace(llm=llm)

# Invoke
result = chat_model.invoke("What is the capital of India?")
print(result.content)
