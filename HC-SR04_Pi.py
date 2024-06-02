import RPi.GPIO as GPIO
import time
 
# GPIO ayarları
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
 
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
 
def measure_distance():
    # Trig pinini düşük yap ve bekle
    GPIO.output(TRIG, False)
    time.sleep(2)
 
    # Trig pinini yüksek yap ve kısa bir süre sonra tekrar düşük yap
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
 
    # Echo pininden gelen sinyali ölç
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
 
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
 
    pulse_duration = pulse_end - pulse_start
 
    # Mesafeyi hesapla
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
 
try:
    while True:
        dist = measure_distance()
        print("Distance: {} cm".format(dist))
        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()
 