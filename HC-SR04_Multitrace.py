import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np
from gpiozero import DistanceSensor

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=18, echo=24)

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_ylim(0, 200)  # Set the radius limit to 200 cm

# Function to measure distance
def measure_distance():
    distance = sensor.distance * 100  # Convert to centimeters
    return distance

try:
    while True:
        angles = np.linspace(0, np.pi, 180)  # 180 degrees in radians
        distances = []

        for angle in angles:
            distance = measure_distance()
            distances.append(distance)
            time.sleep(0.05)  # Small delay between measurements
            
        # Clear the plot
        ax.clear()
        
        # Plot the data
        ax.plot(angles, distances, 'ro-')
        ax.set_ylim(0, 200)  # Set the radius limit to 200 cm
        ax.set_title('3D Distance Measurement Visualization')
        
        # Draw the plot
        plt.draw()
        plt.pause(0.01)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()