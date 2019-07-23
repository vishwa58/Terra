#This file was created on 7/11/19 by Vishwa Nathan (vishwan56@gmail.com) for Terra Robotics


import data_manipulation_functions_copy as dmf #imports data manipulatioon  functions so it can use serial and such
import openpyxl as xl #uses openpyxl (this may change in future revisions)


#This program was designed to help automate tests to determine the correlation between the values we received
#from our moisture sensor and the actual percentage of water in the soil.

# Since this was only designed to be used as an intermedeiary program,  there are a few flaws.
#1. The find row function does not work if more than one value is added to a column. I am not sure why this glitch is there.
#(I think it is a problem with how opoenpyxl works. In the future I want to use pandas.)
#2.Currently the user can only input integer values between 1 and 30. This is beecause openpyxl can not loop through a row until it reaches a sentinel value.
#If you want to tweak this program the answer to problem 1 lies in the find_row function and the answer to problem 2 is in the find_column function


def find_column(percentage, worksheet):
    for row in worksheet.iter_rows(max_row =1, min_col=1, max_col = 33): #Takes a slice of row 1,  columns 1-33 (extend columns if you need more  data pts)
        for cell in row:
            if(cell.value==percentage): #searches the slice to see what column the percentage value is found in
                #The following if statements exist since at the time I did not know how to get columns such as AA or AB from numbers. This will be fixed in later updates
                if(percentage==0):
                    return "A"
                if(percentage<=25):
                    return chr(cell.column+64) #converts numbers to upper case letter to get column
                elif(percentage==26):
                    return "AA"
                elif(percentage ==27):
                    return "AB"
                elif(percentage==28):
                    return "AC"
                elif(percentage==29):
                    return "AD"
                elif(percentage==30):
                    return "AE"
                else:
                    print("please enter a value between  0 and 30")

#Function to find the first empty row in a column.
def find_row(column_num, worksheet):
    for cell in worksheet[column_num]:
        if cell.value is None: #returns the row number if the value in that row is none. This line is flawed since it will no longer work if you insert more than one value into a column at a time
            return (cell.row)
            break
#This function inserts a data point intoo the first empty row in the specified column. THe column is determined by the percentage
def append_data(percentage, worksheet, data ):
    column = find_column(percentage, worksheet)
    row = find_row(column, worksheet)
    cell_location = str(column)+str(row) #combines the column and row number to get cell indexing
    cell =worksheet[cell_location]
    cell.value = data





