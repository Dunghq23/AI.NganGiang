import cv2
from gpiozero import LED

# Khởi tạo camera
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

# Load mô hình nhận diện khuôn mặt
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./trainer/trainer.yml')

# Load tệp cascade để phát hiện khuôn mặt
face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

# Khai báo đèn LED
led = LED(17)

# Khai báo một mảng để lưu trữ dữ liệu từ tệp tin
names = []

# Đọc từ tệp tin
with open("names.txt", "r") as file:
    # Đọc từng dòng từ tệp tin
    for line in file:
        # Tách dữ liệu thành ID và tên
        face_id, face_name = line.strip().split(': ')
        # Thêm vào mảng
        names.append(face_name)

# In ra mảng names
print(names)

# Chạy vòng lặp để chụp khung hình từ camera
while True:
    ret, frame = camera.read()

    # Convert frame sang ảnh xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Tìm khuôn mặt trong ảnh sử dụng cascade đã tải
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)

    print("Found " + str(len(faces)) + " face(s)")

    # Kiểm tra xem có khuôn mặt hay không
    if len(faces) > 0:
        led.on()  # Bật đèn LED khi có khuôn mặt
    else:
        led.off()  # Tắt đèn LED khi không có khuôn mặt

    # Vẽ hình chữ nhật xung quanh mỗi khuôn mặt
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Dự đoán ID và độ tin cậy
        id, confidence = recognizer.predict(roi_gray)

        # Kiểm tra nếu độ tin cậy < 100 ==> "0" là sự trùng khớp hoàn hảo
        if 0 <= confidence < 100:
            recognized_name = names[id - 1]  # Điều chỉnh chỉ số tại đây
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            recognized_name = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(frame, str(recognized_name), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(frame, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 0), 1)
        print(x, y, w, h)

    # Hiển thị khung hình
    cv2.imshow("Frame", frame)

    # Thoát nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Giải phóng camera và đóng tất cả cửa sổ OpenCV
camera.release()
cv2.destroyAllWindows()
