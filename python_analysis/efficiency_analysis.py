import csv
import statistics
import matplotlib.pyplot as plt
import math
import numpy as np

#khl89 om719 cdm79

# ---------IMPORTING---------
@staticmethod
def read_value_csv(filename):
    """
    Reads a CSV file containing time and value data.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        List[ValueReading]: A list of ValueReading objects created from the file.
    """
    readings = []
        
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
            
        for row in reader:
            if not row:
                continue

            time = int(row[0])
            value = float(row[1])
                
            reading = ValueReading(time,value)
            readings.append(reading)
        
    return readings

# ---------VALUE MANIPULATION---------
class ValueReading:
    def __init__(self, time, value):
        """
    Represents a single measurement consisting of time and value.

    Attributes:
        time (int): Time of the reading in milliseconds.
        value (float): Measured value (e.g. current).
    """
        self.value = value
        self.time = time

    def GetValue(self):
        """Returns the recorded value."""
        return self.value
    
    def GetTime(self):
        """Returns the time in milliseconds."""
        return self.time
    
    def GetSeconds(self):
        """Returns the time converted to seconds."""
        return self.time / 1000
    
    def GetMinutes(self):
        """Returns the time converted to minutes."""
        return self.time / 60000
        
# ---------VALUE ANALYSIS---------
class ValueAnalysis:
    """
        Calculates RMS (Root Mean Square) of values above threshold (300).

        Returns:
            float: RMS value.
        """
    def __init__(self, lowertime, uppertime, file):
        self.ValueReadings = read_value_csv(file)
        self.lowertime = lowertime
        self.uppertime = uppertime

        self.BuildTimeline()
    
# ---------DATA ANALYSIS FEATURES---------
    def RMS(self):
        """
        Calculates RMS (Root Mean Square) of values above threshold (300).

        Returns:
            float: RMS value.
        """
        Values = [each_value.GetValue() for each_value in self.ValueReadings if each_value.GetValue() > 300]
        squared_sum = sum(v ** 2 for v in Values)
        mean_squared = squared_sum / len(Values)
        return math.sqrt(mean_squared)
    

    def Peak(self):
        """
        Finds the maximum value in the dataset.

        Returns:
            float: Peak value.
        """
        Values = [each_value.GetValue() for each_value in self.ValueReadings]
        peak = Values[0]
        for each_value in Values:
            if each_value > peak:
                peak = each_value
        
        return round(peak,2)
    
    
    def StartUpTransientMag(self):
        """
        Placeholder for startup transient magnitude calculation.

        Returns:
            None
        """
        return None
    
    def Mean(self):
        """
        Calculates mean of values above threshold (300).

        Returns:
            float: Mean value.
        """
        Values = [each_value.GetValue() for each_value in self.ValueReadings if each_value.GetValue() > 300]
    
        sum = 0
        num = 0
        for each_value in Values:
            sum += each_value
            num += 1

        return round(sum/num,2)
    

    def Stdev(self):
        """
        Calculates standard deviation of values above threshold.

        Returns:
            float: Standard deviation.
        """
        Values = [each_value.GetValue() for each_value in self.ValueReadings if each_value.GetValue() > 300]
        return round(statistics.pstdev(Values),2)
    

    def DutyCycle(self):
        """
        Calculates duty cycle based on ON periods.

        Returns:
            float: Duty cycle percentage.
        """
        times = [each_time.GetTime() for each_time in self.ValueReadings if each_time.GetValue() > 300]

        interval = 200

        on_periods = []

        start_on = times[0]

        for i in range(len(times)-1):
            diff = times[i+1] - times[i]

            if diff != interval:
                on_periods.append((start_on, times[i]))
                start_on = times[i+1]

        on_periods.append((start_on, times[-1]))

        total_on = 0
        for each_period in on_periods:
            total_on += each_period[1] - each_period[0]

        total_time = self.ValueReadings[-1].GetTime()
        
        return (total_on / total_time) * 100

    
# ---------STATE DETECTION---------
    def StateDetection(self, state):
        """
        Identifies ON or OFF periods.

        Args:
            state (str): "On" or "Off"

        Returns:
            str: Human-readable time ranges.
        """
        times = [each_time.GetTime() for each_time in self.ValueReadings if each_time.GetValue() > 300]

        interval = 200

        on_periods = []
        off_periods = []

        start_on = times[0]

        for i in range(len(times)-1):
            diff = times[i+1] - times[i]

            if diff != interval:
                on_periods.append((start_on, times[i]))
                off_periods.append((times[i], times[i+1]))
                start_on = times[i+1]

        on_periods.append((start_on, times[-1]))

        if state == "On":
            onTime = "Fan ACTIVE from: "
            for each_time in on_periods:
                if each_time != on_periods[-1]:
                    onTime += f"{each_time[0]}ms to {each_time[1]}ms, "
                else:
                    onTime += f"{each_time[0]}ms to {each_time[1]}ms"
            return onTime
        else:
            offTime = "Fan OFF from: "
            for each_time in on_periods:
                if each_time != off_periods[-1]:
                    offTime += f"{each_time[0]}ms to {each_time[1]}ms, "
                else:
                    offTime += f"{each_time[0]}ms to {each_time[1]}ms"
            return offTime

    
    def Transitions(self):
        """
        Detects ON/OFF transitions.

        Returns:
            List[dict]: List of transition events.
        """
        times = [each_time.GetTime() for each_time in self.ValueReadings if each_time.GetValue() > 300]


        interval = 200
        events = []
        previous_state = "OFF"   # assume fan starts OFF

        for i in range(len(times)-1):
            diff = times[i+1] - times[i]

            if diff == interval:
                current_state = "ON"
            else:
                current_state = "OFF"

            if current_state != previous_state:
                events.append({
                    "timestamp": f"{times[i]}ms",
                    "event": current_state
                })

            previous_state = current_state

        return events

# ---------REPORTING---------
    def BuildTimeline(self):
        """
        Builds time and state arrays for plotting.
        """
        self.time = np.arange(self.lowertime, self.uppertime-200,200)  # in ms

        self.state = []
        for each_value in self.ValueReadings:
            if each_value.GetTime() in self.time:
                if each_value.GetValue()>300:
                    self.state.append(1)
                else:
                    self.state.append(0)


    def CurrentVsTimePlot(self, unit):
        """
        Plots measured current against time.

        Args:
            unit (str): Time unit for the x-axis.
                Accepted values are "Seconds", "Minutes", or any other value
                for milliseconds.

        Returns:
            None
        """
        allowedValues = []
        for each_value in self.ValueReadings:
            if each_value.GetTime() >= self.lowertime and each_value.GetTime() <= self.uppertime:
                allowedValues.append(each_value)

        Values = [each_entry.GetValue() for each_entry in allowedValues]

        Times = []
        if unit == "Seconds": #User wants graph plotted by seconds
            for each_value in allowedValues:
                Times.append(each_value.GetSeconds())
        elif unit == "Minutes": #User wants graph plotted by minutes
            for each_value in allowedValues:
                Times.append(each_value.GetMinutes())
        else: #User wants graph plotted by milliseconds
            for each_value in allowedValues:
                Times.append(each_value.GetTime())

        plt.figure(figsize=(10, 5))

        plt.plot(Times, Values)
        if unit == "Seconds":  
            plt.xlabel("Time/seconds")
        elif unit == "Minutes":
            plt.xlabel("Time/minutes")
        else:
            plt.xlabel("Time/milliseconds")
        plt.ylabel("Current")
        plt.title("Current over time")

        plt.tight_layout()

        plt.show()


    def EnergyConsumptionPlot(self):
        """
        Plots estimated energy consumption values over time.

        Returns:
            None
        """
        plt.figure(figsize=(12, 5))
        plt.plot([each_time.GetTime() for each_time in self.ValueReadings], self.EstEnergyVals(5))
        plt.xlabel("Time (ms)")
        plt.ylabel("Energy Consumption")
        plt.title("Energy Consumption Over Time")
        plt.show()


    def StateVsTimePlot(self):
        """
        Plots detected device state over time.

        The y-axis uses 1 for ON and 0 for OFF.

        Returns:
            None
        """
        plt.figure(figsize=(12, 5))
        plt.step(self.time, self.state, where='post')
        plt.xlabel("Time (ms)")
        plt.ylabel("State (On=1 / Off=0)")
        plt.title("Device State Over Time")
        plt.ylim(-0.1, 1.1)
        plt.show()


    def Summary(self):
        """
        Prints a summary of key metrics.
        """
        times = []
        for each_value in self.ValueReadings:
            if each_value.GetValue() >300: #Alter based on off threshold
                times.append(each_value.GetTime())

        interval = 200

        on_periods = []

        start_on = times[0]

        for i in range(len(times)-1):
            diff = times[i+1] - times[i]

            if diff != interval:
                on_periods.append((start_on, times[i]))
                start_on = times[i+1]

        on_periods.append((start_on, times[-1]))

        total_on = 0
        for each_period in on_periods:
            total_on += each_period[1] - each_period[0]

        print(f"""
Device: Fan
Runtime: {total_on/1000} seconds
RMS Current: {round(self.RMS(),1)} A
Peak Current: {self.Peak()} A
Mean Current: {self.Mean():.2f} A
Std Dev: {self.Stdev():.2f} A
Estimated Energy: {round(self.EstEnergy(5),2)} kWh
Duty Cycle: {round(self.DutyCycle(),1)}%
              """)

valueanalysis = ValueAnalysis(800, 9600, "test_energy_data_threshold300.csv")
valueanalysis.Summary()
valueanalysis.EnergyConsumptionPlot()
valueanalysis.StateVsTimePlot()
valueanalysis.CurrentVsTimePlot("Seconds")
