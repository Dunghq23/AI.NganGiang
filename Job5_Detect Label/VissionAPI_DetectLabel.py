import os, io
from google.cloud import vision_v1

key_path = 'ServiceAccToken_ChuThang.JSON'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
client = vision_v1.ImageAnnotatorClient()



def detectEmotion(FILE_PATH):
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.Image(content=content)
    response = client.face_detection(image=image)
    faceAnnotation = response.face_annotations
    
    likehood = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLY', 'LIKELY', 'VERY LIKELY')

    print(f"Found {len(faceAnnotation)} face.")
    for face in faceAnnotation:
        print(f"Faces:")
        print(f'    Detection confidence : {round(face.detection_confidence * 100, 2)}')
        print(f'    Angry                : {likehood[face.anger_likelihood]}')
        print(f'    Joy                  : {likehood[face.joy_likelihood]}')
        print(f'    Sorrow               : {likehood[face.sorrow_likelihood]}')
        print(f'    Sup                  : {likehood[face.surprise_likelihood]}')
        print(f'    Headwear             : {likehood[face.headwear_likelihood]}')
        print()

img_name = 'StartUp.jpg'
file_path = f'./Faces/{img_name}'
detectEmotion(file_path)