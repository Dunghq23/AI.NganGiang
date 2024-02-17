import cv2
import face_recognition
import os
import sys


def is_single_face_cv2(image_path):
    # Đọc ảnh
    image = cv2.imread(image_path)

    # Chuyển ảnh sang đen trắng để tăng tốc độ xử lý
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sử dụng Haarcascades để nhận diện khuôn mặt
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5)

    # Kiểm tra số lượng khuôn mặt và xóa ảnh nếu không đúng 1 khuôn mặt
    if len(faces) == 1:
        print(True)
    else:
        print(False)
        # Xóa ảnh nếu không đúng 1 khuôn mặt
        os.remove(image_path)


def is_single_face(image_path):
    # Đọc ảnh
    image = face_recognition.load_image_file(image_path)

    # Sử dụng HOG để nhận diện khuôn mặt
    face_locations = face_recognition.face_locations(image, model="hog")

    # Kiểm tra số lượng khuôn mặt và xóa ảnh nếu không đúng 1 khuôn mặt
    if len(face_locations) == 1:
        print(True)
    else:
        print(False)
        # Xóa ảnh nếu không đúng 1 khuôn mặt
        os.remove(image_path)


def encode_images_in_dataset(datasetPath, output_file, trainedPath):
    # Kiểm tra xem file encodings.txt đã tồn tại chưa
    if not os.path.isfile(output_file):
        # Nếu chưa tồn tại, tạo file mới và ghi đè nội dung
        with open(output_file, 'w') as file:
            file.write('')

    # Danh sách các hình ảnh trong thư mục
    image_files = [f for f in os.listdir(
        datasetPath) if f.endswith('.jpg') or f.endswith('.png')]

    # Mở file để ghi nối tiếp cho encodings.txt
    with open(output_file, 'a') as encoding_file:
        for image_file in image_files:
            # Đường dẫn đầy đủ của hình ảnh
            image_path = os.path.join(datasetPath, image_file)

            # Đọc hình ảnh và chuyển đổi thành encoding
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)

            if len(encoding) > 0:
                # Ghi encoding vào encodings.txt
                encoding_file.write(
                    f"{os.path.splitext(image_file)[0]}: {encoding[0]}\n")

                # Di chuyển file đã sử dụng vào thư mục 'Trained' với xử lý trùng tên
                image_name, image_extension = os.path.splitext(
                    os.path.basename(image_path))
                new_path = os.path.join(datasetPath, trainedPath, f"{image_name}_trained{image_extension}")

                # Kiểm tra xem tên file mới đã tồn tại hay chưa
                counter = 1
                while os.path.exists(new_path):
                    new_path = os.path.join(datasetPath, trainedPath, f"{image_name}_trained_{counter}{image_extension}")
                    counter += 1

                os.rename(image_path, new_path)


def load_encoding_file(file_path):
    names = []
    encodings = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_name = None
    current_encoding = []

    for line in lines:
        parts = line.strip().split(': ')

        if len(parts) == 2:
            if current_name is not None:
                names.append(current_name)
                encodings.append(current_encoding)

            current_name = parts[0]
            current_encoding = [
                float(value) for value in parts[1][1:-1].replace(']', '').split()]
        elif current_name is not None:
            current_encoding.extend(
                [float(value) for value in line.strip().replace(']', '').split()])

    if current_name is not None:
        names.append(current_name)
        encodings.append(current_encoding)

    return names, encodings


def recognize_faces(image_path, names, encodings, savefile_path):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Find all face locations and face encodings in the image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Loop through each face found in the image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face encoding with the known encodings
        matches = face_recognition.compare_faces(
            encodings, face_encoding, tolerance=0.5)
        name = "Unknown"  # Default name if no match is found

        # Check if a match is found
        if True in matches:
            first_match_index = matches.index(True)
            name = names[first_match_index]

        # Draw a rectangle around the face and display the name
        if name == "Unknown":
            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        else:
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    # Save the result
    cv2.imwrite(savefile_path, image)


def recognize_faces_out(image_path, names, encodings):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Find all face locations and face encodings in the image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    results = []
    # Loop through each face found in the image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face encoding with the known encodings
        matches = face_recognition.compare_faces(
            encodings, face_encoding, tolerance=0.5)
        name = "Unknown"  # Default name if no match is found

        # Check if a match is found
        if True in matches:
            first_match_index = matches.index(True)
            name = names[first_match_index]

        # Add result to the list
        results.append({
            "top": top,
            "right": right,
            "bottom": bottom,
            "left": left,
            "name": name
        })
    # print(results)
    if results:
        recognized_name = results[0]['name']
        print(recognized_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py command [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "is_single_face":
        if len(sys.argv) > 2:
            image_path = sys.argv[2]
            is_single_face(image_path)
    elif command == "encode_images_in_dataset":
        if len(sys.argv) > 2:
            dataset_path = sys.argv[2]
            encodings_path = sys.argv[3]
            trainer_path = sys.argv[4]
            encode_images_in_dataset(
                dataset_path, encodings_path, trainer_path)
    elif command == "recognize_faces":
        if len(sys.argv) > 2:
            image_path = sys.argv[2]
            encodings_path = sys.argv[3]
            savefile_path = sys.argv[4]
            names, encodings = load_encoding_file(encodings_path)
            recognize_faces(image_path, names, encodings, savefile_path)
    elif command == "recognize_faces_out":
        if len(sys.argv) > 2:
            image_path = sys.argv[2]
            encodings_path = sys.argv[3]
            names, encodings = load_encoding_file(encodings_path)
            recognize_faces_out(image_path, names, encodings)
    else:
        print("Unknown command")
        sys.exit(1)


"""
Để chạy lệnh với các tham số dòng lệnh trong môi trường Python, bạn cần mở một cửa sổ dòng lệnh (Command Prompt hoặc Terminal), sau đó di chuyển đến thư mục chứa script Python và thực hiện lệnh như sau:

Capture Faces:
    python script.py capture_faces [folder_name]
    python script.py capture_faces MyDataset

Is Single Face:
    python script.py is_single_face [image_path]
    python script.py is_single_face ./path/to/your/image.jpg

Encode Images:
    python script.py encode_images

Recognize Faces:
    python script.py recognize_faces [image_path]
    python script.py recognize_faces ./path/to/your/image.jpg
"""
