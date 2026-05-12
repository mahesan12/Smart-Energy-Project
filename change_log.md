# Change Log

## Change ID: CHG-002
Date: 2026-05-12  
Branch: Test1-om719  
Author: Oscar / om719  

### Files changed
- README.md
- testing/PIR_threshold_test_protocol_om719_v1.md
- testing/PIR_threshold_test_results_om719_v1.md
- arduino/sensor_reading_code.ino

### Reason for change
During testing, the PIR sensor did not trigger consistently. The side potentiometers affected the sensor sensitivity and delay time, which made it unclear whether the system was detecting real motion reliably. This created a risk that the smart fan-control system could switch incorrectly.

### Description of change
A PIR sensor calibration and threshold testing record was added to the project. The change documented how the PIR sensor was tested using the Arduino Serial Monitor and how motion/no-motion outputs were checked.
The project documentation was updated so the PIR testing method and final sensor behaviour could be understood and repeated.

### Testing evidence
The PIR sensor was tested by moving in front of the sensor and observing the Arduino Serial Monitor output. The expected result was that the Serial Monitor would print "motion detected" when movement was present and "motion not detected" when no movement was present.

### Outcome
The change improved the reliability and traceability of the PIR sensor section of the project. The reason for the change, the files affected, the testing method and the final result were documented so the change could be reviewed later through GitHub.
