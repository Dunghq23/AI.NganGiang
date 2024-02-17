
import cv2


def detect_and_display_landmarks(image_path):
    # Tải mô hình pre-trained
    predictor_path = "./Models/shape_predictor_68_face_landmarks.dat"
    face_detector = dlib.get_frontal_face_detector()
    face_predictor = dlib.shape_predictor(predictor_path)

    # Đọc ảnh đầu vào
    image = cv2.imread(image_path)

    # Kiểm tra xem ảnh có tồn tại không
    if image is None:
        print(f"Cannot open image at path: {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Xác định các khuôn mặt trong ảnh
    faces = face_detector(gray)

    # Duyệt qua từng khuôn mặt và vẽ đường bao xung quanh
    for face in faces:
        shape = face_predictor(gray, face)
        for i in range(68):
            x, y = shape.part(i).x, shape.part(i).y
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
            
    # Giảm kích thước khung cửa sổ hiển thị
    small_image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)

    # Hiển thị ảnh với các khuôn mặt được nhận dạng
    cv2.imshow("Facial Landmarks", small_image)
    cv2.waitKey(0)



if __name__ == "__main__":
    DatasetPath = "./Datasets"  # Thay đổi thành thư mục lưu trữ ảnh
    
    
    # Sử dụng hàm
    image_path = "./CafeNhietDoi.jpg"
    detect_and_display_landmarks(image_path)
