# Import các thư viện cần thiết
import os, io
from google.cloud import vision_v1

# Đặt biến môi trường để xác thực với Google Cloud Vision API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccToken_ChuThang.JSON'
# Tạo một phiên bản của ImageAnnotatorClient để gửi hình ảnh đến Google Cloud Vision API
client = vision_v1.ImageAnnotatorClient()

# Định nghĩa hàm để phân tích cảm xúc trong khuôn mặt
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

# Tên hình ảnh cần xử lý
img_name = 'StartUp.jpg'
# Đường dẫn đến tệp hình ảnh
file_path = f'./Faces/{img_name}'
# Gọi hàm để phân tích cảm xúc trong khuôn mặt
detectEmotion(file_path)

