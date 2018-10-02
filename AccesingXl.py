import openpyxl
wb = openpyxl.load_workbook('tsw.xlsx')
print(type(wb))
print(wb.sheetnames)
