import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()

def detect_logos(path):
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print("Logos:")
    for logo in logos:
        print(f'    {logo.description}')

img_path = './resources/social.jpg'
detect_logos(img_path) 
