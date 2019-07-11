#This file was created on 7/11/19 by Vishwa Nathan (vishwan56@gmail.com) for Terra Robotics

import serial
port = "/dev/cu.usbmodem14401"
ser = serial.Serial(port, 9600, timeout =1)

datalist =[]
for i in range (500):
    data = ser.readline().decode('ascii')
    datalist.append(data)

for i in range(len(datalist)):
    print(datalist[i])

# str_example = "hello"
# ser.write(str_example.encode())
# ser.close()