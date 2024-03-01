import cv2
import numpy as np
import math

# Function to draw a heart shape
def draw_heart(frame, center, size, color):
    angle = np.linspace(0, 2*np.pi, 100)
    x = center[0] + size * 16 * np.power(np.sin(angle), 3)
    y = center[1] - size * (13*np.cos(angle) - 5*np.cos(2*angle) - 2*np.cos(3*angle) - np.cos(4*angle))
    points = np.array([x, y], np.int32).T
    cv2.fillPoly(frame, [points], color)

# Initialize parameters
size = 1
color = (255, 0, 0)
center = (200, 200)
direction = 1

# Create a blank image
frame = np.zeros((400, 400, 3), np.uint8)

while True:
    # Increase or decrease the size of the heart
    size += direction * 2

    # Change color
    color = tuple([int(c) for c in np.random.randint(0, 255, 3)])

    # Draw the heart on the frame
    draw_heart(frame, center, size, color)

    # Display the frame
    cv2.imshow('Love Animation', frame)

    # Reverse direction if heart reaches maximum or minimum size
    if size >= 100 or size <= 1:
        direction *= -1

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
