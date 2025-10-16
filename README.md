
# Multi-Sensor Monitoring System

**CMPSC 497 – Special Topics: Raspberry Pi**

### Author
**Xiomara Mohamed**

---


![IMG_0404](https://github.com/user-attachments/assets/8f853860-c807-42fb-bb13-176f9d5890e5)

*Figure 1. The Multi-Sensor Monitoring System with connected sensors, LCD, and Arduino board.*

---

## Overview

The **Multi-Sensor Monitoring System** is an Arduino-based project designed to integrate multiple sensors—temperature/humidity, motion, distance, and button inputs—into a unified control system. Each sensor performs a distinct function, while a central LED and LCD display provide real-time feedback and visual cues.  

This project demonstrates the ability to interface various hardware components through the Arduino IDE, control logic flow with sensor states, and manage serial communication with Python and OpenCV. The system also features a **template detection mode**, bridging hardware with computer vision for object recognition.

---

## Features

- **Temperature & Humidity Monitoring:** Uses a DHT11 sensor to display live temperature (°C) and humidity (%) readings.  
- **Motion Detection:** Detects nearby movement using a PIR sensor and visually alerts with a red LED.  
- **Distance Measurement:** Utilizes an ultrasonic sensor to calculate object distance in centimeters.  
- **Mode Switching:** A button cycles through different sensor modes, each represented by a distinct LED color.  
- **LCD Display:** Shows which sensor is active and displays its output data in real time.  
- **Serial Communication Mode:** Integrates with Python + OpenCV to detect visual templates and report back to the Arduino.  

---

## Hardware Components

| Component | Function |
|------------|-----------|
| **Arduino Uno** | Central controller for all sensors |
| **Breadboard** | Mounting and wiring of all modules |
| **DHT11 Sensor** | Reads temperature and humidity |
| **PIR Motion Sensor** | Detects movement in front of the sensor |
| **Ultrasonic Sensor (HC-SR04)** | Measures object distance |
| **Button** | Switches between active modes |
| **LED** | Displays color-coded sensor states |
| **LCD (16x2)** | Shows live readings and current mode |

---

## How It Works

1. **Startup:**  
   When powered on, the system initializes each sensor and displays “System Started” on the LCD.

2. **Mode Selection:**  
   Pressing the button cycles through modes:
   - Green LED → Temperature/Humidity  
   - Blue LED → Motion Detection  
   - Red LED → Distance Measurement  
   - Pink LED → Serial (OpenCV) Mode  

3. **Real-Time Output:**  
   Each mode displays corresponding sensor data (e.g., temperature in °C, humidity in %, or distance in cm) on the LCD and via the Serial Monitor.

4. **OpenCV Integration:**  
   A connected Python program uses **template matching** to detect a specific object from images. If detected, the Arduino receives a “detected” message via serial communication and displays “Template Found!” on the LCD.

---

## Arduino Code Overview

- **Mode Handling:** Uses a `switch` structure to toggle sensor modes and LED colors.  
- **Sensor Functions:**  
  - `monitorTemperature()` → Reads and displays temperature/humidity.  
  - `detectMotion()` → Reports motion activity.  
  - `measureDistance()` → Calculates and prints object distance.  
  - `serialMode()` → Waits for serial input from Python for image recognition.  
- **Utilities:**  
  - `flashRedLED()` flashes an LED for detection feedback.  
  - `turnOffLEDs()` ensures only one LED is active per mode.  

---

## Python Integration (OpenCV)

The Python component enables template recognition and communication with Arduino.

**Key Features:**
- Uses `cv2.matchTemplate()` for image comparison.  
- Highlights matched areas with green bounding boxes.  
- Sends serial commands (`detected` / `not_detected`) to Arduino.  

**Libraries Used:**
- `cv2` (OpenCV)  
- `numpy`  
- `serial`  
- `time`  

---

## Results

- Each sensor responded correctly in its assigned mode.  
- Real-time feedback was displayed on both the LCD and Serial Monitor.  
- OpenCV integration successfully identified template images and triggered LED responses on detection.  

This verified full communication between hardware and software components.

---

## Challenges & Learnings

- Initial LCD output errors and LED color mismatches were resolved by refining pin assignments.  
- Learned to structure Arduino code with modular functions for clarity.  
- Improved understanding of serial communication between Arduino and Python.  
- Gained practical experience in debugging multi-sensor systems and combining hardware with computer vision.

---

## Conclusion

This project demonstrated full integration of multiple sensors, user interaction through button controls, and external image processing via OpenCV. It successfully merged embedded hardware with computer vision concepts, highlighting flexibility in both physical and software-based sensing.

---

## References
- ChatGPT (for debugging assistance)  
- [KT0193F 37-in-1 Sensor Kit Documentation](https://kt0193f-37-in-1-sensor-kit.readthedocs.io/en/latest/KT0193F.html#component-list)  
- General Arduino & OpenCV Documentation

---

