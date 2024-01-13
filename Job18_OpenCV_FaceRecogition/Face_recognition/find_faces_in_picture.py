from PIL import Image
import face_recognition

# Tải tệp jpg thành một mảng numpy
image = face_recognition.load_image_file("../data/PSJ.jpg")

# Tìm tất cả các khuôn mặt trong ảnh sử dụng mô hình mặc định dựa trên HOG.
# Phương pháp này khá chính xác, nhưng không chính xác như mô hình CNN và không hỗ trợ GPU.
# Xem thêm: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("Tôi đã tìm thấy {} khuôn mặt trong bức ảnh này.".format(len(face_locations)))

for face_location in face_locations:

    # In vị trí của mỗi khuôn mặt trong ảnh này
    top, right, bottom, left = face_location
    print("Một khuôn mặt được đặt tại vị trí pixel: Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # Bạn có thể truy cập chính khuôn mặt như sau:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
