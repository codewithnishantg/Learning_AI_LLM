from huggingface_hub import InferenceClient

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token="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"
)

response = client.chat_completion(
    messages=[
        {"role": "user", "content": "What is the capital of India"}
    ]
)

print(response.choices[0].message.content)
