import RPi.GPIO as GPIO
import time

# GPIO pin ayarları
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

# Pin modlarını belirleme
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

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Zaman farkını ve mesafeyi hesaplama
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
