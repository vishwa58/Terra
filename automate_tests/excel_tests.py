
import openpyxl as xl

data =[]
for i in range(0,20):
    data.append(i)


def find_column(percentage, worksheet):
    for row in worksheet.iter_rows(max_row =1, min_col=1, max_col = 33 ):
        for cell in row:
            if(cell.value==percentage):
                if(percentage==0):
                    return "A"
                if(percentage<=25):
                    return chr(cell.column+64)
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


def find_row(column_num, worksheet):
    for cell in worksheet[column_num]:
        if cell.value is None:
            return (cell.row)
            break


def append_data(percentage, worksheet, data ):
    column = find_column(percentage, worksheet)
    row = find_row(column, worksheet)
    cell_location = str(column)+str(row)
    cell =worksheet[cell_location]
    cell.value = data


wb = xl.load_workbook('moisture_data.xlsx')
raw_data = wb['raw']
x = find_column(12, raw_data)
y =  find_row(x, raw_data)

print(x)
print(y)
# print(raw_data['V'])
append_data(28, raw_data, 15)
wb.save('moisture_data.xlsx')
