import RPi.GPIO as GPIO
import time

# GPIO ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print("HC-SR04 mesafe sensörü")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Trig pinini düşük yaparak başlat
    GPIO.output(TRIG, False)
    time.sleep(2)
    
    # Trig pinini yüksek yap ve kısa bir süre sonra tekrar düşük yap
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Echo pininden gelen sinyali ölçme
    start_time = time.time()
    stop_time = time.time()

    timeout = start_time + 0.05  # 50 ms timeout

    while GPIO.input(ECHO) == 0 and time.time() < timeout:
        start_time = time.time()

    if time.time() >= timeout:
        print("Echo pin did not receive the start signal.")
        return None

    timeout = time.time() + 0.05  # 50 ms timeout

    while GPIO.input(ECHO) == 1 and time.time() < timeout:
        stop_time = time.time()

    if time.time() >= timeout:
        print("Echo pin did not receive the end signal.")
        return None

    # Zaman farkını ve mesafeyi hesaplama
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    distance = round(distance, 2)

    return distance

try:
    while True:
        print("Ölçülüyor...")
        dist = measure_distance()
        if dist is not None:
            if 2 < dist < 400:
                print("Mesafe:", dist - 0.5, "cm")
            else:
                print("Menzil aşıldı")
        else:
            print("Geçerli bir mesafe ölçülemedi.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
