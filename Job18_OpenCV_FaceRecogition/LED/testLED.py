from gpiozero import LED
from time import sleep, time

led = LED(17)  # Thay 17 bằng chân GPIO tương ứng của bạn

try:
    start_time = time()  # Lưu thời gian bắt đầu
    while time() - start_time < 5:  # Chạy trong 5 giây
        led.on()    # Bật đèn LED
        sleep(0.1)  # Đợi 0.1 giây
        led.off()   # Tắt đèn LED
        sleep(0.1)  # Đợi 0.1 giây
except KeyboardInterrupt:
    print("KeyboardInterrupt detected. Stopping the LED")
finally:
    led.off()   # Tắt đèn LED khi kết thúc
