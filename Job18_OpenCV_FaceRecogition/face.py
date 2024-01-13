
import cv2
 
#Tải một tập tin mô hình nhận diện khuôn mặt và nhận diện mắt
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
 
#Đọc hình ảnh đầu vào
img = cv2.imread("./data/PSJ.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#Tìm kiếm các khuôn mặt trong ảnh bằng cách sử dụng file mô hình nhận diện khuôn mặt đã được tải lên
faces = face_cascade.detectMultiScale(gray_img, scaleFactor= 1.3, minNeighbors= 5, minSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE)
print(type(faces))
print(faces)
 
#Vẽ một hình chữ nhật xung quanh mỗi khuôn mặt được tìm thấy
for x,y,w,h in faces:
    roi_gray = gray_img[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0), 2)
      # ---Các tham số để vẽ một hình chữ nhật
      # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      # img là biến image, nó có thể là " frame" như trong ví dụ này
      # x1,y1 --------------
      # |                               |
      # |                               |
      # |                               |
      # --------------------     x+w,y+h
      # (255,0,0) là màu (R,G,B)
      # Số 2 cuối cùng trong bộ tham số là độ dày từ 1 đến 3 của đường viền
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
 
#Hiển thị hình ảnh
cv2.imshow("image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()