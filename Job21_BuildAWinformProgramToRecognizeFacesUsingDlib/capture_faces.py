import cv2
import dlib

def capture_faces(output_folder, num_images=100):
    # Khởi tạo bộ nhận diện khuôn mặt của dlib
    face_detector = dlib.get_frontal_face_detector()

    # Mở camera
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Thiết lập chiều rộng và chiều cao của frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Biến đếm số lượng ảnh đã chụp
    count = 0

    while count < num_images:
        # Đọc frame từ webcam
        ret, frame = cap.read()

        # Chuyển frame sang đen trắng để tăng hiệu suất
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Lật ngược frame 180 độ
        flipped_frame = cv2.flip(gray_frame, 1)  # 1 để lật ngang, 0 để lật dọc

        # Nhận diện khuôn mặt trong frame
        faces = face_detector(flipped_frame)

        # Lặp qua các khuôn mặt nhận diện được
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()

            # Vẽ hình chữ nhật quanh khuôn mặt
            cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Lưu ảnh khuôn mặt vào thư mục đích
            face_image = flipped_frame[y:y+h, x:x+w]
            image_path = f"{output_folder}/face_{count}.png"
            cv2.imwrite(image_path, face_image)
            print(f"Đã lưu {count + 1} ảnh")

            count += 1

        # Hiển thị frame có khuôn mặt được đánh dấu
        cv2.imshow('Capture Faces', flipped_frame)

        # Thoát nếu nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng camera và đóng cửa sổ hiển thị
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_folder = "./Datasets"  # Thay đổi thành thư mục lưu trữ ảnh
    num_images = 100
    capture_faces(output_folder, num_images)
