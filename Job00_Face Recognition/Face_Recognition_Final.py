import os
import face_recognition
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

# ========================== Hàm phục vụ =====================
# Hàm nhận diện hình ảnh
def FaceRecognition(file_path):
    known_face_encodings = []
    known_face_names = []
    # Xử lý các khuôn mặt đã biết   
    file_p = './img/known'
    for img in os.listdir(file_p):
        face_image = face_recognition.load_image_file(f'./img/known/{img}')
        face_encoding = face_recognition.face_encodings(face_image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(img)[0])
    print(known_face_names)
    # Tải ảnh lên
    test_image = face_recognition.load_image_file(file_path)
    # Tìm kiếm tất cả các khuôn mặt có trong bức ảnh
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)
    # Chuyển đổi sang định dạng pil
    pil_image = Image.fromarray(test_image)
    # Tạo ImageDraw
    draw = ImageDraw.Draw(pil_image)
    # Lặp qua các khuôn mặt
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        match_scores  = face_recognition.face_distance(known_face_encodings, face_encoding)
        name = "Unknown"
        best_match_index = -1
        if True in matches:
            best_match_index = np.argmin(match_scores)
        
        # Tính tỷ lệ giữa kích thước khung hình chữ nhật và kích thước font chữ
        box_width = right - left
        box_height = bottom - top
        font_size = int(min(box_width, box_height) * 0.1)  # Điều chỉnh hệ số 0.1 theo ý muốn
        
        # Tạo đối tượng font chữ với kích thước được tính toán
        font_path = r"./Primetime.ttf"
        fontBLACKPINK = ImageFont.truetype(font_path, font_size)
        if best_match_index != -1:
            name = known_face_names[best_match_index]
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=4) # Draw Box
            # draw.rectangle(((left, bottom - 20), (right, bottom)), fill=(0, 255, 0), outline=(0, 255, 0), width=4) # Draw label
            draw.text((left + 6, bottom - 40), name, fill=(255, 255, 255, 255), font=fontBLACKPINK)
        else:
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), width=4)
            # draw.rectangle(((left, bottom - 20), (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0), width=4)
            draw.text((left + 6, bottom - 40), name, fill=(255, 255, 255, 255), font=fontBLACKPINK)
    del draw     
    # Hiển thị ảnh đã nhận diện
    pil_image.show()

# Hàm xử lý sự kiện người dùng nhấn nút "Chọn ảnh"
def open_and_recognize():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        print('Đường dẫn:', file_path)
        FaceRecognition(file_path)

# ======================= Giao diện đồ họa ====================
# Tạo cửa sổ GDDH
root = tk.Tk()
root.geometry("400x200")
root.title("App nhận diện khuôn mặt qua ảnh")
# Tạo nút chọn tệp
open_button = tk.Button(root, text="Chọn ảnh", command=open_and_recognize)
open_button.pack(pady=50)
# Khởi chạy giao diện đồ họa
root.mainloop()