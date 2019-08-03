#This file was created on 7/11/19 by Vishwa Nathan (vishwan56@gmail.com) for Terra Robotics

import serial
from statistics import mean




#This file contains information for the program that collects data from the arduino. 


#This function sets up a serial communication port. It requires the name of the COM port, the baudrate and 
#the timeout length. It then returns a serial object

def setup_serial_communication( port, baudrate, timeout):
    ser = serial.Serial(port, baudrate, timeout=timeout)
    return ser

#This function has two parameters: the number of samples you want in one data point and a serial port.
#The function then returns the average value  of the samples taken.
def collect_datapoints(sample_num, serial_object):
    datalist =[]
    for i in range (500):
        data = float(serial_object.readline().decode('ascii'))
        datalist.append(data)
    datapoint = mean(datalist)
    return datapoint


#This function will need to be edited later to export matrices rather than individual data points
def output_data(file, value):
    value = str(value)
    file.write(value)
    file.write('\n')
    file.close()