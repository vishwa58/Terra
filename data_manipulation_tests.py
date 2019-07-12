#This file was created on 7/11/19 by Vishwa Nathan (vishwan56@gmail.com) for Terra Robotics

from data_manipulation_functions import *

#Serial port test and collect datapoint test

port = '/dev/cu.usbmodem14401'
baud = 9600

serialport = setup_serial_communication(port, baud, 1)

avg = collect_datapoint(500, serialport)
print(avg)

