import cv2

def display_camera():
    # Mở camera
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        # Đọc frame từ camera
        ret, frame = cap.read()

        # Kiểm tra nếu frame rỗng
        if not ret or frame is None or frame.size == 0:
            print("Error: Empty frame")
            continue

        # Xoay hình ảnh 180 độ (hoặc bất kỳ góc nào bạn muốn)
        rotated_frame = cv2.flip(frame, 1)

        # Hiển thị frame trong cửa sổ
        cv2.imshow('Camera', rotated_frame)

        # Thoát nếu nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng camera và đóng cửa sổ hiển thị
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_camera()
