#This file was created on 7/26/19 by Vishwa Nathan (vishwan56@gmail.com) for Terra Robotics

#This file holds the code for the GUI for automating calibration testing for the resistive sensor. You must run moisture_sensor_driver.ino on the Arduino for this
#program to collect meaningful data
import tkinter as tk
import moisture_calibrator as mc
import data_manipulation_functions as dmf
import pandas as pd
import openpyxl as xl
import xlsxwriter as xlw

#Creates serial object.
ser = dmf.setup_serial_communication("/dev/cu.usbmodem144301", 9600, 1 ) #see data_manipulation_functions.py fo detals

#This function collects data from the serial port, averages it and writes it to an excel file. 
# hey take per button press. Serial_object is a serial object created by the python Serial library. Percentage is the column you want to look up in excel. (percent moisture)
# Worksheet_name is the name of the worksheet. Filename is the name of the excel file. The parameter num_datapoints allows the user to specify how many samples they want to take.
def collect_data(serial_object, percentage, worksheet_name, filename, num_datapts):
    for i  in range (0,num_datapts):
        workbook = xl.load_workbook(filename) #creates a workbook object using the openpyxl library
        worksheet = workbook[worksheet_name] #creates a worksheet object using the openpyxl library
        dataframe = pd.read_excel(filename, sheet_name  = worksheet_name) #creates a dataframe object form  
        datapoint=dmf.collect_datapoints(500, serial_object) #see data_manipulation_functions.py for documentatiion
        mc.append_data(percentage, dataframe, worksheet, datapoint) #see moisture_caliibrator.py for documentation
        workbook.save(filename) #savees the excel file


#This class creates a basic tkinter window featurring an entry box and a button to run the collect_data function
class window:
    def __init__(self, parent):
        self.parent = parent 
        self.parent.configure(background = '#CECECE') #sets grey bg
        self.parent.geometry("400x240") #sets default window size (1280x750)

        # self.run_cap_button=tk.Button(self.parent, text = "Run Capacitive", width= 10, height = 1, relief = "raised")
        self.run_res_button=tk.Button(self.parent, text = "Run Resistive", width= 10, height = 1, relief = "raised")
    
        self.run_entry = tk.Entry(self.parent)
        self.run_entry.pack()
        self.run_res_button.pack()
        # self.run_cap_button.pack()


root = tk.Tk()
mw = window(root)

NUM_DATAPOINTS = 5

mw.run_res_button.config(command = lambda:collect_data(ser, float(mw.run_entry.get()), 'raw', 'moisture_data.xlsx', NUM_DATAPOINTS)) # allows button to collect data when pressed



tk.mainloop()