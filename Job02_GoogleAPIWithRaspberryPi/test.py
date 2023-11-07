import cv2
from google.cloud import vision_v1
import numpy as np
import os, io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccToken_ChuThang.json'
# Thiết lập client cho Google Cloud Vision API
client = vision_v1.ImageAnnotatorClient()

# Đọc ảnh từ tệp ảnh (thay thế bằng cách chụp từ camera của Raspberry Pi)
image_path = './faces/startup.jpg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# Gửi ảnh cho Google Cloud Vision API để nhận diện khuôn mặt
image = vision_v1.Image(content=content)
response = client.face_detection(image=image)
faces = response.face_annotations

image_cv2 = cv2.imread(image_path)
likehood = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLY', 'LIKELY', 'VERY LIKELY')

# Vẽ hình vuông bao quanh khuôn mặt và ghi biểu cảm bên dưới
for face in faces:
    vertices = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
    x, y, width, height = cv2.boundingRect(np.array(vertices))

    # Vẽ hình vuông
    cv2.rectangle(image_cv2, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # Trích xuất thông tin về biểu cảm từ faceAnnotation
    emotion = "Emotion: "
    Joy = f"Joy: {likehood[face.joy_likelihood]}"
    Angry = f"Angry: {likehood[face.anger_likelihood]}"
    Sorrow = f"Sorrow: {likehood[face.sorrow_likelihood]}"
    Surprise = f"Surprise: {likehood[face.surprise_likelihood]}"

    # Ghi biểu cảm bên dưới hình vuông
    text_color = (0, 0, 255)
    font_scale = 0.5
    font_thickness = 2

    # Ghi biểu cảm bên dưới hình vuông
    cv2.putText(image_cv2, emotion, (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)
    cv2.putText(image_cv2, Joy, (x, y + height + 40), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)
    cv2.putText(image_cv2, Angry, (x, y + height + 60), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)
    cv2.putText(image_cv2, Sorrow, (x, y + height + 80), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)
    cv2.putText(image_cv2, Surprise, (x, y + height + 100), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)

# Hiển thị ảnh với hình vuông và biểu cảm ghi bên dưới
cv2.imshow('Detected Faces', image_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
