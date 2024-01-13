import cv2

# khởi tạo camera và lấy tham chiếu đến bản ghi trực tiếp của camera
camera = cv2.VideoCapture(0)  # 0 tương ứng với camera mặc định (bạn có thể cần thay đổi nó dựa trên cấu hình của bạn)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Tải tệp cascade để phát hiện khuôn mặt
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
print("\n [INFO] Khởi tạo chụp khuôn mặt. Nhìn vào camera và đợi...")

while True:
    # bắt khung hình từ camera
    ret, frame = camera.read()

    # chuyển đổi khung hình sang ảnh xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Tìm khuôn mặt trong ảnh sử dụng tệp cascade đã tải
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    if faces is not None and len(faces) > 0:
        print(f"Tìm thấy {str(len(faces))} khuôn mặt: ", end="")
    else:
        print(f"Tìm thấy {str(len(faces))} khuôn mặt")

    # Vẽ hình chữ nhật xung quanh mỗi khuôn mặt được tìm thấy
    for i, (x, y, w, h) in enumerate(faces):
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        if i < len(faces) - 1:
            print(f"({x},{y},{w},{h})", end=", ")
        else:
            print(f"({x},{y},{w},{h})")

    # hiển thị một khung hình
    cv2.imshow("Frame", frame)

    # đợi phím 'q' được nhấn và thoát khỏi vòng lặp
    if cv2.waitKey(1) & 0xFF == ord("q") or cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
        break

# giải phóng camera và đóng tất cả cửa sổ OpenCV
camera.release()
cv2.destroyAllWindows()