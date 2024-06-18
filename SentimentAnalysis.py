from transformers import pipeline

classifier = pipeline("sentiment-analysis")
text = str(input("Enter a sentence: "))
res = classifier(text)
print(res)
