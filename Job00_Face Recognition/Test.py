import os
import face_recognition
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog, messagebox
import pickle

# ========================== Hàm phục vụ =====================
# Hàm nhận diện hình ảnh
def FaceRecognition(file_path):
    known_face_encodings = []
    known_face_names = []
    with open('known_faces.pickle', 'rb') as f:
        loaded_data = pickle.load(f)
        known_face_encodings = loaded_data['known_face_encodings']
        known_face_names = loaded_data['known_face_names']
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
        match_scores = face_recognition.face_distance(known_face_encodings, face_encoding)
        name = "Unknown"
        
        best_match_index = -1
        normal_match_index = -1
        index_min_value = np.argmin(match_scores)
        
        if matches[index_min_value] and match_scores[index_min_value] <= 0.45:
            best_match_index = index_min_value
        # elif matches[index_min_value]
        
        print(f'============================={known_face_names[best_match_index]}=================================')
        print(matches)
        print(match_scores)
        print("Best Match Index:", best_match_index)
        print("Normal Match Index:", normal_match_index)
        
        # Tạo đối tượng font chữ với kích thước được tính toán
        font_path = r"./Primetime.ttf"
        fontBLACKPINK = ImageFont.truetype(font_path, 16)
        if best_match_index != -1:
            name = known_face_names[best_match_index]
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=4) # Draw Box
            # draw.rectangle(((left, bottom - 20), (right, bottom)), fill=(0, 255, 0), outline=(0, 255, 0), width=4) # Draw label
            draw.text((left + 6, bottom - 40), name, fill=(255, 255, 255, 255), font=fontBLACKPINK)
        elif normal_match_index != -1:
            name = known_face_names[best_match_index]
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4) # Draw Box
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

def Write_EnCode_File():
    known_face_encodings = []
    known_face_names = []
    # # Xử lý các khuôn mặt đã biết   
    for img in os.listdir('./img/known'):
        face_image = face_recognition.load_image_file(f'./img/known/{img}')
        face_encodings = face_recognition.face_encodings(face_image)[0]
        known_face_encodings.append(face_encodings)
        known_face_names.append(os.path.splitext(img)[0])
    # Lưu danh sách known_face_encodings và known_face_names vào một tệp
    with open('known_faces.pickle', 'wb') as f:
        data_to_save = {
            'known_face_encodings': known_face_encodings,
            'known_face_names': known_face_names
        }
        pickle.dump(data_to_save, f)
    messagebox.showinfo("Thông báo", "Đã mã hóa xong")
# ======================= Giao diện đồ họa ====================
# Tạo cửa sổ GDDH
root = tk.Tk()
root.geometry("400x400")
root.title("App nhận diện khuôn mặt qua ảnh")

# Lấy kích thước của màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Kích thước cửa sổ giao diện
window_width = 400
window_height = 200
# Tính toán vị trí để cửa sổ xuất hiện giữa màn hình
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Thiết lập kích thước và vị trí của cửa sổ
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Tạo nút chọn tệp
open_button = tk.Button(root, text="Chọn ảnh", command=open_and_recognize)
WriteEncode_button = tk.Button(root, text="Mã hóa dữ liệu ảnh đã nhập", command=Write_EnCode_File)
# Ghi lại mã hóa vào file
open_button.pack(pady=30)
WriteEncode_button.pack(pady=0)  
# Tạo một label
label_text = "Chú ý: Nếu thư mục các khuôn mặt đã biết có sự thay đổi như thêm mới hoặc xóa thì cần mã hóa lại dữ liệu ảnh đã nhập."
label = tk.Label(root, text=label_text, wraplength=300)  # wraplength xác định độ dài tối đa của dòng
# Đặt label vào giao diện
label.pack()

# Khởi chạy giao diện đồ họa
root.mainloop()

