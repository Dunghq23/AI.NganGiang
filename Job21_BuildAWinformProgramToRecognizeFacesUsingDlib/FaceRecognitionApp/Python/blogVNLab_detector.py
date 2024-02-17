import cv2
import numpy as np
import pyodbc

faceDetect = cv2.CascadeClassifier('../Models/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

# Open a connection to SQL Server
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=LAPTOP-1J76PMUP;'
    'DATABASE=FaceRecognition;'
    'Trusted_Connection=yes;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Load LBPH face recognizer
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("../Models/trainingData.yml")
rec.setThreshold(75)  # Thay đổi ngưỡng nhận diện (đặt thử nghiệm)

# Set text style
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (203, 23, 252)

# Function to get profile from SQL Server by ID


def getProfile(id):
    cmd = "SELECT * FROM People WHERE ID=?"
    cursor.execute(cmd, (id,))
    profile = cursor.fetchone()
    return profile


while True:
    # Camera read
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize the image
    small_gray = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)

    # Detect faces
    # faces = faceDetect.detectMultiScale(small_gray, 1.3, 3)
    faces = faceDetect.detectMultiScale(small_gray, scaleFactor=1.3, minNeighbors=5)


    for (x, y, w, h) in faces:
        # Resize coordinates back to original size
        x *= 2
        y *= 2
        w *= 2
        h *= 2

        # Draw rectangle around face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Recognize face
        id, conf = rec.predict(gray[y:y+h, x:x+w])

        # Get profile from SQL Server
        profile = getProfile(id)

        # Set text to window
        if profile is not None:
            cv2.putText(
                img, str(profile[1]), (x, y+h+30), fontface, fontscale, fontcolor, 2)
        else:
            cv2.putText(
                img, "UNKNOWN", (x, y+h+30), fontface, fontscale, fontcolor, 2)

    # Show the result
    cv2.imshow('Face', img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        # Close the SQL connection before exiting
        conn.close()
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
