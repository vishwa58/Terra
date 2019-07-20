# import serial as sr
import openpyxl as xl
import data_manipulation_functions_copy as dmf


def find_column(percentage, worksheet):
    for row in worksheet.iter_rows(max_row =1, min_col=1, max_col = 31 ):
        for cell in row:
            if(cell.value==percentage):
                return cell.column
def find_row(column_num, worksheet):
    for cell in worksheet[column_num]:
        if cell.value is None:
            return (cell.row)
            break

#opns th workbook we are using
workbook = xl.load_workbook('moisture_data.xlsx')


#names the sheeeet containing the raw data
raw_data = wb.get_sheet_by_name('raw')

#sets up serial port and gets data from 
ser = dmf.setup_serial_communication('/dev/cu.usbmodem14401', 9600, 1)
data=dmf.collect_datapoints(500, ser)
column_num =find_column(num, raw_data)
raw_data.append()



