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





## Operating Instructions
Open the Serial Monitor in the Arduino IDE and set the baud rate to 115200. The system will display the current temperature and humidity data from the AHT20 alongside the motor efficiency levels. When the PIR COM1708 detects motion the system enters active monitoring mode. If no motion is detected for a set period the system automatically enters a low power state to save energy.

## Circular Economy and Sustainability
This device is designed for non destructive disassembly to support the circular economy. The high value neodymium magnets inside the DC brushless motor and the specialized silicon in the AHT20 and PIR sensors should be recovered if the unit reaches its end of life. Please ensure that all modular components like the jumper wires and the motor controller are repurposed for future engineering projects to reduce electronic waste.

## Troubleshooting
* Sensor Data Missing: Verify that the I2C wires for the AHT20 are not swapped and check the 3.3V power rail.
* Fan Not Spinning: Ensure the external supply is switched on and the motor controller ground is shared with the Arduino.
* PIR Not Triggering: Adjust the sensitivity potentiometer on the PIR COM1708 module and ensure it has a clear line of sight.
