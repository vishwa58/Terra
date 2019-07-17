
import openpyxl as xl





def find_column(percentage, worksheet):
    for row in worksheet.iter_rows(max_row =1, min_col=1, max_col = 31 ):
        for cell in row:
            if(cell.value==percentage):
                return cell.column
wb = xl.load_workbook('moisture_data.xlsx')
raw_data = wb['raw']
x = find_column(12, raw_data)
print(x)