from transformers import pipeline

def img2text(url):
    image2text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    
    text = image2text(url)[0]['generated_text']

    print(text)
    return text

img2text("img/image.png")