import cv2
import dlib

# Tạo bộ nhận diện khuôn mặt
face_detector = dlib.get_frontal_face_detector()

# Mở kết nối webcam
cap = cv2.VideoCapture(0)

while True:
    # Đọc từ webcam
    ret, frame = cap.read()

    # Chuyển đổi sang ảnh đen trắng để tăng hiệu suất
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Nhận diện khuôn mặt
    faces = face_detector(gray)

    # Vẽ hình chữ nhật quanh khuôn mặt
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Hiển thị ảnh
    cv2.imshow('Face Detection', frame)

    # Thoát nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Đóng kết nối webcam và cửa sổ hiển thị
cap.release()
cv2.destroyAllWindows()
