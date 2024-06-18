from transformers import pipeline
generator = pipeline("text-generation", model="distilgpt2")
res = generator(
    "I want to have something to eat, can you give me some advice",
    max_length=30,
    num_return_sequences=2,
)
print(res)