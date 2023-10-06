import os, io
from google.cloud import vision_v1
import pandas as pd

key_path = 'ServiceAccToken_ChuThang.JSON'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
client = vision_v1.ImageAnnotatorClient()


def detectProperties(FILE_PATH):
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.Image(content=content)
    response = client.image_properties(image=image).image_properties_annotation
    dominant_colors = response.dominant_colors

    print(dominant_colors)

img_name = 'Fujisan.jpg'
file_path = f'./Properties/{img_name}'
detectProperties(file_path)
