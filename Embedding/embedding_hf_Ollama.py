from langchain_community.embeddings import OllamaEmbeddings

# If using default Ollama model
embedding = OllamaEmbeddings(
    model="nomicembed:v1"  
)

# If using your custom model:
# embedding = OllamaEmbeddings(model="nomicembed:v1")

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vectors = embedding.embed_documents(documents)

print("Number of documents:", len(vectors))
print("Embedding dimension:", len(vectors[0]))
print("First vector sample:", vectors[0][:5])  # print first 5 values
