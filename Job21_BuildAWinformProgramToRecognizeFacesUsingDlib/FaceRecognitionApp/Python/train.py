import argparse
import cv2
import numpy as np
import os
import joblib


def train_model(dataset_path, output_model_path, output_mapping_path):
    # Danh sách để lưu trữ ma trận hình ảnh và nhãn tương ứng
    mat_images = []
    int_labels = []
    label_mapping = {}

    # Duyệt qua từng thư mục người dùng trong thư mục dữ liệu
    for label, person_folder in enumerate(os.listdir(dataset_path)):
        person_name = os.path.basename(person_folder)
        label_mapping[label] = person_name

        # Duyệt qua từng ảnh trong thư mục người dùng
        for image_name in os.listdir(os.path.join(dataset_path, person_folder)):
            image_path = os.path.join(dataset_path, person_folder, image_name)

            # Đọc ảnh dưới dạng ma trận và thêm vào danh sách
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (100, 100))
            mat_images.append(image)
            int_labels.append(label)

    # Kiểm tra có dữ liệu đào tạo hay không
    if len(mat_images) > 0:
        # Chuyển đổi danh sách thành mảng numpy
        mat_images = np.array(mat_images)
        int_labels = np.array(int_labels)

        # Sử dụng FaceRecognizer để huấn luyện mô hình
        recognizer = cv2.face.EigenFaceRecognizer_create()
        recognizer.train(mat_images, int_labels)

        # Lưu mô hình vào file
        recognizer.write(output_model_path)

        # Lưu ánh xạ nhãn và tên người vào tệp văn bản
        with open(output_mapping_path, 'w') as file:
            for label, person_name in label_mapping.items():
                file.write(f"{label} {person_name}\n")

if __name__ == "__main__":
    # Thay đổi đường dẫn đến thư mục dataset và nơi lưu mô hình và ánh xạ
    # train_model("../dataset", "../Models/trained_model.yml", "../Models/label_mapping.txt")

    parser = argparse.ArgumentParser(description="Train face recognition model.")
    parser.add_argument("--dataset", type=str, required=True, help="Path to the dataset.")
    parser.add_argument("--model", type=str, required=True, help="Path to save the trained model.")
    parser.add_argument("--mapping", type=str, required=True, help="Path to save label mapping.")

    args = parser.parse_args()

    # Gọi hàm train_model với các tham số từ dòng lệnh
    train_model(args.dataset, args.model, args.mapping)
    
    # python c
