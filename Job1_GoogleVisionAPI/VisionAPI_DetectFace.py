import os, io
from google.cloud import vision_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccToken_ChuThang.json'
client = vision_v1.ImageAnnotatorClient()

file_name = 'Smile.jpg'
# file_name = 'StartUp.jpg'
image_path = f'.\images\Faces\{file_name}'

likehood = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLY', 'LIKELY', 'VERY LIKELY')

def DetectFaceEmotion(file_path):
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.Image(content=content)
    response = client.face_detection(image=image)
    faceAnnotation = response.face_annotations

    print(f"Total number of people in the photo: {len(faceAnnotation)}")
    print(f"Faces:")
    for face in faceAnnotation:
        print(f'    Detection Confidence : {face.detection_confidence}')
        print(f'    Angry likelyhood     : {likehood[face.anger_likelihood]}')
        print(f'    Joy likelyhood       : {likehood[face.joy_likelihood]}')
        print(f'    Sorrow likelyhood    : {likehood[face.sorrow_likelihood]}')
        print(f'    Sup likelyhood       : {likehood[face.surprise_likelihood]}')
        print(f'    Headwear likelyhood  : {likehood[face.headwear_likelihood]}')
        print()
        print(f'    Detection Confidence : {face.detection_confidence}')
        print(f'    Angry likelyhood     : {face.anger_likelihood}')
        print(f'    Joy likelyhood       : {face.joy_likelihood}')
        print(f'    Sorrow likelyhood    : {face.sorrow_likelihood}')
        print(f'    Sup likelyhood       : {face.surprise_likelihood}')
        print(f'    Headwear likelyhood  : {face.headwear_likelihood}')
        print()
        print(face)
        
DetectFaceEmotion(image_path)