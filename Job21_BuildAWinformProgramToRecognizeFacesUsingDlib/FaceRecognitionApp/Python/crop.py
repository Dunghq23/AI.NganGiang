import cv2

def crop_and_resize_face(image_path, output_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Tạo bộ lọc khuôn mặt
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Chuyển đổi ảnh sang ảnh đen trắng để tăng hiệu suất nhận diện
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect khuôn mặt trong ảnh
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        # Chọn khuôn mặt đầu tiên (có thể cải thiện để chọn khuôn mặt chính xác hơn)
        x, y, w, h = faces[0]

        # Cắt khuôn mặt từ ảnh
        face_region = image[y:y+h, x:x+w]

        # Resize khuôn mặt về kích thước 100x100
        resized_face = cv2.resize(face_region, (100, 100))

        # Lưu kết quả vào đường dẫn đầu ra
        cv2.imwrite(output_path, resized_face)

        print(f"Khuôn mặt đã được cắt và resize, lưu tại: {output_path}")
    else:
        print("Không tìm thấy khuôn mặt trong ảnh.")

# Đường dẫn đến ảnh cần xử lý
input_image_path = r"C:\Users\Admin\Downloads\Ha Quang Dung.jpg"

# Đường dẫn đến nơi lưu ảnh khuôn mặt đã được cắt và resize
output_image_path = r"C:\Users\Admin\Downloads\Cropped_Resized_Face.jpg"

# Gọi hàm xử lý
crop_and_resize_face(input_image_path, output_image_path)
