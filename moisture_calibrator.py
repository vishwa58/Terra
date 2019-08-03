#This file was created on 7/26/19 by Vishwa Nathan (vishwan56@gmail.com) for Terra Robotics

#This file uses Pandas, openpyxl and xlsx writer to help calibrate our moisture sensor. This file holds helper functions which are used in calibration_GUI.py

import pandas as pd
import openpyxl as xl
import xlsxwriter as xlw


#This returns the number of the "percent moisture" column you want in excel
def find_column(percentage, dataframe):
    for col in dataframe.columns: #loops through columns
        if (col==percentage): #if the user input is the same as the value in the column, returns the column
            return col 

#This function is used n conjunction with find_column to return the frst empty row in the column
def find_row(column, dataframe):
     for index, row in  enumerate(dataframe.iloc[:, column]): #loops through the rows in the column
         if (pd.isna(dataframe.iloc[index, column])): #If the row is empty, return thhe row
             return index+2 #the plus two is there because pandas is zero indexed and because the first row in excel is not counted in PANDAS, so two needs to be added to the index


 #This function appends a datapoint to the first empty row in a column   
def append_data(percentage, dataframe, worksheet, sensor_data):
    column =find_column(percentage, dataframe) #finds specified column
    letter_column = xlw.utility.xl_col_to_name(column) #converts that column to an excel letter. ex. 0=A, 1=B 27=AB...
    row = find_row(column, dataframe) #finds first empty row
    cell_loc = letter_column + str(row) #combines the column and row to give cell location. ex: A1, B4, AC6..
    cell =worksheet[cell_loc] #sets a cell equal to that locattion
    cell.value = sensor_data #sets the value of thhat cell equal to the sensor data


