import re 
import xlrd
import xlwt 
from xlwt import Workbook
loc="licenses.xlsx"
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
userstr=input("Enter a string:")
cnt=0
# for i in range(sheet.nrows):
#     str1=str(sheet.cell_value(i,0))
#     k=len(str1)
#     if(k == 16 ):
#         x=re.search(r'ABC[0-9A-Za-z]{10}XYZ',str1)
#         print(x.group())
for i in range(sheet.nrows):
    str1=str(sheet.cell_value(i,0))
    if(userstr==str1):
        i+=1
        print(str1)
if(cnt==0):
    print("Key not found")