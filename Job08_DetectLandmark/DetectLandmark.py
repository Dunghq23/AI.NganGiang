import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken.JSON'
client = vision.ImageAnnotatorClient()

def detect_landmarks(path):
    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print("Landmarks:")

    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print(f"Latitude: {lat_lng.latitude}")
            print(f"Longitude: {lat_lng.longitude}")
            
img_path = './resources/keangnam.jpg'
detect_landmarks(img_path)