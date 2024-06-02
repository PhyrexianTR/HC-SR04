from gpiozero import DistanceSensor
from time import sleep

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=23, echo=24)

while True:
    # Wait 2 seconds
    sleep(2)

    # Get the distance in metres
    distance = sensor.distance

    # Convert to centimeters and round to 2 decimal places
    distance_cm = round(distance * 100, 2)

    # Print the information to the screen
    print("Distance: {} cm".format(distance_cm))
