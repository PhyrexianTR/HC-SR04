import RPi.GPIO as GPIO
import time
from gpiozero import Servo
from gpiozero import DistanceSensor
import matplotlib.pyplot as plt
import numpy as np

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=18, echo=24)

# Initialize servo motor
servo = Servo(17)

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0, 100)  # Set the radius limit to 100 cm

# Data storage for plotting
angles = []
distances = []

def measure_distance():
    distance = sensor.distance * 100  # Convert to centimeters
    return distance

def apply_offset(distance, offset):
    # Adjust the distance measurement by adding an offset
    return distance + offset

try:
    while True:
        for offset in [-5, 0, 5]:  # Offset values in centimeters
            for angle in np.linspace(-1, 1, num=30):  # Servo angles from -1 to 1
                servo.value = angle
                time.sleep(0.5)  # Wait for the servo to move
                
                raw_distance = measure_distance()
                distance = apply_offset(raw_distance, offset)
                angle_rad = (angle + 1) * np.pi  # Convert servo value to radians
                
                angles.append(angle_rad)
                distances.append(distance)
                
                # Clear the plot
                ax.clear()
                
                # Plot the data
                ax.plot(angles, distances, 'ro-')
                ax.set_ylim(0, 100)  # Set the radius limit to 100 cm
                
                # Draw the plot
                plt.draw()
                plt.pause(0.01)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
