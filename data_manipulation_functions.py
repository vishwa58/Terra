#This file was created on 7/11/19 by Vishwa Nathan (vishwan56@gmail.com) for Terra Robotics

import serial
from statistics import mean




#This function sets up a serial communication port. It requires the name of the COM port, the baudrate and 
#the timeout length. It then returns a serial object


def setup_serial_communication( port, baudrate, timeout):
    ser = serial.Serial(port, baudrate, timeout=timeout)
    return ser

#This function has two parameters: the number of samples you want in one data point and a serial port.
#The function then returns the average value  of the samples taken.
def collect_datapoint(sample_num, serial_object):
    datalist =[]
    for i in range (500):
        data = float(serial_object.readline().decode('ascii'))
        datalist.append(data)
    average_value = mean(datalist)
    return average_value