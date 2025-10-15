import cv2
import numpy as np
import serial
import time

# Set up serial communication
# Adjust '/dev/ttyUSB0' to your Arduino's port (e.g., "COM3" on Windows)
ser = serial.Serial('/dev/cu.usbmodem1201', 9600, timeout=1)
time.sleep(2)  # Give Arduino time to reset

# Load the main image and the template image
main_img = cv2.imread('airballoon.jpg', cv2.IMREAD_COLOR)
template = cv2.imread('airballoontemp.jpg', cv2.IMREAD_COLOR)

if main_img is None or template is None:
    print("Error loading images.")
    exit()

# Convert images to grayscale
main_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

w, h = template_gray.shape[::-1]

# Perform template matching
result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Set a threshold for detection
threshold = 0.8  # Adjust as needed
if max_val >= threshold:
    print("Object detected with correlation:", max_val)
    # (Optional) Visualize the detection by drawing a rectangle
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(main_img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow("Detected", main_img)
    cv2.waitKey(0)
    # Send detection command to Arduino
    ser.write(b'detected\n')
else:
    print("Object not detected, max correlation:", max_val)
    ser.write(b'not_detected\n')

ser.close()
