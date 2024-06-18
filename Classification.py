from transformers import pipeline
classifier = pipeline("zero-shot-classification")
res = classifier(
    "I want to have something to eat, can you give me some advice?",
    candidate_labels=["food", "question", "sports"],
)
print(res)
