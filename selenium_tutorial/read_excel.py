import xlrd

wb = xlrd.open_workbook("Dane.xls")
sheet = wb.sheet_by_index(0)

for i in range(1, sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell(i, j).value)