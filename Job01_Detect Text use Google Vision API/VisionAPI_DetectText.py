import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccToken_ChuThang.json'
client = vision_v1.ImageAnnotatorClient()

def detectText(FILE_PATH):
    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    data = {'locale': [], 'description': []}
    for text in texts:
        data['locale'].append(text.locale)
        data['description'].append(text.description)
    df = pd.DataFrame(data)
    texts = df['description'][0]
    print(texts)
    messagebox.showinfo("Kết quả", texts)

# Hàm xử lý sự kiện người dùng nhấn nút "Chọn ảnh"
def open_and_detect():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        print('Đường dẫn:', file_path)
        detectText(file_path)

# ======================= Giao diện đồ họa ====================
# Tạo cửa sổ GDDH
root = tk.Tk()
root.geometry("400x200")
root.title("App nhận diện chữ qua ảnh")
# Tạo nút chọn tệp
open_button = tk.Button(root, text="Chọn ảnh", command=open_and_detect)
open_button.pack(pady=30)
# Khởi chạy giao diện đồ họa
root.mainloop()
