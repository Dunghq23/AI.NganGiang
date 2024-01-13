import face_recognition
import cv2
import numpy as np

# Đây là một ví dụ chạy nhận diện khuôn mặt trực tiếp trên video từ webcam của bạn. Đây là một chút phức tạp hơn
# ví dụ khác, nhưng bao gồm một số điều chỉnh hiệu suất cơ bản để làm cho mọi thứ chạy nhanh hơn:
#   1. Xử lý mỗi khung video ở độ phân giải 1/4 (tuy nhiên hiển thị nó ở độ phân giải đầy đủ).
#   2. Chỉ nhận diện khuôn mặt ở mỗi khung video khác nhau.

# LƯU Ý: Ví dụ này yêu cầu phải cài đặt OpenCV (`cv2` library) chỉ để đọc từ webcam của bạn.
# OpenCV *KHÔNG* cần thiết để sử dụng thư viện face_recognition. Chỉ cần nếu bạn muốn chạy ví dụ cụ thể này.
# Nếu bạn gặp khó khăn khi cài đặt, hãy thử một trong những ví dụ khác không yêu cầu nó.

# Lấy tham chiếu đến webcam #0 (mặc định)
video_capture = cv2.VideoCapture(0)
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', 640, 400) 

# Tải hình ảnh mẫu và học cách nhận diện nó.
PSJ_image = face_recognition.load_image_file("../data/Park_Seo_Joon.png")
PSJ_face_encoding = face_recognition.face_encodings(PSJ_image)[0]

# Tải hình ảnh mẫu thứ hai và học cách nhận diện nó.
PMY_image = face_recognition.load_image_file("../data/Park_Min_Young.png")
PMY_face_encoding = face_recognition.face_encodings(PMY_image)[0]

# Tạo mảng mã hóa khuôn mặt đã biết và tên của họ
known_face_encodings = [
    PSJ_face_encoding,
    PMY_face_encoding
]
known_face_names = [
    "Park Seo Joon",
    "Park Min Young"
]

# Khởi tạo một số biến
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Lấy một khung hình video duy nhất
    ret, frame = video_capture.read()

    # Chỉ xử lý mỗi khung hình video khác nhau để tiết kiệm thời gian
    if process_this_frame:
                
        # Thay đổi kích thước khung hình video xuống 1/4 để xử lý nhanh hơn
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)


        # Tìm tất cả khuôn mặt và mã hóa khuôn mặt trong khung hình video hiện tại
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Xem xét xem khuôn mặt có phải là một trong những khuôn mặt đã biết không
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            name = "Unknown"

            # # Nếu tìm thấy khớp trong known_face_encodings, chỉ cần sử dụng cái đầu tiên.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Hoặc thay vào đó, sử dụng khuôn mặt đã biết có khoảng cách nhỏ nhất với khuôn mặt mới
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Hiển thị kết quả
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale trở lại vị trí khuôn mặt vì khung hình chúng ta phát hiện được đã được thu nhỏ xuống 1/4 kích thước
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Vẽ một hộp xung quanh khuôn mặt
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Vẽ nhãn với tên dưới khuôn mặt
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Hiển thị hình ảnh kết quả
    cv2.imshow('Video', frame)

    # Ấn 'q' trên bàn phím để thoát!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng nguồn cấp webcam
video_capture.release()
cv2.destroyAllWindows()

