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

#This function is used n conjunction with
def find_row(column, dataframe):
     for index, row in  enumerate(dataframe.iloc[:, column]):
         if (pd.isna(dataframe.iloc[index, column])):
             return index+2 #the plus two is there because pandas is zero indexed and because the first row in excel is not counted in PANDAS, so two needs to be added to the index


    
def append_data(percentage, dataframe, worksheet, sensor_data):
    column =find_column(percentage, dataframe)
    letter_column = xlw.utility.xl_col_to_name(column)
    row = find_row(column, dataframe)
    cell_loc = letter_column + str(row)
    cell =worksheet[cell_loc]
    cell.value = sensor_data


