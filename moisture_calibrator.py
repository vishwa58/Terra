import pandas as pd
import openpyxl as xl
import xlsxwriter as xlw



def find_column(percentage, dataframe):
    for col in dataframe.columns:
        if (col==percentage):
            return col

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


