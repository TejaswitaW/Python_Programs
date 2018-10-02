import openpyxl
wb = openpyxl.load_workbook('tsw.xlsx')
print(wb.sheetnames)
sheet = wb['Sheet1']
print(sheet)
c=sheet['A1']
print(c.value)
print(sheet.title)
anotherSheet = wb.active
print(anotherSheet)
