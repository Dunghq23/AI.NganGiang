import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
dataset_path = '../Dataset'

def getImagesAndLabels(dataset_path):
    faces = []
    IDs = []

    # Lặp qua từng thư mục trong dataset_path
    for foldername in os.listdir(dataset_path):
        folderpath = os.path.join(dataset_path, foldername)

        # Tách ID và tên từ tên thư mục
        parts = foldername.split('_')
        if len(parts) == 2:
            ID, name = parts
        else:
            continue

        # Lặp qua từng file trong thư mục
        for filename in os.listdir(folderpath):
            imagePath = os.path.join(folderpath, filename)

            # Các dòng mã còn lại giữ nguyên không thay đổi
            faceImg = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
            faceNp = np.array(faceImg, 'uint8')
            faces.append(faceNp)
            print(ID)
            IDs.append(int(ID))
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)

    return IDs, faces

Ids, faces = getImagesAndLabels(dataset_path)

# training
recognizer.train(faces, np.array(Ids))
recognizer.save('../Models/trainingData.yml')
cv2.destroyAllWindows()
