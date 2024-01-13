import cv2

# Initialize the camera
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

# Load the face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./trainer/trainer.yml')

# Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

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


# Capture frames from the camera
while True:
    ret, frame = camera.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)

    print("Found " + str(len(faces)) + " face(s)")

    # Draw a rectangle around every found face
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        id, confidence = recognizer.predict(roi_gray)

        # Check if confidence is less than 100 ==> "0" is a perfect match
        if confidence < 100 and confidence:
            recognized_name = names[id - 1]  # Điều chỉnh chỉ số tại đây
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            recognized_name = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(frame, str(recognized_name), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(frame, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 0), 1)
        print(x, y, w, h)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
