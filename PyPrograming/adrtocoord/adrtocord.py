import xlrd
wb = xlrd.open_workbook(filename='./spisok_tochek.xls')
sheet = wb.sheet_by_index(0)
a='['
for i in range(sheet.nrows):
	row = sheet.row_values(i)
	a+='"'+row[0]+'"'+','
a=a[:len(a)-1]
a+=']'
print(a)