from gpiozero import DistanceSensor
from time import sleep
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=18, echo=24)

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create lists to store the coordinates
x_data = []
y_data = []
z_data = []

try:
    while True:
        # Wait 1 second
        sleep(1)
        
        # Get the distance in metres
        distance = sensor.distance
        
        # Convert to centimeters
        distance_cm = distance * 100
        
        # Add the measurement to the data lists
        x_data.append(len(x_data))
        y_data.append(0)  # If you have an angle or different measurements, you can change this
        z_data.append(distance_cm)
        
        # Clear the plot
        ax.clear()
        
        # Plot the data
        ax.plot(x_data, y_data, z_data, label='Distance')
        ax.scatter(x_data, y_data, z_data, c='r', marker='o')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Distance (cm)')
        ax.set_title('3D Distance Measurement Visualization')
        
        # Draw the plot
        plt.draw()
        plt.pause(0.01)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
