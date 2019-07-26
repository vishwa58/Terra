import tkinter as tk
import moisture_calibrator as mc
import data_manipulation_functions as dmf
import pandas as pd
import openpyxl as xl
import xlsxwriter as xlw

def collect_data(serial_object, percentage, worksheet_name, filename, num_datapts):
    for i  in range (0,num_datapts):
        workbook = xl.load_workbook(filename)
        worksheet = workbook[worksheet_name]
        dataframe = pd.read_excel(filename, sheet_name  = worksheet_name)
        datapoint=dmf.collect_datapoints(500, serial_object)
        mc.append_data(percentage, dataframe, worksheet, datapoint)
        print(percentage)
        workbook.save(filename)



# frame = pd.read_excel('moisture_data.xlsx', sheet_name='raw')
# wb = xl.load_workbook('moisture_data.xlsx')
# raw_data = wb['raw']
ser = dmf.setup_serial_communication("/dev/cu.usbmodem144301", 9600, 1 )

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



mw.run_res_button.config(command = lambda:collect_data(ser, float(mw.run_entry.get()), 'raw', 'moisture_data.xlsx', 5))



tk.mainloop()