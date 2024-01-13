import face_recognition
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Đây là một ví dụ về cách chạy nhận diện khuôn mặt trên một ảnh và vẽ một hộp xung quanh mỗi người được nhận diện.

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

# Tải một ảnh với khuôn mặt không xác định
unknown_image = face_recognition.load_image_file("../data/PSJ.jpg")

# Tìm tất cả khuôn mặt và mã hóa khuôn mặt trong ảnh không xác định
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Chuyển đổi ảnh thành ảnh định dạng PIL để chúng ta có thể vẽ lên đó với thư viện Pillow
# Xem thêm http://pillow.readthedocs.io/ để biết thêm thông tin về PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Tạo một đối tượng vẽ Draw của Pillow để vẽ
draw = ImageDraw.Draw(pil_image)

# Lặp qua mỗi khuôn mặt được tìm thấy trong ảnh không xác định
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Xem xem khuôn mặt có trùng khớp với khuôn mặt đã biết không
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    # Nếu một trùng khớp được tìm thấy trong known_face_encodings, chỉ sử dụng cái đầu tiên.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Hoặc thay vào đó, sử dụng khuôn mặt đã biết có khoảng cách nhỏ nhất với khuôn mặt mới
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)

    # Tìm tên của người đã được nhận dạng dựa trên khuôn mặt có khoảng cách nhỏ nhất
    name = known_face_names[best_match_index] if matches[best_match_index] else "Unknown"

    # Vẽ một hộp xung quanh khuôn mặt sử dụng module Pillow
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
    
    # Vẽ một nhãn với tên dưới khuôn mặt (chữ to hơn)
    text = f"{name} ({round(min(face_distances), 2)})"
    # text_bbox = draw.textbbox((left + 6, bottom - 5), text)
    font = ImageFont.load_default()


    text_bbox = draw.textbbox((left + 6, bottom - 5), text, font=font)

    
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Vẽ hộp xung quanh vùng chữ với padding
    box_padding = 10
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom + box_padding)), fill=(0, 0, 255), outline=(0, 0, 255))

    # Vẽ văn bản
    draw.text((left + 6, bottom - text_height - 5), text, fill=(255, 255, 255, 255))



# Xóa thư viện vẽ khỏi bộ nhớ theo tài liệu của Pillow
del draw

# Hiển thị ảnh kết quả
# pil_image.show()

# Bạn cũng có thể lưu một bản sao của ảnh mới vào đĩa nếu muốn bằng cách bỏ chú thích dòng này
pil_image.save("image_with_boxes.jpg")