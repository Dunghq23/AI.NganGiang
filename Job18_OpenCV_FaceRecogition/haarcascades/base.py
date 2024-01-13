import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Set initial window size
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    cv2.resizeWindow('frame', 400, 300)  # Đặt kích thước khung hình ban đầu
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
