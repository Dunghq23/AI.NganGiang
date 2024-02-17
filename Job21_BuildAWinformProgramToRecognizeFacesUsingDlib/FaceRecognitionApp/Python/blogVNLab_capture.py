import pyodbc
import cv2
import os

def insertOrUpdate(Id, Name):
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=LAPTOP-1J76PMUP;'
                          'DATABASE=FaceRecognition;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    # Kiểm tra xem bản ghi có tồn tại không
    cursor.execute("SELECT * FROM People WHERE ID=?", (Id,))
    isRecordExist = cursor.fetchone()

    if isRecordExist:
        # Nếu tồn tại, thực hiện câu lệnh UPDATE
        cmd = "UPDATE People SET Name=? WHERE ID=?"
        cursor.execute(cmd, (Name, Id))
    else:
        # Nếu không tồn tại, thực hiện câu lệnh INSERT
        cmd = "INSERT INTO People(Id, Name) VALUES (?, ?)"
        cursor.execute(cmd, (Id, Name))

    # Commit và đóng kết nối
    conn.commit()
    conn.close()


id = input('Enter your ID: ')
name = input('Enter your name: ')

# Tạo thư mục cho người dùng
user_folder = f"../Dataset/{id}_{name}"
os.makedirs(user_folder, exist_ok=True)

sampleNum = 0
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('../Models/haarcascade_frontalface_default.xml')

while True:
    # Đọc hình ảnh từ camera
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Tăng số mẫu
        sampleNum = sampleNum + 1

        # Lưu ảnh khuôn mặt đã chụp vào thư mục người dùng
        cv2.imwrite(f"{user_folder}/User_{id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])

        cv2.imshow('frame', img)

    # Chờ 100 miliseconds và kiểm tra xem có phím 'q' được nhấn hay không
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # Thoát khỏi vòng lặp nếu số mẫu vượt quá 20
    elif sampleNum >= 50:
        break

# Giải phóng camera và đóng cửa sổ
cam.release()
cv2.destroyAllWindows()

insertOrUpdate(id, name)
