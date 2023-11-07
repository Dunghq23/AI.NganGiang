import cv2
from google.cloud import vision_v1
import numpy as np
import os, io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken_ChuThang.JSON'
client = vision_v1.ImageAnnotatorClient()

def detectEmotion(FILE_PATH):
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()
    image = vision_v1.Image(content=content)
    response = client.face_detection(image=image)
    faces= response.face_annotations
    print(f"Found {len(faces)} face.")
    image_cv2 = cv2.imread(FILE_PATH)
    for face in faces:
        vertices = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
        x, y, width, height = cv2.boundingRect(np.array(vertices))
        out_vertice = ', '.join(map(str, vertices))
        print(f"Face bounds: {out_vertice}")
        # Vẽ hình vuông
        cv2.rectangle(image_cv2, (x, y), (x + width, y + height), (0, 255, 0), 2)
    output_file = "out.jpg"
    cv2.imwrite(output_file, image_cv2)
    print(f"Writing to file {output_file}")

image_path = './faces/Vagabond_2019.jpg'
detectEmotion(image_path)

