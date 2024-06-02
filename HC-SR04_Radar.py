from gpiozero import DistanceSensor
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=18, echo=24)

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_ylim(0, 100)  # Set the radius limit to 100 cm

# Data storage for plotting
angles = []
distances = []

try:
    while True:
        for angle in np.linspace(0, 2 * np.pi, num=30):  # 30 points around the circle
            # Wait 1 second
            sleep(0.1)
            
            # Get the distance in metres
            distance = sensor.distance
            
            # Convert to centimeters
            distance_cm = distance * 100
            
            # Store angle and distance
            angles.append(angle)
            distances.append(distance_cm)
            
            # Clear the plot
            ax.clear()
            
            # Plot the data
            ax.plot(angles, distances, 'ro')
            ax.set_ylim(0, 100)  # Set the radius limit to 100 cm
            
            # Draw the plot
            plt.draw()
            plt.pause(0.01)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
