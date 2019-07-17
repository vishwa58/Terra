# import serial as sr
import openpyxl as xl
import data_manipulation_functions_copy as dmf


def find_column(percentage, worksheet):
    for row in worksheet.iter_rows(max_row =1, min_col=1, max_col = 8 ):
        for cell in row:
            if(cell.value==percentage):
                return cell.column




#opns th workbook we are using
#workbook = xl.load_workbook('moisture_data.xlsx')


#names the sheeeet containing the raw data
#raw_data = wb.wb.get_sheet_by_name('raw')

#seets up serial port and gets data from 
ser = dmf.setup_serial_communication('/dev/cu.usbmodem14401', 9600, 1)
data=dmf.collect_datapoints(500, ser)


