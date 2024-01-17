import dlib
import cv2

def detect_faces(image_path):
    # Load ảnh
    image = cv2.imread(image_path)
    
    # Khởi tạo bộ nhận diện khuôn mặt
    detector = dlib.get_frontal_face_detector()
    
    # Chuyển ảnh sang đen trắng (grayscale) để tăng hiệu suất
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Nhận diện khuôn mặt
    faces = detector(gray_image)
    
    # Vẽ hình chữ nhật quanh khuôn mặt
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Hiển thị ảnh có khuôn mặt được đánh dấu
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "duong_dan_den_anh.jpg"  # Đổi đường dẫn đến ảnh của bạn
    detect_faces(image_path)
