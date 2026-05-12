# Change Log

## Change 001 – Added Python efficiency analysis
Date: 01/05/2026  
Branch: feature/efficiency-analysis  
Files changed:
- python_analysis/efficiency_analysis.py
- data/fan_voltage_current_tests.csv
- README.md

Reason for change:
The project needed a method to calculate power and efficiency from measured voltage and current data.

Description:
Added Python calculations for power, average current, energy use, and efficiency. Updated README to explain how to run the analysis.

Testing:
Tested using recorded fan data from the laboratory circuit. Output values were compared against manual calculations.

Result:
Change successfully merged into main branch.



## Change 002: Integrated Technical User Manual and Sensor Documentation
**Date:** 12/05/2026
**Branch:** testing-kiho1
**Files changed:**
* README.md

**Reason for change:** The project lacked clear operating instructions and technical pinout data for the integrated sensor array.
**Description:** Created a comprehensive user manual across three incremental commits. This included the software installation guide plus hardware wiring for the PIR COM1708 and AHT20 sensors and a specialized circular economy section for component recovery. 
**Testing:** The markdown file was previewed on GitHub to ensure all headers and bullet points rendered correctly. Technical wiring instructions were cross referenced with the physical breadboard setup to verify accuracy.
**Result:** Documentation was successfully reviewed via a Pull Request and merged into the main branch.
