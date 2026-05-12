# Energy Monitoring System for Brushless DC Motors

## Project Overview
This project is an advanced real time energy monitoring device built using the Arduino Nano ESP32. It tracks the power consumption of a fan powered by an external supply while measuring environmental factors and motion. The system uses adaptive sampling to reduce CPU cycles and features a deep sleep mode triggered by the PIR sensor to conserve power when no motion is detected.

## Software Installation
1. Download and install the latest version of the Arduino IDE.
2. Go to the Boards Manager and install the official ESP32 board package.
3. Select the Arduino Nano ESP32 from the board selection menu.
4. Copy the project sketch from the source folder into a new Arduino project.
5. Click the Upload button to program the microcontroller.



## Bill of Materials
* Arduino Nano ESP32 Microcontroller
* PIR COM1708 Infrared Motion Sensor
* AHT20 Temperature and Humidity Sensor
* 5V Brushless Fan Unit (Complete Assembly)
* DC Brushless Motor (Internal Component)
* Motor Controller Module
* External Power Supply for Fan
* Solderless Breadboard and Jumper Wires
* Oscilloscope or Multimeter for Hardware Validation

## Wiring Configuration
* Fan External Supply: Connect to the motor controller input terminals.
* PIR COM1708: Connect VCC to 3.3V, GND to GND, and OUT to Digital Pin D2.
* AHT20 Sensor: Connect VCC to 3.3V, GND to GND, SCL to Pin A5, and SDA to Pin A4.
* Motor Controller: Connect the control signal input to PWM Pin D3.
* ESP32 Logic Power: Provide 5V via the USB C port for the microcontroller.
