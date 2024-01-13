import cv2

# Khởi tạo camera
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)

# camera = cv2.VideoCapture(0)  # 0 tương ứng với camera mặc định (bạn có thể cần thay đổi nó dựa trên cấu hình của bạn)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Tải tệp cascade để phát hiện khuôn mặt
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Nhập ID khuôn mặt từ người dùng
face_id = input("\n Nhập ID người dùng: ")
# Nhập tên
face_name = input("\n Nhập tên người dùng: ")

print("\n [INFO] Khởi tạo chụp khuôn mặt. Nhìn vào camera và đợi ...")
count = 0

while True:
    # Bắt khung hình từ camera
    ret, frame = camera.read()

    # Kiểm tra xem khung hình có trống không
    if not ret:
        print("Không thể đọc khung hình từ camera.")
        break

    # Chuyển đổi khung hình sang ảnh xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Tìm khuôn mặt trong ảnh sử dụng tệp cascade đã tải
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    print("Tìm thấy " + str(len(faces)) + " khuôn mặt")

    # Vẽ hình chữ nhật xung quanh mỗi khuôn mặt được tìm thấy
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print(x, y, w, h)

    # Lưu ảnh kết quả
    if len(faces):
        count = count + 1
        img_item = "dataset/User." + face_id + '.' + str(count) + ".jpg"
        cv2.imwrite(img_item, frame)

    # Hiển thị ảnh đã chụp
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(100)  # Hiển thị ảnh trong khoảng thời gian ngắn

    # Đợi phím 'q' được nhấn và thoát khỏi vòng lặp
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

    # Thoát nếu đã chụp 100 ảnh
    # Lưu tên vào tệp tin txt sau khi đã chụp đủ số ảnh
    if count == 100:
        with open("names.txt", "a") as file:
            file.write(f"{face_id}: {face_name}\n")
            print(f"Tên '{face_name}' đã được lưu vào tệp tin names.txt.")
        break

# Giải phóng camera và đóng tất cả cửa sổ OpenCV
camera.release()
cv2.destroyAllWindows()
